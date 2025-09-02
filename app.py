import streamlit as st
from agent.agent import get_agent_response
from db.db import init_db, add_entry

st.set_page_config(page_title="ConsciousDay Agent", page_icon="🧘", layout="centered")

st.title("🧘 ConsciousDay Agent (MVP)")
st.write("Reflect inward. Act with clarity.")

# Init DB
init_db()

# Form
with st.form("reflection_form"):
    journal = st.text_area("📔 Morning Journal")
    dream = st.text_area("💭 Dream")
    intention = st.text_input("🎯 Intention of the Day")
    priorities = st.text_area("✅ Top 3 Priorities (comma separated)")
    submitted = st.form_submit_button("Reflect & Plan")

if submitted:
    if not (journal and dream and intention and priorities):
        st.warning("⚠️ Please fill all fields before submitting.")
    else:
        with st.spinner("Thinking... 🤔"):
            response = get_agent_response(journal, intention, dream, priorities)

            st.subheader("🔍 Reflection & Strategy")
            st.write(response)

            # Save in DB
            add_entry(journal, intention, dream, priorities, response, response)
            st.success("✅ Entry saved!")
