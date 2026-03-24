import streamlit as st
import os
from brief_generator import generate_brief, generate_docx

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="WAI USA | Campaign Brief Builder",
    page_icon="🤖",
    layout="wide"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main { background: #F8FAFC; }
    
    .wai-header {
        background: linear-gradient(135deg, #0D476B 0%, #0A7B8C 100%);
        padding: 2rem 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white;
    }
    .wai-header h1 { 
        color: white; 
        font-size: 1.8rem; 
        font-weight: 700; 
        margin: 0 0 0.25rem 0;
    }
    .wai-header p { 
        color: rgba(255,255,255,0.8); 
        margin: 0; 
        font-size: 0.95rem;
    }
    
    .section-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: #0A7B8C;
        margin-bottom: 0.75rem;
        display: block;
    }
    
    .brief-output {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 2rem;
        font-size: 0.92rem;
        line-height: 1.7;
        white-space: pre-wrap;
        font-family: 'Inter', sans-serif;
    }
    
    .status-badge {
        display: inline-block;
        background: #D1FAE5;
        color: #065F46;
        font-size: 0.75rem;
        font-weight: 600;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        margin-left: 0.5rem;
    }
    
    div[data-testid="stButton"] > button {
        background: linear-gradient(135deg, #0D476B, #0A7B8C);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0.6rem 1.5rem;
        width: 100%;
        transition: opacity 0.2s;
    }
    div[data-testid="stButton"] > button:hover { opacity: 0.9; }
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid #CBD5E1;
        font-family: 'Inter', sans-serif;
    }
    
    .approve-note {
        background: #FFF7ED;
        border-left: 4px solid #F59E0B;
        padding: 0.75rem 1rem;
        border-radius: 0 8px 8px 0;
        font-size: 0.85rem;
        color: #92400E;
        margin-top: 1rem;
    }
    
    hr { border-color: #E2E8F0; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="wai-header">
    <h1>🚀 WAI USA Campaign Brief Builder</h1>
    <p>Marketing Operating System · Module 1 of 3 · Powered by Claude + WAI USA Brand Voice</p>
</div>
""", unsafe_allow_html=True)

# ── Layout ─────────────────────────────────────────────────────────────────────
col_form, col_output = st.columns([1, 1.3], gap="large")

with col_form:
    st.markdown('<span class="section-label">📋 Campaign Intake Form</span>', unsafe_allow_html=True)

    with st.container():
        campaign_name = st.text_input(
            "Campaign Name *",
            placeholder="e.g. IWD 2026 | Women in AI Spotlight"
        )

        campaign_type = st.selectbox(
            "Campaign Type *",
            ["", "Awareness / Brand", "Event Promotion", "Partnership / Sponsorship",
             "Program Launch", "Community Engagement", "Recruitment / Membership",
             "Content Series", "Fundraising", "Other"]
        )

        primary_goal = st.text_area(
            "Primary Goal *",
            placeholder="What does success look like? Be specific — 'Increase LinkedIn followers by 20%' not 'grow awareness'.",
            height=80
        )

        target_audience = st.text_area(
            "Target Audience *",
            placeholder="Who are we reaching? (e.g. Women in AI aged 25-40, currently in tech roles, interested in career growth)",
            height=80
        )

        key_message = st.text_area(
            "Key Message *",
            placeholder="Core thing we want our audience to think, feel, or do after seeing this campaign.",
            height=80
        )

    st.markdown("---")
    st.markdown('<span class="section-label">📡 Channels & Programs</span>', unsafe_allow_html=True)

    channels = st.multiselect(
        "Channels *",
        ["LinkedIn", "Instagram", "Email Newsletter", "Twitter/X",
         "Website/Blog", "Events", "Press/Media", "Community Slack/Discord"]
    )

    programs = st.multiselect(
        "WAI USA Programs Involved",
        ["WaiTALKs", "WaiMentorship USA", "PeakSkill Program",
         "Girls in AI", "WAI Educate USA", "None"]
    )

    st.markdown("---")
    st.markdown('<span class="section-label">📅 Timeline & Resources</span>', unsafe_allow_html=True)

    col_t1, col_t2 = st.columns(2)
    with col_t1:
        timeline = st.text_input("Campaign Timeline", placeholder="e.g. March 1–31, 2026")
    with col_t2:
        budget = st.text_input("Budget / Resources", placeholder="e.g. $0 / volunteer-run")

    notes = st.text_area(
        "Additional Notes or Constraints",
        placeholder="Anything Suparna needs to know? Pending approvals? Content restrictions?",
        height=80
    )

    st.markdown("---")

    api_key = st.text_input(
        "Anthropic API Key",
        type="password",
        placeholder="sk-ant-..."
    )
    st.caption("Your key is never stored. Used only to generate the brief.")

    generate_btn = st.button("⚡ Generate Campaign Brief", use_container_width=True)

# ── Output Column ──────────────────────────────────────────────────────────────
with col_output:
    st.markdown('<span class="section-label">📄 Generated Campaign Brief</span>', unsafe_allow_html=True)

    if "brief" not in st.session_state:
        st.session_state.brief = None
        st.session_state.campaign_data = None

    if generate_btn:
        # Validation
        errors = []
        if not campaign_name.strip():
            errors.append("Campaign Name is required.")
        if not campaign_type:
            errors.append("Campaign Type is required.")
        if not primary_goal.strip():
            errors.append("Primary Goal is required.")
        if not target_audience.strip():
            errors.append("Target Audience is required.")
        if not key_message.strip():
            errors.append("Key Message is required.")
        if not channels:
            errors.append("At least one Channel is required.")
        if not api_key.strip():
            errors.append("Anthropic API Key is required.")

        if errors:
            for e in errors:
                st.error(e)
        else:
            os.environ["ANTHROPIC_API_KEY"] = api_key.strip()

            campaign_data = {
                "campaign_name": campaign_name,
                "campaign_type": campaign_type,
                "primary_goal": primary_goal,
                "target_audience": target_audience,
                "key_message": key_message,
                "channels": channels,
                "programs": programs,
                "timeline": timeline,
                "budget": budget,
                "notes": notes
            }

            with st.spinner("Generating brief using WAI USA brand voice..."):
                try:
                    brief = generate_brief(campaign_data)
                    st.session_state.brief = brief
                    st.session_state.campaign_data = campaign_data
                    st.success("Brief generated! Review below before sending to Suparna.")
                except Exception as ex:
                    st.error(f"Error generating brief: {str(ex)}")

    if st.session_state.brief:
        brief = st.session_state.brief
        campaign_data = st.session_state.campaign_data

        # Copy-paste text area
        st.text_area(
            "Copy-pasteable brief (for Suparna / Notion / email)",
            value=brief,
            height=480,
            key="brief_copy"
        )

        # Approval note
        st.markdown("""
        <div class="approve-note">
            ⚠️ <strong>Reminder:</strong> Send to Suparna for approval before any external execution. 
            Check "Approval Notes for Suparna" section at the bottom of the brief.
        </div>
        """, unsafe_allow_html=True)

        # DOCX Download
        st.markdown("---")
        st.markdown('<span class="section-label">📥 Download</span>', unsafe_allow_html=True)

        try:
            docx_bytes = generate_docx(campaign_data, brief)
            safe_name = campaign_data['campaign_name'].replace(' ', '_').replace('|', '').replace('/', '-')
            st.download_button(
                label="⬇️ Download Brief as DOCX",
                data=docx_bytes,
                file_name=f"WAI_USA_Brief_{safe_name}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        except Exception as ex:
            st.warning(f"DOCX generation issue: {ex}. Use the copy-paste version above.")

    else:
        st.markdown("""
        <div style="text-align:center; padding: 4rem 2rem; color: #94A3B8;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📝</div>
            <div style="font-weight: 600; font-size: 1rem; margin-bottom: 0.5rem;">Brief will appear here</div>
            <div style="font-size: 0.85rem;">Fill in the intake form and hit Generate</div>
        </div>
        """, unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:0.78rem; color:#94A3B8; padding: 0.5rem 0;">
    WAI USA Marketing Operating System · Module 1: Campaign Intake & Brief Builder · 
    Module 2: Partnership Copilot (coming next) · Module 3: Event-to-Impact Agent
</div>
""", unsafe_allow_html=True)
