import streamlit as st
from ui_utils import *

hide_sidebar(set_wide=False)

st.title("Welcome to AI Learning Study")

intro = '''
In this study, you will watch a short video, summarize your understanding, and then receive feedback from an AI learning peer.
'''
st.write(intro)

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
aias_1 = st.select_slider(
    label = "I believe that AI will improve my life.",
    options=range(1, 11),
    key="aias_1"
)
likert_labels()

aias_2 = st.select_slider(
    label = "I believe that AI will improve my work.",
    options=range(1, 11),
    key="aias_2"
)
likert_labels()

aias_3 = st.select_slider(
    label = "I think I will use AI technology in the future.",
    options=range(1, 11),
    key="aias_3"
)
likert_labels()

aias_4 = st.select_slider(
    label = "I think AI technology is positive for humanity.",
    options=range(1, 11),
    key="aias_4"
)
likert_labels()

st.divider()

### TIPI ###
st.write("### Personality")
st.write("I see myself as...")

extraverted = st.select_slider(
    label = "**Extraverted, enthusiastic**",
    options=range(1, 8),
    key="tipi_1"
)
likert_labels()

critical = st.select_slider(
    label = "**Critical, quarrelsome**",
    options=range(1, 8),
    key="tipi_2"
)
likert_labels()

dependable = st.select_slider(
    label = "**Dependable, self-disciplined**",
    options=range(1, 8),
    key="tipi_3"
)
likert_labels()

anxious = st.select_slider(
    label = "**Anxious, easily upset**",
    options=range(1, 8),
    key="tipi_4"
)
likert_labels()

open = st.select_slider(
    label = "**Open to new experiences, complex**",
    options=range(1, 8),
    key="tipi_5"
)
likert_labels()

reserved = st.select_slider(
    label = "**Reserved, quiet**",
    options=range(1, 8),
    key="tipi_6"
)
likert_labels()

sympathetic = st.select_slider(
    label = "**Sympathetic, warm**",
    options=range(1, 8),
    key="tipi_7"
)
likert_labels()

disorganized = st.select_slider(
    label = "**Disorganized, careless**",
    options=range(1, 8),
    key="tipi_8"
)
likert_labels()

calm = st.select_slider(
    label = "**Calm, emotionally stable**",
    options=range(1, 8),
    key="tipi_9"
)
likert_labels()

conventional = st.select_slider(
    label = "**Conventional, uncreative**",
    options=range(1, 8),
    key="tipi_10"
)
likert_labels()

st.divider()

### Receptivity to Instructional Feedback (RIF) ###
st.write("### Feedback Receptivity")
st.write("Please rate your agreement with the following statements:")

rif_1 = st.select_slider(
    label="I am open to incorporating feedback to improve my performance.",
    options=range(1, 8),
    key="rif_1"
)
likert_labels()  

rif_2 = st.select_slider(
    label="I find constructive criticism helpful for my learning.",
    options=range(1, 8),
    key="rif_2"
)
likert_labels()

rif_3 = st.select_slider(
    label="I actively seek out feedback on my work.",
    options=range(1, 8),
    key="rif_3"
)
likert_labels()

rif_4_reverse = st.select_slider(
    label="I often feel defensive when receiving feedback.",   
    options=range(1, 8),
    key="rif_4"
)
likert_labels()

rif_5 = st.select_slider(
    label="I value others' perspectives on my performance.",
    options=range(1, 8),
    key="rif_5"
)
likert_labels()

rif_6_reverse = st.select_slider(
    label="I tend to ignore feedback that doesn't align with my self-assessment.",   
    options=range(1, 8),
    key="rif_6"
)
likert_labels()

st.divider()

### Meterology Knowledge ###
me_knowledge1 = st.select_slider(
    label="Please rate your knowledge about meteorology on a scale from 1 (very little) to 5 (very much).",
    options=range(1, 6),
    key='me_knowledge1'
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
st.write("Please rate your current feelings by placing selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
st.write("Happiness")
st.image('SAM1.jpg')
sam1 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam1",
    label_visibility="hidden"
)
st.write("Excitement")
st.image('SAM2.jpg')
sam2 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam2",
    label_visibility="hidden"
)
st.write("Confidence")
st.image('SAM3.jpg')
sam3 = st.select_slider(
    label="empty",
    options=range(1, 10),
    key="sam3",
    label_visibility="hidden"
)

st.divider()

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    Please ensure your speakers are working and your volume is on. The next page contains important audio information.
</div>
"""
st.markdown(html_reminder, unsafe_allow_html=True)

# Validation before allowing to proceed
def validate_all_questions():
    """Check if all required questions have been answered"""
    missing_fields = []
    
    # Check text inputs
    if not prolific_id or prolific_id.strip() == "":
        missing_fields.append("Prolific ID")
    if not major or major.strip() == "":
        missing_fields.append("Subject interest")
    
    # Check radio buttons
    if education is None:
        missing_fields.append("Education Level")
    if AI_usage is None:
        missing_fields.append("AI Usage frequency")
    if neurodivergent is None:
        missing_fields.append("Neurodivergent/Neurotypical identification")
    
    # Check slider
    slider_questions = {
        "aias_1": "AI will improve my life",
        "aias_2": "AI will improve my work", 
        "aias_3": "Will use AI in future",
        "aias_4": "AI is positive for humanity",
        "tipi_1": "Extraverted personality",
        "tipi_2": "Critical personality",
        "tipi_3": "Dependable personality",
        "tipi_4": "Anxious personality",
        "tipi_5": "Open personality",
        "tipi_6": "Reserved personality",
        "tipi_7": "Sympathetic personality",
        "tipi_8": "Disorganized personality",
        "tipi_9": "Calm personality",
        "tipi_10": "Conventional personality",
        "rif_1": "Open to feedback",
        "rif_2": "Constructive criticism helpful",
        "rif_3": "Actively seek feedback",
        "rif_4": "Feel defensive",
        "rif_5": "Value others' perspectives",
        "rif_6": "Ignore misaligned feedback"
    }
    
    # Check if sliders have been set (they exist in session state)
    for key, description in slider_questions.items():
        if key not in st.session_state:
            missing_fields.append(description)
    
    return missing_fields

st.write("")
if st.button("Next"):
    missing = validate_all_questions()
    
    if missing:
        st.error(f"⚠️ **Please answer all questions before proceeding.**")
        st.warning("Missing responses for:")
        for field in missing:
            st.write(f"- {field}")
    else:
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

        st.switch_page("pages/video.py")