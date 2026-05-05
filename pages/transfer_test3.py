import streamlit as st
import time
from ui_utils import *

hide_sidebar(set_wide=False)

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?
if 'ttest3_time' not in st.session_state:
    st.session_state['ttest3_time'] = 0
if 't3_time_up' not in st.session_state:
    st.session_state['t3_time_up'] = False

TIME_LIMIT = 120

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['ttest3_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['ttest3_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

q3 = st.text_area(
    label = "What does air temperature have to do with lightning?",
    height=300,
    key='q3',
    disabled=st.session_state['t3_time_up']
)

if st.button("Submit"):
    st.session_state['ttest_3_ans'] = q3
    st.switch_page("pages/transfer_test4.py")

# Time-up dialog
if st.session_state['ttest3_time'] == TIME_LIMIT:
    @st.dialog("⏰ Time's Up!", dismissible=True)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")

    time_up_dialog()

# Timer update
if st.session_state['ttest3_time'] < TIME_LIMIT:
    time.sleep(1)
    st.session_state['ttest3_time'] += 1
    st.rerun()
else:
    st.session_state['t3_time_up'] = True
    time.sleep(1)
    st.session_state['ttest3_time'] += 1
    st.rerun()