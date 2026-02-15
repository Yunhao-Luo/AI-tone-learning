import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

# Post study measures: (22 items)

# Affective-relational stance with AI (Did I trust/like the AI as a partner)

### Trust
# I would trust this AI to help me learn other science topics.
# I believed the AI’s explanation was scientifically correct

### Likability
# The AI was likable.
# The feedback felt supportive.
# The AI feedback felt overly critical
# The AI feedback made me feel encouraged to keep learning

### Competence
# The AI was competent.
# The AI was an expert

# Cognitive load (How hard was thinking with AI) 

### Cognitive Load
# I put in a lot of effort to understand the AI's feedback.
# The AI communicated ideas in a clear and understandable way.
# I found myself mentally working hard to follow the AI's reasoning. 

# Learning Outcome (Did AI help me learn)

### Usefulness 
# The AI feedback helped me improve my explanation.
# The AI feedback made it clear what I should change.
# The AI feedback made me reflect on gaps in my understanding.
# The AI feedback I received facilitated my learning. 
# I would use this AI to learn more advanced science topics. 

# Metacognition Monitoring (Do I understand my own learning & reliance)

### Confidence
# How well do you think you did on the quiz just now?
# I feel confident that I now understand how lightning forms.
# How much do you still need to learn to fully understand how lightning forms?

### Dependence
# I relied on the AI feedback rather than generating my own revisions.
# I could explain how lightning forms without looking back at the AI feedback.
# The feedback told me what to write more than it helped me understand why.

#SAM
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

#Likert

# Trust 
trust = st.select_slider(
    "**I would trust this AI to help me learn other science topics.**",
    options=range(1, 8),
    key="trust"
)
likert_labels()

trust_scientifically_correct = st.select_slider(
    "**I believed the AI’s explanation was scientifically correct.**",
    options=range(1, 8),
    key="trust_scientifically_correct"
)
likert_labels()

# Cognitive load 
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

attention_1 = st.select_slider(
    "**I will select 2 for this question. This is an attention check.**",
    options=range(1, 8),
    key="attention_1"
)
likert_labels()

mental_hard = st.select_slider(
    "**I found myself mentally working hard to follow the AI's reasoning.**",
    options=range(1, 8),
    key="mental_hard"
)
likert_labels()

##############

# Likability / perception
likable = st.select_slider(
    "**The AI was likable.**",
    options=range(1, 8),
    key="likable"
)
likert_labels()

supportive = st.select_slider(
    "**The feedback felt supportive.**",
    options=range(1, 8),
    key="supportive"
)
likert_labels()

encouraged_to_keep_learning = st.select_slider(
    "**The AI feedback made me feel encouraged to keep learning.**",
    options=range(1, 8),
    key="encouraged_to_keep_learning"
)
likert_labels()

competent = st.select_slider(
    "**The AI was competent.**",
    options=range(1, 8),
    key="competent"
)
likert_labels()

ai_was_expert = st.select_slider(
    "**The AI was an expert.**",
    options=range(1, 8),
    key="ai_was_expert"
)
likert_labels()

critical = st.select_slider(
    "**The AI feedback felt overly critical.**",
    options=range(1, 8),
    key="critical"
)
likert_labels()

# Usefulness
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

# Dependence
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


# Confidence 
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

# ============================================================
# Submit
# ============================================================
if st.button("Submit"):
    st.session_state['post_feedback'] = {
        # Existing fields (unchanged keys)
        'sam_1': sam1,
        'sam_2': sam2,
        'sam_3': sam3,
        'sam_open': sam_open,
        
        'trust': trust,
        'trust_scientifically_correct': trust_scientifically_correct,
        'effort_to_understand': effort_to_understand,
        'clear_to_understand': clear_to_understand,
        'mental_hard': mental_hard,

        'attention_1': attention_1,

        'likable': likable,
        'supportive': supportive,
        'encouraged_to_keep_learning': encouraged_to_keep_learning,
        'competent': competent,
        'ai_was_expert': ai_was_expert,
        'critical': critical,
        'improve': improve,
        'clarity': clarity,
        'reflect': reflect,
        'facilitated': facilitated,
        'learn_advanced': learn_advanced,

        'rely': rely,
        'confidencewoai': confidencewoai,
        'depend': depend,

        'quiz_performance': quiz_performance,
        'confidence': confidence,
        'need_to_learn': need_to_learn,
    }

    st.switch_page("pages/post_study_questions_open.py")