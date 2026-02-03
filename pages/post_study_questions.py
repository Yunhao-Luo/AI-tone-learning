import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# Trust toward AI
# - I would trust this AI to help me learn other science topics. (add)

# Cognitive Effort
# - I put in a lot of effort to understand the AI's feedback. (add)
# - The AI communicated ideas in a clear and understandable way. (add)
# - I found myself mentally working hard to follow the AI's reasoning. (add)

# Perception of AI
# - The AI was likable.
# - The AI was competent.
# - The feedback felt supportive.

# Usefulness of AI
# - The AI feedback helped me improve my explanation.
# - The AI feedback made it clear what I should change.
# - The AI feedback made me reflect on gaps in my understanding.
# - The AI feedback I received facilitated my learning. (add)
# - I would use this AI to learn more advanced science topics. (add)

# Dependence on AI
# - I relied on the AI feedback rather than generating my own revisions.
# - I could explain how lightning forms without looking back at the AI feedback.
# - The feedback told me what to write more than it helped me understand why.

# Confidence aobut learning
# - How well do you think you did on the quiz just now?
# - I feel confident that I now understand how lightning forms.
# - How much do you still need to learn to fully understand how lightning forms?

############### SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.select_slider(
    label="1",
    options=range(1, 10),
    key="sam1_1",
    label_visibility="hidden"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.select_slider(
    label="2",
    options=range(1, 10),
    key="sam2_1",
    label_visibility="hidden"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.select_slider(
    label="3",
    options=range(1, 10),
    key="sam3_1",
    label_visibility="hidden"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**"
)

st.divider()

############### Likert
trust = st.select_slider(
    "**I would trust this AI to help me learn other science topics.**",
    options=range(1, 8),
    key="trust"
)
likert_labels()

##############

effort_to_understand = st.select_slider(
    "**I put in a lot of effort to understand the AI's feedback.**",
    options=range(1, 8),
    key="effort_to_understand"
)
likert_labels()

clear_to_understand = st.select_slider(
    "**The AI communicated ideas in a clear and understandable way.**",
    options=range(1, 8),
    key="clear_to_understand"
)
likert_labels()

mental_hard = st.select_slider(
    "**I found myself mentally working hard to follow the AI's reasoning.**",
    options=range(1, 8),
    key="mental_hard"
)
likert_labels()

##############

likable = st.select_slider(
    "**The AI was likable.**",
    options=range(1, 8),
    key="likable"
)
likert_labels()

competent = st.select_slider(
    "**The AI was competent.**",
    options=range(1, 8),
    key="competent"
)
likert_labels()

supportive = st.select_slider(
    "**The feedback felt supportive.**",
    options=range(1, 8),
    key="supportive"
)
likert_labels()

critical = st.select_slider(
    "**The AI feedback felt overly critical.**",
    options=range(1, 8),
    key="critical"
)
likert_labels()

##############
attention1 = st.select_slider(
    "**Please select disagree strongly. This is an attention check question.**",
    options=range(1, 8),
    key="attention1"
)
likert_labels()
##############

improve = st.select_slider(
    "**The AI feedback helped me improve my explanation.**",
    options=range(1, 8),
    key="improve"
)
likert_labels()

clarity = st.select_slider(
    "**The AI feedback made it clear what I should change.**",
    options=range(1, 8),
    key="clarity"
)
likert_labels()


reflect = st.select_slider(
    "**The AI feedback made me reflect on gaps in my understanding.**",
    options=range(1, 8),
    key="reflect"
)
likert_labels()

facilitated = st.select_slider(
    "**The AI feedback I received facilitated my learning.**",
    options=range(1, 8),
    key="facilitated"
)
likert_labels()

learn_advanced = st.select_slider(
    "**I would use this AI to learn more advanced science topics.**",
    options=range(1, 8),
    key="learn_advanced"
)
likert_labels()

##############

rely = st.select_slider(
    "**I relied on the AI feedback rather than generating my own revisions.**",
    options=range(1, 8),
    key="rely"
)
likert_labels()

confidencewoai = st.select_slider(
    "**I could explain how lightning forms without looking back at the AI feedback.**",
    options=range(1, 8),
    key="confidencewoai"
)
likert_labels()

depend = st.select_slider(
    "**The feedback told me what to write more than it helped me understand why.**",
    options=range(1, 8),
    key="depend"
)
likert_labels()

##############

quiz_performance = st.select_slider(
    "**How well do you think you did on the quiz just now?**",
    options=range(1, 8),
    key="quiz_performance"
)
likert_labels(left="Very poorly", right="Very well")

confidence = st.select_slider(
    "**I feel confident that I now understand how lightning forms.**",
    options=range(1, 8),
    key="confidence"
)
likert_labels()

need_to_learn = st.select_slider(
    "**How much do you still need to learn to fully understand how lightning forms?**",
    options=range(1, 8),
    key="need_to_learn"
)
likert_labels(left="Nothing", right="A lot")

##############

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
        'improve': improve,
        'clarity': clarity,
        'reflect': reflect,
        'likable': likable,
        'competent': competent,
        'supportive': supportive,
        'critical': critical,
        'trust': trust,
        'confidence': confidence,
        'ai_learning_tools': ai_learning_tools,
        'feedback_format': feedback_format,
        'need_to_learn': need_to_learn,
        'improvements': improvements,
        'rely': rely,
        'confidencewoai': confidencewoai,
        'depend': depend,
        'other_feedback': other_feedback,
    }
    
    st.switch_page("pages/final_page.py")