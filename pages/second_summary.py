import streamlit as st
import time
from ui_utils import *

hide_status_bar()
hide_sidebar(set_wide=False)

########## session states ##########
if 'second_summary_time' not in st.session_state:
    st.session_state.second_summary_time = 0

if 'second_summary_time_up' not in st.session_state:
    st.session_state.second_summary_time_up = False

TIME_LIMIT = 240  # 4 minutes

st.title("Please rewrite your explanation of how lightning works.")
st.write("*You have up to 4 mins for this section. You may proceed once you are finished. Please click the submit button before the time is up.*")

# Timer display
minutes_left = (TIME_LIMIT - st.session_state['second_summary_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['second_summary_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    Please submit before the time is up; otherwise, your participation may be invalid.
</div>
"""
st.markdown(html_reminder, unsafe_allow_html=True)
st.write("")

# Input box
user_summary = st.text_area(
    label="Rewrite your explanation",
    height=300,
    key="summary_text_key",
    label_visibility="hidden",
    disabled=st.session_state['second_summary_time_up']
)

if st.button("Submit"):
    st.session_state.user_answer_second = user_summary
    st.switch_page("pages/sam_after_second_summary.py")

# Time-up dialog
if st.session_state.second_summary_time == TIME_LIMIT:
    @st.dialog("⏰ Time's Up!", dismissible=True)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")

    time_up_dialog()

# Timer update
if st.session_state.second_summary_time < TIME_LIMIT:
    time.sleep(1)
    st.session_state.second_summary_time += 1
    st.rerun()
else:
    st.session_state.second_summary_time_up = True
    time.sleep(1)
    st.session_state.second_summary_time += 1
    st.rerun()
