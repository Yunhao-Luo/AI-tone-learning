import streamlit as st
import time
from ui_utils import *

hide_status_bar()
hide_sidebar()

########## session states ##########
if 'initial_summary_time' not in st.session_state:
    st.session_state['initial_summary_time'] = 0
if 'time_up' not in st.session_state:
    st.session_state['time_up'] = False

TIME_LIMIT = 240

st.title("Please explain how lightning works in your own words.")
st.write("*You have up to 4 mins for this section. You may proceed once you are finished.*")

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['initial_summary_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['initial_summary_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

user_summary = st.text_area(
    label="user input", 
    label_visibility="hidden", 
    height=300,
    key='summary_text_key',
    disabled=st.session_state['time_up']
)

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    Please click on Submit before the time is up; otherwise, the study will be invalid.
</div>
"""
st.markdown(html_reminder, unsafe_allow_html=True)
st.write("")

# Show popup when time is up
if st.session_state['time_up']:
    @st.dialog("⏰ Time's Up!", dismissible=False)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")
        if st.button("Proceed", use_container_width=True, type="primary"):
            st.session_state['user_answer'] = st.session_state.get('summary_text_key', '')
            st.session_state['time_up'] = False
            st.switch_page("pages/sam_after_first_summary.py")
    
    time_up_dialog()
else:
    submit = st.button(
        label="Submit"
    )
    
    if submit:
        st.session_state['user_answer'] = user_summary
        st.switch_page("pages/sam_after_first_summary.py")

# Timer logic
if st.session_state['initial_summary_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['initial_summary_time'] += 1
    st.rerun()
elif st.session_state['initial_summary_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()