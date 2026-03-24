import anthropic
from brand_voice import BRAND_VOICE_FINGERPRINT

def generate_brief(campaign_data: dict) -> str:
    """Generate a structured campaign brief using Claude + WAI USA brand voice."""
    
    client = anthropic.Anthropic()
    
    prompt = f"""
You are the WAI USA Marketing Intelligence system. Generate a complete, structured campaign brief based on the intake data below.

{BRAND_VOICE_FINGERPRINT}

## Campaign Intake Data:
- Campaign Name: {campaign_data.get('campaign_name', 'N/A')}
- Campaign Type: {campaign_data.get('campaign_type', 'N/A')}
- Primary Goal: {campaign_data.get('primary_goal', 'N/A')}
- Target Audience: {campaign_data.get('target_audience', 'N/A')}
- Key Message: {campaign_data.get('key_message', 'N/A')}
- Channels: {', '.join(campaign_data.get('channels', []))}
- Timeline: {campaign_data.get('timeline', 'N/A')}
- Budget/Resources: {campaign_data.get('budget', 'N/A')}
- Programs Involved: {', '.join(campaign_data.get('programs', [])) if campaign_data.get('programs') else 'None specified'}
- Additional Notes: {campaign_data.get('notes', 'None')}

## Generate a Campaign Brief with these exact sections:

**1. CAMPAIGN OVERVIEW**
One punchy paragraph that captures what this campaign is, why it matters, and what success looks like. WAI USA voice. No fluff.

**2. CAMPAIGN OBJECTIVE**
Primary objective (one clear sentence) + 2-3 supporting objectives as bullet points.

**3. TARGET AUDIENCE**
Who we're reaching, what they care about, and what motivates them to act.

**4. KEY MESSAGES**
3-4 core messages, each as a single punchy line. These should feel like copy hooks.

**5. CHANNEL STRATEGY**
For each selected channel, write 1-2 sentences on how we use it specifically for this campaign (tone, content type, frequency if relevant).

**6. CONTENT PILLARS**
3 content pillars for this campaign. Each: pillar name + 1-sentence description + 1 example content idea.

**7. CALLS TO ACTION**
2-3 specific CTAs for this campaign. Make them action-forward and channel-appropriate.

**8. SUCCESS METRICS**
4-5 specific KPIs to track. Be concrete (e.g., "LinkedIn post impressions" not just "engagement").

**9. TIMELINE & MILESTONES**
Break the campaign timeline into phases with key milestones. Be specific to the dates/duration provided.

**10. APPROVAL NOTES FOR SUPARNA**
2-3 bullet points flagging any decisions, approvals, or inputs needed from leadership before execution begins.

Write in WAI USA voice throughout. Be specific, not generic. This brief should be ready to hand to Suparna for review.
"""

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=2500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text


def generate_docx(campaign_data: dict, brief_text: str) -> bytes:
    """Generate a downloadable DOCX of the campaign brief."""
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    import io

    doc = Document()

    # Page setup
    section = doc.sections[0]
    section.page_width = 12240  # 8.5 inches
    section.page_height = 15840  # 11 inches
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)

    # Title
    title = doc.add_heading(f"Campaign Brief: {campaign_data.get('campaign_name', 'Untitled')}", 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in title.runs:
        run.font.color.rgb = RGBColor(0x0D, 0x47, 0x6B)  # WAI navy
        run.font.size = Pt(20)

    # Subtitle
    sub = doc.add_paragraph(f"WAI USA Marketing Operating System  |  Campaign Type: {campaign_data.get('campaign_type', 'N/A')}  |  {campaign_data.get('timeline', 'TBD')}")
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in sub.runs:
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

    doc.add_paragraph()

    # Parse and write brief sections
    lines = brief_text.split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            doc.add_paragraph()
            continue
        
        # Section headers (bold + larger)
        if line.startswith('**') and line.endswith('**') and any(char.isdigit() for char in line[:5]):
            clean = line.strip('*').strip()
            h = doc.add_heading(clean, level=2)
            for run in h.runs:
                run.font.color.rgb = RGBColor(0x0D, 0x47, 0x6B)
        # Bullet points
        elif line.startswith('- ') or line.startswith('• '):
            p = doc.add_paragraph(line[2:], style='List Bullet')
            for run in p.runs:
                run.font.size = Pt(11)
        # Bold inline
        elif '**' in line:
            p = doc.add_paragraph()
            parts = line.split('**')
            for i, part in enumerate(parts):
                if not part:
                    continue
                run = p.add_run(part)
                run.bold = (i % 2 == 1)
                run.font.size = Pt(11)
        else:
            p = doc.add_paragraph(line)
            for run in p.runs:
                run.font.size = Pt(11)

    # Footer note
    doc.add_paragraph()
    footer_p = doc.add_paragraph("Generated by WAI USA Marketing Operating System  |  Requires Suparna approval before execution")
    footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in footer_p.runs:
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0x99, 0x99, 0x99)
        run.font.italic = True

    # Save to bytes
    buffer = io.BytesIO()
    doc.save(buffer)
    return buffer.getvalue()
