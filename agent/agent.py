import os
import streamlit as st
from openai import OpenAI

PROMPT_TEMPLATE = """
You are a daily reflection and planning assistant. Your goal is:
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

        # 2️⃣ Set environment variables for OpenAI v1.0+ (required by OpenRouter)
        os.environ["OPENAI_API_KEY"] = api_key
        os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"

        # 3️⃣ Prepare the final prompt
        final_prompt = PROMPT_TEMPLATE.format(
            journal=journal,
            intention=intention,
            dream=dream,
            priorities=priorities
        )

        # 4️⃣ Initialize OpenAI client
        client = OpenAI()  # no params here in v1.0+

        # 5️⃣ Make the API call
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful daily reflection assistant."},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.7
        )

        # 6️⃣ Return the assistant response
        return response.choices[0].message["content"]

    except Exception as e:
        return f"Error calling API: {e}"
