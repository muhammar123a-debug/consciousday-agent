import streamlit as st
from db.db import get_entries

st.title("📅 Reflection History")

entries = get_entries()

if entries:
    for entry in entries:
        st.markdown(f"### 🗓️ {entry[1]}")
        st.write(f"**Journal:** {entry[2]}")
        st.write(f"**Intention:** {entry[3]}")
        st.write(f"**Dream:** {entry[4]}")
        st.write(f"**Priorities:** {entry[5]}")
        st.write(f"**Reflection & Strategy:** {entry[6]}")
        st.divider()
else:
    st.info("No past entries found.")
