# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
#     "pandas>=3.0.2",
#     "matplotlib>=3.10.8",
#     "seaborn>=0.13.2",
#     "altair>=6.0.0",
#     "plotly>=6.7.0",
# ]
# ///

import marimo

__generated_with = "0.23.1"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


# ============================================================
# TITLE
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Week 7: Data Visualization to Communicate Results
    ### Concept Guide — Numerical Overview
    ---
    This notebook walks through the key concepts covered in
    `7_DataVisualizationToCommunicateResults.py`, in the order they appear.
    Each section includes a description of the concept, an example code snippet,
    and an explanation of what the code demonstrates.
    """)
    return


# ============================================================
# CONCEPT 1 — What is Data Visualization
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 1: What is Data Visualization?

    **Definition:** Data visualization is the graphical representation of
    information and data using visual elements such as charts, graphs, and maps.

    **Why it matters:**
    - Humans process visuals much faster than raw numbers or text.
    - Helps reveal trends, outliers, and patterns that would be invisible
      in a spreadsheet.
    - Supports data-driven decision making by making complex data accessible.

    **Key insight from the lecture:** Our eyes are drawn to colors and patterns.
    A well-designed chart lets us *internalize* information quickly — it is
    storytelling with a purpose.
    """)
    return


@app.cell
def _():
    # Simple example: turning a table of numbers into a bar chart
    import matplotlib.pyplot as plt

    categories = ['Category A', 'Category B', 'Category C', 'Category D']
    values = [42, 78, 55, 91]

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Left: raw table (text)
    axes[0].axis('off')
    table_data = [['Category', 'Value']] + [[c, v] for c, v in zip(categories, values)]
    axes[0].table(cellText=table_data, loc='center', cellLoc='center')
    axes[0].set_title('Raw Data (hard to interpret quickly)')

    # Right: bar chart (visual)
    axes[1].bar(categories, values, color='steelblue')
    axes[1].set_title('Same Data as a Bar Chart (instantly clear)')
    axes[1].set_ylabel('Value')

    plt.tight_layout()
    plt.gca()
    return fig, axes, categories, values


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left panel shows the same data as a plain text table — you have to read
    every row to compare values. The right panel turns it into a bar chart
    where the tallest bar (Category D = 91) is immediately obvious.
    This is the core argument for data visualization: the visual form
    communicates the same information far more efficiently.
    """)
    return


# ============================================================
# CONCEPT 2 — Exploratory vs. Explanatory Visualization
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 2: Exploratory vs. Explanatory Visualization

    There are two distinct purposes a visualization can serve:

    | Type | Purpose | Audience |
    |---|---|---|
    | **Exploratory** | Understand the data yourself; find what is worth sharing | You / your team |
    | **Explanatory** | Communicate a specific story or finding to others | External audience |

    **The course focuses on Explanatory visualizations** — the kind you make
    *after* you already know what the data says and you want to present it clearly.

    Think of it this way: exploratory is the rough draft; explanatory is the
    polished final presentation.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Simulate a small dataset
    import random
    random.seed(42)
    data = pd.DataFrame({
        'month': list(range(1, 13)),
        'sales': [120, 135, 98, 160, 175, 210, 198, 220, 195, 230, 250, 310]
    })

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # --- Exploratory: quick, unstyled, all data shown ---
    axes[0].plot(data['month'], data['sales'], marker='o')
    axes[0].set_title('Exploratory: Quick Look at Sales')
    axes[0].set_xlabel('Month')
    axes[0].set_ylabel('Sales')

    # --- Explanatory: styled, focused, with annotation ---
    axes[1].plot(data['month'], data['sales'], marker='o', color='steelblue', linewidth=2)
    axes[1].axvline(x=12, color='red', linestyle='--', alpha=0.6)
    axes[1].annotate('Holiday Peak\n+48% vs prior month',
                     xy=(12, 310), xytext=(9, 290),
                     arrowprops=dict(arrowstyle='->', color='red'),
                     color='red', fontsize=9)
    axes[1].set_title('Explanatory: December Holiday Sales Surge')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Sales')
    axes[1].set_xticks(range(1, 13))
    axes[1].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun',
                              'Jul','Aug','Sep','Oct','Nov','Dec'])

    plt.tight_layout()
    plt.gca()
    return axes, data, fig, pd, random, sns


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left plot is *exploratory* — a quick line chart to see if a trend exists.
    The right plot is *explanatory* — it has been styled, labeled clearly, and
    annotated to direct the audience's attention to the December holiday sales surge.
    Notice how the annotation and red reference line tell the audience exactly
    what conclusion to draw without them having to figure it out themselves.
    """)
    return


