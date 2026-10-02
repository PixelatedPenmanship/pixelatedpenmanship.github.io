# UI/UX Specification: "Ink & Silicon" (Refined Edition)
**System Name:** Pixelated Penmanship Design System  
**Version:** 2.1 (Deep-Dive & Defect Remediation)  
**Target:** MkDocs Material Customization (`docs/`, `overrides/`, `mkdocs.yml`)  

---

## 1. Aesthetic Vision & North Star

The core concept of **Pixelated Penmanship** is the dialogue between two tactile worlds:
1. **The Analog Craft:** Fountain pens, gold/steel nib geometries, capillary action, fountain pen ink shading, and archival paper textures.
2. **The Digital Architecture:** Systems programming, embedded security, hardware roots of trust, clean code, and minimal user interfaces.

### Core Aesthetic Principles
* **Tactile Minimalism:** No synthetic neon gradients or blurry SaaS glassmorphism. Surfaces evoke warm archival paper in daylight and a quiet obsidian terminal at night.
* **Editorial Authority:** Long-form reviews and roadmaps read like an artisanal print journal—crisp typography, ample breathing room, and intentional layout.
* **Pure Markdown Fidelity:** The design system must style **standard Markdown primitives** (headings, tables, lists, blockquotes, definition lists, images) beautifully, without forcing the author to insert raw HTML `<div>` boilerplate into their notes.
* **Geometric & Typographic Precision:** Zero clipped descenders, awkward line heights, or mismatched border-radii across pages.

---

## 2. Inconsistency & Defect Registry

A complete inventory of UI/UX defects identified during the deep-dive review:

| Defect ID | Component / Area | Defect Description | Root Cause | Target Fix |
| :--- | :--- | :--- | :--- | :--- |
| **DEF-01** | Navigation Tabs Bar | Descenders ('g' in Writing, 'g'/'y' in Technology, 'p' in Portfolio) are sliced off; active tab underline is jammed against text baseline. | In `extra.css`, `.md-tabs__link` has `padding: 0.75rem 1rem !important`. MkDocs Material sets `.md-tabs__item { height: 2.4rem }` and clips overflow. | Remove forced vertical padding; use flex alignment `height: 2.4rem; display: inline-flex; align-items: center; margin-top: 0 !important;` so descenders have full clearance. |
| **DEF-02** | Blog Dates | Post dates display invalid calendar days (e.g., "February 33, 2026", "March 89, 2025", "November 318, 2025"). | In `mkdocs.yml`, `post_date_format: MMMM D, YYYY` uses uppercase `D` (Day of Year 1–366 in Babel) instead of `d` (Day of Month 1–31). | Change `post_date_format` to `MMMM d, yyyy` in `mkdocs.yml`. |
| **DEF-03** | Hub Card Inconsistency | Cards on `/writing/` and `/tech/` (`.grid.cards`) have sharp 1.6px square corners and default Material borders, while blog post cards have 10px rounded borders. | `.grid.cards` was not styled in `extra.css`, leaving it with default Material styles. | Unify `.grid.cards > ul > li` with `.md-post--excerpt` styling (10px radius, hairline border, 2px hover lift). |
| **DEF-04** | Article Sidebar Card Glitch | In individual blog posts, the left metadata sidebar is wrapped in a card with padding, border, and hover lift. | In `extra.css`, `.md-post` was styled globally, but Material uses `<div class="md-sidebar__inner md-post">` for the article sidebar. | Scope card styling strictly to `.md-post--excerpt` and `article.md-post--excerpt`. |
| **DEF-05** | Hub Page Titles & Metadata | `/writing/` and `/tech/` have raw emojis in H1 (`# ✒️ Fountain Pens...`, `# 💻 Technology...`) and lack YAML frontmatter. | Missing YAML frontmatter causes browser tab titles and search indices to display raw emojis and inconsistent text. | Add clean YAML frontmatter (`title: Writing`, `title: Technology`) and use clean editorial H1 headings without emoji prefixes. |
| **DEF-06** | Specification Presentation | Raw HTML `<div class="pp-specs-card">` clutters pure markdown notes and was removed by the author. | Inability to style specs without writing raw HTML in markdown. | Style native Markdown tables (`.md-typeset table`) and definition lists (`.md-typeset dl`) to automatically look like bespoke specs cards. |
| **DEF-07** | Post Content Asymmetry | `.md-content__inner` had `margin-left: auto; margin-right: auto; max-width: 80ch;`, which causes asymmetric positioning on pages with a table of contents sidebar. | Over-constraining `.md-content__inner` inside a multi-column flex layout. | Set `max-width: 80ch` on the content wrapper without overriding flex margins on multi-column layouts. |
| **DEF-08** | Image Presentation in Posts | Photos in reviews render edge-to-edge with sharp unstyled borders. | No custom styling for `.md-typeset img`. | Add subtle `border-radius: 8px`, hairline border `1px solid var(--pp-border-subtle)`, and soft elevation to all review images. |
| **DEF-09** | Table of Contents Styling | Secondary TOC links in dark mode lack contrast and clear active indicator. | Default Material styles for `.md-nav--secondary`. | Add custom styling for `.md-nav--secondary` with `--pp-accent-nib` active indicator and comfortable line-height. |
| **DEF-10** | Search Output & Header Parity | Search results dropdown in light mode uses generic styles that clash with the warm paper canvas. | Search dropdown variables were unmapped. | Style `.md-search__output` and `.md-search-result__item` to inherit `--pp-surface-card` and `--pp-border-subtle`. |
| **DEF-11** | Subpage Image Resolution | Avatar image broken on `/about/` displaying vertical alt text string `A\nr\na\nv...`. | Absolute/root-relative asset assumption with raw `<img src="img/avatar.jpg">` 404s when page is served at `/about/`. | Use native Markdown image syntax `![Aravind A](img/avatar.jpg){: .pp-profile-avatar }` which MkDocs automatically adjusts to `../img/avatar.jpg`. |
| **DEF-12** | Profile Raw HTML Code Block Glitch | Profile text rendered inside a raw gray `<pre><code>` code box instead of styled heading and paragraph. | 4-space indentation inside `<div markdown="1">` triggers Python-Markdown's indented code block parser rule. | Remove 4-space indentation and write content as flush markdown or unindented HTML tags. |

