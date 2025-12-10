import streamlit as st
from ui_utils import *

hide_sidebar()

# What could you do to decrease the intensity of lightning?
# Suppose you see clouds in the sky, but no lightning. Why not?
# What does air temperature have to do with lightning?
# What causes lightning?

st.title("Please answer the following questions.")
q1 = st.text_area(
    label = "What could you do to decrease the intensity of lightning?",
    height=100,
    key='q1'
)
st.write("#")
q2 = st.text_area(
    label = "Suppose you see clouds in the sky, but no lightning. Why not?",
    height=100,
    key='q2'
)
st.write("#")
q3 = st.text_area(
    label = "What does air temperature have to do with lightning?",
    height=100,
    key='q3'
)
st.write("#")
q4 = st.text_area(
    label = "What causes lightning?",
    height=100,
    key='q4'
)
st.write("#")
submit = st.button(
    label="Submit"
)

if submit:
    st.session_state['transfer_q1'] = q1
    st.session_state['transfer_q2'] = q2
    st.session_state['transfer_q3'] = q3
    st.session_state['transfer_q4'] = q4
    st.switch_page("pages/final_page.py")