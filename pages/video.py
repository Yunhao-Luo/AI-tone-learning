import streamlit as st
import time
from ui_utils import *

hide_status_bar()
hide_sidebar()

########## session states ##########
st.session_state['time'] = 0

st.video("lesson.mp4", autoplay=True, muted=False)

timer_placeholder = st.empty()
st.write("*You will be directed to the next stage when time is up.*")
TIME_LIMIT = 160
for secs in range(TIME_LIMIT + 10):
    timer_placeholder.markdown(f"⏳ Time remaining: **{TIME_LIMIT - st.session_state['time']} seconds**")
    time.sleep(1)
    st.session_state['time'] += 1
    if st.session_state['time'] == TIME_LIMIT:
        st.switch_page('pages/user_answer.py')