# ============================================================
# CONCEPT 3 — Context: Who, What, How
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 3: Context — Who, What, How

    Before creating any visualization, the lecture emphasizes three planning questions:

    - **Who** are you communicating to?
      Know your audience's background, expertise level, and what they care about.
    - **What** do you want to communicate?
      Have a single, clear message. If you cannot state it in one sentence, rethink it.
    - **How** can you use data to support your point?
      Choose the chart type, data subset, and format that best supports the message.

    **Guided by a question:** Every good explanatory visualization is built around
    a specific question to be answered.

    **Example from the lecture:** The film dialogue visualization (Hanah Anderson
    and Matt Daniels) asked: *"Is there a gender disparity in spoken lines of
    dialogue in major Hollywood films?"* Every design choice flowed from that question.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Simulated salary data — same dataset, two different "who/what/how" framings
    departments = ['Engineering', 'Marketing', 'HR', 'Finance', 'Operations']
    avg_salary = [95000, 72000, 65000, 85000, 70000]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Framing 1: for HR team — "are salaries fair across departments?"
    colors_hr = ['steelblue'] * 5
    axes[0].barh(departments, avg_salary, color=colors_hr)
    axes[0].set_title('For HR: Average Salary by Department\n(Is pay equitable?)')
    axes[0].set_xlabel('Average Salary ($)')
    axes[0].axvline(x=sum(avg_salary)/len(avg_salary), color='red',
                    linestyle='--', label='Company Average')
    axes[0].legend()

    # Framing 2: for executive team — "where is headcount spend highest?"
    highlight = ['tomato' if d == 'Engineering' else 'lightgrey' for d in departments]
    axes[1].barh(departments, avg_salary, color=highlight)
    axes[1].set_title('For Executives: Engineering Drives\nHighest Per-Person Cost')
    axes[1].set_xlabel('Average Salary ($)')

    plt.tight_layout()
    plt.gca()
    return avg_salary, colors_hr, departments, fig, axes, highlight, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    Both charts use exactly the same underlying data, but they answer different
    questions for different audiences. The left chart is designed for an HR team
    comparing all departments to a company average. The right chart highlights
    Engineering specifically — the message is tailored for an executive audience
    asking about where the highest per-person cost sits. Choosing *who* and *what*
    first changes every design decision that follows.
    """)
    return


# ============================================================
# CONCEPT 4 — Altair Interactive Chart (mo.ui.altair_chart)
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 4: Interactive Charts with Altair and Marimo (`mo.ui.altair_chart`)

    The lecture builds its main visualization — a stacked bar chart of Disney film
    dialogue broken down by gender — using **Altair** wrapped in Marimo's
    `mo.ui.altair_chart`. This combination creates a fully reactive, clickable chart.

    **How it works:**
    - `alt.Chart(df).mark_bar()` specifies the chart type.
    - `.encode()` maps data columns to visual channels: x-axis, y-axis, and color.
    - `alt.Scale(domain=..., range=...)` lets you assign specific colors to categories.
    - Wrapping the chart in `mo.ui.altair_chart(...)` makes it interactive inside Marimo:
      clicking a bar updates `chart.value` in a reactive downstream cell.

    **From the project file (lines 395-418):**
    ```python
    final_plot = mo.ui.altair_chart(
        alt.Chart(top_30).mark_bar().encode(
            x=alt.X('percentage:Q', title='Percent'),
            y=alt.Y('title:N', title='Movie Title', sort=male_order),
            color=alt.Color('gender:N', title='Gender',
                            scale=alt.Scale(
                                domain=['m', 'f'],
                                range=['#3266ad', '#c9a0b5']
                            ))
        ).properties(
            title='Top 16 Disney Movies by Word Count (Percentage), distinguished by Gender',
            width=500,
            height=400
        )
    )
    final_plot
    ```
    The cell below demonstrates the same pattern with the wages dataset.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import altair as alt
    import marimo as mo

    wages = pd.read_csv('/mnt/project/wages.csv')

    # Clean salary: remove '$' and ',' then convert to float
    wages['Salary_num'] = (wages['Salary']
                           .str.replace('$', '', regex=False)
                           .str.replace(',', '', regex=False)
                           .astype(float))

    dept_gender = (wages.groupby(['Department', 'Gender'])['Salary_num']
                   .mean()
                   .reset_index(name='Avg_Salary'))

    interactive_chart = mo.ui.altair_chart(
        alt.Chart(dept_gender).mark_bar().encode(
            x=alt.X('Avg_Salary:Q', title='Average Salary ($)'),
            y=alt.Y('Department:N', title='Department'),
            color=alt.Color('Gender:N', title='Gender',
                            scale=alt.Scale(
                                domain=['Male', 'Female'],
                                range=['#3266ad', '#c9a0b5']
                            ))
        ).properties(
            title='Average Salary by Department and Gender',
            width=450,
            height=250
        )
    )
    interactive_chart
    return alt, dept_gender, interactive_chart, mo, pd, wages


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    This replicates the pattern from the project file using the `wages.csv` dataset.
    `alt.Chart` builds the chart specification declaratively — you describe *what*
    to show, not *how* to draw it. `mark_bar()` selects a bar chart.
    `encode()` binds columns to axes and color. The `alt.Scale` inside
    `alt.Color` manually maps Male to blue and Female to pink, matching the
    intentional color choices from the lecture. Wrapping everything in
    `mo.ui.altair_chart` makes the bars clickable in Marimo — clicking filters
    the data reactively.
    """)
    return


