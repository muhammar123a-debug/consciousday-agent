from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import streamlit as st

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
    api_key = st.secrets["OPENROUTER_API_KEY"]

    llm = ChatOpenAI(
        model="openai/gpt-3.5-turbo",
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        temperature=0.7
    )

    prompt = PromptTemplate(
        input_variables=["journal", "intention", "dream", "priorities"],
        template=PROMPT_TEMPLATE,
    )

    final_prompt = prompt.format(
        journal=journal,
        intention=intention,
        dream=dream,
        priorities=priorities
    )

    response = llm.invoke(final_prompt)
    return response.content
