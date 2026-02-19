import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# ============================================================
# Open-ended
# ============================================================
ai_roles = st.text_input(
    "**What role did you believe this AI was fulfilling in your learning process? e.g., tutor, teacher, peer, a tool.**",
    key='ai_roles'
)
ai_learning_tools = st.text_input(
    "**Do you use any AI tools for learning? If so, what are they?**",
    key='ai_learning_tools'
)
feedback_format = st.text_input(
    "**Do you like the way AI provides feedback in this study to assist you in learning?**",
    key='feedback_format'
)
improvements = st.text_input(
    "**What other kinds of feedback would be helpful from an AI study peer?**",
    key='improvements'
)
other_feedback = st.text_input(
    "**Do you have anything else about your learning experience that you want to share with us?**",
    key='other_feedback'
)

if st.button("Submit"):
    st.session_state['post_feedback_open'] = {
        'ai_roles': ai_roles,
        'ai_learning_tools': ai_learning_tools,
        'feedback_format': feedback_format,
        'improvements': improvements,
        'other_feedback': other_feedback
    }

    keys_to_validate = [
        'ai_roles', 'ai_learning_tools', 'feedback_format', 'improvements', 'other_feedback'
    ]

    missing = validate_session_keys(keys_to_validate)

    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
    else:
        st.switch_page("pages/final_page.py")