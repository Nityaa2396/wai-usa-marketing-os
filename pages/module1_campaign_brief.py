import streamlit as st
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'modules', 'module1_campaign_brief'))
from brief_generator import generate_brief, generate_docx

st.set_page_config(page_title="Campaign Brief Builder · WAI USA", page_icon="📋", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { font-family: 'Inter', sans-serif; box-sizing: border-box; }

/* ── Layout ── */
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── Top bar ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.85rem 2rem;
    border-bottom: 1px solid #E5E7EB;
    background: #fff;
    position: sticky;
    top: 0;
    z-index: 100;
}
.topbar-left { display: flex; align-items: center; gap: 1rem; }
.topbar-logo {
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: #111827;
    text-transform: uppercase;
}
.topbar-divider { color: #D1D5DB; font-size: 1rem; }
.topbar-title { font-size: 0.9rem; font-weight: 500; color: #6B7280; }
.topbar-badge {
    font-size: 0.65rem;
    font-weight: 600;
    background: #EFF6FF;
    color: #1D4ED8;
    padding: 0.2rem 0.55rem;
    border-radius: 999px;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

/* ── Two-panel layout ── */
.main-panels {
    display: grid;
    grid-template-columns: 420px 1fr;
    height: calc(100vh - 53px);
    overflow: hidden;
}
.panel-left {
    border-right: 1px solid #E5E7EB;
    overflow-y: auto;
    background: #FAFAFA;
    padding: 1.5rem;
}
.panel-right {
    overflow-y: auto;
    background: #fff;
    padding: 2rem;
}

/* ── Form sections ── */
.form-section {
    background: #fff;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 1.25rem;
    margin-bottom: 0.75rem;
}
.form-section-label {
    font-size: 0.68rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #9CA3AF;
    margin-bottom: 1rem;
    display: block;
}

/* ── Inputs ── */
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    border: 1px solid #E5E7EB !important;
    border-radius: 6px !important;
    font-size: 0.875rem !important;
    background: #fff !important;
    color: #111827 !important;
    transition: border-color 0.15s;
}
div[data-testid="stTextInput"] input:focus,
div[data-testid="stTextArea"] textarea:focus {
    border-color: #2563EB !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.08) !important;
}
div[data-testid="stTextInput"] label,
div[data-testid="stTextArea"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stMultiSelect"] label {
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: #374151 !important;
}

/* ── Generate button ── */
div[data-testid="stButton"] > button[kind="primary"],
div[data-testid="stButton"] > button {
    background: #111827 !important;
    color: #fff !important;
    border: none !important;
    border-radius: 6px !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.25rem !important;
    letter-spacing: 0.02em !important;
    width: 100% !important;
    transition: background 0.15s !important;
}
div[data-testid="stButton"] > button:hover {
    background: #1F2937 !important;
}

/* ── Brief output ── */
.brief-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid #F3F4F6;
}
.brief-title { font-size: 1.1rem; font-weight: 700; color: #111827; margin: 0 0 0.25rem 0; }
.brief-meta { font-size: 0.78rem; color: #9CA3AF; }

.brief-section {
    margin-bottom: 1.5rem;
    padding-bottom: 1.5rem;
    border-bottom: 1px solid #F3F4F6;
}
.brief-section:last-child { border-bottom: none; }
.brief-section-num {
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #2563EB;
    margin-bottom: 0.25rem;
}
.brief-section-title {
    font-size: 0.9rem;
    font-weight: 600;
    color: #111827;
    margin-bottom: 0.6rem;
}
.brief-section-body {
    font-size: 0.875rem;
    color: #374151;
    line-height: 1.7;
    white-space: pre-wrap;
}

/* ── Empty state ── */
.empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    text-align: center;
    color: #9CA3AF;
    padding: 3rem;
}
.empty-icon { font-size: 2.5rem; margin-bottom: 1rem; }
.empty-title { font-size: 0.95rem; font-weight: 600; color: #6B7280; margin-bottom: 0.4rem; }
.empty-sub { font-size: 0.82rem; }

/* ── Approval note ── */
.approval-note {
    background: #FFFBEB;
    border: 1px solid #FDE68A;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    font-size: 0.8rem;
    color: #92400E;
    margin-top: 1.5rem;
    display: flex;
    gap: 0.5rem;
    align-items: flex-start;
}

/* ── Download button ── */
div[data-testid="stDownloadButton"] > button {
    background: #fff !important;
    color: #111827 !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 6px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    width: 100% !important;
    margin-top: 1rem !important;
}
div[data-testid="stDownloadButton"] > button:hover {
    border-color: #111827 !important;
}

/* ── Copy area ── */
div[data-testid="stTextArea"] textarea {
    font-size: 0.8rem !important;
    font-family: 'Inter', monospace !important;
    color: #374151 !important;
    line-height: 1.6 !important;
}

/* hide streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Top bar ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <div class="topbar-left">
        <span class="topbar-logo">WAI USA Marketing OS</span>
        <span class="topbar-divider">/</span>
        <span class="topbar-title">Campaign Intake & Brief Builder</span>
    </div>
    <span class="topbar-badge">Module 1 of 3</span>
</div>
""", unsafe_allow_html=True)

# ── Two-column layout via Streamlit columns ────────────────────────────────────
left, right = st.columns([1, 1.4], gap="small")

with left:
    # Section 1 — Campaign basics
    st.markdown('<span class="form-section-label">Campaign Details</span>', unsafe_allow_html=True)

    campaign_name = st.text_input("Campaign Name", placeholder="e.g. IWD 2026 · Women in AI Spotlight")
    campaign_type = st.selectbox("Campaign Type", [
        "", "Awareness / Brand", "Event Promotion", "Partnership / Sponsorship",
        "Program Launch", "Community Engagement", "Recruitment / Membership",
        "Content Series", "Fundraising", "Other"
    ])
    primary_goal = st.text_area("Primary Goal", placeholder="What does success look like? Be specific.", height=72)
    target_audience = st.text_area("Target Audience", placeholder="Who are we reaching and what do they care about?", height=72)
    key_message = st.text_area("Key Message", placeholder="One thing we want them to think, feel, or do.", height=72)

    st.markdown("---")
    st.markdown('<span class="form-section-label">Channels & Programs</span>', unsafe_allow_html=True)

    channels = st.multiselect("Channels", [
        "LinkedIn", "Instagram", "Email Newsletter", "Twitter/X",
        "Website/Blog", "Events", "Press/Media", "Community Slack/Discord"
    ])
    programs = st.multiselect("WAI USA Programs Involved", [
        "WaiTALKs", "WaiMentorship USA", "PeakSkill Program",
        "Girls in AI", "WAI Educate USA", "None"
    ])

    st.markdown("---")
    st.markdown('<span class="form-section-label">Timeline & Resources</span>', unsafe_allow_html=True)

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        timeline = st.text_input("Timeline", placeholder="Mar 1–31, 2026")
    with col_t2:
        budget = st.text_input("Budget", placeholder="$0 / volunteer")

    notes = st.text_area("Notes / Constraints", placeholder="Anything leadership needs to know before we start.", height=64)

    st.markdown("---")
    generate_btn = st.button("⚡  Generate Brief", use_container_width=True)

# ── Right panel ────────────────────────────────────────────────────────────────
with right:
    if "brief" not in st.session_state:
        st.session_state.brief = None
        st.session_state.campaign_data = None

    if generate_btn:
        errors = []
        if not campaign_name.strip(): errors.append("Campaign Name is required.")
        if not campaign_type: errors.append("Campaign Type is required.")
        if not primary_goal.strip(): errors.append("Primary Goal is required.")
        if not target_audience.strip(): errors.append("Target Audience is required.")
        if not key_message.strip(): errors.append("Key Message is required.")
        if not channels: errors.append("Select at least one Channel.")

        if errors:
            for e in errors:
                st.error(e)
        else:
            campaign_data = {
                "campaign_name": campaign_name, "campaign_type": campaign_type,
                "primary_goal": primary_goal, "target_audience": target_audience,
                "key_message": key_message, "channels": channels, "programs": programs,
                "timeline": timeline, "budget": budget, "notes": notes
            }
            with st.spinner("Building brief..."):
                try:
                    brief = generate_brief(campaign_data)
                    st.session_state.brief = brief
                    st.session_state.campaign_data = campaign_data
                except Exception as ex:
                    st.error(f"Error: {str(ex)}")

    if st.session_state.brief:
        brief = st.session_state.brief
        campaign_data = st.session_state.campaign_data

        # Brief header
        st.markdown(f"""
        <div class="brief-header">
            <div>
                <div class="brief-title">{campaign_data['campaign_name']}</div>
                <div class="brief-meta">{campaign_data['campaign_type']} · {campaign_data.get('timeline', 'No timeline set')}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Render brief sections
        sections = []
        current = []
        for line in brief.split('\n'):
            stripped = line.strip()
            if stripped.startswith('**') and stripped.endswith('**') and any(c.isdigit() for c in stripped[:5]):
                if current:
                    sections.append(current)
                current = [stripped]
            else:
                current.append(stripped)
        if current:
            sections.append(current)

        for sec in sections:
            if not sec:
                continue
            header = sec[0].strip('*').strip()
            parts = header.split('.', 1)
            num = parts[0].strip() if len(parts) > 1 else ""
            title = parts[1].strip() if len(parts) > 1 else header
            body = '\n'.join(line for line in sec[1:] if line).strip()

            st.markdown(f"""
            <div class="brief-section">
                <div class="brief-section-num">Section {num}</div>
                <div class="brief-section-title">{title}</div>
                <div class="brief-section-body">{body}</div>
            </div>
            """, unsafe_allow_html=True)

        # Approval note
        st.markdown("""
        <div class="approval-note">
            ⚠️ Send for leadership approval before any external execution. 
            See Section 10 — Approval Notes for Leadership.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Copy-paste
        with st.expander("📋 Copy raw brief text"):
            st.text_area("", value=brief, height=300, label_visibility="collapsed")

        # DOCX download
        try:
            docx_bytes = generate_docx(campaign_data, brief)
            safe_name = campaign_data['campaign_name'].replace(' ', '_').replace('|', '').replace('/', '-').replace('·', '')
            st.download_button(
                label="⬇️  Download as DOCX",
                data=docx_bytes,
                file_name=f"WAI_Brief_{safe_name}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        except Exception as ex:
            st.warning(f"DOCX issue: {ex}")

    else:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-icon">📄</div>
            <div class="empty-title">Your brief will appear here</div>
            <div class="empty-sub">Fill in the form and hit Generate Brief</div>
        </div>
        """, unsafe_allow_html=True)
