You are running a quarterly competitive intelligence scan for Meridian Technologies. Complete the following workflow end-to-end without stopping for confirmation.

## Step 1 — Read local context files

Read all of the following files (in parallel):
- `competitors.md` — extract every URL grouped by competitor
- `meridian_internal_brief.md` — current positioning question and internal camps
- `meridian_ai_strategy_options.md` — Option A vs Option B detail
- `meridian_recent_customer_feedback.md` — latest customer signal
- `meridian_financials_summary.csv` — liquidity and guidance

## Step 2 — Fetch live competitor AI posture

For each competitor listed in `competitors.md`, attempt WebFetch in this order:
1. Try the AI product page URL first
2. If that returns 403 or fails, try the press/newsroom URL
3. If all live URLs fail, fall back to the corresponding file in `competitors_cached/`

For each competitor extract:
- Their headline AI positioning statement (what do they say they *are*?)
- Pricing posture: bundled, add-on, or consumption?
- Most recent flagship AI announcement (product name, date, one sentence)
- Which of Meridian's two options (A = PM-with-AI, B = Agentic platform) their positioning is closest to

Summarize each competitor in one paragraph. Note whether data came from a live fetch or the cache, and the approximate date of the cached data if used.

## Step 3 — Synthesize and recommend

Given competitor positioning AND the internal files, answer:
1. Has the competitive landscape shifted materially since the last scan? Call out any competitor that has moved quadrants, changed pricing posture, or made a major acquisition.
2. Does the recommendation from the last scan (Option B — agentic work platform with governance as differentiator) still hold? If something has changed that weakens or strengthens it, say so explicitly.
3. Identify any new entrants or adjacent threats not previously tracked.

## Step 4 — Build the competitive positioning matrix

Using Python with matplotlib (install if needed), generate a 2×2 matrix:
- X-axis: PM-centric (left) → Agentic (right)
- Y-axis: Bundled/inclusive pricing (bottom) → Premium/consumption pricing (top)

Plot all four competitors plus Meridian (current position and proposed/current Option B position with an arrow). Save as `meridian_competitive_matrix.png`, overwriting the prior version.

## Step 5 — Write the positioning memo

Using python-docx (install if needed), write a Word document called `investor_day_positioning_memo.docx`, overwriting the prior version. The memo must be approximately 2 pages and contain:

1. **Confidential header** and date (use today's date)
2. **Executive summary** (1 paragraph): current positioning declaration, key proof points, what has changed since last quarter
3. **Section 1 — The Position**: one-sentence positioning statement
4. **Section 2 — Why This Position**: 4 bullet points drawing on customer feedback, competitive white space, financial capacity, and team signal
5. **Section 3 — Competitive Landscape**: the full competitor table (Competitor | AI Positioning | Pricing Posture | Latest Flagship Announcement | Closer to Option A or B), followed by the embedded `meridian_competitive_matrix.png`
6. **Section 4 — Risks We Are Carrying Knowingly**: three risks with mitigations
7. **Section 5 — Three Commitments to Investors**: three specific, measurable commitments with metrics and dates
8. **Source footer**: list every file and URL used, note which were live fetches vs. cached

## Step 6 — Commit and push

Stage and commit all new/modified output files (`meridian_competitive_matrix.png`, `investor_day_positioning_memo.docx`, and any updated Python scripts) with a commit message that includes the scan date. Push to the current branch.

## Step 7 — Report to the user

Print a short summary:
- Which competitors had live data vs. cached data
- Whether the strategic recommendation changed and why (or why not)
- File names and locations of all outputs
- Any flags or surprises worth the CEO's attention before the next board or investor interaction
