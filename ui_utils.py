import streamlit as st
import feedback_agent

def hide_sidebar(set_wide=True):
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

def get_holistic_feedback_in_tone(user_ans, tone):
    grader = feedback_agent.AI_Feedback_Agent(user_answer=user_ans, api_key=st.secrets['openrouter']['api_key'])
    feedback = grader.holistic_feedback_in_tone(tone)
    return feedback

def likert_labels(left="Disagree strongly", right='Agree strongly'):
    st.markdown(f'''
    <div style="display: flex; justify-content: space-between; width: 100%;">
        <span>{left}</span>
        <span>{right}</span>
    </div>
    <br>
    ''', unsafe_allow_html=True)