# ============================================================
# CONCEPT 5 — Telling a Data Story
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 5: Telling a Data Story

    Data storytelling combines data visualization with a compelling narrative.
    The lecture identifies four ingredients of a great data story:

    1. **Relevant** — content fits the audience's knowledge level and helps them
       reach a goal.
    2. **Good data** — from a reputable, verifiable source; honest and unbiased.
    3. **Clear narrative** — has a beginning, middle, and end with a specific
       call to action.
    4. **Intentional visuals** — appropriate chart type, well-labeled, legible,
       and not misleading.

    **Key quote from the lecture:**
    > "Data storytelling couples data visualization with compelling narratives
    > that help audiences better comprehend and take action based on data analysis."

    The structure mirrors traditional storytelling: introduce the topic,
    present the data, and conclude with a clear takeaway or call to action.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    # Demonstrate a data story arc in one figure with three panels
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    support_tickets = [120, 135, 155, 190, 230, 280]
    staff_count = [10, 10, 10, 10, 10, 12]

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # Panel 1 — Beginning: introduce the problem
    axes[0].bar(months, support_tickets, color='steelblue')
    axes[0].set_title('1. Beginning: Tickets Are Rising', fontweight='bold')
    axes[0].set_ylabel('Support Tickets')

    # Panel 2 — Middle: show the gap (staff flat, tickets rising)
    axes[1].plot(months, support_tickets, marker='o', label='Tickets', color='tomato')
    axes[1].plot(months, [s * 20 for s in staff_count],
                 marker='s', label='Staff Capacity', color='steelblue', linestyle='--')
    axes[1].set_title('2. Middle: Staff Cannot Keep Up', fontweight='bold')
    axes[1].set_ylabel('Count')
    axes[1].legend()

    # Panel 3 — End: call to action
    axes[2].axis('off')
    axes[2].text(0.5, 0.6,
                 'Call to Action:\nHire 4 additional\nsupport staff by Q3',
                 ha='center', va='center', fontsize=13,
                 bbox=dict(boxstyle='round', facecolor='#f9e79f', edgecolor='orange'),
                 transform=axes[2].transAxes)
    axes[2].set_title('3. End: A Clear Recommendation', fontweight='bold')

    plt.tight_layout()
    plt.gca()
    return axes, fig, months, pd, staff_count, support_tickets


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The three panels demonstrate the beginning-middle-end arc of a data story.
    Panel 1 introduces the problem (rising tickets). Panel 2 shows why it matters
    (staff capacity is not growing with demand). Panel 3 delivers the call to action
    (hire more staff). Without all three panels, the audience either lacks context
    or lacks direction. Together they form a complete, actionable story.
    """)
    return


# ============================================================
# CONCEPT 6 — Clutter and Cognitive Load
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 6: Clutter and Cognitive Load

    **Clutter** is defined in the lecture as *visual elements that take up space
    but do not increase understanding*. Every extra element an audience has to
    process is mental work — this is called **cognitive load**.

    High cognitive load means your audience spends energy decoding the chart
    instead of understanding the message. The goal is to reduce cognitive load
    by removing anything that does not serve the story.

    Common sources of clutter:
    - Gridlines that are too heavy or too numerous
    - Unnecessary borders and tick marks
    - Redundant axis labels
    - 3D effects on 2D data
    - Too many colors with no meaning attached
    - Legends that could be replaced by direct labels
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    categories = ['Q1', 'Q2', 'Q3', 'Q4']
    revenue = [220, 310, 275, 410]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # --- Cluttered version ---
    ax = axes[0]
    bars = ax.bar(categories, revenue, color=['red', 'blue', 'green', 'orange'],
                  edgecolor='black', linewidth=1.5)
    ax.set_title('HIGH CLUTTER: Quarterly Revenue Report!!!', fontsize=10,
                 fontweight='bold', color='purple')
    ax.set_xlabel('QUARTER (Q1-Q4)', fontsize=9)
    ax.set_ylabel('REVENUE ($000s)', fontsize=9)
    ax.yaxis.grid(True, linestyle='-', linewidth=1.2, color='grey')
    ax.set_facecolor('#fffacd')
    for bar, val in zip(bars, revenue):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                f'${val}k', ha='center', fontsize=8)
    ax.spines['top'].set_visible(True)
    ax.spines['right'].set_visible(True)
    ax.tick_params(length=8)

    # --- Clean version ---
    ax2 = axes[1]
    bars2 = ax2.bar(categories, revenue, color='steelblue')
    ax2.set_title('Quarterly Revenue — Q4 Strongest', fontsize=10)
    ax2.set_ylabel('Revenue ($000s)')
    ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey', alpha=0.7)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.tick_params(length=0)
    # Highlight Q4 only
    bars2[3].set_color('tomato')
    ax2.text(3, revenue[3] + 8, 'Best quarter', ha='center', fontsize=8, color='tomato')

    plt.tight_layout()
    plt.gca()
    return ax, ax2, axes, bars, bars2, categories, fig, np, revenue


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left chart is deliberately cluttered: four different bar colors (no meaning),
    heavy gridlines, a loud title, a yellow background, visible top and right spines,
    and long tick marks. Every one of those elements adds cognitive load without
    adding information. The right chart strips all of that away: one color for all
    bars, light dashed gridlines, no unnecessary spines, and a single red highlight
    on Q4 with a direct annotation. The message (Q4 was best) is visible in
    seconds on the right and buried in noise on the left.
    """)
    return


