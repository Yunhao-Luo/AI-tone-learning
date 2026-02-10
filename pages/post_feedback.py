import streamlit as st
import feedback_agent
from ui_utils import *

# 1: supportive; mechanistic
# 2: supportive; oversimplified
# 3: critical; mechanistic
# 4: critical; oversimplified

CURRENT_CONDITION = 3

CONDITION_MAPPING = {
    1: ["supportive", "mechanistic"],
    2: ["supportive", "oversimplified"],
    3: ["critical", "mechanistic"],
    4: ["critical", "oversimplified"],
}

TONE = CONDITION_MAPPING[CURRENT_CONDITION][0]
DEPTH = CONDITION_MAPPING[CURRENT_CONDITION][1]

hide_sidebar(set_wide=False)

# ans_expander = st.expander("### Your answer:\n")
# ans_expander.write(st.session_state['user_answer'])

# feedback_expander = st.expander("### AI feedback for your summary:\n")
# feedback_expander.write(st.session_state['AI_feedback'])

st.divider()

valid = st.select_slider(
    "**Do you think the AI feedback is valid?**",
    options=range(1, 8),
    key="valid_feedback"
)
likert_labels(left="Not at all valid", right="Extremely valid")

style = st.select_slider(
    "**Is the style of the AI feedback appropriate?**",
    options=range(1, 8),
    key="style_feedback"
)
likert_labels(left="Not at all appripriate", right="Extremely appropriate")

confidence = st.select_slider(
    "**After reading the AI feedback, do you feel more confident about your understanding?**",
    options=range(1, 8),
    key="confidence_feedback"
)
likert_labels(left="Not at all confident", right="Extremely confident")

motivation = st.select_slider(
    "**How motivated are you to learn with this AI?**",
    options=range(1, 8),
    key="motivation_feedback"
)
likert_labels(left="Not at all motivated", right="Extremely motivated")

motivation_topic = st.select_slider(
    "**How motivated are you to learn more about how lighting forms?**",
    options=range(1, 8),
    key="motivation_topic_feedback"
)
likert_labels(left="Not at all motivated", right="Extremely motivated")

# SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam1_feedback",
    label_visibility="hidden"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam2_feedback",
    label_visibility="hidden"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam3_feedback",
    label_visibility="hidden"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**"
)

# Submit
if st.button("Submit"):
    if valid is None:
        st.warning("Please select an option before continuing.")
        st.stop()
    
    st.switch_page("pages/second_summary.py")