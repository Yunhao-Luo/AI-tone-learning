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
sam1 = st.pills(
    label="1",
    options=range(1, 10),
    key="sam1_post",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.pills(
    label="2",
    options=range(1, 10),
    key="sam2_post",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.pills(
    label="3",
    options=range(1, 10),
    key="sam3_post",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)

sam_open = st.text_input(
    "**Could you explain why you selected the options above?**",
    key='sam_open_post'
)

st.divider()

#Likert

# Trust 
trust = st.pills(
    "**I would trust this AI to help me learn other science topics.**",
    options=range(1, 8),
    key="trust",
    selection_mode="single",
    width="stretch"
)
likert_labels()

trust_scientifically_correct = st.pills(
    "**I believed the AI’s explanation was scientifically correct.**",
    options=range(1, 8),
    key="trust_scientifically_correct",
    selection_mode="single",
    width="stretch"
)
likert_labels()

# Cognitive load 
effort_to_understand = st.pills(
    "**I put in a lot of effort to understand the AI's feedback.**",
    options=range(1, 8),
    key="effort_to_understand",
    selection_mode="single",
    width="stretch"
)
likert_labels()

clear_to_understand = st.pills(
    "**The AI communicated ideas in a clear and understandable way.**",
    options=range(1, 8),
    key="clear_to_understand",
    selection_mode="single",
    width="stretch"
)
likert_labels()

attention_1 = st.pills(
    "**I will select 2 for this question. This is an attention check.**",
    options=range(1, 8),
    key="attention_1",
    selection_mode="single",
    width="stretch"
)
likert_labels()

mental_hard = st.pills(
    "**I found myself mentally working hard to follow the AI's reasoning.**",
    options=range(1, 8),
    key="mental_hard",
    selection_mode="single",
    width="stretch"
)
likert_labels()

##############

# Likability / perception
likable = st.pills(
    "**The AI was likable.**",
    options=range(1, 8),
    key="likable",
    selection_mode="single",
    width="stretch"
)
likert_labels()

supportive = st.pills(
    "**The feedback felt supportive.**",
    options=range(1, 8),
    key="supportive",
    selection_mode="single",
    width="stretch"
)
likert_labels()

encouraged_to_keep_learning = st.pills(
    "**The AI feedback made me feel encouraged to keep learning.**",
    options=range(1, 8),
    key="encouraged_to_keep_learning",
    selection_mode="single",
    width="stretch"
)
likert_labels()

competent = st.pills(
    "**The AI was competent.**",
    options=range(1, 8),
    key="competent",
    selection_mode="single",
    width="stretch"
)
likert_labels()

ai_was_expert = st.pills(
    "**The AI was an expert.**",
    options=range(1, 8),
    key="ai_was_expert",
    selection_mode="single",
    width="stretch"
)
likert_labels()

critical = st.pills(
    "**The AI feedback felt overly critical.**",
    options=range(1, 8),
    key="critical",
    selection_mode="single",
    width="stretch"
)
likert_labels()

# Usefulness
improve = st.pills(
    "**The AI feedback helped me improve my explanation.**",
    options=range(1, 8),
    key="improve",
    selection_mode="single",
    width="stretch"
)
likert_labels()

clarity = st.pills(
    "**The AI feedback made it clear what I should change.**",
    options=range(1, 8),
    key="clarity",
    selection_mode="single",
    width="stretch"
)
likert_labels()

reflect = st.pills(
    "**The AI feedback made me reflect on gaps in my understanding.**",
    options=range(1, 8),
    key="reflect",
    selection_mode="single",
    width="stretch"
)
likert_labels()

facilitated = st.pills(
    "**The AI feedback I received facilitated my learning.**",
    options=range(1, 8),
    key="facilitated",
    selection_mode="single",
    width="stretch"
)
likert_labels()

learn_advanced = st.pills(
    "**I would use this AI to learn more advanced science topics.**",
    options=range(1, 8),
    key="learn_advanced",
    selection_mode="single",
    width="stretch"
)
likert_labels()

# Dependence
rely = st.pills(
    "**I relied on the AI feedback rather than generating my own revisions.**",
    options=range(1, 8),
    key="rely",
    selection_mode="single",
    width="stretch"
)
likert_labels()

confidencewoai = st.pills(
    "**I could explain how lightning forms without looking back at the AI feedback.**",
    options=range(1, 8),
    key="confidencewoai",
    selection_mode="single",
    width="stretch"
)
likert_labels()

depend = st.pills(
    "**The feedback told me what to write more than it helped me understand why.**",
    options=range(1, 8),
    key="depend",
    selection_mode="single",
    width="stretch"
)
likert_labels()


# Confidence 
quiz_performance = st.pills(
    "**How well do you think you did on the quiz just now?**",
    options=range(1, 8),
    key="quiz_performance",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Very poorly", right="Very well")

confidence = st.pills(
    "**I feel confident that I now understand how lightning forms.**",
    options=range(1, 8),
    key="confidence",
    selection_mode="single",
    width="stretch"
)
likert_labels()

need_to_learn = st.pills(
    "**How much do you still need to learn to fully understand how lightning forms?**",
    options=range(1, 8),
    key="need_to_learn",
    selection_mode="single",
    width="stretch"
)
likert_labels(left="Nothing", right="A lot")

# ============================================================
# Submit
# ============================================================
if st.button("Submit"):
    st.session_state['post_feedback'] = {
        # Existing fields (unchanged keys)
        'sam_1': st.session_state.get('sam1_post'),
        'sam_2': st.session_state.get('sam2_post'),
        'sam_3': st.session_state.get('sam3_post'),
        'sam_open': st.session_state.get('sam_open_post'),
        
        'trust': st.session_state.get('trust'),
        'trust_scientifically_correct': st.session_state.get('trust_scientifically_correct'),
        'effort_to_understand': st.session_state.get('effort_to_understand'),
        'clear_to_understand': st.session_state.get('clear_to_understand'),
        'mental_hard': st.session_state.get('mental_hard'),

        'attention_1': st.session_state.get('attention_1'),

        'likable': st.session_state.get('likable'),
        'supportive': st.session_state.get('supportive'),
        'encouraged_to_keep_learning': st.session_state.get('encouraged_to_keep_learning'),
        'competent': st.session_state.get('competent'),
        'ai_was_expert': st.session_state.get('ai_was_expert'),
        'critical': st.session_state.get('critical'),
        'improve': st.session_state.get('improve'),
        'clarity': st.session_state.get('clarity'),
        'reflect': st.session_state.get('reflect'),
        'facilitated': st.session_state.get('facilitated'),
        'learn_advanced': st.session_state.get('learn_advanced'),

        'rely': st.session_state.get('rely'),
        'confidencewoai': st.session_state.get('confidencewoai'),
        'depend': st.session_state.get('depend'),

        'quiz_performance': st.session_state.get('quiz_performance'),
        'confidence': st.session_state.get('confidence'),
        'need_to_learn': st.session_state.get('need_to_learn'),
    }

    keys_to_validate = [
        'sam_1', 'sam_2', 'sam_3', 'sam_open', 'trust', 'trust_scientifically_correct',
        'effort_to_understand', 'clear_to_understand', 'mental_hard', 'attention_1',
        'likable', 'supportive', 'encouraged_to_keep_learning', 'competent', 'ai_was_expert',
        'critical', 'improve', 'clarity', 'reflect', 'facilitated', 'learn_advanced',
        'rely', 'confidencewoai', 'depend', 'quiz_performance', 'confidence', 'need_to_learn'
    ]

    missing = validate_session_keys(keys_to_validate)

    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
    else:
        st.switch_page("pages/post_study_questions_open.py")