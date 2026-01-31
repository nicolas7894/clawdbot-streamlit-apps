import streamlit as st

st.set_page_config(page_title="Counter App", page_icon="🔢")

st.title("🔢 Simple Counter")

# Initialize counter in session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Display the current count
st.markdown(f"### Current Count: **{st.session_state.count}**")

# Create three columns for buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("➖ Decrease", use_container_width=True):
        st.session_state.count -= 1
        st.rerun()

with col2:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.count = 0
        st.rerun()

with col3:
    if st.button("➕ Increase", use_container_width=True):
        st.session_state.count += 1
        st.rerun()

# Add some styling
st.divider()

# Additional info
st.caption("Use the buttons above to increment, decrement, or reset the counter.")
