import streamlit as st
import feedback_agent
import dropbox
from datetime import datetime
import json


def hide_sidebar(set_wide=True):
    pass
    if set_wide:
        st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
    else:
        st.set_page_config(initial_sidebar_state="collapsed", layout="centered")
    no_sidebar_style = """
        <style>
            div[data-testid="stSidebarNav"] {display: none;}
        </style>
    """
    st.markdown(no_sidebar_style, unsafe_allow_html=True)

def hide_status_bar():
    st.markdown("""
        <style>
            /* Hide the running man/toolbar */
            div[data-testid="stToolbar"] { visibility: hidden; height: 0%; }
            div[data-testid="stDecoration"] { visibility: hidden; height: 0%; }
            /* Hide the stop button */
            div[data-testid="stStatusWidget"] button { display: none; }
            /* Hide the main menu */
            #MainMenu { visibility: hidden; }
            /* Hide the header/footer */
            header { visibility: hidden; height: 0%; }
            footer { visibility: hidden; height: 0%; }
        </style>
    """, unsafe_allow_html=True)

def larger_chat_font():
    st.markdown(
        """
        <style>
        div[data-testid="stChatMessageContent"] .stMarkdown p {
            font-size: 24px !important;
            line-height: 1.8 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
        )
    
def narrow_chat_container(width_px=760):
    st.markdown(
        f"""
        <style>
        /* Center the main block and limit width */
        .block-container {{
            max-width: {width_px}px;
            padding-top: 2rem;
            padding-left: 1rem;
            padding-right: 1rem;
            margin-left: auto;
            margin-right: auto;
        }}

        /* Make chat input follow same width */
        section[data-testid="stChatInput"] {{
            max-width: {width_px}px;
            margin-left: auto;
            margin-right: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_feedback_in_two_tones(user_ans, feedback_num, tone_1, tone_2):
    grader = feedback_agent.AI_Feedback_Agent(user_answer=user_ans, api_key=st.secrets['openrouter']['api_key'])
    resA = grader.feedback_for_point_in_tone(tone_1, feedback_num)
    resB = grader.feedback_for_point_in_tone(tone_2, feedback_num)
    return resA, resB

def get_holistic_feedback_in_tone(user_ans, tone, depth):
    grader = feedback_agent.AI_Feedback_Agent(user_answer=user_ans, api_key=st.secrets['openrouter']['api_key'])
    feedback = grader.generate_feedback(tone, depth)
    return feedback

def likert_labels(left="Disagree strongly", right='Agree strongly'):
    st.markdown(f'''
    <div style="display: flex; justify-content: space-between; width: 100%; margin-top: -20px;">
        <span style="font-size: 16px;">{left}</span>
        <span style="font-size: 16px;">{right}</span>
    </div>
    <br>
    ''', unsafe_allow_html=True)

def collect_all_survey_data():
    """
    Collect all survey responses from session state into a dictionary.
    
    Returns:
        dict: All survey responses
    """
    
    data = {
        # Timestamp
        'timestamp': datetime.now().isoformat(),
        
        # Demographics
        'prolific_id': st.session_state.get('prolific_id', ''),
        'education': st.session_state.get('education', ''),
        'major': st.session_state.get('major', ''),
        'AI_usage': st.session_state.get('AI_usage', ''),
        'neurodivergent': st.session_state.get('neurodivergent', ''),
        
        # AIAS (AI Attitude Scale)
        'aias_1': st.session_state.get('aias_1', None),
        'aias_2': st.session_state.get('aias_2', None),
        'aias_3': st.session_state.get('aias_3', None),
        'aias_4': st.session_state.get('aias_4', None),
        
        # TIPI (Personality)
        'tipi_extraverted': st.session_state.get('tipi_1', None),
        'tipi_critical': st.session_state.get('tipi_2', None),
        'tipi_dependable': st.session_state.get('tipi_3', None),
        'tipi_anxious': st.session_state.get('tipi_4', None),
        'tipi_open': st.session_state.get('tipi_5', None),
        'tipi_reserved': st.session_state.get('tipi_6', None),
        'tipi_sympathetic': st.session_state.get('tipi_7', None),
        'tipi_disorganized': st.session_state.get('tipi_8', None),
        'tipi_calm': st.session_state.get('tipi_9', None),
        'tipi_conventional': st.session_state.get('tipi_10', None),
        
        # RIF (Receptivity to Instructional Feedback)
        'rif_1': st.session_state.get('rif_1', None),
        'rif_2': st.session_state.get('rif_2', None),
        'rif_3': st.session_state.get('rif_3', None),
        'rif_4_reverse': st.session_state.get('rif_4', None),
        'rif_5': st.session_state.get('rif_5', None),
        'rif_6_reverse': st.session_state.get('rif_6', None),
    }
    
    return data

def make_json_safe(obj):
    """Convert Streamlit session_state values to JSON-serializable types."""
    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [make_json_safe(v) for v in obj]
    elif hasattr(obj, "__dict__"):
        return str(obj)
    else:
        return obj
    
def upload_file_to_dropbox(file_path, dropbox_path):
    """Upload a file to Dropbox using OAuth2 authentication.

    Returns:
        dropbox.files.FileMetadata: Metadata for the uploaded file.
    """
    app_key = st.secrets["dropbox"]["app_key"]
    app_secret = st.secrets["dropbox"]["app_secret"]
    refresh_token = st.secrets["dropbox"]["refresh_token"]
    
    try:
        dbx = dropbox.Dropbox(
            oauth2_refresh_token=refresh_token,
            app_key=app_key,
            app_secret=app_secret
        )
        
        with open(file_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

        # Verify the file exists in Dropbox and return metadata
        metadata = dbx.files_get_metadata(dropbox_path)
        return metadata
            
    except Exception as e:
        # Re-raise with more context
        raise Exception(f"Dropbox upload failed: {str(e)}")


def save_all_experiment_data():
    """
    Collect all experimental data from session_state and save to Dropbox.
    Call this in your final_page.py before showing the completion message.
    
    Returns:
        str: Filename of the saved data
    """
    import os
    
    # Collect ALL data from the experiment
    complete_data = {
        # Metadata
        'timestamp': datetime.now().isoformat(),
        'prolific_id': st.session_state.get('prolific_id', 'unknown_id'),
        'condition': st.session_state.get('condition', 'unknown_condition'),
        
        # Demographics & Pre-study questionnaires
        'education': st.session_state.get('education', ''),
        'major': st.session_state.get('major', ''),
        'AI_usage': st.session_state.get('AI_usage', ''),
        'neurodivergent': st.session_state.get('neurodivergent', ''),
        
        # AI Attitudes (AIAS)
        'aias': st.session_state.get('aias', {}),
        
        # TIPI Personality
        'tipi': st.session_state.get('tipi', {}),
        
        # Receptivity to Feedback (RIF)
        'rif': st.session_state.get('rif', {}),
        
        # Meteorology knowledge
        'meteorology_knowledge': st.session_state.get('meteorology_knowledge', {}),
        
        # SAM responses (baseline)
        'sam1_baseline': st.session_state.get('sam1_ans', {}),

        'pre_study_attention': st.session_state.get('attention_check_pre', {}),
        
        # video time
        'video_time': st.session_state.get('video_time', {}),

        # Initial summary
        'initial_summary': st.session_state.get('user_answer', ''),
        'initial_summary_time': st.session_state.get('initial_summary_time', 0),
        
        # SAM after first summary
        'sam2_after_first_summary': st.session_state.get('sam2_ans', {}),
        
        # AI Feedback phase
        'AI_feedback': st.session_state.get('AI_feedback', ''),
        'feedback_chat_history': st.session_state.get('history', []),
        'feedback_chat_time': st.session_state.get('feedback_chat_time', 0),
        
        # Post-feedback questionnaire
        # Try the saved dictionary first, fall back to individual keys
        'post_feedback_responses': st.session_state.get('post_feedback_responses', {
            'valid': st.session_state.get('valid_feedback', None),
            'style': st.session_state.get('style_feedback', None),
            'confidence': st.session_state.get('confidence_feedback', None),
            'motivation': st.session_state.get('motivation_feedback', None),
            'motivation_topic': st.session_state.get('motivation_topic_feedback', None),
            'sam1': st.session_state.get('sam1_feedback', None),
            'sam2': st.session_state.get('sam2_feedback', None),
            'sam3': st.session_state.get('sam3_feedback', None),
            'sam_open': st.session_state.get('sam_open_feedback', ''),
        }),
        
        # Second summary (after feedback)
        'second_summary': st.session_state.get('user_answer_second', ''),
        'second_summary_time': st.session_state.get('second_summary_time', 0),
        
        # SAM after second summary
        'sam3_after_second_summary': st.session_state.get('sam3_ans', {}),
        
        # Transfer test questions
        'transfer_test_1': st.session_state.get('ttest_1_ans', ''),
        'transfer_test_1_time': st.session_state.get('ttest1_time', 0),
        'transfer_test_2': st.session_state.get('ttest_2_ans', ''),
        'transfer_test_2_time': st.session_state.get('ttest2_time', 0),
        'transfer_test_3': st.session_state.get('ttest_3_ans', ''),
        'transfer_test_3_time': st.session_state.get('ttest3_time', 0),
        'transfer_test_4': st.session_state.get('ttest_4_ans', ''),
        'transfer_test_4_time': st.session_state.get('ttest4_time', 0),
        
        # Final post-study questionnaire
        'post_study_likert': st.session_state.get('post_feedback', {}),
        'post_study_open': st.session_state.get('post_feedback_open', {}),

        # direct dump of all session_state
        'all_session_state': st.session_state

    }
    
    # Make data JSON-safe
    safe_data = make_json_safe(complete_data)
    
    # Create filename with timestamp and prolific ID
    prolific_id = st.session_state.get('prolific_id', 'unknown_id')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # FIXED: Include both prolific_id AND timestamp in filename
    filename = f"data_{prolific_id}_{timestamp}.json"
    
    # Write to local file first (use /tmp/ which always exists)
    os.makedirs("/tmp", exist_ok=True)
    local_path = f"/tmp/{filename}"
    with open(local_path, 'w', encoding='utf-8') as f:
        json.dump(safe_data, f, indent=2, ensure_ascii=False)
    
    # Verify file was written
    import os
    file_size = os.path.getsize(local_path)
    if file_size < 100:
        raise Exception(f"Data file suspiciously small ({file_size} bytes). Check data collection.")
    
    # Upload to Dropbox in /tone-study/ folder
    dropbox_path = f"/tone-study/{filename}"
    metadata = upload_file_to_dropbox(local_path, dropbox_path)

    if not metadata:
        raise Exception("Dropbox verification failed: no metadata returned.")
    
    return filename


def chatgpt_like_chat_style():
    st.markdown(
        """
        <style>

        /* Slightly smaller text than Streamlit default */
        .stMarkdown p {
            font-size: 1.2rem;
            line-height: 1.55;

            /* KEY: restore paragraph spacing */
            margin-top: 0.6rem;
            margin-bottom: 0.6rem;
        }

        /* First paragraph in a message shouldn't have top gap */
        .stMarkdown p:first-child {
            margin-top: 0.1rem;
        }

        /* Lists spacing similar to ChatGPT */
        .stMarkdown ul, .stMarkdown ol {
            margin-top: 0.4rem;
            margin-bottom: 0.6rem;
        }

        .stMarkdown li {
            margin-bottom: 0.25rem;
            line-height: 1.5;
        }

        /* Chat message container padding */
        [data-testid="stChatMessage"] {
            padding-top: 0.35rem;
            padding-bottom: 0.35rem;
        }

        /* Message bubble content spacing */
        [data-testid="stChatMessageContent"] {
            padding: 0.4rem 0.6rem;
        }

        /* Code blocks readable but compact */
        .stMarkdown pre {
            font-size: 0.9rem;
            line-height: 1.45;
            padding: 0.65rem;
            margin: 0.5rem 0;
        }

        </style>
        """,
        unsafe_allow_html=True
    )