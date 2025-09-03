import os
from openai import OpenAI

# OpenRouter client init
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

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
"""

def get_agent_response(journal, intention, dream, priorities):
    final_prompt = PROMPT_TEMPLATE.format(
        journal=journal,
        intention=intention,
        dream=dream,
        priorities=priorities
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # ya jo bhi tum OpenRouter par use kar rahe ho
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.7,
        )

        # ✅ New SDK me dict style nahi chalega
        return response.choices[0].message.content

    except Exception as e:
        return f"Error calling API: {str(e)}"