# ============================================================
# CONCEPT 7 — Visual Order, Alignment, and White Space
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 7: Visual Order, Alignment, and White Space

    The lecture covers two closely related design principles:

    **Visual Order / Alignment:** When elements on a page are aligned to an
    invisible grid, the design feels organized and professional. Misaligned
    elements feel accidental and uncomfortable, even if the viewer cannot
    articulate why.

    **White Space:** Empty space in a visual is not wasted — it is a design tool.
    White space:
    - Gives the eye a place to rest.
    - Draws attention to the non-white-space areas.
    - Makes a layout feel clean and intentional rather than cramped.

    The lecture analogy: white space in a visual is like pauses in a speech.
    A presentation without pauses is exhausting to listen to; a chart without
    white space is exhausting to look at.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # --- Poor alignment and no white space ---
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title('Poor Alignment / No White Space', fontsize=10)
    ax.axis('off')
    # Elements scattered randomly
    positions = [(0.1, 8.5), (3.0, 5.2), (6.5, 9.0), (1.0, 2.0),
                 (5.0, 1.5), (8.0, 4.0), (0.5, 6.0), (7.0, 7.5)]
    for i, (x, y) in enumerate(positions):
        ax.add_patch(patches.FancyBboxPatch((x, y), 1.8, 0.8,
                     boxstyle='round,pad=0.1', facecolor='#aed6f1', edgecolor='grey'))
        ax.text(x + 0.9, y + 0.4, f'Item {i+1}', ha='center', va='center', fontsize=7)

    # --- Good alignment and white space ---
    ax2 = axes[1]
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title('Good Alignment / Strategic White Space', fontsize=10)
    ax2.axis('off')
    # Elements aligned to a grid with consistent spacing
    for row in range(4):
        for col in range(2):
            x = 1.5 + col * 4.5
            y = 7.5 - row * 2.0
            ax2.add_patch(patches.FancyBboxPatch((x, y), 3.5, 1.2,
                          boxstyle='round,pad=0.1', facecolor='#aed6f1', edgecolor='grey'))
            ax2.text(x + 1.75, y + 0.6, f'Item {row*2+col+1}',
                     ha='center', va='center', fontsize=8)

    plt.tight_layout()
    plt.gca()
    return ax, ax2, axes, col, fig, i, patches, positions, row, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left panel scatters elements at random positions — there is no alignment
    and elements crowd each other. The right panel places the same number of items
    on a regular grid with consistent spacing. Even though the content is identical,
    the right layout feels calm and organized while the left feels chaotic.
    This mirrors the before/after example in the lecture (visual_order1.png vs
    visual_order2.png): minor alignment changes can make a large difference in
    how approachable a visual feels.
    """)
    return


# ============================================================
# CONCEPT 8 — Preattentive Attributes
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 8: Preattentive Attributes

    **Preattentive attributes** are visual properties that the human brain
    processes *before* conscious attention kicks in — in roughly 250 milliseconds.
    Because they are processed so fast, they are extremely powerful tools for
    directing an audience's attention.

    The lecture highlights several preattentive attributes:
    - **Color** (hue and intensity)
    - **Size** (length, area)
    - **Position**
    - **Orientation**
    - **Shape**

    **Strategic use:** Pick one or two preattentive attributes to highlight the
    most important element in your chart. Using too many at once defeats the
    purpose — if everything stands out, nothing does.
    """)
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import numpy as np

    # Demonstrate color as a preattentive attribute
    np.random.seed(7)
    x = np.random.rand(30)
    y = np.random.rand(30)
    colors = ['lightgrey'] * 30
    sizes = [60] * 30

    # Make one point stand out
    colors[14] = 'tomato'
    sizes[14] = 200

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Left: no preattentive cue — all points identical
    axes[0].scatter(x, y, color='steelblue', s=60)
    axes[0].set_title('No Preattentive Attribute\n(Which point matters?)')
    axes[0].axis('off')

    # Right: color + size as preattentive cues
    axes[1].scatter(x, y, c=colors, s=sizes)
    axes[1].set_title('Color + Size as Preattentive Attributes\n(Eye goes straight to the outlier)')
    axes[1].axis('off')

    plt.tight_layout()
    plt.gca()
    return axes, colors, fig, np, sizes, x, y


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    On the left, all 30 points look identical — your eye has no idea where to go.
    On the right, one point is red and larger: your eye jumps to it instantly,
    before you consciously think about the chart. That is a preattentive attribute
    at work. In a real chart you would use this to highlight the outlier, the key
    result, or the data point your narrative is about.
    """)
    return


# ============================================================
# CONCEPT 9 — Eliminate Distractions
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 9: Eliminate Distractions

    The lecture quotes Antoine de Saint-Exupery: *"You know you've achieved
    perfection, not when you have nothing more to add, but when you have nothing
    to take away."*

    When reviewing a chart, ask:
    - **Does this element change anything if removed?** If no, remove it.
    - **Is this detail necessary for the audience?** If not, summarize or cut it.
    - **Is this distracting from the main message?** Push it to the background
      with light grey or remove it entirely.

    The four checklist items from the lecture:
    1. Not all data are equally important — remove noncritical components.
    2. When detail is not needed, summarize.
    3. If eliminating something changes nothing, eliminate it.
    4. Push necessary but non-message items to the background using light grey.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    wages = pd.read_csv('/mnt/project/wages.csv')
    wages['Salary_num'] = (wages['Salary']
                           .str.replace('$', '', regex=False)
                           .str.replace(',', '', regex=False)
                           .astype(float))

    dept_avg = wages.groupby('Department')['Salary_num'].mean().sort_values(ascending=False)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # --- Before: distracting elements ---
    ax1 = axes[0]
    bars = ax1.bar(dept_avg.index, dept_avg.values,
                   color=['red','blue','green','orange','purple','pink','brown'],
                   edgecolor='black', linewidth=1.5)
    ax1.set_title('BEFORE: Average Salary by Department', fontsize=10, fontweight='bold')
    ax1.set_xlabel('Department')
    ax1.set_ylabel('Average Salary ($)')
    ax1.tick_params(axis='x', rotation=45)
    for bar, val in zip(bars, dept_avg.values):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                 f'${val:,.0f}', ha='center', fontsize=6, rotation=0)
    ax1.yaxis.grid(True, linestyle='-', linewidth=1.0, color='grey')
    ax1.spines['top'].set_visible(True)
    ax1.spines['right'].set_visible(True)

    # --- After: distractions eliminated ---
    ax2 = axes[1]
    highlight_dept = dept_avg.index[0]  # highest paid department
    bar_colors = ['tomato' if d == highlight_dept else 'lightgrey' for d in dept_avg.index]
    bars2 = ax2.bar(dept_avg.index, dept_avg.values, color=bar_colors)
    ax2.set_title(f'AFTER: {highlight_dept} Has Highest Average Pay', fontsize=10)
    ax2.set_ylabel('Average Salary ($)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey', alpha=0.6)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.tick_params(length=0)
    # Annotate only the highlighted bar
    top_val = dept_avg.values[0]
    ax2.text(0, top_val + 500, f'${top_val:,.0f}', ha='center', fontsize=8, color='tomato')

    plt.tight_layout()
    plt.gca()
    return (ax1, ax2, axes, bar_colors, bars, bars2,
            dept_avg, fig, highlight_dept, pd, top_val, wages)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left chart has seven different bar colors (meaningless), heavy gridlines,
    visible top and right spines, value labels on every bar, and rotated x-tick marks —
    all fighting for attention at once. The right chart eliminates every element that
    does not serve the message: one color for the key bar, grey for everything else,
    a single annotation, no unnecessary spines. The conclusion (which department pays
    the most) is immediate on the right and buried on the left.
    """)
    return


