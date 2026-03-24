import streamlit as st

st.set_page_config(
    page_title="WAI USA Marketing OS",
    page_icon="🚀",
    layout="wide"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .os-header {
        background: linear-gradient(135deg, #0D476B 0%, #0A7B8C 100%);
        padding: 2.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .os-header h1 { color: white; font-size: 2rem; font-weight: 700; margin: 0 0 0.5rem 0; }
    .os-header p { color: rgba(255,255,255,0.8); margin: 0; font-size: 1rem; }

    .module-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        height: 100%;
    }
    .module-card.active { border-color: #0A7B8C; border-width: 2px; }
    .module-card.coming { opacity: 0.5; }
    .module-card h3 { font-size: 1rem; font-weight: 600; color: #0D476B; margin: 0.5rem 0 0.25rem 0; }
    .module-card p { font-size: 0.82rem; color: #64748B; margin: 0; }
    .badge {
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 600;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        margin-bottom: 0.5rem;
    }
    .badge-live { background: #D1FAE5; color: #065F46; }
    .badge-soon { background: #F1F5F9; color: #64748B; }
</style>
""", unsafe_allow_html=True)

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="os-header">
    <h1>🚀 WAI USA Marketing OS</h1>
    <p>AI-Powered Marketing Operations · 3 Modules · Built on Claude</p>
</div>
""", unsafe_allow_html=True)

# ── Module Cards ───────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="module-card active">
        <span class="badge badge-live">✅ Live</span>
        <h3>Module 1</h3>
        <h3>Campaign Intake & Brief Builder</h3>
        <p>Turn campaign inputs into a full structured brief with DOCX download.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card coming">
        <span class="badge badge-soon">🔜 Coming Soon</span>
        <h3>Module 2</h3>
        <h3>Partnership Copilot</h3>
        <p>Turn a partner profile into outreach strategy and a ready-to-send email.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="module-card coming">
        <span class="badge badge-soon">🔜 Coming Soon</span>
        <h3>Module 3</h3>
        <h3>Event-to-Impact Agent</h3>
        <p>Turn event data into a formatted impact report for sponsors and leadership.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ── Navigation ─────────────────────────────────────────────────────────────────
st.markdown("### Launch a Module")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("⚡ Open Campaign Brief Builder", use_container_width=True):
        st.switch_page("pages/module1_campaign_brief.py")

with col_btn2:
    st.button("🔒 Partnership Copilot — Coming Soon", disabled=True, use_container_width=True)

with col_btn3:
    st.button("🔒 Event-to-Impact Agent — Coming Soon", disabled=True, use_container_width=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-size:0.78rem; color:#94A3B8;">
    WAI USA Marketing OS · Powered by Claude (Anthropic) · Built by WAI USA Marketing Team
</div>
""", unsafe_allow_html=True)
