import streamlit as st
from ui_utils import *

hide_sidebar()

st.title("Please explain how lightning forms, as clearly and thoroughly as possible.")

user_summary = st.text_area(
    label="user input", 
    label_visibility="hidden", 
    height=300
)

confirm = st.button(
    label="Submit"
)

if confirm:
    st.session_state['user_answer'] = user_summary
    st.switch_page("pages/individual_feedback.py")