# ============================================================
# CONCEPT 10 — Text as a Design Element (Annotation)
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 10: Text as a Design Element (Annotation)

    The lecture says: *"Text plays a number of roles in communicating with data:
    use it to label, introduce, explain, reinforce, highlight, recommend, and
    tell a story."*

    **Non-negotiable text rules from the lecture:**
    - Every chart must have a **title**.
    - Every axis must have a **title** (exceptions are extremely rare).
    - If you want the audience to draw a specific conclusion, **state it in words**.
    - Use annotation to explain nuances, highlight interesting points, or describe
      external factors.

    **Reference example from the lecture:** David McCandless's "Peak Break-up Times"
    chart uses short annotations at each spike to tell the story of *why* break-ups
    happen when they do, transforming a raw line chart into a memorable narrative.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    wages = pd.read_csv('/mnt/project/wages.csv')
    wages['Salary_num'] = (wages['Salary']
                           .str.replace('$', '', regex=False)
                           .str.replace(',', '', regex=False)
                           .astype(float))
    wages['Age_group'] = pd.cut(wages['Age'], bins=[20, 30, 40, 50, 60, 70],
                                labels=['20s', '30s', '40s', '50s', '60s'])

    age_salary = wages.groupby('Age_group', observed=True)['Salary_num'].mean()

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # --- No annotation: audience must figure it out ---
    axes[0].plot(age_salary.index, age_salary.values, marker='o', color='steelblue')
    axes[0].set_title('Average Salary by Age Group')
    axes[0].set_ylabel('Average Salary ($)')
    axes[0].set_xlabel('Age Group')

    # --- With annotation: audience is guided ---
    axes[1].plot(age_salary.index, age_salary.values, marker='o',
                 color='steelblue', linewidth=2)
    axes[1].set_title('Salary Peaks in the 40s Then Plateaus')
    axes[1].set_ylabel('Average Salary ($)')
    axes[1].set_xlabel('Age Group')

    # Annotate the peak
    peak_idx = age_salary.values.argmax()
    peak_label = age_salary.index[peak_idx]
    peak_val = age_salary.values[peak_idx]
    axes[1].annotate(f'Peak: ${peak_val:,.0f}\ncareer mid-point',
                     xy=(peak_idx, peak_val),
                     xytext=(peak_idx + 0.5, peak_val - 3000),
                     arrowprops=dict(arrowstyle='->', color='tomato'),
                     color='tomato', fontsize=9)

    plt.tight_layout()
    plt.gca()
    return (age_salary, axes, fig, pd, peak_idx, peak_label, peak_val, wages)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left chart has a title and axis labels, but leaves all interpretation to
    the audience. The right chart adds an annotation at the salary peak, pointing
    directly to the key finding and naming it. Matplotlib's `annotate()` function
    places text with an arrow at a specific data coordinate. This is the technique
    behind the McCandless break-up chart referenced in the lecture: a few well-placed
    words make the story self-evident without requiring the audience to search.
    """)
    return


# ============================================================
# CONCEPT 11 — Don't Overcomplicate Things
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 11: Don't Overcomplicate Things

    The lecture cites a University of Michigan study: when the same exercise
    instructions were printed in a hard-to-read font, students rated the workout
    as harder and were less likely to try it. The principle translates directly
    to data visualization: *"The more complicated it looks, the more time your
    audience perceives it will take to understand, and the less likely they are
    to spend time to understand it."*

    Practical rules from the lecture:
    - **Legible font** — consistent typeface, appropriate size.
    - **Clean design** — leverage visual affordances.
    - **Straightforward language** — simple over complex, fewer words over more.
    - **Remove unnecessary complexity** — when in doubt, favor simple.

    This does not mean oversimplifying data; it means not making things harder
    than they need to be.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt

    wages = pd.read_csv('/mnt/project/wages.csv')
    wages['Salary_num'] = (wages['Salary']
                           .str.replace('$', '', regex=False)
                           .str.replace(',', '', regex=False)
                           .astype(float))

    gender_salary = wages.groupby('Gender')['Salary_num'].mean()

    fig, axes = plt.subplots(1, 2, figsize=(11, 5))

    # --- Overcomplicated ---
    ax1 = axes[0]
    wedges, texts, autotexts = ax1.pie(
        gender_salary.values,
        labels=[f'{g}\n${v:,.0f}\n({v/gender_salary.sum()*100:.1f}%)'
                for g, v in zip(gender_salary.index, gender_salary.values)],
        autopct='',
        colors=['#3266ad', '#c9a0b5'],
        startangle=90,
        explode=[0.05, 0.05],
        shadow=True
    )
    ax1.set_title('OVERCOMPLICATED:\nAverage Salary — Male vs Female\n(3D? Exploded? Redundant labels?)',
                  fontsize=8)

    # --- Simple bar chart: same info, much clearer ---
    ax2 = axes[1]
    bars = ax2.bar(gender_salary.index, gender_salary.values,
                   color=['#3266ad', '#c9a0b5'], width=0.4)
    ax2.set_title('SIMPLE: Average Salary by Gender', fontsize=10)
    ax2.set_ylabel('Average Salary ($)')
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.yaxis.grid(True, linestyle='--', linewidth=0.5, color='lightgrey')
    ax2.tick_params(length=0)
    for bar, val in zip(bars, gender_salary.values):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 200,
                 f'${val:,.0f}', ha='center', fontsize=10)

    plt.tight_layout()
    plt.gca()
    return (ax1, ax2, axes, bars, fig, gender_salary, pd,
            texts, autotexts, wedges, wages)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The left chart is a pie chart with exploded slices, a shadow, and redundant
    labels showing name, value, and percentage all at once — visually busy and
    harder to compare than a simple bar chart. The right chart uses two clean bars
    with a single value label each. The comparison is immediate. Pie charts with
    only two categories are a classic example of unnecessary complexity; a bar
    chart does the same job with less cognitive load, which is exactly the
    "don't overcomplicate things" principle the lecture teaches.
    """)
    return


