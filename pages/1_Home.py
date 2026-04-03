import streamlit as st
from styles import inject_custom_css

st.set_page_config(
    page_title="Curio — Reem's AI Career Twin",
    page_icon="🧠",
    layout="wide"
)

st.markdown(inject_custom_css(), unsafe_allow_html=True)


# Inject styles
st.markdown(inject_custom_css(), unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

col1, col2 = st.columns([3, 1], gap="large")

with col1:
    st.markdown(
        '<div class="curio-tag">AI-powered career experience</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="curio-title">Curio — Reem’s AI Career Twin</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="curio-lead">
            Instead of a static CV, I built an AI career twin that lets you explore my experience,
            thinking, and impact in a more dynamic way.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="curio-sub">
            Built without a technical background to demonstrate how AI can be used to structure
            and communicate professional experience more effectively.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="curio-sub">
            Go beyond bullet points—explore real projects, measurable outcomes, challenges,
            and the way I approach problem-solving.
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown('<div style="margin-top: 70px;">', unsafe_allow_html=True)
    st.image("assets/profile.jpg", width=260)
    st.markdown('</div>', unsafe_allow_html=True)

# ✅ Divider OUTSIDE columns (fixed)
st.markdown('<div class="curio-divider"></div>', unsafe_allow_html=True)

# =========================
# WHAT I BRING
# =========================

st.markdown("## What I bring")

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Operations & Transformation</div>
            <div class="curio-muted">
              Operating model design, supply chain optimization, and KPI frameworks to improve performance across complex, multi-site environments.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Operational Analytics</div>
            <div class="curio-muted">
                Python, and dashboards to turn supply chain and facility operations data into clear, actionable decisions.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Measurable Impact</div>
            <div class="curio-muted">
                Cost reduction, faster execution, and improved service performance across operations, supply chain, and facility management initiatives.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================
# EXPLORE CURIO
# =========================

st.markdown("## Explore Curio")

d1, d2, d3 = st.columns(3, gap="large")

with d1:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Ask Curio</div>
            <div class="curio-muted">
                Explore my background, achievements, projects, and the way I think
                through AI-powered answers.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d2:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Role Fit</div>
            <div class="curio-muted">
                Paste a job description and get an instant, structured assessment of
                how well I fit the role.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d3:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Contact</div>
            <div class="curio-muted">
                Reach out directly if you’d like to connect, discuss a role, or explore
                a fit conversation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


   # =========================
# CTA BUTTONS (FIXED)
# =========================

st.markdown('<div style="margin-top: 14px;"></div>', unsafe_allow_html=True)

cta1, cta2, cta3 = st.columns(3, gap="large")

with cta1:
    if st.button("⚙ Ask Curio", key="cta_ask", use_container_width=True):
        st.switch_page("pages/2_Ask_Curio.py")

with cta2:
    if st.button("▤ Analyze Role Fit", key="cta_fit", use_container_width=True):
        st.switch_page("pages/3_Role_Fit.py")

with cta3:
    if st.button("✉ Contact Reem", key="cta_contact", use_container_width=True):
        st.switch_page("pages/4_Contact_Reem.py")

# =========================
# THE AI BEHIND THE EXPERIENCE
# =========================

st.markdown("## The AI behind the experience")

r1, r2 = st.columns([1, 3], gap="large")

with r1:
    st.image("assets/curio_robot.jpg", width=260)

with r2:
    st.markdown(
        """
        <div class="curio-card">
            <div class="curio-section-title">Meet Curio</div>
            <div class="curio-muted">
                Curio is the AI layer of this experience — built to make it easier to explore
                my background, achievements, problem-solving approach, and fit for roles in a
                more dynamic way than a traditional CV.
            </div>
            <br>
            <div class="curio-section-title">What makes it different</div>
            <div class="curio-muted">
                It combines real career evidence, structured storytelling, role-fit analysis,
                and AI-powered interaction in one place.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# =========================
# SIGNATURE LINE
# =========================

st.markdown(
    """
    <div style="margin-top: 2rem; font-size: 1.08rem; color: #6B6B6B; font-weight: 500;">
        This is how I think. This is how I work. This is the value I bring.
    </div>
    """,
    unsafe_allow_html=True,
)