---

## 3. Detailed Component Specifications

### 3.1 Navigation & Header Specification (Fixing DEF-01)
The primary navigation bar must be completely free of clipping:

```css
/* Container & Bar */
.md-tabs {
  background-color: var(--pp-tabs-bg) !important;
  border-bottom: 1px solid var(--pp-header-border);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  line-height: normal;
}

.md-tabs__list {
  display: flex;
  align-items: center;
  overflow-x: auto;
  overflow-y: hidden;
  scrollbar-width: none;
}

.md-tabs__item {
  height: 2.75rem; /* Expanded from 2.4rem to give generous vertical breathing room */
  padding: 0 0.5rem;
  display: flex;
  align-items: center;
}

.md-tabs__link {
  font-family: var(--pp-font-sans);
  font-weight: 500;
  font-size: 0.9rem;
  color: var(--pp-ink-secondary) !important;
  opacity: 0.85;
  height: 100%;
  display: inline-flex;
  align-items: center;
  padding: 0 0.75rem !important;
  margin-top: 0 !important; /* Overrides native Material .8rem margin */
  position: relative;
  transition: color 0.2s ease, opacity 0.2s ease;
}

.md-tabs__link:hover {
  color: var(--pp-ink-primary) !important;
  opacity: 1;
}

/* Active Tab Indicator */
.md-tabs__item--active .md-tabs__link {
  color: var(--pp-ink-primary) !important;
  font-weight: 700;
  opacity: 1;
}

.md-tabs__item--active .md-tabs__link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0.5rem;
  right: 0.5rem;
  height: 2.5px;
  background-color: var(--pp-accent-nib);
  border-radius: 9999px;
}
```

### 3.2 Date Formatting Specification (Fixing DEF-02)
In `mkdocs.yml`:
```yaml
plugins:
  - blog:
      post_date_format: MMMM d, yyyy  # Lowercase 'd' for day of month (1-31), lowercase 'yyyy' for year
      post_readtime: true
      post_readtime_words_per_minute: 200
```
*Expected Output:*  
`March 30, 2025` (instead of `March 89, 2025`)  
`February 2, 2026` (instead of `February 33, 2026`)  
`November 14, 2025` (instead of `November 318, 2025`)

### 3.3 Universal Card Design Specification (Fixing DEF-03 & DEF-04)
Unify all cards across the blog list (`.md-post--excerpt`), hub grids (`.grid.cards`), and portfolio cards:

