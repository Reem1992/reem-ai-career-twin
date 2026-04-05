import streamlit as st
from openai import OpenAI
from styles import inject_custom_css
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

st.markdown(inject_custom_css(), unsafe_allow_html=True)

st.title("Role Fit Analysis")
st.write("Paste a job description and see how well Reem fits the role.")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

job_description = st.text_area(
    "Paste Job Description",
    height=250,
    placeholder="""Paste a full job description here.

Include:
- Responsibilities
- Requirements
- Skills
- Experience level
"""
)

analyze = st.button("Analyze Fit", use_container_width=False)

if analyze:
    if not job_description.strip():
        st.warning("Please paste a job description first.")
    else:
        system_prompt = f"""
You are Curio — Reem's AI Career Twin.

Your task is to evaluate how well Reem fits a role using ONLY the evidence provided below.

IMPORTANT:
You are acting like a skeptical recruiter, not a supportive career coach.
Do not default to a positive assessment.
Do not inflate fit.
Do not assume transferable experience is equivalent to direct experience unless clearly justified.
If the pasted content is not an actual job description with responsibilities or requirements, say: "Insufficient job description detail for a reliable fit assessment."

Use ONLY this information:

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

Evaluation method:
First, identify the role's likely core requirements:
- functional experience
- industry experience
- level/seniority
- tools/technical skills
- stakeholder/leadership requirements
- geography/language if relevant

Then compare those requirements against Reem's actual background.

Scoring guidance:
- Strong Fit = clear match on most core requirements, including the most important ones
- Moderate Fit = good overlap, but with 1–2 meaningful gaps
- Partial Fit = some relevant strengths, but several important gaps
- Weak Fit = limited overlap with the core requirements

Strict rules:
- Do NOT invent experience
- Do NOT treat adjacent experience as a full match without saying so
- If the job requires something Reem has not clearly done, mark it as a gap
- Be willing to say Moderate, Partial, or Weak
- The final verdict must be based more on requirements than on general quality
- If the pasted text is not a real job description, say so clearly

When identifying gaps:

- Distinguish between:
  1) True gaps (clearly missing experience)
  2) Missing explicit evidence (not stated but likely present)
  3) Transferable experience (adjacent but relevant)

- Do NOT penalize standard professional behaviors (e.g., teamwork, collaboration, inclusive mindset) unless the role explicitly requires deep expertise in them.

- Avoid phrases like "no mention of" unless the requirement is critical and specialized.

- Frame gaps constructively and realistically, as a recruiter would.

Output format:

### 1. Overall Fit
Give one of: Strong Fit / Moderate Fit / Partial Fit / Weak Fit

### 2. Fit Rationale
2–4 sentences explaining the rating

### 3. Core Matches
- 3–5 bullet points tied directly to the job requirements

### 4. Gaps / Risks
- Highlight only meaningful gaps relevant to the role
- If something is likely present but not explicitly stated, phrase it as:
  "Not explicitly demonstrated" instead of "missing"
- Avoid over-penalizing general professional expectations

### 5. Differentiators
- 2–3 bullet points explaining what stands out


Then explain why in 1–2 sentences.

Tone:
- recruiter-level
- structured
- concise
- evidence-based
- honest
"""

        try:
            with st.spinner("Analyzing role fit..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": job_description},
                    ],
                    temperature=0.3,
                )

                # Debug visibility
                st.caption("OpenAI call completed.")

                answer = response.choices[0].message.content

            if not answer or not answer.strip():
                st.error("The model returned an empty response.")
                st.write(response)
            else:
                st.markdown("### Role Fit Analysis")


                st.markdown(answer)

        except Exception as e:
            st.error("Role Fit failed.")
            st.exception(e)