# ============================================================
# CONCEPT 12 — Design Thinking Process
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Concept 12: Design Thinking

    The lecture closes with **Design Thinking**, a five-phase iterative process
    used by designers to solve complex problems creatively.

    | Phase | What you do |
    |---|---|
    | **Empathize** | Understand the user's problem from their perspective |
    | **Define** | Clarify the challenge clearly, without assumptions |
    | **Ideate** | Brainstorm freely — exhaust all ideas |
    | **Prototype** | Build simple test versions; fail fast and adjust |
    | **Test** | Evaluate the finished solution; gather new insights |

    Applied to data visualization, this means:
    - Empathize with what your audience actually needs to understand.
    - Define the single question your chart must answer.
    - Ideate multiple chart types or designs before committing.
    - Prototype a rough version and get feedback.
    - Test whether a fresh viewer draws the right conclusion.

    The process is non-linear — insights from the Test phase often loop back
    to Ideate or even Empathize.
    """)
    return


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches

    # Illustrate the Design Thinking loop as a simple diagram
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis('off')

    phases = ['Empathize', 'Define', 'Ideate', 'Prototype', 'Test']
    colors = ['#85c1e9', '#82e0aa', '#f9e79f', '#f0b27a', '#c39bd3']
    x_positions = [1, 2.8, 4.6, 6.4, 8.2]

    for i, (phase, color, xpos) in enumerate(zip(phases, colors, x_positions)):
        circle = plt.Circle((xpos, 2), 0.75, color=color, ec='grey', lw=1.5)
        ax.add_patch(circle)
        ax.text(xpos, 2, phase, ha='center', va='center', fontsize=8, fontweight='bold')
        if i < len(phases) - 1:
            ax.annotate('', xy=(x_positions[i+1] - 0.77, 2),
                        xytext=(xpos + 0.77, 2),
                        arrowprops=dict(arrowstyle='->', color='grey', lw=1.5))

    # Loop-back arrow
    ax.annotate('', xy=(x_positions[0], 1.22),
                xytext=(x_positions[-1], 1.22),
                arrowprops=dict(arrowstyle='<-', color='#c39bd3',
                                connectionstyle='arc3,rad=0.3', lw=1.5))
    ax.text(5, 0.6, 'Iterative — test insights loop back to earlier phases',
            ha='center', fontsize=8, color='grey', style='italic')

    ax.set_title('Design Thinking: A Non-Linear Iterative Process', fontsize=11)
    plt.tight_layout()
    plt.gca()
    return (ax, circle, color, colors, fig, i, mpatches,
            pd, phase, phases, x_positions, xpos)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **What this code shows:**
    The diagram visualizes the five Design Thinking phases as circles connected
    by arrows, with a loop-back arrow from Test back toward Empathize. Matplotlib's
    `annotate` with `arrowprops` draws the directional arrows, and `plt.Circle`
    draws the phase bubbles. The loop-back illustrates the lecture's point that
    Design Thinking is non-linear: new insights from testing often send you back
    to rethink the problem definition or generate new ideas.
    """)
    return


