import streamlit as st
from ui_utils import *

# Cognitive Effort
# Trust toward AI
# Perception of AI
# Confidence aobut learning

improve = st.select_slider(
    "**The AI feedback helped me improve my explanation.**",
    options=range(1, 8),
    key="improve"
)
likert_labels(left="Not at all", right="A lot")


clarity = st.select_slider(
    "**The AI feedback made it clear what I should change.**",
    options=range(1, 8),
    key="clarity"
)
likert_labels(left="Not at all", right="A lot")


reflect = st.select_slider(
    "**The AI feedback made me reflect on gaps in my understanding.**",
    options=range(1, 8),
    key="reflect"
)
likert_labels(left="Not at all", right="A lot")


supportive = st.select_slider(
    "**The feedback felt supportive.**",
    options=range(1, 8),
    key="supportive"
)
likert_labels(left="Not at all", right="A lot")


critical = st.select_slider(
    "**The feedback felt overly critical.**",
    options=range(1, 8),
    key="critical"
)
likert_labels(left="Not at all", right="A lot")


trust = st.select_slider(
    "**I would trust this AI peer to give me feedback on other science topics.**",
    options=range(1, 8),
    key="trust"
)
likert_labels(left="Not at all", right="A lot")


prefer = st.select_slider(
    "**If I had access to this AI, I would prefer using it over asking a classmate for feedback.**",
    options=range(1, 8),
    key="prefer"
)
likert_labels(left="Not at all", right="A lot")


confidence = st.select_slider(
    "**I feel confident that I now understand how lightning forms.**",
    options=range(1, 8),
    key="confidence"
)
likert_labels(left="Not at all", right="A lot")

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

if st.button("Submit"):
    st.switch_page("pages/final_page.py")