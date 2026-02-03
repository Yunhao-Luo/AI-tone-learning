import streamlit as st
import time
from ui_utils import *

hide_sidebar()

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?
if 'ttest1_time' not in st.session_state:
    st.session_state['ttest1_time'] = 0
if 'time_up' not in st.session_state:
    st.session_state['time_up'] = False
if 'show_answer' not in st.session_state:
    st.session_state['show_answer'] = False
if 'countdown' not in st.session_state:
    st.session_state['countdown'] = 5
if 'choice_made' not in st.session_state:
    st.session_state['choice_made'] = False

TIME_LIMIT = 120

# Sample answer - replace with your actual answer
ANSWER = """Lightning intensity can be decreased by reducing the charge separation in clouds. Some methods include:
- Cloud seeding to alter cloud electrical properties
- Reducing atmospheric moisture and temperature differences
- Installing lightning rods to provide easier discharge paths"""

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['ttest1_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['ttest1_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

q1 = st.text_area(
    label = "What could you do to decrease the intensity of lightning?",
    height=300,
    key='q1'
)

# Show popup when time is up
if st.session_state['time_up']:
    @st.dialog("⏰ Time's Up!", dismissible=False)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")
        if st.button("Proceed", use_container_width=True, type="primary"):
            st.session_state['user_answer'] = st.session_state.get('summary_text_key', '')
            st.session_state['time_up'] = False
            st.switch_page("pages/transfer_test2.py")
    
    time_up_dialog()
else:
    # Show choice dialog after submission (before revealing answer)
    if st.session_state['show_answer'] and not st.session_state['choice_made']:
        @st.dialog("What would you like to do?", dismissible=False)
        def choice_dialog():
            st.write("You can choose to see the correct answer or proceed to the next question. To see the correct answer, you will need to wait for a random amount of time between 5 and 25 seconds.")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("⏳ Wait to see answer", use_container_width=True, type="primary"):
                    st.session_state['choice_made'] = True
                    st.session_state['countdown'] = 18
                    st.rerun()
            
            with col2:
                if st.button("➡️ Proceed directly", use_container_width=True, type="secondary"):
                    st.session_state['show_answer'] = False
                    st.session_state['choice_made'] = False
                    st.switch_page("pages/transfer_test2.py")
        
        choice_dialog()
    
    # Show countdown and then answer if user chose to wait
    elif st.session_state['show_answer'] and st.session_state['choice_made']:
        @st.dialog("Answer Review", dismissible=False)
        def answer_dialog():
            if st.session_state['countdown'] > 0:
                st.info(f"✨ Answer will be revealed in {st.session_state['countdown']} seconds...")
            else:
                st.success("✅ Correct Answer:")
                st.write(ANSWER)
                st.divider()
                st.info("**Your Answer:**")
                st.write(st.session_state.get('ttest_1_ans', ''))
                
                if st.button("Proceed to Next Question", use_container_width=True, type="primary"):
                    st.session_state['show_answer'] = False
                    st.session_state['choice_made'] = False
                    st.session_state['countdown'] = 18
                    st.switch_page("pages/transfer_test2.py")
        
        answer_dialog()
        
        # Countdown logic
        if st.session_state['countdown'] > 0:
            time.sleep(1)
            st.session_state['countdown'] -= 1
            st.rerun()
    else:
        submit = st.button(
            label="Submit"
        )
        
        if submit:
            st.session_state['ttest_1_ans'] = q1
            st.session_state['show_answer'] = True
            st.rerun()

# Timer logic
if st.session_state['ttest1_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['ttest1_time'] += 1
    st.rerun()
elif st.session_state['ttest1_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()