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
aias_1 = st.select_slider(
    label = "I believe that AI will improve my life.",
    options=range(1, 11)
)
likert_labels()

aias_2 = st.select_slider(
    label = "I believe that AI will improve my work.",
    options=range(1, 11)
)
likert_labels()

aias_3 = st.select_slider(
    label = "I think I will use AI technology in the future.",
    options=range(1, 11)
)
likert_labels()

aias_4 = st.select_slider(
    label = "I think AI technology is positive for humanity.",
    options=range(1, 11)
)
likert_labels()

st.divider()

### TIPI ###
extraverted = st.select_slider(
    label = "I see myself as **extraverted, enthusiastic**.",
    options=range(1, 8)
)
likert_labels()

critical = st.select_slider(
    label = "I see myself as **critical, quarrelsome**.",
    options=range(1, 8)
)
likert_labels()

dependable = st.select_slider(
    label = "I see myself as **dependable, self-disciplined**.",
    options=range(1, 8)
)
likert_labels()

anxious = st.select_slider(
    label = "I see myself as **anxious, easily upset**.",
    options=range(1, 8)
)
likert_labels()

open = st.select_slider(
    label = "I see myself as **open to new experiences, complex**.",
    options=range(1, 8)
)
likert_labels()

reserved = st.select_slider(
    label = "I see myself as **reserved, quiet**.",
    options=range(1, 8)
)
likert_labels()

sympathetic = st.select_slider(
    label = "I see myself as **sympathetic, warm**.",
    options=range(1, 8)
)
likert_labels()

disorganized = st.select_slider(
    label = "I see myself as **disorganized, careless**.",
    options=range(1, 8)
)
likert_labels()

calm = st.select_slider(
    label = "I see myself as **calm, emotionally stable**.",
    options=range(1, 8)
)
likert_labels()

conventional = st.select_slider(
    label = "I see myself as **conventional, uncreative**.",
    options=range(1, 8)
)
likert_labels()

html_reminder = """
<div style='background-color: #ff6347; color: #f0f2f6; padding: 10px;'>
    Please ensure your speakers are working and your volume is on. The next page contains important audio information.
</div>
"""
st.markdown(html_reminder, unsafe_allow_html=True)
if st.button("Next"):
    st.switch_page("pages/video.py")