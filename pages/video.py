import streamlit as st
import time
from ui_utils import *

hide_sidebar()

########## session states ##########
st.session_state['time'] = 0

st.video("https://www.youtube.com/watch?v=VqXnN_FQfrc&t=2s", autoplay=True, muted=False)


########## session states ##########
TIME_LIMIT = 180
for secs in range(TIME_LIMIT + 10):
    time.sleep(1)
    st.session_state['time'] += 1
    if st.session_state['time'] == TIME_LIMIT:
        st.switch_page('pages/user_answer.py')