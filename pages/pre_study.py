import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

prolific_id = st.text_input("**Prolific ID:**")
education = st.radio(
    "Education Level:",
    options=['High School Degree', 'College Degree', 'Master\'s Degree', 'PhD Degree', 'Others'],
    index=None
)
major = st.text_input("What subject are you interested in studying?")
AI_usage = st.radio(
    label="How often do you use AI?",
    options=['Daily', 'Few times a week', 'Few times a month', 'Few times a year','Never'],
    index=None
)

st.divider()

### AIAS ###
st.write("### AI Attitudes")
aias_1 = st.pills(
    label = "I believe that AI will improve my life.",
    options=range(1, 11),
    key="aias_1",
    selection_mode="single",
    width="stretch"
)
likert_labels()

aias_2 = st.pills(
    label = "I believe that AI will improve my work.",
    options=range(1, 11),
    key="aias_2",
    selection_mode="single",
    width="stretch"
)
likert_labels()

aias_3 = st.pills(
    label = "I think I will use AI technology in the future.",
    options=range(1, 11),
    key="aias_3",
    selection_mode="single",
    width="stretch"
)
likert_labels()

aias_4 = st.pills(
    label = "I think AI technology is positive for humanity.",
    options=range(1, 11),
    key="aias_4",
    selection_mode="single",
    width="stretch"
)
likert_labels()

st.divider()

### TIPI ###
st.write("### Personality")
st.write("I see myself as...")

extraverted = st.pills(
    label = "**Extraverted, enthusiastic**",
    options=range(1, 8),
    key="tipi_1",
    selection_mode="single",
    width="stretch"
)
likert_labels()

critical = st.pills(
    label = "**Critical, quarrelsome**",
    options=range(1, 8),
    key="tipi_2",
    selection_mode="single",
    width="stretch"
)
likert_labels()

dependable = st.pills(
    label = "**Dependable, self-disciplined**",
    options=range(1, 8),
    key="tipi_3",
    selection_mode="single",
    width="stretch"
)
likert_labels()

anxious = st.pills(
    label = "**Anxious, easily upset**",
    options=range(1, 8),
    key="tipi_4",
    selection_mode="single",
    width="stretch"
)
likert_labels()

open = st.pills(
    label = "**Open to new experiences, complex**",
    options=range(1, 8),
    key="tipi_5",
    selection_mode="single",
    width="stretch"
)
likert_labels()

reserved = st.pills(
    label = "**Reserved, quiet**",
    options=range(1, 8),
    key="tipi_6",
    selection_mode="single",
    width="stretch"
)
likert_labels()

sympathetic = st.pills(
    label = "**Sympathetic, warm**",
    options=range(1, 8),
    key="tipi_7",
    selection_mode="single",
    width="stretch"
)
likert_labels()

disorganized = st.pills(
    label = "**Disorganized, careless**",
    options=range(1, 8),
    key="tipi_8",
    selection_mode="single",
    width="stretch"
)
likert_labels()

calm = st.pills(
    label = "**Calm, emotionally stable**",
    options=range(1, 8),
    key="tipi_9",
    selection_mode="single",
    width="stretch"
)
likert_labels()

conventional = st.pills(
    label = "**Conventional, uncreative**",
    options=range(1, 8),
    key="tipi_10",
    selection_mode="single",
    width="stretch"
)
likert_labels()

st.divider()

### Receptivity to Instructional Feedback (RIF) ###
st.write("### Feedback Receptivity")
st.write("Please rate your agreement with the following statements:")

rif_1 = st.pills(
    label="I am open to incorporating feedback to improve my performance.",
    options=range(1, 8),
    key="rif_1",
    selection_mode="single",
    width="stretch"
)
likert_labels()  

rif_2 = st.pills(
    label="I find constructive criticism helpful for my learning.",
    options=range(1, 8),
    key="rif_2",
    selection_mode="single",
    width="stretch"
)
likert_labels()

attention_1 = st.pills(
    label="I will select 5 for this question. This is an attention check.",
    options=range(1, 8),
    key="attention_1",
    selection_mode="single",
    width="stretch"
)
likert_labels()

rif_3 = st.pills(
    label="I actively seek out feedback on my work.",
    options=range(1, 8),
    key="rif_3",
    selection_mode="single",
    width="stretch"
)
likert_labels()

rif_4_reverse = st.pills(
    label="I often feel defensive when receiving feedback.",   
    options=range(1, 8),
    key="rif_4",
    selection_mode="single",
    width="stretch"
)
likert_labels()

rif_5 = st.pills(
    label="I value others' perspectives on my performance.",
    options=range(1, 8),
    key="rif_5",
    selection_mode="single",
    width="stretch"
)
likert_labels()

