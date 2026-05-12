import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Data ──────────────────────────────────────────────────────────────────
# X: 0 = fully PM-centric  →  10 = fully agentic
# Y: 0 = fully bundled      →  10 = fully premium / consumption

companies = {
    'Smartsheet':            {'x': 2.0, 'y': 4.2, 'color': '#7a7a7a',  'marker': 'o', 'size': 180},
    'Monday.com':            {'x': 4.8, 'y': 1.5, 'color': '#e8513a',  'marker': 'o', 'size': 180},
    'Asana':                 {'x': 7.0, 'y': 2.5, 'color': '#f06a35',  'marker': 'o', 'size': 180},
    'Atlassian':             {'x': 8.8, 'y': 7.8, 'color': '#0052cc',  'marker': 'o', 'size': 180},
    'Meridian\n(today)':     {'x': 4.2, 'y': 5.5, 'color': '#1a6eb5',  'marker': 's', 'size': 200},
    'Meridian\n(Option B)':  {'x': 7.8, 'y': 7.2, 'color': '#1a6eb5',  'marker': '*', 'size': 420},
}

label_offsets = {
    'Smartsheet':           (-0.35,  0.45),
    'Monday.com':           ( 0.15,  0.38),
    'Asana':                ( 0.15,  0.38),
    'Atlassian':            ( 0.15,  0.38),
    'Meridian\n(today)':    (-0.45,  0.45),
    'Meridian\n(Option B)': ( 0.20,  0.45),
}

# ── Canvas ────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 8))
fig.patch.set_facecolor('#f9f9f9')
ax.set_facecolor('#f9f9f9')

ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# ── Quadrant shading ──────────────────────────────────────────────────────
ax.fill_between([0, 5], [5, 5], [10, 10], color='#eaf3fb', alpha=0.6, zorder=0)   # TL
ax.fill_between([5, 10], [5, 5], [10, 10], color='#e8f6ee', alpha=0.6, zorder=0)  # TR ← target
ax.fill_between([0, 5], [0, 0], [5, 5], color='#fdf5e6', alpha=0.6, zorder=0)     # BL
ax.fill_between([5, 10], [0, 0], [5, 5], color='#fdeaea', alpha=0.6, zorder=0)    # BR

# Quadrant labels
quad_style = dict(fontsize=8.5, color='#999999', style='italic', ha='center', va='center')
ax.text(2.5, 9.2, 'Cautious / Premium\n(niche regulated play)', **quad_style)
ax.text(7.5, 9.2, 'Agentic + Premium\n(target white space)', **quad_style)
ax.text(2.5, 0.8, 'Cautious / Bundled\n(commodity risk)', **quad_style)
ax.text(7.5, 0.8, 'Agentic / Bundled\n(volume play, low margin)', **quad_style)

# ── Axes lines ────────────────────────────────────────────────────────────
ax.axvline(5, color='#cccccc', linewidth=1.2, zorder=1)
ax.axhline(5, color='#cccccc', linewidth=1.2, zorder=1)

# ── Arrow: Meridian trajectory ───────────────────────────────────────────
src = companies['Meridian\n(today)']
dst = companies['Meridian\n(Option B)']
ax.annotate('',
    xy=(dst['x'] - 0.15, dst['y'] - 0.15),
    xytext=(src['x'] + 0.15, src['y'] + 0.15),
    arrowprops=dict(arrowstyle='->', color='#1a6eb5', lw=1.8,
                    connectionstyle='arc3,rad=0.15'),
    zorder=3)

# ── Plot points ───────────────────────────────────────────────────────────
for name, d in companies.items():
    ax.scatter(d['x'], d['y'], color=d['color'], marker=d['marker'],
               s=d['size'], zorder=4,
               edgecolors='white', linewidths=1.2)
    dx, dy = label_offsets[name]
    ax.text(d['x'] + dx, d['y'] + dy, name,
            ha='center', va='bottom', fontsize=9,
            fontweight='bold' if 'Option B' in name else 'normal',
            color=d['color'], zorder=5)

# ── Axis labels & ticks ───────────────────────────────────────────────────
ax.set_xlabel('AI Positioning  ←  PM-centric · · · · · · · · · Agentic  →',
              fontsize=10, labelpad=10)
ax.set_ylabel('Pricing Posture  ←  Bundled / Inclusive · · · Premium / Consumption  →',
              fontsize=10, labelpad=10)
ax.set_xticks([])
ax.set_yticks([])
ax.spines[['top', 'right', 'bottom', 'left']].set_visible(False)

# ── Legend ────────────────────────────────────────────────────────────────
legend_elements = [
    plt.scatter([], [], marker='o', color='#7a7a7a', s=80, label='Competitor'),
    plt.scatter([], [], marker='s', color='#1a6eb5', s=80, label='Meridian today'),
    plt.scatter([], [], marker='*', color='#1a6eb5', s=160, label='Meridian Option B (proposed)'),
]
ax.legend(handles=legend_elements, fontsize=8.5, loc='lower left',
          frameon=True, framealpha=0.85, edgecolor='#cccccc')

# ── Title & footnote ──────────────────────────────────────────────────────
ax.set_title('Competitive Positioning Matrix\nAI Strategy × Pricing Posture',
             fontsize=13, fontweight='bold', pad=14)
fig.text(0.5, 0.01,
         'Source: competitors_cached/  |  Prepared for Investor Day, March 11 2026',
         ha='center', fontsize=7.5, color='#999999')

plt.tight_layout()
plt.savefig('/home/user/Spicer/meridian_competitive_matrix.png', dpi=150,
            bbox_inches='tight', facecolor='#f9f9f9')
print("Matrix saved.")
