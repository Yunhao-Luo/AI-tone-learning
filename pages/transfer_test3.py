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
if 'show_answer_3' not in st.session_state:
    st.session_state['show_answer_3'] = False
if 'countdown_3' not in st.session_state:
    st.session_state['countdown_3'] = 5
if 'choice_made_3' not in st.session_state:
    st.session_state['choice_made_3'] = False

TIME_LIMIT = 120

# Sample answer - replace with your actual answer
ANSWER = """Air temperature plays a crucial role in lightning formation:
- Warm air rises rapidly, creating strong updrafts necessary for charge separation
- Temperature differences between cloud levels affect ice crystal formation
- Warmer surface temperatures lead to more atmospheric instability
- The freezing level in clouds (where water becomes ice) is critical for charging
- Greater temperature contrasts create more vigorous convection, increasing lightning probability

Warmer temperatures generally increase lightning activity by enhancing the conditions needed for thunderstorm development."""

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
    # Show choice dialog after submission (before revealing answer)
    if st.session_state['show_answer_3'] and not st.session_state['choice_made_3']:
        @st.dialog("What would you like to do?", dismissible=False)
        def choice_dialog():
            st.write("Choose one of the following options:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("⏳ Wait 5s to see answer", use_container_width=True, type="primary"):
                    st.session_state['choice_made_3'] = True
                    st.session_state['countdown_3'] = 5
                    st.rerun()
            
            with col2:
                if st.button("➡️ Proceed directly", use_container_width=True, type="secondary"):
                    st.session_state['show_answer_3'] = False
                    st.session_state['choice_made_3'] = False
                    st.switch_page("pages/transfer_test4.py")
        
        choice_dialog()
    
    # Show countdown and then answer if user chose to wait
    elif st.session_state['show_answer_3'] and st.session_state['choice_made_3']:
        @st.dialog("Answer Review", dismissible=False)
        def answer_dialog():
            if st.session_state['countdown_3'] > 0:
                st.info(f"✨ Answer will be revealed in {st.session_state['countdown_3']} seconds...")
            else:
                st.success("✅ Correct Answer:")
                st.write(ANSWER)
                st.divider()
                st.info("**Your Answer:**")
                st.write(st.session_state.get('ttest_3_ans', ''))
                
                if st.button("Proceed to Next Question", use_container_width=True, type="primary"):
                    st.session_state['show_answer_3'] = False
                    st.session_state['choice_made_3'] = False
                    st.session_state['countdown_3'] = 5
                    st.switch_page("pages/transfer_test4.py")
        
        answer_dialog()
        
        # Countdown logic
        if st.session_state['countdown_3'] > 0:
            time.sleep(1)
            st.session_state['countdown_3'] -= 1
            st.rerun()
    else:
        submit = st.button(
            label="Submit"
        )
        
        if submit:
            st.session_state['ttest_3_ans'] = q3
            st.session_state['show_answer_3'] = True
            st.rerun()

# Timer logic
if st.session_state['ttest3_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['ttest3_time'] += 1
    st.rerun()
elif st.session_state['ttest3_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()