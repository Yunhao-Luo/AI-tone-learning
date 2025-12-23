import streamlit as st
import feedback_agent

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
    <div style="display: flex; justify-content: space-between; width: 100%;">
        <span>{left}</span>
        <span>{right}</span>
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