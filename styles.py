def inject_custom_css():
    return """
    <style>
    .stApp {
        background: linear-gradient(180deg, #F8F7F2 0%, #F4F1E8 100%);
        color: #1F1F1F;
    }

    /* Main page width */
    [data-testid="stAppViewContainer"] .main .block-container {
    max-width: 1400px !important;
    padding-top: 1.5rem !important;
    padding-bottom: 2rem !important;
    padding-left: 3rem !important;
    padding-right: 3rem !important;
}

/* Optional: make content use more of the screen */
section.main > div {
    max-width: 1400px !important;
}

    h1, h2, h3 {
        color: #1F1F1F;
        font-weight: 700;
        letter-spacing: -0.03em;
    }


    .curio-hero {
        background: linear-gradient(135deg, #FFFFFF 0%, #FFFDF7 100%);
        padding: 2.4rem;
        border-radius: 24px;
        border: 1px solid #EFE2A3;
        box-shadow: 0 14px 36px rgba(0, 0, 0, 0.06);
        margin-bottom: 2rem;
    }

    .curio-tag {
        display: inline-block;
        padding: 0.45rem 0.9rem;
        border-radius: 999px;
        background-color: #FFF4CC;
        color: #B88400;
        font-size: 0.92rem;
        font-weight: 700;
        margin-bottom: 1.1rem;
    }

    .curio-title {
       font-size: 3rem;
       line-height: 1.05;
       font-weight: 800;
       color: #1F1F1F;
       margin-bottom: 1rem;
       max-width: 1100px;
}

    .curio-lead {
       font-size: 1.22rem;
       line-height: 1.7;
       color: #2B2B2B;
       max-width: 1100px;
       margin-bottom: 1rem;
}

    .curio-sub {
       font-size: 1rem;
       line-height: 1.7;
       color: #6B6B6B;
       max-width: 1100px;
       margin-bottom: 0.7rem;
}

    .curio-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 1.4rem;
        border-radius: 18px;
        border: 1px solid #EFE2A3;
        box-shadow: 0 8px 22px rgba(0,0,0,0.04);
        min-height: 180px;
    }

    .curio-section-title {
        font-size: 1.15rem;
        font-weight: 800;
        margin-bottom: 0.6rem;
        color: #1F1F1F;
    }

    .curio-muted {
        color: #6B6B6B;
        font-size: 0.98rem;
        line-height: 1.65;
    }

    .stButton > button {
        border-radius: 14px;
        border: 1px solid #E0A800;
        background: #FFFFFF;
        color: #1F1F1F;
        font-weight: 700;
        padding: 0.65rem 1rem;
    }

    .stButton > button:hover {
        border-color: #B88400;
        color: #B88400;
        background: #FFF9E8;
    }

    .stTextInput > div > div > input,
    .stTextArea textarea {
        border-radius: 12px !important;
        border: 1px solid #E6DFC9 !important;
        background-color: #FFFFFF !important;
    }

    /* Sidebar shell */
[data-testid="stSidebar"] {
    background-color: #F5F2E9;
    border-right: 1px solid #E7DFC7;
}

/* Remove Streamlit header spacing inside sidebar */
[data-testid="stSidebarNav"] {
    padding-top: 1.1rem;
    padding-left: 0.7rem;
    padding-right: 0.7rem;
}

/* Hide the default "App" label */
[data-testid="stSidebarNav"] > div:first-child {
    height: 0;
    overflow: hidden;
}

/* Sidebar links */
[data-testid="stSidebarNav"] a {
    display: flex !important;
    align-items: center;
    gap: 8px;

    padding: 0.75rem 0.95rem !important;
    margin: 0.15rem 0 0.35rem 0 !important;

    border-radius: 14px;

    color: #5C6578 !important;   /* softer default */
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    line-height: 1.2;

    text-decoration: none !important;

    width: 100% !important;   /* 🔥 important for alignment */

    transition: all 0.15s ease;
}

    /* Inactive hover */
    [data-testid="stSidebarNav"] a:hover {
        background: #FBF8EF !important;
        color: #1F1F1F !important;
        transform: translateX(2px);
    }

    /* Active page */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: #E0A800 !important;
        color: #1F1F1F !important;
        box-shadow: 0 8px 20px rgba(224, 168, 0, 0.18);
    }

    /* Icon sizing */
    [data-testid="stSidebarNav"] a span {
        font-size: 1.02rem !important;
        opacity: 0.95;
    }

    /* Make inactive items softer */
    [data-testid="stSidebarNav"] a:not([aria-current="page"]) {
        opacity: 0.92;
    }

    /* Sidebar collapse button area */
    button[kind="header"] {
        color: #5C6578 !important;
    }

    /* Optional: slightly narrower sidebar for a cleaner feel */
    section[data-testid="stSidebar"] {
        width: 255px !important;
    }

    header[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: none !important;
}
    

    .curio-divider {
    height: 4px;
    width: 60px;
    background: linear-gradient(90deg, #E0A800, #FFD84D);
    border-radius: 999px;
    margin: 20px 0 30px 0;
    }

/* Profile image styling */
img {
    border-radius: 18px;
    border: 2px solid #EFE2A3;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    }

    div[data-testid="stPageLink"] a {
    display: block;
    text-align: center;
    background: #FFFFFF;
    border: 1px solid #E0A800;
    border-radius: 14px;
    padding: 0.9rem 1rem;
    font-weight: 700;
    color: #1F1F1F !important;
    text-decoration: none !important;
    box-shadow: 0 6px 16px rgba(0,0,0,0.04);
}

div[data-testid="stPageLink"] a:hover {
    background: #FFF8E1;
    border-color: #B88400;
    color: #B88400 !important;
}

/* CTA row links */
div[data-testid="stPageLink"] {
    width: 100%;
}

/* CTA buttons */
button[kind="secondary"] {
    min-height: 60px;
    border-radius: 18px !important;
    font-weight: 700 !important;
    font-size: 1.2rem !important;
    border: 1px solid #E0A800 !important;
    box-shadow: 0 6px 16px rgba(0,0,0,0.04);
}

/* Primary CTA = first button only */
div[data-testid="stHorizontalBlock"] > div:nth-child(1) button[kind="secondary"] {
    background: #E0A800 !important;
    color: #1F1F1F !important;
    box-shadow: 0 8px 20px rgba(224,168,0,0.22);
}

/* Secondary CTAs */
div[data-testid="stHorizontalBlock"] > div:nth-child(2) button[kind="secondary"],
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button[kind="secondary"] {
    background: #FFFFFF !important;
    color: #1F1F1F !important;
}

/* Hover */
button[kind="secondary"]:hover {
    border-color: #B88400 !important;
    transform: translateY(-2px);
}

div[data-testid="stHorizontalBlock"] > div:nth-child(1) button[kind="secondary"]:hover {
    background: #C99700 !important;
    color: #1F1F1F !important;
}

div[data-testid="stHorizontalBlock"] > div:nth-child(2) button[kind="secondary"]:hover,
div[data-testid="stHorizontalBlock"] > div:nth-child(3) button[kind="secondary"]:hover {
    background: #FFF8E1 !important;
    color: #B88400 !important;
}

/* Chat input wrapper */
[data-testid="stChatInput"] {
    background: transparent !important;
}

/* Main chat input box */
[data-testid="stChatInput"] > div {
    background: #FFFDF7 !important;
    border: 1.5px solid #E0A800 !important;
    border-radius: 20px !important;
    box-shadow: 0 6px 16px rgba(0,0,0,0.04);
    padding: 6px 10px !important;
}

/* Text area inside chat input */
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: #1F1F1F !important;
    font-size: 1rem !important;
}

/* Placeholder */
[data-testid="stChatInput"] textarea::placeholder {
    color: #8A8A8A !important;
}

/* Send button */
[data-testid="stChatInput"] button {
    background: #E0A800 !important;
    color: #1F1F1F !important;
    border-radius: 14px !important;
    border: none !important;
    width: 42px !important;
    height: 42px !important;
}

/* Send button hover */
[data-testid="stChatInput"] button:hover {
    background: #C99700 !important;
    color: #1F1F1F !important;
}

/* Remove odd gray default areas */
[data-testid="stChatInputContainer"] {
    background: transparent !important;
    border-top: none !important;
}

</style>
    """
