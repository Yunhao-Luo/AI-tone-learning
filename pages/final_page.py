import streamlit as st
from ui_utils import hide_sidebar, save_all_experiment_data, make_json_safe
import json

hide_sidebar(set_wide=False)

st.title("Thank you for your participation in the study!")

# Save all experimental data using the comprehensive function
try:
    filename = save_all_experiment_data()
    st.success("✅ Your responses have been successfully saved!")
    st.info(f"📁 Data file: `{filename}`")
    
except Exception as e:
    st.error("⚠️ There was an error saving your data.")
    
    # Get prolific ID for error reporting
    prolific_id = st.session_state.get('prolific_id', 'unknown_id')
    st.warning(f"**Please contact the researcher immediately with your Prolific ID: {prolific_id}**")
    st.code(f"Error details: {str(e)}")
    
    # Provide download backup
    session_data = make_json_safe(dict(st.session_state))
    
    st.download_button(
        label="📥 Download your responses as backup",
        data=json.dumps(session_data, indent=2),
        file_name=f"backup_{prolific_id}.json",
        mime="application/json"
    )

st.divider()

st.markdown("""
### Next Steps
1. Return to the Prolific study page
2. Enter the completion code to receive credit
3. You may now close this window

**Completion Code:** `TONE2025COMPLETE`  
*(Update this with your actual Prolific completion code)*

If you encountered any technical issues, please contact: **rose.e.wang@wustl.edu**
""")

# Optional: Debug view
with st.expander("🔍 Debug Information (optional)"):
    st.write("**Data successfully collected for:**")
    st.write(f"- Prolific ID: `{st.session_state.get('prolific_id', 'NOT SET')}`")
    st.write(f"- Education: `{st.session_state.get('education', 'NOT SET')}`")
    st.write(f"- Initial summary: {len(st.session_state.get('user_answer', ''))} characters")
    st.write(f"- Revised summary: {len(st.session_state.get('user_answer_second', ''))} characters")
    st.write(f"- Chat messages: {len(st.session_state.get('history', []))} exchanges")
    st.write(f"- Transfer test answers: {sum([1 for i in range(1,5) if st.session_state.get(f'ttest_{i}_ans')])}/4 completed")