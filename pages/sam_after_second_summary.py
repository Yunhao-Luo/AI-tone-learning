import streamlit as st

# SAM
st.divider()
st.write("Please rate your current feelings by placing selecting the number on the scale that best represents your experience. You can select a number under any figure or a number between figures")
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

if st.button("Submit"):
    st.switch_page("pages/transfer_test1.py")