import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.pills(
    label="1",
    options=range(1, 10),
    key="sam1_2",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.pills(
    label="2",
    options=range(1, 10),
    key="sam2_2",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.pills(
    label="3",
    options=range(1, 10),
    key="sam3_2",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**",
    key="sam_open_feedback_2"
)

summary_confidence = st.pills(
    "**How confidence are you that you performed well in your summary?**",
    options=range(1, 8),
    key="summary_confidence_2",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all", right="Very much")

summary_curiosity = st.pills(
    "**How curious are you to find out the answer to how lightning forms?**",
    options=range(1, 8),
    key="summary_curiosity_2",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Not at all", right="Very much")

if st.button("Submit"):

    st.session_state['sam3_ans'] = {
        'sam1': st.session_state.get('sam1_2'),
        'sam2': st.session_state.get('sam2_2'),
        'sam3': st.session_state.get('sam3_2'),
        'sam_open': st.session_state.get('sam_open_feedback_2'),
        "summary_confidence": st.session_state.get('summary_confidence_2'),
        "summary_curiosity": st.session_state.get('summary_curiosity_2'),
    }

    keys_to_validate = [
        'sam1_2', 'sam2_2', 'sam3_2', 'sam_open_feedback_2', 'summary_confidence_2', 'summary_curiosity_2'
    ]

    missing = validate_session_keys(keys_to_validate)

    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
    else:
        st.switch_page("pages/transfer_test1.py")