import streamlit as st
from openai import OpenAI

PROMPT_TEMPLATE = """
You are a daily reflection and planning assistant. Your goal is to:
1. Reflect on the user's journal and dream input
2. Interpret the user's emotional and mental state
3. Understand their intention and 3 priorities
4. Generate a practical, energy-aligned strategy for their day

INPUT:
Morning Journal: {journal}
Intention: {intention}
Dream: {dream}
Top 3 Priorities: {priorities}

OUTPUT:
1. Inner Reflection Summary
2. Dream Interpretation Summary
3. Energy/Mindset Insight
4. Suggested Day Strategy (time-aligned tasks)
"""

def get_agent_response(journal, intention, dream, priorities):
    try:
        # 1️⃣ Load API key from Streamlit secrets
        api_key = st.secrets["OPENROUTER_API_KEY"]
        if not api_key:
            return "API key not found in Streamlit secrets!"

        # 2️⃣ Initialize OpenAI client for OpenRouter (v1.0+ style)
        client = OpenAI(
            api_key=api_key,
            api_base="https://openrouter.ai/api/v1"
        )

        # 3️⃣ Prepare final prompt
        final_prompt = PROMPT_TEMPLATE.format(
            journal=journal,
            intention=intention,
            dream=dream,
            priorities=priorities
        )

        # 4️⃣ Make API call using new interface
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # OpenRouter model
            messages=[
                {"role": "system", "content": "You are a helpful daily reflection assistant."},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.7
        )

        # 5️⃣ Return assistant response safely
        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error calling API: {e}"
