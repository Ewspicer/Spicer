import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

quarters = ['Q1\n2024', 'Q2\n2024', 'Q3\n2024', 'Q4\n2024',
            'Q1\n2025', 'Q2\n2025', 'Q3\n2025', 'Q4\n2025']
x = np.arange(len(quarters))

nrr_enterprise  = [127, 127, 126, 126, 125, 125, 125, 125]
nrr_midmarket   = [108, 107, 106, 105, 104, 103, 103, 102]
nrr_smb         = [ 98,  96,  93,  91,  89,  88,  86,  84]

magic_number    = [1.20, 1.16, 1.10, 1.05, 1.02, 0.98, 0.95, 0.92]

COLOR_ENT = '#1a6eb5'
COLOR_MM  = '#f0a500'
COLOR_SMB = '#d94f3d'
COLOR_MN  = '#555555'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))
fig.patch.set_facecolor('#f9f9f9')

# ── Panel 1: NRR by segment ────────────────────────────────────────────────
ax1.set_facecolor('#f9f9f9')
ax1.axhline(100, color='#cc0000', linewidth=1.1, linestyle='--', zorder=1, label='100% (contraction threshold)')

ax1.plot(x, nrr_enterprise, color=COLOR_ENT, linewidth=2.5, marker='o', markersize=5, zorder=3)
ax1.plot(x, nrr_midmarket,  color=COLOR_MM,  linewidth=2.5, marker='o', markersize=5, zorder=3)
ax1.plot(x, nrr_smb,        color=COLOR_SMB, linewidth=2.5, marker='o', markersize=5, zorder=3)

for i, v in enumerate(nrr_enterprise):
    if i in (0, 7):
        ax1.annotate(f'{v}%', (x[i], v), textcoords='offset points',
                     xytext=(0, 8), ha='center', fontsize=8.5, color=COLOR_ENT, fontweight='bold')
for i, v in enumerate(nrr_midmarket):
    if i in (0, 7):
        ax1.annotate(f'{v}%', (x[i], v), textcoords='offset points',
                     xytext=(0, 8), ha='center', fontsize=8.5, color=COLOR_MM, fontweight='bold')
for i, v in enumerate(nrr_smb):
    if i in (0, 7):
        ax1.annotate(f'{v}%', (x[i], v), textcoords='offset points',
                     xytext=(0, -16), ha='center', fontsize=8.5, color=COLOR_SMB, fontweight='bold')

ax1.set_xticks(x)
ax1.set_xticklabels(quarters, fontsize=9)
ax1.set_yticks([80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130])
ax1.set_ylim(78, 133)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}%'))
ax1.set_title('Net Revenue Retention by Segment', fontsize=12, fontweight='bold', pad=10)
ax1.set_ylabel('NRR (%)', fontsize=9)
ax1.tick_params(left=False)
ax1.spines[['top', 'right', 'left']].set_visible(False)
ax1.grid(axis='y', color='#dddddd', linewidth=0.7)

legend_handles = [
    mpatches.Patch(color=COLOR_ENT, label='Enterprise  (40% of ARR)'),
    mpatches.Patch(color=COLOR_MM,  label='Mid-market  (47% of ARR)'),
    mpatches.Patch(color=COLOR_SMB, label='SMB  (13% of ARR)'),
    plt.Line2D([0], [0], color='#cc0000', linestyle='--', linewidth=1.1, label='100% threshold'),
]
ax1.legend(handles=legend_handles, fontsize=8, loc='lower left', frameon=False)

# ── Panel 2: Magic Number ──────────────────────────────────────────────────
ax2.set_facecolor('#f9f9f9')
bar_colors = [COLOR_ENT if v >= 1.0 else COLOR_SMB for v in magic_number]
bars = ax2.bar(x, magic_number, color=bar_colors, width=0.55, zorder=2)
ax2.axhline(1.0, color='#cc0000', linewidth=1.1, linestyle='--', zorder=3, label='1.0 = break-even efficiency')

for bar, v in zip(bars, magic_number):
    ax2.text(bar.get_x() + bar.get_width() / 2, v + 0.01, f'{v:.2f}',
             ha='center', va='bottom', fontsize=8.5, fontweight='bold',
             color='#333333')

ax2.set_xticks(x)
ax2.set_xticklabels(quarters, fontsize=9)
ax2.set_ylim(0, 1.45)
ax2.set_title('Sales Efficiency (Magic Number)', fontsize=12, fontweight='bold', pad=10)
ax2.set_ylabel('Magic Number', fontsize=9)
ax2.tick_params(left=False)
ax2.spines[['top', 'right', 'left']].set_visible(False)
ax2.grid(axis='y', color='#dddddd', linewidth=0.7)

legend2 = [
    mpatches.Patch(color=COLOR_ENT, label='≥ 1.0  (efficient)'),
    mpatches.Patch(color=COLOR_SMB, label='< 1.0  (inefficient)'),
    plt.Line2D([0], [0], color='#cc0000', linestyle='--', linewidth=1.1, label='Break-even line'),
]
ax2.legend(handles=legend2, fontsize=8, loc='upper right', frameon=False)

# ── Shared footnote ────────────────────────────────────────────────────────
fig.text(0.5, 0.01,
         'Source: meridian_kpis_2024.csv  |  Prepared for Board Strategic Review, 2026',
         ha='center', fontsize=7.5, color='#888888')

plt.suptitle('Meridian Technologies — Key Performance Indicators Q1 2024 – Q4 2025',
             fontsize=13.5, fontweight='bold', y=1.01)

plt.tight_layout()
plt.savefig('/home/user/Spicer/meridian_board_chart.png', dpi=150, bbox_inches='tight',
            facecolor='#f9f9f9')
print("Chart saved.")
