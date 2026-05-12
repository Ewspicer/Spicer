from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page margins ─────────────────────────────────────────────────────────
section = doc.sections[0]
section.top_margin    = Inches(0.9)
section.bottom_margin = Inches(0.9)
section.left_margin   = Inches(1.1)
section.right_margin  = Inches(1.1)

# ── Helper: add a horizontal rule ────────────────────────────────────────
def add_rule(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(2)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'CCCCCC')
    pBdr.append(bottom)
    pPr.append(pBdr)

# ── Helper: styled paragraph ─────────────────────────────────────────────
def styled_para(doc, text, bold=False, size=11, color=None, space_before=0, space_after=6, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    if align:
        p.alignment = align
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    if color:
        run.font.color.rgb = RGBColor(*color)
    return p

# ══════════════════════════════════════════════════════════════════════════
# HEADER BLOCK
# ══════════════════════════════════════════════════════════════════════════

# Confidential tag
conf = doc.add_paragraph()
conf.paragraph_format.space_before = Pt(0)
conf.paragraph_format.space_after  = Pt(4)
conf.alignment = WD_ALIGN_PARAGRAPH.RIGHT
run = conf.add_run('CONFIDENTIAL — BOARD USE ONLY')
run.font.size = Pt(8)
run.font.color.rgb = RGBColor(150, 150, 150)

# Headline
hl = doc.add_paragraph()
hl.paragraph_format.space_before = Pt(0)
hl.paragraph_format.space_after  = Pt(4)
hl.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = hl.add_run('Meridian is strong where it counts — and needs a decision\nwhere the window is closing.')
run.bold = True
run.font.size = Pt(18)
run.font.color.rgb = RGBColor(15, 60, 110)

# Byline
bl = doc.add_paragraph()
bl.paragraph_format.space_before = Pt(0)
bl.paragraph_format.space_after  = Pt(2)
bl.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = bl.add_run('Catherine Park, CEO  |  Annual Board Strategic Review  |  2026')
run.font.size = Pt(9)
run.font.color.rgb = RGBColor(100, 100, 100)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# OPENING
# ══════════════════════════════════════════════════════════════════════════
opening = doc.add_paragraph()
opening.paragraph_format.space_before = Pt(8)
opening.paragraph_format.space_after  = Pt(10)
run = opening.add_run(
    'Thank you. This is my first annual strategic review with you as CEO, and I want to use '
    'these five minutes to give you my honest read — not a curated highlight reel. '
    'We have real strengths, two issues that demand board-level attention, and one decision '
    'I need from this room today.'
)
run.font.size = Pt(11)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# ISSUE 1
# ══════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after  = Pt(3)
r1 = p.add_run('ISSUE 1 OF 3 — ')
r1.bold = True
r1.font.size = Pt(10)
r1.font.color.rgb = RGBColor(150, 100, 0)
r2 = p.add_run('The AI execution window is closing.')
r2.bold = True
r2.font.size = Pt(13)
r2.font.color.rgb = RGBColor(15, 60, 110)

body1 = doc.add_paragraph()
body1.paragraph_format.space_before = Pt(0)
body1.paragraph_format.space_after  = Pt(8)
r = body1.add_run(
    'AI Copilot reached GA in September 2025. We closed Q4 with 710 paying seats and a '
    '44% attach rate on enterprise renewals — ahead of our internal 40% target. '
    'The Helio acquisition gives us an agent framework that our CPO estimates compresses '
    'our roadmap by 15 months. That is the good news.\n\n'
    'The sobering news: Asana bundled agents into their standard tier in October. Monday is '
    'now larger than us by ARR. ClearAI Work raised $120M at a $1B+ valuation. Atlassian '
    'announced agentic Jira in January. We have two acquisition targets in early diligence '
    '— both AI-native — and the board needs to understand that doing nothing is also a choice, '
    'and that choice has a cost. Our 2026 roadmap (agent builder Q2, workflow marketplace Q3, '
    'consumption pricing Q3) is credible only if we hire ~80 engineers net in H1. At current '
    '15% attrition, we will net approximately 25. That gap is the binding constraint.'
)
r.font.size = Pt(11)

# Evidence callout — Issue 1
p_ev1 = doc.add_paragraph()
p_ev1.paragraph_format.space_before = Pt(0)
p_ev1.paragraph_format.space_after  = Pt(10)
p_ev1.paragraph_format.left_indent  = Inches(0.25)
r = p_ev1.add_run('Evidence: ')
r.bold = True
r.font.size = Pt(9.5)
r.font.color.rgb = RGBColor(80, 80, 80)
r2 = p_ev1.add_run(
    'meridian_kpis_2024.csv — AI Copilot paying seats: 0 (Q1–Q1 2025) → 710 (Q4 2025).  '
    'meridian_product_roadmap_2025.md — "Net adds closer to 25 [not 80]… agent-builder depends on Helio retention."  '
    'meridian_earnings_call_q4_2025.txt — two additional AI-native acquisition targets in early diligence.'
)
r2.italic = True
r2.font.size = Pt(9.5)
r2.font.color.rgb = RGBColor(80, 80, 80)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# ISSUE 2
# ══════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after  = Pt(3)
r1 = p.add_run('ISSUE 2 OF 3 — ')
r1.bold = True
r1.font.size = Pt(10)
r1.font.color.rgb = RGBColor(150, 100, 0)
r2 = p.add_run('Mid-market is plateauing and sales efficiency has broken.')
r2.bold = True
r2.font.size = Pt(13)
r2.font.color.rgb = RGBColor(15, 60, 110)

body2 = doc.add_paragraph()
body2.paragraph_format.space_before = Pt(0)
body2.paragraph_format.space_after  = Pt(8)
r = body2.add_run(
    'Mid-market is 47% of ARR — our single largest segment. NRR has compressed from 115% '
    '(2022) to 102% (Q4 2025), eight consecutive quarters of decline. The magic number — '
    'a measure of how efficiently each sales dollar generates new ARR — crossed below 1.0 '
    'in Q2 2025 and ended Q4 at 0.92. Below 1.0 means we are spending more to acquire ARR '
    'than we are efficiently getting back. CAC payback has stretched from 18 to 22 months.\n\n'
    'The resource management module — the top-3 ask from our customer advisory board — was '
    'deferred twice in 2025 in favor of AI work. It is now on the 2026 draft roadmap for Q2. '
    'If mid-market NRR slips through 100% before Copilot generates meaningful attach in this '
    'segment, we face ARR contraction in our largest segment simultaneously with elevated '
    'go-to-market spend. That is the scenario that breaks 2026 margin guidance.'
)
r.font.size = Pt(11)

p_ev2 = doc.add_paragraph()
p_ev2.paragraph_format.space_before = Pt(0)
p_ev2.paragraph_format.space_after  = Pt(10)
p_ev2.paragraph_format.left_indent  = Inches(0.25)
r = p_ev2.add_run('Evidence: ')
r.bold = True
r.font.size = Pt(9.5)
r.font.color.rgb = RGBColor(80, 80, 80)
r2 = p_ev2.add_run(
    'meridian_kpis_2024.csv — magic number 1.20 (Q1 2024) → 0.92 (Q4 2025); '
    'CAC payback 18.2 → 22.4 months.  '
    'meridian_segments_overview.md — mid-market NRR 102%, gross logo churn 10.2%.  '
    'meridian_earnings_call_q3_2025.txt — "renewals push for price hold, expanded seats, '
    'or AI Copilot bundled in at no cost."  See chart below.'
)
r2.italic = True
r2.font.size = Pt(9.5)
r2.font.color.rgb = RGBColor(80, 80, 80)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# ISSUE 3
# ══════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after  = Pt(3)
r1 = p.add_run('ISSUE 3 OF 3 — ')
r1.bold = True
r1.font.size = Pt(10)
r1.font.color.rgb = RGBColor(150, 100, 0)
r2 = p.add_run('The organization is running hot, and a talent cliff is 90 days away.')
r2.bold = True
r2.font.size = Pt(13)
r2.font.color.rgb = RGBColor(15, 60, 110)

body3 = doc.add_paragraph()
body3.paragraph_format.space_before = Pt(0)
body3.paragraph_format.space_after  = Pt(8)
r = body3.add_run(
    'Our October 2025 employee survey (81% response rate, N=1,945) surfaced three signals '
    'the board should know. First, "roadmap thrash" is the single most common theme in '
    'engineering and product (31% of engineering open-ends) — the organization needs to '
    'believe the current direction is durable. Second, 27% of senior engineers flagged '
    'compensation as a concern; our People team has specifically identified a risk of losing '
    '15–25 senior engineers if equity is not refreshed in Q1 2026. Third, 19% of all '
    'respondents — and 28% of sales — said they can no longer clearly articulate what '
    'makes Meridian different from a competitor with AI features.\n\n'
    'Investor Day is March 11. Our new plan is due to the board by Q1 2026. We are asking '
    'the organization to execute a pricing model shift, three segment P&Ls, 80 engineer '
    'hires, and a Helio integration simultaneously. Burnout is a real risk. The comp '
    'refresh is not optional.'
)
r.font.size = Pt(11)

p_ev3 = doc.add_paragraph()
p_ev3.paragraph_format.space_before = Pt(0)
p_ev3.paragraph_format.space_after  = Pt(10)
p_ev3.paragraph_format.left_indent  = Inches(0.25)
r = p_ev3.add_run('Evidence: ')
r.bold = True
r.font.size = Pt(9.5)
r.font.color.rgb = RGBColor(80, 80, 80)
r2 = p_ev3.add_run(
    'meridian_employee_survey_2025.md — "specific risk of losing 15–25 senior engineers"; '
    '"roadmap thrash" 31% of engineering; identity confusion 28% of sales.  '
    'meridian_product_roadmap_2025.md — "net adds closer to 25 [engineers], not 80."'
)
r2.italic = True
r2.font.size = Pt(9.5)
r2.font.color.rgb = RGBColor(80, 80, 80)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# CHART
# ══════════════════════════════════════════════════════════════════════════
p_chart_label = doc.add_paragraph()
p_chart_label.paragraph_format.space_before = Pt(10)
p_chart_label.paragraph_format.space_after  = Pt(4)
r = p_chart_label.add_run('Supporting data — Key Performance Indicators Q1 2024–Q4 2025')
r.bold = True
r.font.size = Pt(10)
r.font.color.rgb = RGBColor(60, 60, 60)

p_img = doc.add_paragraph()
p_img.paragraph_format.space_before = Pt(0)
p_img.paragraph_format.space_after  = Pt(4)
p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_img = p_img.add_run()
run_img.add_picture('/home/user/Spicer/meridian_board_chart.png', width=Inches(6.2))

p_cap = doc.add_paragraph()
p_cap.paragraph_format.space_before = Pt(0)
p_cap.paragraph_format.space_after  = Pt(12)
p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_cap.add_run(
    'Left: NRR by segment — enterprise holding at 125%, mid-market compressing toward 100%, '
    'SMB at 84% and declining. Right: Magic number crossed below 1.0 in Q2 2025 and '
    'has not recovered — sales efficiency is deteriorating.\n'
    'Source: meridian_kpis_2024.csv'
)
r.italic = True
r.font.size = Pt(8.5)
r.font.color.rgb = RGBColor(100, 100, 100)

add_rule(doc)

# ══════════════════════════════════════════════════════════════════════════
# THE ASK
# ══════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(12)
p.paragraph_format.space_after  = Pt(4)
r1 = p.add_run('MY ONE ASK OF THIS BOARD')
r1.bold = True
r1.font.size = Pt(13)
r1.font.color.rgb = RGBColor(180, 30, 30)

ask_body = doc.add_paragraph()
ask_body.paragraph_format.space_before = Pt(0)
ask_body.paragraph_format.space_after  = Pt(8)
r = ask_body.add_run(
    'Authorize the People & Compensation Committee to approve a senior IC engineering '
    'equity refresh in Q1 2026, sized to re-benchmark against AI-native startup '
    'compensation. The cost is estimated at $4–7M in additional equity. The cost of '
    'losing 15–25 senior engineers in the six months before Investor Day — when we are '
    'building the product that defines our next chapter — is not recoverable. '
    'Everything else I will bring back to you at the March session. This one cannot wait.'
)
r.font.size = Pt(11.5)
r.bold = False

# Closing line
closing = doc.add_paragraph()
closing.paragraph_format.space_before = Pt(8)
closing.paragraph_format.space_after  = Pt(0)
r = closing.add_run(
    'I am proud of what this team has built. I am clear-eyed about what we have to do. '
    'Let\'s get to work.'
)
r.font.size = Pt(11)
r.italic = True

add_rule(doc)

# Footer note
foot = doc.add_paragraph()
foot.paragraph_format.space_before = Pt(6)
foot.paragraph_format.space_after  = Pt(0)
foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = foot.add_run(
    'Prepared from internal source documents: meridian_financials_2022_2025.csv, '
    'meridian_kpis_2024.csv, meridian_segments_overview.md, meridian_board_memo_strategic_outlook_2024.md, '
    'meridian_strategic_plan_2023_2026.md, meridian_earnings_call_q1–q4_2025.txt, '
    'meridian_employee_survey_2025.md, meridian_product_roadmap_2025.md'
)
r.font.size = Pt(7.5)
r.font.color.rgb = RGBColor(160, 160, 160)

doc.save('/home/user/Spicer/board_opening_remarks.docx')
print("Document saved.")
