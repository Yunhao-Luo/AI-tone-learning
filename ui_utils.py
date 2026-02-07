import streamlit as st
import feedback_agent
import dropbox

def hide_sidebar(set_wide=True):
    pass
    if set_wide:
        st.set_page_config(initial_sidebar_state="collapsed", layout="wide")
    else:
        st.set_page_config(initial_sidebar_state="collapsed")
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
    from datetime import datetime
    
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
    except Exception as e:
        print("Error during file upload:", e)


def chatgpt_like_chat_style():
    st.markdown(
        """
        <style>

        /* Slightly smaller text than Streamlit default */
        .stMarkdown p {
            font-size: 0.96rem;
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
