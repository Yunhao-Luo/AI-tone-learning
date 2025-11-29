import streamlit as st
from ui_utils import *

hide_sidebar()

st.title("Welcome to AI Learning Study")

intro = '''
In this study, you will watch a short video, summarize your understanding, and then receive feedback from an AI learning peer.
'''
st.write(intro)

major = st.text_input("**What did you study**")
AI_usage = st.radio(
    label="How often do you use AI?",
    options=['Daily', 'Few times a week', 'Few times a month', 'Few times a year','Never'],
    index=None
)

if st.button("Next"):
    st.switch_page("pages/video.py")