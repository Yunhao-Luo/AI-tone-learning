import streamlit as st
import time
from ui_utils import *

hide_sidebar()

########## session states ##########
st.session_state['time'] = 0

st.title("Please write down an explanation of how lightning works.")
st.write("*You have up to 4 mins for this section. You may proceed once you are finished.*")

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


TIME_LIMIT = 240
for secs in range(TIME_LIMIT + 10):
    time.sleep(1)
    st.session_state['time'] += 1
    if st.session_state['time'] == TIME_LIMIT:
        st.switch_page('pages/individual_feedback.py')