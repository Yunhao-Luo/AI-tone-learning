import streamlit as st
import time
from ui_utils import *

hide_sidebar()

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?
if 'ttest4_time' not in st.session_state:
    st.session_state['ttest4_time'] = 0
if 'time_up' not in st.session_state:
    st.session_state['time_up'] = False
if 'show_answer_4' not in st.session_state:
    st.session_state['show_answer_4'] = False
if 'countdown_4' not in st.session_state:
    st.session_state['countdown_4'] = 5
if 'choice_made_4' not in st.session_state:
    st.session_state['choice_made_4'] = False

TIME_LIMIT = 120

# Sample answer - replace with your actual answer
ANSWER = """Lightning is caused by electrical discharge resulting from charge separation in clouds:

1. **Charge Separation**: Within a thunderstorm cloud, ice particles and water droplets collide as they move in updrafts and downdrafts, transferring electrical charge.

2. **Charge Distribution**: Typically, positive charges accumulate at the top of the cloud while negative charges concentrate at the bottom.

3. **Electric Field**: The separation creates a strong electric field between the cloud and ground (or within/between clouds).

4. **Breakdown**: When the electric field becomes strong enough to overcome air's insulating properties, it ionizes the air, creating a conductive path.

5. **Discharge**: Electrical current flows through this path as lightning, equalizing the charge difference and releasing energy as light and heat.

The entire process is driven by atmospheric convection and the physics of charge transfer during particle collisions."""

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['ttest4_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['ttest4_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

q4 = st.text_area(
    label = "What causes lightning?",
    height=300,
    key='q4'
)

# Show popup when time is up
if st.session_state['time_up']:
    @st.dialog("⏰ Time's Up!", dismissible=False)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")
        if st.button("Proceed", use_container_width=True, type="primary"):
            st.session_state['user_answer'] = st.session_state.get('summary_text_key', '')
            st.session_state['time_up'] = False
            st.switch_page("pages/post_study_questions.py")
    
    time_up_dialog()
else:
    # Show choice dialog after submission (before revealing answer)
    if st.session_state['show_answer_4'] and not st.session_state['choice_made_4']:
        @st.dialog("What would you like to do?", dismissible=False)
        def choice_dialog():
            st.write("Choose one of the following options:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("⏳ Wait 5s to see answer", use_container_width=True, type="primary"):
                    st.session_state['choice_made_4'] = True
                    st.session_state['countdown_4'] = 5
                    st.rerun()
            
            with col2:
                if st.button("➡️ Proceed directly", use_container_width=True, type="secondary"):
                    st.session_state['show_answer_4'] = False
                    st.session_state['choice_made_4'] = False
                    st.switch_page("pages/post_study_questions.py")
        
        choice_dialog()
    
    # Show countdown and then answer if user chose to wait
    elif st.session_state['show_answer_4'] and st.session_state['choice_made_4']:
        @st.dialog("Answer Review", dismissible=False)
        def answer_dialog():
            if st.session_state['countdown_4'] > 0:
                st.info(f"✨ Answer will be revealed in {st.session_state['countdown_4']} seconds...")
            else:
                st.success("✅ Correct Answer:")
                st.write(ANSWER)
                st.divider()
                st.info("**Your Answer:**")
                st.write(st.session_state.get('ttest_4_ans', ''))
                
                if st.button("Proceed to Next Section", use_container_width=True, type="primary"):
                    st.session_state['show_answer_4'] = False
                    st.session_state['choice_made_4'] = False
                    st.session_state['countdown_4'] = 5
                    st.switch_page("pages/post_study_questions.py")
        
        answer_dialog()
        
        # Countdown logic
        if st.session_state['countdown_4'] > 0:
            time.sleep(1)
            st.session_state['countdown_4'] -= 1
            st.rerun()
    else:
        submit = st.button(
            label="Submit"
        )
        
        if submit:
            st.session_state['ttest_4_ans'] = q4
            st.session_state['show_answer_4'] = True
            st.rerun()

# Timer logic
if st.session_state['ttest4_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['ttest4_time'] += 1
    st.rerun()
elif st.session_state['ttest4_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()