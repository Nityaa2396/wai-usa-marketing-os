import streamlit as st

st.set_page_config(
    page_title="WAI USA Marketing OS",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    background-color: #13223d !important;
    font-family: 'DM Sans', sans-serif !important;
}
.block-container {
    padding: 2rem 3rem !important;
    max-width: 100% !important;
}
#MainMenu, footer, header { visibility: hidden; }
section[data-testid="stSidebar"] { display: none; }

/* Buttons */
div[data-testid="stButton"] > button {
    background-color: #ffc100 !important;
    color: #13223d !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.65rem 1.5rem !important;
    width: 100% !important;
    transition: opacity 0.2s !important;
}
div[data-testid="stButton"] > button:hover { opacity: 0.88 !important; }
div[data-testid="stButton"] > button:disabled {
    background-color: rgba(255,255,255,0.08) !important;
    color: rgba(255,255,255,0.25) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Nav bar ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="display:flex;align-items:center;justify-content:space-between;
            padding:0.75rem 0;border-bottom:1px solid rgba(255,255,255,0.08);margin-bottom:3rem;">
    <span style="font-family:'Syne',sans-serif;font-size:0.9rem;font-weight:800;
                 letter-spacing:0.12em;text-transform:uppercase;color:#ffc100;">
        WAI USA Marketing OS
    </span>
    <span style="font-size:0.7rem;font-weight:500;letter-spacing:0.1em;
                 text-transform:uppercase;color:rgba(255,255,255,0.3);">
        AI-Powered · 3 Modules · Built on Claude
    </span>
</div>
""", unsafe_allow_html=True)

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:2rem 0 3.5rem;">
    <p style="font-size:0.7rem;font-weight:700;letter-spacing:0.18em;text-transform:uppercase;
              color:#ffc100;margin-bottom:1rem;">Marketing Operating System</p>
    <h1 style="font-family:'Syne',sans-serif;font-size:3rem;font-weight:800;
               color:#ffffff;line-height:1.15;letter-spacing:-0.02em;margin-bottom:1rem;">
        Built for <span style="color:#ffc100;">Women in AI</span>.<br>Powered by AI.
    </h1>
    <p style="font-size:1rem;color:rgba(255,255,255,0.45);max-width:480px;
              margin:0 auto;line-height:1.65;">
        Three intelligent modules that handle campaign briefs, partnerships,
        and event impact — all in one place.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Module cards ───────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3, gap="medium")

def module_card(container, num, title, desc, status, active=False):
    border = "rgba(255,193,0,0.3)" if active else "rgba(255,255,255,0.08)"
    bg = "rgba(255,193,0,0.04)" if active else "rgba(255,255,255,0.02)"
    top_line = f'<div style="height:2px;background:linear-gradient(90deg,#ffc100,transparent);border-radius:2px;margin-bottom:1.25rem;"></div>' if active else '<div style="height:2px;background:transparent;margin-bottom:1.25rem;"></div>'
    num_color = "#ffc100" if active else "rgba(255,255,255,0.2)"
    badge_bg = "rgba(255,193,0,0.12)" if active else "rgba(255,255,255,0.05)"
    badge_color = "#ffc100" if active else "rgba(255,255,255,0.3)"
    badge_border = "rgba(255,193,0,0.25)" if active else "rgba(255,255,255,0.08)"

    container.markdown(f"""
    <div style="background:{bg};border:1px solid {border};border-radius:12px;
                padding:1.75rem;min-height:200px;">
        {top_line}
        <p style="font-size:0.62rem;font-weight:700;letter-spacing:0.14em;
                  text-transform:uppercase;color:{num_color};margin-bottom:0.75rem;">
            {num}
        </p>
        <p style="font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;
                  color:#ffffff;line-height:1.35;margin-bottom:0.6rem;">{title}</p>
        <p style="font-size:0.8rem;color:rgba(255,255,255,0.4);
                  line-height:1.6;margin-bottom:1.25rem;">{desc}</p>
        <span style="display:inline-block;font-size:0.62rem;font-weight:700;
                     letter-spacing:0.08em;text-transform:uppercase;
                     padding:0.25rem 0.7rem;border-radius:999px;
                     background:{badge_bg};color:{badge_color};
                     border:1px solid {badge_border};">{status}</span>
    </div>
    """, unsafe_allow_html=True)

module_card(col1, "01 · Module", "Campaign Intake & Brief Builder",
            "Turn campaign inputs into a full structured brief with DOCX download — ready for leadership review.",
            "✦ Live", active=True)

module_card(col2, "02 · Module", "Partnership Copilot",
            "Turn a partner profile into an outreach strategy and a ready-to-send email in minutes.",
            "Coming Soon")

module_card(col3, "03 · Module", "Event-to-Impact Agent",
            "Turn event data into a formatted impact report for sponsors and leadership.",
            "Coming Soon")

# ── Launch buttons ─────────────────────────────────────────────────────────────
st.markdown("<div style='margin-top:2rem;'>", unsafe_allow_html=True)
b1, b2, b3 = st.columns(3, gap="medium")

with b1:
    if st.button("⚡  Open Campaign Brief Builder", use_container_width=True):
        st.switch_page("pages/module1_campaign_brief.py")
with b2:
    st.button("🔒  Partnership Copilot — Coming Soon", disabled=True, use_container_width=True)
with b3:
    st.button("🔒  Event-to-Impact Agent — Coming Soon", disabled=True, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;margin-top:3rem;padding-top:1.5rem;
            border-top:1px solid rgba(255,255,255,0.06);
            font-size:0.72rem;color:rgba(255,255,255,0.18);letter-spacing:0.04em;">
    WAI USA Marketing OS · Powered by Claude (Anthropic) · Women in AI USA
</div>
""", unsafe_allow_html=True)
