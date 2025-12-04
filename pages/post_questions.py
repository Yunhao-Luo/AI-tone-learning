import streamlit as st

st.title("Post-Study Questions")

ai_learning_tools = st.text_input(
    "**Do you use any AI tools for learning? If so, what are they?**"
)

feedback_format = st.text_input(
    "**Do you like the way AI provides feedback in this study to assist you in learning?**"
)

improvements = st.text_input(
    "**What kind of AI would you like to provide you with learning feedback?**"
)

other_feedback = st.text_input(
    "**Any other feedback for the study?**"
)