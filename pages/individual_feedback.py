import streamlit as st
import feedback_agent
from ui_utils import *

hide_sidebar()

########## session states ##########
if "feedback_num" not in st.session_state:
    st.session_state.feedback_num = 1

########## state checking ##########
if "user_answer" not in st.session_state or not st.session_state["user_answer"]:
    st.error("No answer found. Please go back and submit your answer first.")
    st.stop()

st.title(f"AI Feedback: {st.session_state.feedback_num}/5")

ans_expander = st.expander("### Your answer:\n")
ans_expander.write(st.session_state['user_answer'])

st.divider()

if "feedback" not in st.session_state:
    with st.spinner("AI is generating feedback..."):
        st.session_state.feedback = get_holistic_feedback_in_tone(st.session_state['user_answer'],"flattering")

colA, colB = st.columns(2)

st.subheader("AI Feedback")
st.write(st.session_state.feedback)

if "feedback" in st.session_state:
    st.markdown("---")

    helpful_key = "helpful_feedback"
    helpful = st.select_slider(
        "**How much did this feedback help you rethink?**",
        options=range(1, 8),
        key=helpful_key
    )
    likert_labels(left="Not at all", right="A lot")

    agree_key = "agree_feedback"
    agree = st.select_slider(
        "**Do you agree with AI's feedback?**",
        options=range(1, 8),
        key=agree_key
    )
    likert_labels()

    st.write("### After this feedback session, you will have a chance to improve your summary.")
    # Submit
    if st.button("Submit"):
        if helpful is None:
            st.warning("Please select an option before continuing.")
            st.stop()
        
        st.switch_page("page/second_summary.py")