```css
/* Scoped Blog Post Excerpt Cards */
.md-post--excerpt {
  padding: 1.75rem 2rem !important;
  margin-bottom: 1.75rem !important;
  background: var(--pp-surface-card) !important;
  border-radius: 10px !important;
  border: 1px solid var(--pp-border-subtle) !important;
  box-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.03);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.md-post--excerpt:hover {
  transform: translateY(-3px);
  border-color: var(--pp-border-strong) !important;
  box-shadow: 0 10px 24px -4px rgba(0, 0, 0, 0.08);
}

/* Hub Grid Cards (.grid.cards) */
.md-typeset .grid.cards > ul > li,
.md-typeset .grid.cards > ol > li,
.md-typeset .grid > .card {
  background: var(--pp-surface-card) !important;
  border: 1px solid var(--pp-border-subtle) !important;
  border-radius: 10px !important;
  padding: 1.5rem !important;
  box-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.03);
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.md-typeset .grid.cards > ul > li:hover,
.md-typeset .grid.cards > ol > li:hover,
.md-typeset .grid > .card:hover {
  transform: translateY(-3px);
  border-color: var(--pp-border-strong) !important;
  box-shadow: 0 10px 24px -4px rgba(0, 0, 0, 0.08);
}

/* Ensure Article Sidebar (which has .md-post) remains clean and borderless */
.md-sidebar--post .md-sidebar__inner.md-post {
  padding: 0 !important;
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  transform: none !important;
}
```

### 3.4 Pure Markdown Specification Sheet (Fixing DEF-06)
Instead of requiring raw HTML `<div>` blocks, style standard Markdown tables and lists as elegant specification sheets:

```css
/* Standard Markdown Tables Styled as Elegant Specs */
.md-typeset table:not([class]) {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  border: 1px solid var(--pp-border-subtle);
  border-radius: 8px;
  overflow: hidden;
  margin: 1.5rem 0 2rem 0;
  background: var(--pp-surface-card);
  font-size: 0.95rem;
}

.md-typeset table:not([class]) th {
  background: var(--pp-surface-subtle);
  color: var(--pp-accent-nib);
  font-family: var(--pp-font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--pp-border-subtle);
}

.md-typeset table:not([class]) td {
  padding: 0.75rem 1rem;
  border-bottom: 1px solid var(--pp-border-subtle);
  color: var(--pp-ink-secondary);
}

.md-typeset table:not([class]) tr:last-child td {
  border-bottom: none;
}

.md-typeset table:not([class]) td:first-child {
  font-weight: 600;
  color: var(--pp-ink-primary);
}
```

### 3.5 Editorial Gallery & Post Image Styling (Fixing DEF-08)
```css
.md-typeset img {
  border-radius: 8px;
  border: 1px solid var(--pp-border-subtle);
  box-shadow: 0 4px 16px -4px rgba(0, 0, 0, 0.06);
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.md-typeset img:hover {
  box-shadow: 0 8px 24px -4px rgba(0, 0, 0, 0.12);
}
```

### 3.6 Hub Pages Frontmatter & Titles (Fixing DEF-05)
* **`docs/writing/index.md`:**
  ```markdown
  ---
  title: Writing Instruments
  description: In-depth evaluations of fountain pens, bulkfillers, ebonite craftsmanship, nib grinding, and ink performance.
  ---

  # Writing Instruments & Craftsmanship
  ```
* **`docs/tech/index.md`:**
  ```markdown
  ---
  title: Technology
  description: Systems engineering, embedded Linux security roadmaps, operating system internals, and developer tooling.
  ---

  # Systems Engineering & Technology
  ```

---

## 4. Verification Benchmarks

1. **Visual Parity:**
   * Tabs bar has zero descender clipping on letters 'g', 'y', 'p'.
   * Active tab underline has rounded pill ends and sits comfortably below text.
   * All post cards, hub cards, and project cards share identical 10px radii and hover elevations.
   * Article sidebar inside individual posts has no card borders or hover movement.
2. **Build Integrity:**
   * `mkdocs build --strict --clean` completes with 0 warnings and 0 errors.
   * Dates in blog archive and individual posts display correct month, day-of-month, and year (e.g., `March 30, 2025`).
3. **Accessibility:**
   * Contrast ratios meet WCAG 2.1 AA (minimum 4.5:1 for body text, 3:1 for UI elements).