# ============================================================
# SUMMARY
# ============================================================
@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Summary of Concepts

    | # | Concept | Core Idea |
    |---|---|---|
    | 1 | What is Data Visualization | Graphical representation to reveal patterns faster than raw data |
    | 2 | Exploratory vs. Explanatory | Exploration finds the story; explanation communicates it |
    | 3 | Context: Who, What, How | Plan audience, message, and data format before drawing anything |
    | 4 | Altair + `mo.ui.altair_chart` | Build interactive, reactive charts inside Marimo |
    | 5 | Telling a Data Story | Relevant data + clear narrative + intentional visuals + call to action |
    | 6 | Clutter and Cognitive Load | Extra visual elements increase mental effort; remove them |
    | 7 | Visual Order, Alignment, White Space | Grid alignment and breathing room make layouts feel trustworthy |
    | 8 | Preattentive Attributes | Color, size, position guide attention before conscious thought |
    | 9 | Eliminate Distractions | If removing it changes nothing, remove it |
    | 10 | Text as a Design Element | Titles, axis labels, and annotations are non-negotiable |
    | 11 | Don't Overcomplicate Things | Simpler always wins when the information is the same |
    | 12 | Design Thinking | Empathize → Define → Ideate → Prototype → Test (iterative) |
    """)
    return


if __name__ == "__main__":
    app.run()
