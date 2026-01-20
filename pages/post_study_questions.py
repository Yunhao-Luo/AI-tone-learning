import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# Cognitive Effort
# Trust toward AI
# Perception of AI
# Confidence aobut learning

quiz_performance = st.select_slider(
    "**How well do you think you did on the quiz just now?**",
    options=range(1, 8),
    key="quiz_performance"
)
likert_labels(left="Very Poorly", right="Very Well")


rewatch = st.radio(
    "**Do you think watching the video again after the AI feedback and before the quiz would have been helpful?**",
    options=['Yes', 'No'],
    key="rewatch"
)

st.divider()

rely = st.select_slider(
    "**I relied on the AI feedback rather than generating my own revisions.**",
    options=range(1, 8),
    key="rely"
)
likert_labels(left="Not at all", right="A lot")

confidencewoai = st.select_slider(
    "**I could explain how lightning forms without looking back at the AI feedback.**",
    options=range(1, 8),
    key="confidencewoai"
)
likert_labels(left="Not at all", right="A lot")

depend = st.select_slider(
    "**The feedback told me what to write more than it helped me understand why.**",
    options=range(1, 8),
    key="depend"
)
likert_labels(left="Not at all", right="A lot")

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
    "**The AI feedback felt overly critical.**",
    options=range(1, 8),
    key="critical"
)
likert_labels(left="Not at all", right="A lot")


trust = st.select_slider(
    "**I would trust this AI to give me feedback on other science topics.**",
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

st.divider()

need_to_learn = st.select_slider(
    "**After receiving AI feedback, I wanted to explore the topic further.**",
    options=range(1, 8),
    key="need_to_learn"
)

curiosity = st.select_slider(
    "**After receiving AI feedback, I wanted to explore the topic further.**",
    options=range(1, 8),
    key="curiosity"
)

st.divider()

ai_roles = st.text_input(
    "**What role did you believe this AI was fulfilling in your learning process? e.g., tutor, teacher, peer, a tool.**"
)

ai_learning_tools = st.text_input(
    "**Do you use any AI tools for learning? If so, what are they?**"
)

feedback_format = st.text_input(
    "**Do you like the way AI provides feedback in this study to assist you in learning?**"
)

improvements = st.text_input(
    "**What other kinds of feedback would be helpful from an AI study peer?**"
)

other_feedback = st.text_input(
    "**Do you have anything else about your learning experience that you want to share with us?**"
)

if st.button("Submit"):
    st.session_state['post_feedback'] = {
        'quiz_performance': quiz_performance,
        'rewatch': rewatch,
        'improve': improve,
        'clarity': clarity,
        'reflect': reflect,
        'supportive': supportive,
        'critical': critical,
        'trust': trust,
        'prefer': prefer,
        'confidence': confidence,
        'ai_learning_tools': ai_learning_tools,
        'feedback_format': feedback_format,
        'need_to_learn': need_to_learn,
        'curiosity': curiosity,
        'improvements': improvements,
        'rely': rely,
        'confidencewoai': confidencewoai,
        'depend': depend,
        'other_feedback': other_feedback,
    }
    
    st.switch_page("pages/final_page.py")