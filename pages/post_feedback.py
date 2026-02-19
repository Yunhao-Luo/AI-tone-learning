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

st.divider()

valid = st.pills(
    "**Do you think the AI feedback is valid?**",
    options=range(1, 8),
    key="valid_feedback",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all valid", right="Extremely valid")

style = st.pills(
    "**Is the style of the AI feedback appropriate?**",
    options=range(1, 8),
    key="style_feedback",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all appripriate", right="Extremely appropriate")

confidence = st.pills(
    "**After reading the AI feedback, do you feel more confident about your understanding?**",
    options=range(1, 8),
    key="confidence_feedback",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all confident", right="Extremely confident")

motivation = st.pills(
    "**How motivated are you to learn with this AI?**",
    options=range(1, 8),
    key="motivation_feedback",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all motivated", right="Extremely motivated")

motivation_topic = st.pills(
    "**How motivated are you to learn more about how lighting forms?**",
    options=range(1, 8),
    key="motivation_topic_feedback",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all motivated", right="Extremely motivated")

# SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam1_feedback",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam2_feedback",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam3_feedback",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**",
    key="sam_open_feedback"
)

# Submit - SAVE ALL VALUES EXPLICITLY
if st.button("Submit"):
    st.session_state['post_feedback_responses'] = {
        'valid': st.session_state.get('valid_feedback'),
        'style': st.session_state.get('style_feedback'),
        'confidence': st.session_state.get('confidence_feedback'),
        'motivation': st.session_state.get('motivation_feedback'),
        'motivation_topic': st.session_state.get('motivation_topic_feedback'),
        'sam1': st.session_state.get('sam1_feedback'),
        'sam2': st.session_state.get('sam2_feedback'),
        'sam3': st.session_state.get('sam3_feedback'),
        'sam_open': st.session_state.get('sam_open_feedback', ''),
    }

    keys_to_validate = [
        'valid_feedback', 'style_feedback', 'confidence_feedback', 'motivation_feedback', 'motivation_topic_feedback',
        'sam1_feedback', 'sam2_feedback', 'sam3_feedback', 'sam_open_feedback'
    ]

    missing = validate_session_keys(keys_to_validate)

    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
    else:
        st.switch_page("pages/second_summary.py")