rif_6_reverse = st.pills(
    label="I tend to ignore feedback that doesn't align with my self-assessment.",   
    options=range(1, 8),
    key="rif_6",
    selection_mode="single",
    width="stretch"
)
likert_labels()

st.divider()

### Meterology Knowledge ###
me_knowledge1 = st.pills(
    label="Please rate your knowledge about meteorology on a scale from 1 (very little) to 5 (very much).",
    options=range(1, 6),
    key='me_knowledge1',
    selection_mode="single",
    width="stretch"
)

st.write("Please check all items that apply to you.")
me_knowledge2_1 = st.checkbox('I regularly read the weather maps in the newspaper')
me_knowledge2_2 = st.checkbox('I know what a cold front is')
me_knowledge2_3 = st.checkbox('I can distinguish between cumculous and nimbus clouds')
me_knowledge2_4 = st.checkbox('I know what a low pressure system is')
me_knowledge2_5 = st.checkbox('I can explain what makes the wind blow')
me_knowledge2_6 = st.checkbox('I know what this symbol means: [symbol for cold front]')
me_knowledge2_7 = st.checkbox('I know what this symbol means: [symbol for warm front]')

col1, col2= st.columns(2)
with col1:
    st.image("cold_front.png", width=300)
    st.caption("Symbol for code front")
with col2:
    st.image("warm_front.png", width=300)
    st.caption("Symbol for warm front")


st.divider()

### Neurodivergence Assessment ###
st.caption(
    "Neurodivergent: thinking or learning differs from typical (e.g., ADHD, autism, dyslexia). "
    "Neurotypical: thinking or learning is generally typical. Self-identification only."
)

neurodivergent = st.radio(
    "Do you identify as neurodivergent or neurotypical?",
    ["Neurodivergent", "Neurotypical", "Unsure", "Prefer not to say"],
    index=None
)


# SAM
st.divider()
st.write("Please rate your current feelings by selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam1",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam2",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.pills(
    label="empty",
    options=range(1, 10),
    key="sam3",
    label_visibility="hidden",
    selection_mode="single",
    width="stretch"
)

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    Please ensure your speakers are working and your volume is on.<br>
    Next, you will watch an instructional vidoe on a scientific topic. If the video does not begin playing automatically, please click the play button.
</div>
"""
st.markdown(html_reminder, unsafe_allow_html=True)

st.write("")
if st.button("Next"):
    st.session_state['prolific_id'] = prolific_id
    st.session_state['education'] = education
    st.session_state['major'] = major
    st.session_state['AI_usage'] = AI_usage
    st.session_state['neurodivergent'] = neurodivergent

    # AI Attitudes (AIAS)
    st.session_state['aias'] = {
        'aias_1': aias_1,
        'aias_2': aias_2,
        'aias_3': aias_3,
        'aias_4': aias_4,
    }

    # TIPI Personality
    st.session_state['tipi'] = {
        'extraverted': extraverted,
        'critical': critical,
        'dependable': dependable,
        'anxious': anxious,
        'open': open,
        'reserved': reserved,
        'sympathetic': sympathetic,
        'disorganized': disorganized,
        'calm': calm,
        'conventional': conventional,
    }

    # Feedback Receptivity (RIF)
    st.session_state['rif'] = {
        'rif_1': rif_1,
        'rif_2': rif_2,
        'rif_3': rif_3,
        'rif_4_reverse': rif_4_reverse,
        'rif_5': rif_5,
        'rif_6_reverse': rif_6_reverse,
    }

    # Meteorology knowledge
    st.session_state['meteorology_knowledge'] = {
        'self_rating': me_knowledge1,
        'read_weather_maps': me_knowledge2_1,
        'know_cold_front': me_knowledge2_2,
        'cloud_types': me_knowledge2_3,
        'low_pressure': me_knowledge2_4,
        'wind_explanation': me_knowledge2_5,
        'cold_front_symbol': me_knowledge2_6,
        'warm_front_symbol': me_knowledge2_7,
    }

    # SAM (affect measures)
    st.session_state['sam1_ans'] = {
        'happiness': sam1,
        'excitement': sam2,
        'confidence': sam3,
    }

    st.session_state['attention_check_pre'] = {
        "attention_1": attention_1
    }

    keys_to_validate = [
        'prolific_id',
        'education',
        'major',
        'AI_usage',
        'neurodivergent',
        'aias',
        'tipi',
        'rif',
        'meteorology_knowledge',
        'sam1_ans',
        'attention_check_pre',
    ]
    
    missing = validate_session_keys(keys_to_validate)

    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
        # st.warning("Missing responses for:")
        # for field in missing:
        #     st.write(f"- {field}")
    else:
        st.switch_page("pages/video.py")