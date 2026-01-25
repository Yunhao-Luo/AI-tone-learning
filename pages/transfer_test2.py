import streamlit as st
import time
from ui_utils import *

hide_sidebar()

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?
if 'ttest2_time' not in st.session_state:
    st.session_state['ttest2_time'] = 0
if 'time_up' not in st.session_state:
    st.session_state['time_up'] = False
if 'show_answer_2' not in st.session_state:
    st.session_state['show_answer_2'] = False
if 'countdown_2' not in st.session_state:
    st.session_state['countdown_2'] = 5
if 'choice_made_2' not in st.session_state:
    st.session_state['choice_made_2'] = False

TIME_LIMIT = 120

# Sample answer - replace with your actual answer
ANSWER = """Clouds without lightning lack sufficient charge separation. Lightning requires:
- Strong updrafts and downdrafts to separate charges
- Ice crystals and water droplets colliding to build up electrical charge
- Sufficient temperature differences within the cloud
- Adequate cloud height and development

Not all clouds have the right conditions for charge separation to occur."""

# Timer Display
minutes_left = (TIME_LIMIT - st.session_state['ttest2_time']) // 60
seconds_left = (TIME_LIMIT - st.session_state['ttest2_time']) % 60
st.write(f"⏱️ Time remaining: {minutes_left}:{seconds_left:02d}")

q2 = st.text_area(
    label = "Suppose you see clouds in the sky, but no lightning. Why not?",
    height=300,
    key='q2'
)

# Show popup when time is up
if st.session_state['time_up']:
    @st.dialog("⏰ Time's Up!", dismissible=False)
    def time_up_dialog():
        st.write("Your time has expired. Please proceed to the next section.")
        if st.button("Proceed", use_container_width=True, type="primary"):
            st.session_state['user_answer'] = st.session_state.get('summary_text_key', '')
            st.session_state['time_up'] = False
            st.switch_page("pages/transfer_test3.py")
    
    time_up_dialog()
else:
    # Show choice dialog after submission (before revealing answer)
    if st.session_state['show_answer_2'] and not st.session_state['choice_made_2']:
        @st.dialog("What would you like to do?", dismissible=False)
        def choice_dialog():
            st.write("Choose one of the following options:")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("⏳ Wait 5s to see answer", use_container_width=True, type="primary"):
                    st.session_state['choice_made_2'] = True
                    st.session_state['countdown_2'] = 5
                    st.rerun()
            
            with col2:
                if st.button("➡️ Proceed directly", use_container_width=True, type="secondary"):
                    st.session_state['show_answer_2'] = False
                    st.session_state['choice_made_2'] = False
                    st.switch_page("pages/transfer_test3.py")
        
        choice_dialog()
    
    # Show countdown and then answer if user chose to wait
    elif st.session_state['show_answer_2'] and st.session_state['choice_made_2']:
        @st.dialog("Answer Review", dismissible=False)
        def answer_dialog():
            if st.session_state['countdown_2'] > 0:
                st.info(f"✨ Answer will be revealed in {st.session_state['countdown_2']} seconds...")
            else:
                st.success("✅ Correct Answer:")
                st.write(ANSWER)
                st.divider()
                st.info("**Your Answer:**")
                st.write(st.session_state.get('ttest_2_ans', ''))
                
                if st.button("Proceed to Next Question", use_container_width=True, type="primary"):
                    st.session_state['show_answer_2'] = False
                    st.session_state['choice_made_2'] = False
                    st.session_state['countdown_2'] = 5
                    st.switch_page("pages/transfer_test3.py")
        
        answer_dialog()
        
        # Countdown logic
        if st.session_state['countdown_2'] > 0:
            time.sleep(1)
            st.session_state['countdown_2'] -= 1
            st.rerun()
    else:
        submit = st.button(
            label="Submit"
        )
        
        if submit:
            st.session_state['ttest_2_ans'] = q2
            st.session_state['show_answer_2'] = True
            st.rerun()

# Timer logic
if st.session_state['ttest2_time'] < TIME_LIMIT and not st.session_state['time_up']:
    time.sleep(1)
    st.session_state['ttest2_time'] += 1
    st.rerun()
elif st.session_state['ttest2_time'] >= TIME_LIMIT and not st.session_state['time_up']:
    st.session_state['time_up'] = True
    st.rerun()