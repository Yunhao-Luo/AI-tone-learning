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

if "respA" not in st.session_state:
    with st.spinner("AI is generating feedback..."):
        st.session_state.respA, st.session_state.respB = get_feedback_in_two_tones(st.session_state['user_answer'],
                                                                                   st.session_state['feedback_num'],
                                                                                   "flattering", 
                                                                                   "imperative")

colA, colB = st.columns(2)

with colA:
    st.subheader("Feedback A")
    st.write(st.session_state.respA)

with colB:
    st.subheader("Feedback B")
    st.write(st.session_state.respB)

if "respA" in st.session_state:
    st.markdown("---")

    preference_key = f"preference_{st.session_state.feedback_num}"
    preference = st.radio(
        "**Which feedback do you prefer?**",
        ["A", "B", "Tie", "Both bad"],
        horizontal=False,
        index=None,
        key=preference_key
    )

    agree_key = f"agree_{st.session_state.feedback_num}"
    agree = st.select_slider(
        "**Do you agree with AI's feedback?**",
        options=range(1, 8),
        key=agree_key
    )
    likert_labels()

    # Submit
    if st.button("Submit"):
        if preference is None:
            st.warning("Please select an option before continuing.")
            st.stop()

        st.session_state.feedback_num += 1

        # clear response and generate new ones in the next round
        del st.session_state["respA"]
        del st.session_state["respB"]
        del st.session_state[preference_key]


        st.rerun()