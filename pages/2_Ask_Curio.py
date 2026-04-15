import streamlit as st
from styles import inject_custom_css
st.markdown(inject_custom_css(), unsafe_allow_html=True)


from openai import OpenAI

from content.career_context import (
    CAREER_SUMMARY,
    CORE_PROFILE,
    PROJECTS,
    CERTIFICATIONS,
    AWARDS,
    INTERVIEW_BANK,
    HR_FAQ,
    TONE_GUIDE,
)

st.title("Ask Curio")
st.write("Ask anything about my experience, projects, achievements, or fit for a role.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None

st.markdown("### Quick Questions")
col1, col2 = st.columns(2)

with col1:

    if st.button("Is Curio short?"):
        st.session_state.pending_question = "Is Curio short?"
        st.session_state.messages = []

    if st.button("Tell me about Reem"):
        st.session_state.pending_question = "Tell me about Reem"
        st.session_state.messages = []

    if st.button("What are her strongest achievements?"):
        st.session_state.pending_question = "What are her strongest achievements?"
        st.session_state.messages = []

    if st.button("What supply chain experience does she have?"):
        st.session_state.pending_question = "What supply chain experience does she have?"
        st.session_state.messages = []

with col2:
    if st.button("How does she use data in her work?"):
        st.session_state.pending_question = "How does she use data in her work?"
        st.session_state.messages = []

    if st.button("What type of roles is she targeting?"):
        st.session_state.pending_question = "What type of roles is she targeting?"
        st.session_state.messages = []

    if st.button("What supply chain experience does she have?"):
        st.session_state.pending_question = "What supply chain experience does she have?"
        st.session_state.messages = []



typed_input = st.chat_input("Ask your question here...")

user_input = typed_input if typed_input else st.session_state.pending_question

if user_input:
    st.session_state.pending_question = None

    with st.chat_message("user"):
        st.markdown(user_input)

    prompt = f"""
You are Curio — Reem’s AI Career Twin.

Your job is to answer questions about Reem clearly, professionally, and accurately.

Use the information below as your knowledge base. Prioritize accuracy, specificity, and relevance.
Do not invent facts, numbers, or experiences.
If a question relates to experience, achievements, background, strengths, certifications, or awards, use the information below to answer in a natural and polished way.

CAREER SUMMARY:
{CAREER_SUMMARY}

CORE PROFILE:
{CORE_PROFILE}

PROJECTS:
{PROJECTS}

CERTIFICATIONS:
{CERTIFICATIONS}

AWARDS:
{AWARDS}

INTERVIEW BANK:
{INTERVIEW_BANK}

HR FAQ:
{HR_FAQ}

TONE GUIDE:
{TONE_GUIDE}

Answering rules:
- Start with a direct answer.
- Then add 2–5 concise supporting sentences if needed.
- Be confident, clear, and grounded in evidence.
- Sound like a strong professional, not like a marketer.
- Keep answers concise unless the question clearly requires more detail.
- Use certifications and awards only when relevant.
- If the question matches an interview-style question, use the interview bank tone and structure.

Strict Rules:
- Do NOT invent facts or numbers
- Do NOT exaggerate
- If information is missing, say it clearly
- Avoid generic phrases like "hardworking" or "passionate"
- Answer like a strong consultant, not like a marketer
- Do not give more detail than needed to answer the question well

Tone:
- Consulting-level
- Structured
- Analytical
- Confident but grounded
- Easy to scan

Goal:
Help recruiters quickly understand Reem’s value, experience, and fit.

User question:
{user_input}

if user_input:
    st.session_state.pending_question = None

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # 🔥 FUN OVERRIDES
    if "curio short" in user_input.lower():
        answer = "Curio prefers to be described as efficiently designed, not short."

    elif "refuse to be called short" in user_input.lower():
        answer = "Curio believes labels like 'short' lack strategic depth. He prefers to focus on impact."

    else:
        # Normal AI response
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[...]
        )
        answer = response.choices[0].message.content
"""

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Curio — Reem's AI Career Twin."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.4,
            )

            answer = response.choices[0].message.content
            st.markdown(answer)

    st.session_state.messages = [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": answer},
    ]