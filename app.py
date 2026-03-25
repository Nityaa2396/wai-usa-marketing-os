import streamlit as st

st.set_page_config(
    page_title="WAI USA Marketing OS",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background: #0d1b2e; }
.block-container { padding: 0 !important; max-width: 100% !important; }
#MainMenu, footer, header { visibility: hidden; }
section[data-testid="stSidebar"] { display: none; }

/* ── Page wrapper ── */
.os-page {
    min-height: 100vh;
    background: #0d1b2e;
    background-image:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(255,193,0,0.08) 0%, transparent 60%),
        radial-gradient(ellipse 40% 40% at 90% 80%, rgba(21,34,71,0.8) 0%, transparent 70%);
    padding: 0;
}

/* ── Nav ── */
.os-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem 3rem;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    background: rgba(13,27,46,0.9);
    backdrop-filter: blur(12px);
    position: sticky;
    top: 0;
    z-index: 100;
}
.os-nav-logo {
    font-family: 'Syne', sans-serif;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #ffc100;
}
.os-nav-tag {
    font-size: 0.7rem;
    font-weight: 500;
    color: rgba(255,255,255,0.35);
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

/* ── Hero ── */
.os-hero {
    text-align: center;
    padding: 5rem 2rem 4rem;
}
.os-hero-eyebrow {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #ffc100;
    margin-bottom: 1.25rem;
}
.os-hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    color: #ffffff;
    line-height: 1.1;
    margin-bottom: 1.25rem;
    letter-spacing: -0.02em;
}
.os-hero-title span { color: #ffc100; }
.os-hero-sub {
    font-size: 1rem;
    color: rgba(255,255,255,0.45);
    font-weight: 400;
    max-width: 480px;
    margin: 0 auto 3rem;
    line-height: 1.6;
}

/* ── Module cards ── */
.modules-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
    max-width: 1000px;
    margin: 0 auto;
    padding: 0 2rem 2rem;
}
.module-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1.75rem;
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
}
.module-card.active {
    background: rgba(255,193,0,0.04);
    border-color: rgba(255,193,0,0.25);
}
.module-card.active::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #ffc100, rgba(255,193,0,0.3));
}
.module-num {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.25);
    margin-bottom: 1rem;
}
.module-card.active .module-num { color: #ffc100; }
.module-name {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.6rem;
    line-height: 1.3;
}
.module-desc {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.4);
    line-height: 1.6;
    margin-bottom: 1.25rem;
}
.module-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.65rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 0.3rem 0.7rem;
    border-radius: 999px;
}
.badge-live { background: rgba(255,193,0,0.12); color: #ffc100; border: 1px solid rgba(255,193,0,0.2); }
.badge-soon { background: rgba(255,255,255,0.05); color: rgba(255,255,255,0.3); border: 1px solid rgba(255,255,255,0.08); }

/* ── Streamlit button overrides ── */
div[data-testid="stButton"] > button {
    background: #ffc100 !important;
    color: #0d1b2e !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.03em !important;
    padding: 0.6rem 1.25rem !important;
    width: 100% !important;
    transition: all 0.15s !important;
}
div[data-testid="stButton"] > button:hover {
    background: #ffcd33 !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] > button:disabled {
    background: rgba(255,255,255,0.06) !important;
    color: rgba(255,255,255,0.2) !important;
    cursor: not-allowed !important;
    transform: none !important;
}

/* ── Footer ── */
.os-footer {
    text-align: center;
    padding: 2rem;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.18);
    letter-spacing: 0.04em;
    border-top: 1px solid rgba(255,255,255,0.05);
    margin-top: 2rem;
}
</style>

<div class="os-page">
    <nav class="os-nav">
        <span class="os-nav-logo">WAI USA Marketing OS</span>
        <span class="os-nav-tag">AI-Powered · 3 Modules · Built on Claude</span>
    </nav>

    <div class="os-hero">
        <div class="os-hero-eyebrow">Marketing Operating System</div>
        <h1 class="os-hero-title">Built for <span>Women in AI</span>.<br>Powered by AI.</h1>
        <p class="os-hero-sub">Three intelligent modules that handle campaign briefs, partnerships, and event impact — all in one place.</p>
    </div>

    <div class="modules-grid">
        <div class="module-card active">
            <div class="module-num">01 · Module</div>
            <div class="module-name">Campaign Intake & Brief Builder</div>
            <div class="module-desc">Turn campaign inputs into a full structured brief with DOCX download — ready for leadership review.</div>
            <span class="module-badge badge-live">✦ Live</span>
        </div>
        <div class="module-card">
            <div class="module-num">02 · Module</div>
            <div class="module-name">Partnership Copilot</div>
            <div class="module-desc">Turn a partner profile into an outreach strategy and a ready-to-send email in minutes.</div>
            <span class="module-badge badge-soon">Coming Soon</span>
        </div>
        <div class="module-card">
            <div class="module-num">03 · Module</div>
            <div class="module-name">Event-to-Impact Agent</div>
            <div class="module-desc">Turn event data into a formatted impact report for sponsors and leadership.</div>
            <span class="module-badge badge-soon">Coming Soon</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='max-width:340px;margin:0 auto;padding:0 2rem 1rem;'>", unsafe_allow_html=True)
if st.button("⚡  Open Campaign Brief Builder"):
    st.switch_page("pages/module1_campaign_brief.py")
st.markdown("</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.button("🔒  Partnership Copilot — Coming Soon", disabled=True)
with col2:
    st.button("🔒  Event-to-Impact Agent — Coming Soon", disabled=True)

st.markdown("""
<div class="os-footer">
    WAI USA Marketing OS · Powered by Claude (Anthropic) · Women in AI USA
</div>
""", unsafe_allow_html=True)
