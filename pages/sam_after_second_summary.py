import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.select_slider(
    label="1",
    options=range(1, 10),
    key="sam1_2",
    label_visibility="hidden"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.select_slider(
    label="2",
    options=range(1, 10),
    key="sam2_2",
    label_visibility="hidden"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.select_slider(
    label="3",
    options=range(1, 10),
    key="sam3_2",
    label_visibility="hidden"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**"
)

summary_confidence = st.select_slider(
    "**How confidence are you that you performed well in your summary?**",
    options=range(1, 8),
    key="quiz_performance"
)
likert_labels(left="Not at all", right="Very much")

summary_curiosity = st.select_slider(
    "**How curious are you to find out the answer to how lightning forms?**",
    options=range(1, 8),
    key="summary_curiosity"
)
likert_labels(left="Not at all", right="Very much")

if st.button("Submit"):

    st.session_state['sam3_ans'] = {
        'happiness': sam1,
        'excitement': sam2,
        'confidence': sam3,
        'open': sam_open,
        "summary_confidence": summary_confidence,
        "summary_curiosity": summary_curiosity
    }
    st.switch_page("pages/transfer_test1.py")