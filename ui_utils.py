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

def get_feedback_in_two_tones(user_ans, feedback_num, tone_1, tone_2):
    grader = feedback_agent.AI_Feedback_Agent(user_answer=user_ans, api_key=st.secrets['openrouter']['api_key'])
    resA = grader.feedback_for_point_in_tone(tone_1, feedback_num)
    resB = grader.feedback_for_point_in_tone(tone_2, feedback_num)
    return resA, resB

def likert_labels():
    st.markdown('''
    <div style="display: flex; justify-content: space-between; width: 100%;">
        <span>Disagree strongly</span>
        <span>Agree strongly</span>
    </div>
    <br>
    ''', unsafe_allow_html=True)