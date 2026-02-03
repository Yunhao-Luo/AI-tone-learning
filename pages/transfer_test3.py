import streamlit as st
import time
from ui_utils import *

hide_sidebar()

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?
if 'ttest3_time' not in st.session_state:
    st.session_state['ttest3_time'] = 0
if 'time_up' not in st.session_state:
    st.session_state['time_up'] = False

TIME_LIMIT = 120

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['ttest3_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['ttest3_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

q3 = st.text_area(
    label = "What does air temperature have to do with lightning?",
    height=300,
    key='q3'
)

# Show popup when time is up
if st.session_state['time_up']:
    @st.dialog("⏰ Time's Up!", dismissible=False)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")
        if st.button("Proceed", use_container_width=True, type="primary"):
            st.session_state['user_answer'] = st.session_state.get('summary_text_key', '')
            st.session_state['time_up'] = False
            st.switch_page("pages/transfer_test4.py")
    
    time_up_dialog()
else:
    submit = st.button(
        label="Submit"
    )
    
    if submit:
        st.session_state['ttest_3_ans'] = q3
        st.switch_page("pages/transfer_test4.py")

# Timer logic
if st.session_state['ttest3_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['ttest3_time'] += 1
    st.rerun()
elif st.session_state['ttest3_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()