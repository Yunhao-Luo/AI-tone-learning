import streamlit as st
import os
from datetime import datetime
import json
from ui_utils import *

st.title("Thank you for your participation in the study!")

session_data = make_json_safe(dict(st.session_state))

prolific_id = st.session_state.get("prolific_id", "unknown_id")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"./tone-study/data_{prolific_id}_{timestamp}.json"
dropbox_filename = '/tone-study/' + str(st.session_state['prolific_id'])

# Save to JSON
with open(filename, "w", encoding="utf-8") as f:
    json.dump(session_data, f, indent=2, ensure_ascii=False)

upload_file_to_dropbox(filename, dropbox_path=dropbox_filename)