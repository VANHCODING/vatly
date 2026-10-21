# -*- coding: utf-8 -*-
"""
Builds vatly.html with Chapters 0, 1, 2, 3, 4, 5 and upcoming outlines 6-16
"""
import json
import os

from data_ch0 import CH0
from data_ch1 import CH1
from data_ch2 import CH2
from data_ch3 import CH3
from data_ch4 import CH4
from data_ch5 import CH5
from data_ch6_8 import CH6, CH7, CH8
from data_ch9_10 import CH9, CH10
from data_ch11_14 import CH11, CH12, CH13, CH14
from data_ch15_16 import CH15, CH16

all_chapters = [
    CH0, CH1, CH2, CH3, CH4, CH5,
    CH6, CH7, CH8,
    CH9, CH10,
    CH11, CH12, CH13, CH14,
    CH15, CH16
]

# Ensure json serialization is safe
chapters_json = json.dumps(all_chapters, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vật lý đại cương 1 — 16 Chương Toàn diện (Lương Duyên Bình)</title>
  
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <!-- KaTeX CSS & JS via CDN -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css">
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>
  <script defer src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js" onload="initKaTeX()"></script>

  <style>
    /* =========================================================
       1. CSS SYSTEM & VARIABLES
       ========================================================= */
    :root {{
      --font-main: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;

      /* Dark Theme Default */
      --bg-base: #090d16;
      --bg-surface: #101626;
      --bg-card: #151d32;
      --bg-card-hover: #1c2642;
      --bg-subtle: #1e293b;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-focus: #6366f1;

      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;

      --primary: #6366f1;
      --primary-light: #818cf8;
      --primary-glow: rgba(99, 102, 241, 0.2);

      --success: #10b981;
      --success-glow: rgba(16, 185, 129, 0.2);
      --danger: #f43f5e;
      --danger-glow: rgba(244, 63, 94, 0.2);
      --warning: #f59e0b;
      --warning-glow: rgba(245, 158, 11, 0.2);
      --info: #0284c7;

      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;

      --header-h: 68px;
      --sidebar-w: 320px;
      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.45);
    }}

    [data-theme="light"] {{
      --bg-base: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #f1f5f9;
      --bg-card-hover: #e2e8f0;
      --bg-subtle: #f8fafc;
      --border-subtle: rgba(0, 0, 0, 0.08);
      --border-focus: #4f46e5;

      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;

      --primary: #4f46e5;
      --primary-light: #6366f1;
      --primary-glow: rgba(79, 70, 229, 0.15);

      --success: #059669;
      --success-glow: rgba(5, 150, 105, 0.15);
      --danger: #e11d48;
      --danger-glow: rgba(225, 29, 72, 0.15);
      --warning: #d97706;
      --warning-glow: rgba(217, 119, 6, 0.15);
      --info: #0284c7;

      --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-main);
      background-color: var(--bg-base);
      color: var(--text-main);
      line-height: 1.65;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
      transition: background-color 0.25s ease, color 0.25s ease;
    }}

    /* =========================================================
       2. TOP NAVBAR
       ========================================================= */
    header.topbar {{
      position: sticky;
      top: 0;
      z-index: 50;
      height: var(--header-h);
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      backdrop-filter: blur(12px);
    }}

    .brand-wrap {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .btn-menu-toggle {{
      display: none;
      background: none;
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      border-radius: var(--radius-sm);
      padding: 0.45rem 0.65rem;
      cursor: pointer;
      font-size: 1.1rem;
    }}

    .logo-badge {{
      width: 38px;
      height: 38px;
      border-radius: 10px;
      background: linear-gradient(135deg, #6366f1, #06b6d4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: #fff;
      font-weight: 800;
      font-size: 1.15rem;
      box-shadow: 0 4px 12px var(--primary-glow);
    }}

    .brand-text h1 {{
      font-size: 1.05rem;
      font-weight: 700;
      letter-spacing: -0.01em;
      line-height: 1.2;
    }}

    .brand-text p {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .top-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .search-box {{
      position: relative;
      width: 250px;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.45rem 0.75rem 0.45rem 2rem;
      border-radius: 20px;
      font-size: 0.85rem;
      font-family: var(--font-main);
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px var(--primary-glow);
    }}

    .search-icon {{
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.85rem;
      pointer-events: none;
    }}

    .btn-nav {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.2s;
    }}

    .btn-nav:hover {{
      background: var(--bg-card-hover);
      border-color: var(--primary);
    }}

    .btn-nav.active {{
      background: var(--primary);
      color: #fff;
      border-color: var(--primary);
    }}

    .theme-btn {{
      padding: 0.45rem 0.65rem;
    }}

    /* =========================================================
       3. APP LAYOUT & SIDEBAR
       ========================================================= */
    .app-layout {{
      display: flex;
      flex: 1;
      height: calc(100vh - var(--header-h));
      overflow: hidden;
    }}

    aside.sidebar {{
      width: var(--sidebar-w);
      background-color: var(--bg-surface);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      flex-shrink: 0;
      transition: transform 0.25s ease;
    }}

    .sidebar-header {{
      padding: 1.1rem 1.25rem 0.75rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .sidebar-header h2 {{
      font-size: 0.85rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--text-dim);
      margin-bottom: 0.35rem;
    }}

    .global-stats {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-card);
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.8rem;
    }}

    .global-stats .score-num {{
      font-weight: 700;
      color: var(--primary-light);
    }}

    .chapter-nav-list {{
      list-style: none;
      padding: 0.75rem 0.5rem 2rem;
    }}

    .part-title-item {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      padding: 0.85rem 0.75rem 0.35rem;
    }}

    .ch-nav-item {{
      margin-bottom: 0.25rem;
    }}

    .ch-nav-btn {{
      width: 100%;
      text-align: left;
      background: none;
      border: 1px solid transparent;
      color: var(--text-main);
      padding: 0.65rem 0.75rem;
      border-radius: var(--radius-sm);
      font-family: var(--font-main);
      font-size: 0.85rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.15s ease;
    }}

    .ch-nav-btn:hover {{
      background: var(--bg-card);
      color: var(--text-main);
    }}

    .ch-nav-btn.active {{
      background: var(--primary-glow);
      border-color: var(--primary);
      color: var(--primary-light);
      font-weight: 700;
    }}

    .ch-badge-status {{
      font-size: 0.68rem;
      font-weight: 600;
      padding: 0.15rem 0.45rem;
      border-radius: 12px;
    }}

    .badge-ready {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--success);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .badge-upcoming {{
      background: rgba(148, 163, 184, 0.12);
      color: var(--text-dim);
    }}

    /* =========================================================
       4. MAIN CONTENT AREA
       ========================================================= */
    main.content-area {{
      flex: 1;
      overflow-y: auto;
      padding: 1.75rem 2.5rem 5rem;
      scroll-behavior: smooth;
    }}

    .container-reading {{
      max-width: 920px;
      margin: 0 auto;
    }}

    /* Chapter Header */
    .ch-header-banner {{
      margin-bottom: 2rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .ch-part-label {{
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--primary-light);
      margin-bottom: 0.4rem;
    }}

    .ch-title-main {{
      font-size: 1.85rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.25;
      margin-bottom: 0.75rem;
    }}

    .ch-summary-text {{
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Section Blocks */
    .section-block {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shadow-sm);
    }}

    .section-header-title {{
      font-size: 1.15rem;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      margin-bottom: 1.1rem;
      padding-bottom: 0.6rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    /* 1. Bản chất grid */
    .nature-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1rem;
    }}

    .nature-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1rem;
    }}

    .nature-card-title {{
      font-size: 0.85rem;
      font-weight: 700;
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}

    .nature-card-title.why {{ color: #38bdf8; }}
    .nature-card-title.meaning {{ color: #a78bfa; }}
    .nature-card-title.conditions {{ color: #34d399; }}
    .nature-card-title.limits {{ color: #fb7185; }}

    .nature-card-body {{
      font-size: 0.875rem;
      color: var(--text-muted);
      line-height: 1.55;
    }}

    /* 2. Formulas and step proofs */
    .formula-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }}

    .formula-name {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.5rem;
    }}

    .formula-display-box {{
      background: var(--bg-subtle);
      border-left: 4px solid var(--primary);
      padding: 0.85rem 1rem;
      border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
      font-size: 1.05rem;
      margin-bottom: 0.75rem;
      overflow-x: auto;
    }}

    .formula-meaning-text {{
      font-size: 0.875rem;
      color: var(--text-muted);
      margin-bottom: 0.85rem;
      line-height: 1.55;
    }}

    .proof-toggle {{
      background: none;
      border: none;
      color: var(--primary-light);
      font-size: 0.825rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      margin-bottom: 0.5rem;
    }}

    .proof-steps-wrap {{
      background: var(--bg-base);
      border: 1px dashed var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.75rem;
      font-size: 0.85rem;
      margin-top: 0.5rem;
    }}

    .proof-step-row {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      padding: 0.4rem 0;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .proof-step-row:last-child {{
      border-bottom: none;
    }}

    .step-math {{
      flex: 1.2;
      overflow-x: auto;
    }}

    .step-reason {{
      flex: 1.5;
      color: var(--text-muted);
      font-size: 0.8rem;
    }}

    .svg-diagram {{
      width: 100%;
      max-width: 480px;
      margin: 1rem auto;
      display: block;
      background: var(--bg-card);
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
      padding: 0.5rem;
    }}

    /* 3. Phân dạng bài tập */
    .type-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.15rem;
      margin-bottom: 1rem;
    }}

    .type-name {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--primary-light);
      margin-bottom: 0.6rem;
    }}

    .algorithm-steps {{
      list-style: none;
      counter-reset: algo-counter;
    }}

    .algorithm-steps li {{
      counter-increment: algo-counter;
      margin-bottom: 0.45rem;
      font-size: 0.875rem;
      color: var(--text-muted);
      display: flex;
      align-items: flex-start;
      gap: 0.6rem;
    }}

    .algorithm-steps li::before {{
      content: counter(algo-counter);
      background: var(--primary-glow);
      color: var(--primary-light);
      font-weight: 700;
      font-size: 0.75rem;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
      margin-top: 1px;
    }}

    /* 4. Ví dụ mẫu */
    .example-card {{
      background: var(--bg-card);
      border-left: 4px solid var(--warning);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1.25rem;
      margin-bottom: 1.25rem;
    }}

    .example-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--warning);
      margin-bottom: 0.5rem;
    }}

    .example-body {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    .example-analysis {{
      background: var(--bg-subtle);
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      margin: 0.65rem 0;
      font-size: 0.84rem;
      border: 1px solid var(--border-subtle);
    }}

    /* 5. Lỗi thường gặp */
    .pitfall-card {{
      background: var(--bg-card);
      border-left: 4px solid var(--danger);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 1rem 1.25rem;
      margin-bottom: 0.85rem;
    }}

    .pitfall-error {{
      font-weight: 700;
      color: var(--danger);
      font-size: 0.88rem;
      margin-bottom: 0.25rem;
    }}

    .pitfall-fix {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 0.35rem;
    }}

    .pitfall-tip {{
      font-size: 0.82rem;
      color: var(--text-dim);
      font-style: italic;
    }}

    /* 6. Bài tập thực hành 10 bài */
    .exercise-item {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
      transition: border-color 0.2s;
    }}

    .exercise-item.solved-correct {{
      border-color: var(--success);
      box-shadow: 0 0 12px var(--success-glow);
    }}

    .exercise-item.solved-wrong {{
      border-color: var(--danger);
      box-shadow: 0 0 12px var(--danger-glow);
    }}

    .exercise-topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.65rem;
    }}

    .ex-index-wrap {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .ex-badge {{
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.15rem 0.5rem;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .badge-easy {{ background: rgba(16, 185, 129, 0.15); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-mid {{ background: rgba(245, 158, 11, 0.15); color: var(--warning); border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-hard {{ background: rgba(244, 63, 94, 0.15); color: var(--danger); border: 1px solid rgba(244, 63, 94, 0.3); }}

    .exercise-question {{
      font-size: 0.92rem;
      color: var(--text-main);
      margin-bottom: 1rem;
      line-height: 1.6;
    }}

    .exercise-interactive-bar {{
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-bottom: 0.85rem;
    }}

    .input-answer {{
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      font-family: var(--font-mono);
      font-size: 0.95rem;
      width: 150px;
      outline: none;
    }}

    .input-answer:focus {{
      border-color: var(--border-focus);
      box-shadow: 0 0 0 2px var(--primary-glow);
    }}

    .ex-unit-label {{
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
    }}

    .btn-action {{
      padding: 0.5rem 0.9rem;
      border-radius: var(--radius-sm);
      font-size: 0.84rem;
      font-weight: 600;
      font-family: var(--font-main);
      cursor: pointer;
      border: 1px solid transparent;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: all 0.15s;
    }}

    .btn-check {{
      background: var(--primary);
      color: #fff;
    }}
    .btn-check:hover {{ background: var(--primary-light); }}

    .btn-secondary {{
      background: var(--bg-subtle);
      color: var(--text-muted);
      border-color: var(--border-subtle);
    }}
    .btn-secondary:hover {{
      background: var(--bg-card-hover);
      color: var(--text-main);
    }}

    .feedback-banner {{
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      margin-bottom: 0.75rem;
      display: none;
    }}

    .feedback-banner.show {{ display: block; }}
    .feedback-banner.success {{ background: rgba(16, 185, 129, 0.15); color: var(--success); border: 1px solid rgba(16, 185, 129, 0.3); }}
    .feedback-banner.error {{ background: rgba(244, 63, 94, 0.15); color: var(--danger); border: 1px solid rgba(244, 63, 94, 0.3); }}

    .hints-content, .solution-content {{
      background: var(--bg-subtle);
      border: 1px dashed var(--border-subtle);
      border-radius: var(--radius-sm);
      padding: 0.85rem;
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.6;
      margin-top: 0.5rem;
      display: none;
    }}

    .hints-content.show, .solution-content.show {{
      display: block;
    }}

    /* Thang điểm cuối chương */
    .scorecard-box {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(6, 182, 212, 0.1));
      border: 1px solid var(--primary);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      text-align: center;
      margin-top: 2rem;
    }}

    .scorecard-val {{
      font-size: 2.25rem;
      font-weight: 800;
      color: var(--primary-light);
      margin-bottom: 0.25rem;
    }}

    .scorecard-rating {{
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 0.75rem;
    }}

    .scorecard-msg {{
      font-size: 0.875rem;
      color: var(--text-muted);
      max-width: 520px;
      margin: 0 auto 1.25rem;
    }}

    /* =========================================================
       5. PRINTABLE FORMULA SHEET VIEW
       ========================================================= */
    #formulaSheetView {{
      display: none;
    }}

    .print-sheet-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.75rem;
      padding-bottom: 1rem;
      border-bottom: 1px solid var(--border-subtle);
    }}

    .print-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 1.25rem;
    }}

    /* =========================================================
       6. REVIEW / PRACTICE MODE VIEW
       ========================================================= */
    #reviewModeView {{
      display: none;
    }}

    .review-header-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
    }}

    /* =========================================================
       7. RESPONSIVE & MOBILE
       ========================================================= */
    @media (max-width: 900px) {{
      aside.sidebar {{
        position: fixed;
        left: 0;
        top: var(--header-h);
        bottom: 0;
        z-index: 40;
        transform: translateX(-100%);
        box-shadow: var(--shadow-md);
      }}

      aside.sidebar.mobile-open {{
        transform: translateX(0);
      }}

      .btn-menu-toggle {{
        display: block;
      }}

      main.content-area {{
        padding: 1.25rem 1rem 4rem;
      }}

      .search-box {{
        width: 160px;
      }}
    }}

    /* =========================================================
       8. PRINT STYLES
       ========================================================= */
    @media print {{
      header.topbar, aside.sidebar, .btn-action, .exercise-interactive-bar,
      .feedback-banner, .btn-menu-toggle, .top-actions {{
        display: none !important;
      }}

      body {{
        background: #fff !important;
        color: #000 !important;
      }}

      .app-layout {{
        height: auto !important;
        overflow: visible !important;
      }}

      main.content-area {{
        padding: 0 !important;
        overflow: visible !important;
      }}

      .section-block, .formula-card, .type-card {{
        background: #fff !important;
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        page-break-inside: avoid;
      }}

      #formulaSheetView {{
        display: block !important;
      }}
      #chapterMainView, #reviewModeView {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- TOPBAR -->
  <header class="topbar">
    <div class="brand-wrap">
      <button class="btn-menu-toggle" id="btnToggleSidebar" aria-label="Menu">☰</button>
      <div class="logo-badge">VL</div>
      <div class="brand-text">
        <h1>Vật lý đại cương 1</h1>
        <p>Cơ – Dao động & Sóng – Nhiệt học (Giáo trình Lương Duyên Bình)</p>
      </div>
    </div>

    <div class="top-actions">
      <!-- Search -->
      <div class="search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm công thức, chương..." autocomplete="off">
      </div>

      <!-- View Switchers -->
      <button class="btn-nav active" id="btnViewLectures" title="Bài giảng & Bài tập">📖 Bài giảng</button>
      <button class="btn-nav" id="btnViewFormulas" title="Bảng công thức in được">📑 Bảng công thức</button>
      <button class="btn-nav" id="btnViewReview" title="Ôn tập ngẫu nhiên">🎲 Ôn tập</button>

      <!-- Theme Switcher -->
      <button class="btn-nav theme-btn" id="btnToggleTheme" title="Đổi giao diện sáng/tối">🌙</button>
    </div>
  </header>

  <!-- APP LAYOUT -->
  <div class="app-layout">

    <!-- SIDEBAR -->
    <aside class="sidebar" id="sidebarNav">
      <div class="sidebar-header">
        <h2>Mục lục bài giảng</h2>
        <div class="global-stats">
          <span>Tiến độ toàn khóa:</span>
          <span class="score-num" id="globalProgressText">0/60 bài (0%)</span>
        </div>
      </div>

      <ul class="chapter-nav-list" id="chapterNavList">
        <!-- Chapter items injected by JavaScript -->
      </ul>
    </aside>

    <!-- MAIN CONTENT -->
    <main class="content-area" id="mainContent">

      <!-- CHAPTER VIEW -->
      <div id="chapterMainView" class="container-reading">
        <!-- Rendered dynamically by renderChapter(id) -->
      </div>

      <!-- PRINTABLE FORMULA SHEET VIEW -->
      <div id="formulaSheetView" class="container-reading">
        <div class="print-sheet-header">
          <div>
            <h2 style="font-size: 1.6rem; font-weight:800;">Bảng tra cứu công thức Vật lý đại cương 1</h2>
            <p style="color:var(--text-muted); font-size:0.9rem;">Toàn bộ công thức trọng tâm — Chuẩn mực tra cứu & In ấn ôn thi</p>
          </div>
          <button class="btn-action btn-check" onclick="window.print()">🖨️ In bảng công thức (PDF / Máy in)</button>
        </div>
        <div class="print-grid" id="printableFormulasContainer">
          <!-- Filled by JS -->
        </div>
      </div>

      <!-- RANDOM PRACTICE / REVIEW VIEW -->
      <div id="reviewModeView" class="container-reading">
        <div class="review-header-card">
          <div>
            <h2 style="font-size: 1.3rem; font-weight:700;">Chế độ ôn tập ngẫu nhiên</h2>
            <p style="color:var(--text-muted); font-size:0.85rem;">Trộn ngẫu nhiên câu hỏi từ các chương đã hoàn thành để rèn phản xạ</p>
          </div>
          <button class="btn-action btn-secondary" id="btnNextReviewQuestion">Đổi câu hỏi tiếp theo ❯</button>
        </div>
        <div id="reviewQuestionContainer">
          <!-- Single exercise injected here -->
        </div>
      </div>

    </main>
  </div>

  <!-- SCRIPT DATA & CORE LOGIC -->
  <script>
    /* =========================================================
       DATA: CH (Array of 17 Chapters: 0 to 16)
       ========================================================= */
    const CH = {chapters_json};

    /* =========================================================
       LOCAL STORAGE & STATE MANAGEMENT (with try-catch)
       ========================================================= */
    const STORAGE_KEY = "vatly_v1_progress";
    let appState = {{
      activeChapterId: 0,
      activeView: "lectures", // 'lectures' | 'formulas' | 'review'
      theme: "dark",
      exercises: {{}} // {{ [exId]: {{ userVal: string, isCorrect: boolean, solvedAt: number }} }}
    }};

    function loadState() {{
      try {{
        const raw = localStorage.getItem(STORAGE_KEY);
        if (raw) {{
          const parsed = JSON.parse(raw);
          if (parsed && typeof parsed === "object") {{
            appState = {{ ...appState, ...parsed }};
          }}
        }}
      }} catch (err) {{
        console.warn("localStorage read failed:", err);
      }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem(STORAGE_KEY, JSON.stringify(appState));
      }} catch (err) {{
        console.warn("localStorage write failed:", err);
      }}
    }}

    /* =========================================================
       KATEX AUTO-RENDER HELPER
       ========================================================= */
    function initKaTeX() {{
      renderAllMath();
    }}

    function renderAllMath() {{
      if (typeof renderMathInElement === "function") {{
        try {{
          renderMathInElement(document.body, {{
            delimiters: [
              {{ left: "$$", right: "$$", display: true }},
              {{ left: "$", right: "$", display: false }},
              {{ left: "\\\\[", right: "\\\\]", display: true }},
              {{ left: "\\\\(", right: "\\\\)", display: false }}
            ],
            throwOnError: false
          }});
        }} catch (e) {{
          console.error("KaTeX render error:", e);
        }}
      }}
    }}

    /* =========================================================
       THEME MANAGEMENT
       ========================================================= */
    function applyTheme(theme) {{
      document.documentElement.setAttribute("data-theme", theme);
      appState.theme = theme;
      saveState();
      const btn = document.getElementById("btnToggleTheme");
      if (btn) btn.textContent = (theme === "dark") ? "🌙" : "☀️";
    }}

    /* =========================================================
       NAVIGATION & SIDEBAR
       ========================================================= */
    function renderSidebar() {{
      const listEl = document.getElementById("chapterNavList");
      if (!listEl) return;
      listEl.innerHTML = "";

      let currentPart = "";

      CH.forEach((ch) => {{
        if (ch.part !== currentPart) {{
          currentPart = ch.part;
          const partLi = document.createElement("li");
          partLi.className = "part-title-item";
          partLi.textContent = currentPart;
          listEl.appendChild(partLi);
        }}

        const li = document.createElement("li");
        li.className = "ch-nav-item";

        // Calculate chapter stats
        const totalEx = (ch.exercises || []).length;
        let correctCount = 0;
        (ch.exercises || []).forEach(ex => {{
          if (appState.exercises[ex.id]?.isCorrect) correctCount++;
        }});

        const isActive = (ch.id === appState.activeChapterId);
        const badgeClass = (ch.status === "ready") ? "badge-ready" : "badge-upcoming";
        const badgeText = (ch.status === "ready")
          ? (totalEx > 0 ? `${{correctCount}}/${{totalEx}} bài` : "Sẵn sàng")
          : "Sắp tới (Lượt 3-5)";

        li.innerHTML = `
          <button class="ch-nav-btn ${{isActive ? 'active' : ''}}" onclick="selectChapter(${{ch.id}})">
            <span><strong>${{ch.num}}.</strong> ${{ch.title}}</span>
            <span class="ch-badge-status ${{badgeClass}}">${{badgeText}}</span>
          </button>
        `;
        listEl.appendChild(li);
      }});

      updateGlobalStats();
    }}

    function updateGlobalStats() {{
      let totalEx = 0;
      let solvedEx = 0;
      CH.forEach(ch => {{
        if (ch.exercises) {{
          totalEx += ch.exercises.length;
          ch.exercises.forEach(ex => {{
            if (appState.exercises[ex.id]?.isCorrect) solvedEx++;
          }});
        }}
      }});
      const pct = totalEx > 0 ? Math.round((solvedEx / totalEx) * 100) : 0;
      const el = document.getElementById("globalProgressText");
      if (el) el.textContent = `${{solvedEx}}/${{totalEx}} bài (${{pct}}%)`;
    }}

    function selectChapter(chId) {{
      appState.activeChapterId = chId;
      saveState();
      switchView("lectures");
      renderSidebar();
      renderCurrentChapter();
      document.getElementById("sidebarNav")?.classList.remove("mobile-open");
    }}

    /* =========================================================
       CHAPTER RENDERING (Full 6 mandatory sections)
       ========================================================= */
    function renderCurrentChapter() {{
      const container = document.getElementById("chapterMainView");
      if (!container) return;

      const ch = CH.find(c => c.id === appState.activeChapterId) || CH[0];

      if (ch.status === "upcoming") {{
        container.innerHTML = `
          <div class="ch-header-banner">
            <span class="ch-part-label">${{ch.part}}</span>
            <h1 class="ch-title-main">Chương ${{ch.num}}: ${{ch.title}}</h1>
            <p class="ch-summary-text">${{ch.summary}}</p>
          </div>

          <div class="section-block" style="text-align:center; padding: 3rem 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">⏳</div>
            <h3 style="font-size: 1.35rem; margin-bottom: 0.6rem; font-weight:700;">Chương ${{ch.num}} sắp ra mắt trong lượt tiếp theo!</h3>
            <p style="color:var(--text-muted); max-width:600px; margin: 0 auto 1.5rem; font-size:0.95rem;">
              Theo lộ trình thực hiện lần lượt 2–3 chương mỗi lượt để đảm bảo chiều sâu giảng dạy, bài tập tính toán kiểm tra kĩ lưỡng. Hiện tại <strong>Chương 0, 1, 2, 3, 4, 5</strong> đã hoàn thiện đầy đủ 60 bài tập thực hành.
            </p>
            <div style="display:flex; justify-content:center; gap:0.75rem; flex-wrap:wrap;">
              <button class="btn-action btn-check" onclick="selectChapter(3)">Đến Chương 3 (Công - Năng lượng)</button>
              <button class="btn-action btn-secondary" onclick="selectChapter(4)">Chương 4 (Hệ chất điểm)</button>
              <button class="btn-action btn-secondary" onclick="selectChapter(5)">Chương 5 (Vật rắn)</button>
            </div>
          </div>
        `;
        renderAllMath();
        return;
      }}

      // 1. Bản chất
      const natureHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>📌</span> 1. Bản chất vật lý</div>
          <div class="nature-grid">
            <div class="nature-card">
              <div class="nature-card-title why"><span>❓</span> Vì sao đại lượng tồn tại?</div>
              <div class="nature-card-body">${{ch.nature.why}}</div>
            </div>
            <div class="nature-card">
              <div class="nature-card-title meaning"><span>💡</span> Ý nghĩa vật lý</div>
              <div class="nature-card-body">${{ch.nature.meaning}}</div>
            </div>
            <div class="nature-card">
              <div class="nature-card-title conditions"><span>⚙️</span> Điều kiện áp dụng</div>
              <div class="nature-card-body">${{ch.nature.conditions}}</div>
            </div>
            <div class="nature-card">
              <div class="nature-card-title limits"><span>⚠️</span> Giới hạn lý thuyết</div>
              <div class="nature-card-body">${{ch.nature.limits}}</div>
            </div>
          </div>
        </div>
      `;

      // 2. Công thức & Chứng minh từng bước
      let formulasHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>📐</span> 2. Công thức & Chứng minh từng bước (Không viết 'dễ thấy')</div>
      `;
      (ch.formulas || []).forEach((f, idx) => {{
        let proofsRows = "";
        (f.proof || []).forEach(p => {{
          proofsRows += `
            <div class="proof-step-row">
              <div class="step-math">$${{p.step}}$</div>
              <div class="step-reason"><strong>Lý do:</strong> ${{p.reason}}</div>
            </div>
          `;
        }});

        formulasHtml += `
          <div class="formula-card">
            <div class="formula-name"><strong>2.${{idx + 1}}</strong> ${{f.name}}</div>
            <div class="formula-display-box">$$${{f.latex}}$$</div>
            <div class="formula-meaning-text"><strong>Ý nghĩa:</strong> ${{f.meaning}}</div>
            ${{f.svg ? f.svg : ''}}
            <button class="proof-toggle" onclick="toggleProof('proof_${{ch.id}}_${{idx}}')">
              <span>🔍 Xem chứng minh từng bước</span>
            </button>
            <div class="proof-steps-wrap" id="proof_${{ch.id}}_${{idx}}" style="display:none;">
              ${{proofsRows}}
            </div>
          </div>
        `;
      }});
      formulasHtml += `</div>`;

      // 3. Phân dạng bài tập
      let typesHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>🧭</span> 3. Phân dạng bài tập & Thuật toán giải chuẩn mực</div>
      `;
      (ch.types || []).forEach((t, idx) => {{
        let algoLi = "";
        (t.algorithm || []).forEach(step => {{
          algoLi += `<li>${{step}}</li>`;
        }});
        typesHtml += `
          <div class="type-card">
            <div class="type-name">${{t.name}}</div>
            <ul class="algorithm-steps">${{algoLi}}</ul>
          </div>
        `;
      }});
      typesHtml += `</div>`;

      // 4. Ví dụ mẫu
      let examplesHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>💡</span> 4. Ví dụ minh họa có lời giải chi tiết</div>
      `;
      (ch.examples || []).forEach((ex, idx) => {{
        examplesHtml += `
          <div class="example-card">
            <div class="example-title">${{ex.title}}</div>
            <div class="example-body">
              <p><strong>Đề bài:</strong> ${{ex.problem}}</p>
              <div class="example-analysis"><strong>Phân tích & Hướng tư duy:</strong> ${{ex.analysis}}</div>
              <p><strong>Lời giải:</strong><br>${{ex.solution.replace(/\\n/g, '<br>')}}</p>
            </div>
          </div>
        `;
      }});
      examplesHtml += `</div>`;

      // 5. Lỗi thường gặp
      let pitfallsHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>⚠️</span> 5. Lỗi thường gặp & Mẹo kiểm tra nhanh</div>
      `;
      (ch.pitfalls || []).forEach(p => {{
        pitfallsHtml += `
          <div class="pitfall-card">
            <div class="pitfall-error">❌ ${{p.error}}</div>
            <div class="pitfall-fix">✅ ${{p.fix}}</div>
            <div class="pitfall-tip">💡 ${{p.tip}}</div>
          </div>
        `;
      }});
      pitfallsHtml += `</div>`;

      // 6. Bài tập thực hành 10 bài
      let exercisesHtml = `
        <div class="section-block">
          <div class="section-header-title"><span>🎯</span> 6. Bài tập thực hành (10 bài: 4 Dễ, 4 Vừa, 2 Khó)</div>
          <p style="font-size:0.875rem; color:var(--text-muted); margin-bottom:1.25rem;">
            Nhập đáp số dạng số thập phân vào ô trống, ấn <strong>Kiểm tra</strong> để chấm điểm tự động. Hệ thống hỗ trợ sai số cho phép $\\pm 2\\% - 5\\%$.
          </p>
      `;
      (ch.exercises || []).forEach((item, idx) => {{
        const saved = appState.exercises[item.id] || {{}};
        const isSolved = saved.isCorrect === true;
        const isWrong = saved.isCorrect === false;
        const badgeClass = item.type === "easy" ? "badge-easy" : (item.type === "mid" ? "badge-mid" : "badge-hard");
        const badgeText = item.type === "easy" ? "Dễ" : (item.type === "mid" ? "Vừa" : "Khó");

        let hintsHtml = "";
        (item.hints || []).forEach((h, hIdx) => {{
          hintsHtml += `<p>• <strong>Gợi ý ${{hIdx+1}}:</strong> ${{h}}</p>`;
        }});

        exercisesHtml += `
          <div class="exercise-item ${{isSolved ? 'solved-correct' : (isWrong ? 'solved-wrong' : '')}}" id="card_${{item.id}}">
            <div class="exercise-topbar">
              <div class="ex-index-wrap">
                <strong>Bài ${{idx + 1}}.</strong>
                <span class="ex-badge ${{badgeClass}}">${{badgeText}}</span>
              </div>
              <span id="badge_status_${{item.id}}" style="font-size:0.8rem; font-weight:700; color:${{isSolved ? 'var(--success)' : (isWrong ? 'var(--danger)' : 'var(--text-dim)')}}">
                ${{isSolved ? '✓ Đã đúng' : (isWrong ? '✗ Chưa đúng' : 'Chưa làm')}}
              </span>
            </div>

            <div class="exercise-question">${{item.q}}</div>

            <div class="exercise-interactive-bar">
              <input type="text" class="input-answer" id="input_${{item.id}}" value="${{saved.userVal || ''}}" placeholder="Nhập đáp số..." onkeydown="if(event.key==='Enter') checkAnswer('${{item.id}}')">
              <span class="ex-unit-label">${{item.unit || ''}}</span>
              <button class="btn-action btn-check" onclick="checkAnswer('${{item.id}}')">Kiểm tra</button>
              <button class="btn-action btn-secondary" onclick="toggleAccordion('hints_${{item.id}}')">💡 Gợi ý</button>
              <button class="btn-action btn-secondary" onclick="toggleAccordion('sol_${{item.id}}')">📖 Lời giải chi tiết</button>
            </div>

            <div class="feedback-banner ${{isSolved ? 'show success' : (isWrong ? 'show error' : '')}}" id="feedback_${{item.id}}">
              ${{isSolved ? '🎉 Chính xác! Bạn đã nắm vững công thức và tính toán chuẩn xác.' : (isWrong ? '⚠️ Chưa chính xác. Hãy kiểm tra lại đơn vị, dấu đại số hoặc mở Gợi ý / Lời giải chi tiết để xem phương pháp.' : '')}}
            </div>

            <div class="hints-content" id="hints_${{item.id}}">
              ${{hintsHtml}}
            </div>

            <div class="solution-content" id="sol_${{item.id}}">
              <strong>Lời giải đầy đủ:</strong><br>
              ${{item.solution.replace(/\\n/g, '<br>')}}
            </div>
          </div>
        `;
      }});

      // Thang điểm cuối chương
      const totalExCount = (ch.exercises || []).length;
      let correctExCount = 0;
      (ch.exercises || []).forEach(e => {{
        if (appState.exercises[e.id]?.isCorrect) correctExCount++;
      }});
      const score10 = totalExCount > 0 ? ((correctExCount / totalExCount) * 10).toFixed(1) : "0.0";
      let ratingText = "Cần ôn tập thêm lý thuyết";
      let ratingColor = "var(--danger)";
      if (score10 >= 9.0) {{
        ratingText = "Xuất sắc! Làm chủ toàn diện kiến thức chương này";
        ratingColor = "var(--success)";
      }} else if (score10 >= 8.0) {{
        ratingText = "Giỏi! Nắm rất chắc lý thuyết và kỹ năng giải toán";
        ratingColor = "var(--primary-light)";
      }} else if (score10 >= 6.5) {{
        ratingText = "Khá! Cần luyện thêm bài tập mức Vừa và Khó";
        ratingColor = "var(--warning)";
      }}

      exercisesHtml += `
          <div class="scorecard-box">
            <div class="scorecard-val" id="chapterScoreVal">${{score10}} / 10</div>
            <div class="scorecard-rating" style="color: ${{ratingColor}}">${{ratingText}}</div>
            <p class="scorecard-msg">
              Bạn đã hoàn thành <strong>${{correctExCount}} / ${{totalExCount}}</strong> bài tập của Chương ${{ch.num}}.
            </p>
            <button class="btn-action btn-secondary" onclick="resetChapterEx(${{ch.id}})">🔄 Làm lại bài tập chương này</button>
          </div>
        </div>
      `;

      // Next / Previous Chapter navigation buttons
      const prevCh = CH.find(c => c.id === ch.id - 1);
      const nextCh = CH.find(c => c.id === ch.id + 1);
      const bottomNavHtml = `
        <div style="display:flex; justify-content:space-between; margin-top:2rem; padding-top:1.5rem; border-top:1px solid var(--border-subtle); flex-wrap:wrap; gap:0.5rem;">
          ${{prevCh ? `<button class="btn-action btn-secondary" onclick="selectChapter(${{prevCh.id}})">❮ Chương ${{prevCh.num}}: ${{prevCh.title}}</button>` : `<div></div>`}}
          ${{nextCh ? `<button class="btn-action btn-check" onclick="selectChapter(${{nextCh.id}})">Chương ${{nextCh.num}}: ${{nextCh.title}} ❯</button>` : `<div></div>`}}
        </div>
      `;

      container.innerHTML = `
        <div class="ch-header-banner">
          <span class="ch-part-label">${{ch.part}}</span>
          <h1 class="ch-title-main">Chương ${{ch.num}}: ${{ch.title}}</h1>
          <p class="ch-summary-text">${{ch.summary}}</p>
        </div>
        ${{natureHtml}}
        ${{formulasHtml}}
        ${{typesHtml}}
        ${{examplesHtml}}
        ${{pitfallsHtml}}
        ${{exercisesHtml}}
        ${{bottomNavHtml}}
      `;

      renderAllMath();
    }}

    /* =========================================================
       EXERCISE INTERACTIVE CHECKER LOGIC
       ========================================================= */
    function checkAnswer(exId) {{
      const inputEl = document.getElementById(`input_${{exId}}`);
      if (!inputEl) return;
      const rawVal = inputEl.value.trim().replace(",", ".");
      const userNum = parseFloat(rawVal);

      // Find exercise
      let targetEx = null;
      for (const ch of CH) {{
        if (ch.exercises) {{
          targetEx = ch.exercises.find(e => e.id === exId);
          if (targetEx) break;
        }}
      }}
      if (!targetEx) return;

      const feedbackEl = document.getElementById(`feedback_${{exId}}`);
      const cardEl = document.getElementById(`card_${{exId}}`);
      const badgeStatusEl = document.getElementById(`badge_status_${{exId}}`);

      if (isNaN(userNum)) {{
        if (feedbackEl) {{
          feedbackEl.className = "feedback-banner show error";
          feedbackEl.textContent = "Vui lòng nhập một số hợp lệ!";
        }}
        return;
      }}

      // Tolerance calculation
      const correctAns = targetEx.ans;
      const tol = targetEx.tol || 0.05;
      let isCorrect = false;

      if (Math.abs(correctAns) < 1e-6) {{
        isCorrect = Math.abs(userNum) <= 0.05;
      }} else {{
        const relErr = Math.abs(userNum - correctAns) / Math.abs(correctAns);
        const absErr = Math.abs(userNum - correctAns);
        isCorrect = (relErr <= tol) || (absErr <= Math.max(tol, 0.05));
      }}

      // Save state
      appState.exercises[exId] = {{
        userVal: rawVal,
        isCorrect: isCorrect,
        solvedAt: Date.now()
      }};
      saveState();

      // UI update
      if (feedbackEl) {{
        feedbackEl.className = `feedback-banner show ${{isCorrect ? 'success' : 'error'}}`;
        feedbackEl.innerHTML = isCorrect
          ? "🎉 <strong>Chính xác!</strong> Bạn đã làm rất tốt."
          : `⚠️ <strong>Chưa chính xác!</strong> Hãy xem lại đơn vị, dấu hoặc mở <em>Gợi ý / Lời giải</em> để được hướng dẫn.`;
      }}

      if (cardEl) {{
        cardEl.className = `exercise-item ${{isCorrect ? 'solved-correct' : 'solved-wrong'}}`;
      }}

      if (badgeStatusEl) {{
        badgeStatusEl.textContent = isCorrect ? "✓ Đã đúng" : "✗ Chưa đúng";
        badgeStatusEl.style.color = isCorrect ? "var(--success)" : "var(--danger)";
      }}

      updateGlobalStats();
      renderSidebar();
    }}

    function toggleAccordion(id) {{
      const el = document.getElementById(id);
      if (!el) return;
      el.classList.toggle("show");
      renderAllMath();
    }}

    function toggleProof(id) {{
      const el = document.getElementById(id);
      if (!el) return;
      el.style.display = (el.style.display === "none") ? "block" : "none";
      renderAllMath();
    }}

    function resetChapterEx(chId) {{
      if (!confirm("Bạn có chắc chắn muốn đặt lại kết quả bài tập của chương này?")) return;
      const ch = CH.find(c => c.id === chId);
      if (ch && ch.exercises) {{
        ch.exercises.forEach(e => {{
          delete appState.exercises[e.id];
        }});
      }}
      saveState();
      renderSidebar();
      renderCurrentChapter();
    }}

    /* =========================================================
       VIEW SWITCHING: Lectures / Printable Formulas / Review
       ========================================================= */
    function switchView(viewName) {{
      appState.activeView = viewName;
      document.getElementById("btnViewLectures")?.classList.toggle("active", viewName === "lectures");
      document.getElementById("btnViewFormulas")?.classList.toggle("active", viewName === "formulas");
      document.getElementById("btnViewReview")?.classList.toggle("active", viewName === "review");

      document.getElementById("chapterMainView").style.display = (viewName === "lectures") ? "block" : "none";
      document.getElementById("formulaSheetView").style.display = (viewName === "formulas") ? "block" : "none";
      document.getElementById("reviewModeView").style.display = (viewName === "review") ? "block" : "none";

      if (viewName === "formulas") renderPrintableFormulas();
      if (viewName === "review") renderReviewQuestion();
      renderAllMath();
    }}

    function renderPrintableFormulas() {{
      const container = document.getElementById("printableFormulasContainer");
      if (!container) return;
      let html = "";
      CH.forEach(ch => {{
        if (ch.formulas && ch.formulas.length > 0) {{
          html += `
            <div class="formula-card">
              <div class="formula-name"><strong>Chương ${{ch.num}}: ${{ch.title}}</strong></div>
          `;
          ch.formulas.forEach(f => {{
            html += `
              <div style="margin-bottom:0.6rem;">
                <div style="font-size:0.82rem; font-weight:600; color:var(--text-muted);">${{f.name}}</div>
                <div class="formula-display-box" style="margin:0.25rem 0;">$$${{f.latex}}$$</div>
              </div>
            `;
          }});
          html += `</div>`;
        }}
      }});
      container.innerHTML = html;
      renderAllMath();
    }}

    /* =========================================================
       REVIEW MODE (Random Shuffle Practice)
       ========================================================= */
    function renderReviewQuestion() {{
      const container = document.getElementById("reviewQuestionContainer");
      if (!container) return;

      const pool = [];
      CH.forEach(ch => {{
        if (ch.exercises) {{
          ch.exercises.forEach(ex => {{
            pool.push({{ ...ex, chNum: ch.num, chTitle: ch.title }});
          }});
        }}
      }});

      if (pool.length === 0) {{
        container.innerHTML = "<p>Chưa có câu hỏi nào sẵn sàng.</p>";
        return;
      }}

      const randomEx = pool[Math.floor(Math.random() * pool.length)];

      const badgeClass = randomEx.type === "easy" ? "badge-easy" : (randomEx.type === "mid" ? "badge-mid" : "badge-hard");
      const badgeText = randomEx.type === "easy" ? "Dễ" : (randomEx.type === "mid" ? "Vừa" : "Khó");

      let hintsHtml = "";
      (randomEx.hints || []).forEach((h, hIdx) => {{
        hintsHtml += `<p>• <strong>Gợi ý ${{hIdx+1}}:</strong> ${{h}}</p>`;
      }});

      container.innerHTML = `
        <div class="exercise-item" id="card_rev_${{randomEx.id}}">
          <div class="exercise-topbar">
            <div>
              <span class="ch-part-label">Chương ${{randomEx.chNum}}: ${{randomEx.chTitle}}</span>
              <span class="ex-badge ${{badgeClass}}" style="margin-left:0.5rem;">${{badgeText}}</span>
            </div>
            <span id="badge_status_rev_${{randomEx.id}}" style="font-size:0.8rem; font-weight:700; color:var(--text-dim)">
              Chế độ ôn tập
            </span>
          </div>

          <div class="exercise-question">${{randomEx.q}}</div>

          <div class="exercise-interactive-bar">
            <input type="text" class="input-answer" id="input_rev_${{randomEx.id}}" placeholder="Nhập đáp số..." onkeydown="if(event.key==='Enter') checkReviewAnswer('${{randomEx.id}}', ${{randomEx.ans}}, ${{randomEx.tol || 0.05}})">
            <span class="ex-unit-label">${{randomEx.unit || ''}}</span>
            <button class="btn-action btn-check" onclick="checkReviewAnswer('${{randomEx.id}}', ${{randomEx.ans}}, ${{randomEx.tol || 0.05}})">Kiểm tra</button>
            <button class="btn-action btn-secondary" onclick="toggleAccordion('hints_rev_${{randomEx.id}}')">💡 Gợi ý</button>
            <button class="btn-action btn-secondary" onclick="toggleAccordion('sol_rev_${{randomEx.id}}')">📖 Lời giải</button>
          </div>

          <div class="feedback-banner" id="feedback_rev_${{randomEx.id}}"></div>

          <div class="hints-content" id="hints_rev_${{randomEx.id}}">${{hintsHtml}}</div>
          <div class="solution-content" id="sol_rev_${{randomEx.id}}">${{randomEx.solution.replace(/\\n/g, '<br>')}}</div>
        </div>
      `;

      renderAllMath();
    }}

    function checkReviewAnswer(id, correctAns, tol) {{
      const inputEl = document.getElementById(`input_rev_${{id}}`);
      if (!inputEl) return;
      const rawVal = inputEl.value.trim().replace(",", ".");
      const userNum = parseFloat(rawVal);
      const feedbackEl = document.getElementById(`feedback_rev_${{id}}`);

      if (isNaN(userNum)) {{
        feedbackEl.className = "feedback-banner show error";
        feedbackEl.textContent = "Vui lòng nhập một số hợp lệ!";
        return;
      }}

      let isCorrect = false;
      if (Math.abs(correctAns) < 1e-6) {{
        isCorrect = Math.abs(userNum) <= 0.05;
      }} else {{
        const relErr = Math.abs(userNum - correctAns) / Math.abs(correctAns);
        const absErr = Math.abs(userNum - correctAns);
        isCorrect = (relErr <= tol) || (absErr <= Math.max(tol, 0.05));
      }}

      feedbackEl.className = `feedback-banner show ${{isCorrect ? 'success' : 'error'}}`;
      feedbackEl.innerHTML = isCorrect
        ? "🎉 <strong>Rất xuất sắc!</strong> Đáp án hoàn toàn chuẩn xác."
        : `⚠️ <strong>Chưa chính xác!</strong> Hãy xem lại gợi ý hoặc lời giải chi tiết.`;
    }}

    /* =========================================================
       SEARCH ENGINE (Instant Filter)
       ========================================================= */
    function initSearch() {{
      const searchInput = document.getElementById("searchInput");
      if (!searchInput) return;

      searchInput.addEventListener("input", (e) => {{
        const query = e.target.value.toLowerCase().trim();
        if (!query) {{
          renderSidebar();
          return;
        }}

        const listEl = document.getElementById("chapterNavList");
        if (!listEl) return;
        listEl.innerHTML = "";

        let matchCount = 0;
        CH.forEach(ch => {{
          const matchTitle = ch.title.toLowerCase().includes(query);
          const matchSummary = ch.summary.toLowerCase().includes(query);
          const matchFormula = (ch.formulas || []).some(f => f.name.toLowerCase().includes(query));

          if (matchTitle || matchSummary || matchFormula) {{
            matchCount++;
            const li = document.createElement("li");
            li.className = "ch-nav-item";
            li.innerHTML = `
              <button class="ch-nav-btn ${{ch.id === appState.activeChapterId ? 'active' : ''}}" onclick="selectChapter(${{ch.id}})">
                <span><strong>${{ch.num}}.</strong> ${{ch.title}}</span>
                <span class="ch-badge-status badge-ready">Khớp</span>
              </button>
            `;
            listEl.appendChild(li);
          }}
        }});

        if (matchCount === 0) {{
          listEl.innerHTML = `<li style="padding:1rem; font-size:0.85rem; color:var(--text-dim); text-align:center;">Không tìm thấy kết quả phù hợp.</li>`;
        }}
      }});
    }}

    /* =========================================================
       INIT & EVENT LISTENERS
       ========================================================= */
    document.addEventListener("DOMContentLoaded", () => {{
      loadState();
      applyTheme(appState.theme || "dark");

      renderSidebar();
      renderCurrentChapter();
      initSearch();

      // Theme toggle button
      document.getElementById("btnToggleTheme")?.addEventListener("click", () => {{
        const newTheme = (appState.theme === "dark") ? "light" : "dark";
        applyTheme(newTheme);
      }});

      // Mobile sidebar toggle
      document.getElementById("btnToggleSidebar")?.addEventListener("click", () => {{
        document.getElementById("sidebarNav")?.classList.toggle("mobile-open");
      }});

      // View buttons
      document.getElementById("btnViewLectures")?.addEventListener("click", () => switchView("lectures"));
      document.getElementById("btnViewFormulas")?.addEventListener("click", () => switchView("formulas"));
      document.getElementById("btnViewReview")?.addEventListener("click", () => switchView("review"));
      document.getElementById("btnNextReviewQuestion")?.addEventListener("click", () => renderReviewQuestion());
    }});
  </script>
</body>
</html>
"""

out_vatly = r"C:\Users\vanh\.gemini\antigravity\scratch\vatly-daicuong1\vatly.html"
out_index = r"C:\Users\vanh\.gemini\antigravity\scratch\vatly-daicuong1\index.html"

with open(out_vatly, "w", encoding="utf-8") as f:
    f.write(html_template)

with open(out_index, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"vatly.html successfully generated at: {out_vatly} (size: {os.path.getsize(out_vatly)} bytes)")
print(f"index.html successfully generated at: {out_index} (size: {os.path.getsize(out_index)} bytes)")
