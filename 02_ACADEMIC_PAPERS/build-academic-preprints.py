import os
import re
import subprocess

PAPERS_DIR = r"D:\Projects\Public\synthetic-humanism-git\02_ACADEMIC_PAPERS"
OUT_DIR = os.path.join(PAPERS_DIR, "dist_pdf")
PANDOC = r"C:\Users\ABC\AppData\Local\Pandoc\pandoc.exe"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

ACADEMIC_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@400;500;600;700&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&family=JetBrains+Mono:wght@400;500&display=swap');

@page {
    size: letter;
    margin: 22mm 20mm 22mm 20mm;
}

*, *:before, *:after {
    box-sizing: border-box;
}

body {
    font-family: 'Lora', 'Charter', 'Cambria', 'Georgia', serif;
    font-size: 10.2pt;
    line-height: 1.58;
    color: #1a202c;
    background-color: #ffffff;
    text-align: justify;
    text-justify: inter-word;
    margin: 0;
    padding: 0;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

/* Academic Masthead / Header Bar */
.running-header {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 7.5pt;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #64748b;
    border-bottom: 0.75pt solid #cbd5e1;
    padding-bottom: 4px;
    margin-bottom: 24px;
    display: flex;
    justify-content: space-between;
}

.running-footer {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 7.5pt;
    letter-spacing: 0.05em;
    color: #94a3b8;
    border-top: 0.5pt solid #e2e8f0;
    padding-top: 6px;
    margin-top: 36px;
    display: flex;
    justify-content: space-between;
}

/* Paper Title */
h1 {
    font-family: 'Cinzel', 'Lora', serif;
    font-size: 20pt;
    font-weight: 700;
    line-height: 1.25;
    color: #0f172a;
    text-align: center;
    margin-top: 8px;
    margin-bottom: 16px;
    letter-spacing: -0.01em;
}

/* Headings */
h2 {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 12.5pt;
    font-weight: 700;
    line-height: 1.35;
    color: #0f2b48;
    margin-top: 24px;
    margin-bottom: 10px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
    break-after: avoid;
    page-break-after: avoid;
}

h3 {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 10.8pt;
    font-weight: 600;
    line-height: 1.35;
    color: #1e3a5f;
    margin-top: 18px;
    margin-bottom: 6px;
    break-after: avoid;
    page-break-after: avoid;
}

h4 {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 9.8pt;
    font-weight: 600;
    color: #334155;
    margin-top: 14px;
    margin-bottom: 4px;
    break-after: avoid;
    page-break-after: avoid;
}

p {
    margin-top: 0;
    margin-bottom: 0.85rem;
}

/* Author Block Styling */
.author-container {
    text-align: center;
    margin-bottom: 24px;
    font-family: 'Inter', -apple-system, sans-serif;
}
.author-name {
    font-size: 12pt;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 2px;
}
.author-affiliation {
    font-size: 9pt;
    color: #475569;
    line-height: 1.4;
}
.author-contact {
    font-size: 8.5pt;
    color: #2563eb;
    margin-top: 3px;
}
.repo-badges {
    margin-top: 12px;
    margin-bottom: 18px;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8pt;
}

/* Abstract Box - Journal Standard */
.abstract-box {
    margin: 20px 24px 28px 24px;
    padding: 14px 20px;
    background-color: #f8fafc;
    border-top: 1.5pt solid #0f2b48;
    border-bottom: 1.5pt solid #0f2b48;
    font-size: 9.4pt;
    line-height: 1.52;
}
.abstract-title {
    font-family: 'Inter', sans-serif;
    font-size: 9.5pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #0f2b48;
    text-align: center;
    margin-bottom: 8px;
}
.keywords-box {
    margin-top: 10px;
    font-family: 'Inter', sans-serif;
    font-size: 8.6pt;
    color: #334155;
}
.keywords-label {
    font-weight: 700;
    color: #0f2b48;
}

/* Blockquotes (Philosophical Axioms / Quotes) */
blockquote {
    border-left: 3pt solid #1e3a5f;
    margin: 16px 0;
    padding: 10px 18px;
    background-color: #f1f5f9;
    font-style: italic;
    color: #1e293b;
    border-radius: 0 4px 4px 0;
    break-inside: avoid;
    page-break-inside: avoid;
}
blockquote p {
    margin: 0;
}

/* Academic Tables - Classic Booktabs Standard */
table {
    border-collapse: collapse;
    width: 100%;
    margin: 18px 0;
    font-size: 8.8pt;
    line-height: 1.42;
    font-family: 'Inter', -apple-system, sans-serif;
    border-top: 2pt solid #0f172a;
    border-bottom: 2pt solid #0f172a;
    break-inside: avoid;
    page-break-inside: avoid;
}
th {
    border-bottom: 1pt solid #0f172a;
    padding: 7px 8px;
    text-align: left;
    font-weight: 600;
    color: #0f172a;
    background-color: #f8fafc;
    letter-spacing: 0.02em;
}
td {
    padding: 6px 8px;
    border-bottom: 0.5pt solid #e2e8f0;
    color: #334155;
    vertical-align: top;
}
tr:nth-child(even) td {
    background-color: #fafbfc;
}

/* Code & Verbatim Blocks */
code {
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8.4pt;
    background-color: #f1f5f9;
    padding: 1px 4px;
    border-radius: 3px;
    color: #0f2b48;
}
pre {
    background-color: #f8fafc;
    border: 0.75pt solid #cbd5e1;
    border-left: 2.5pt solid #3b82f6;
    border-radius: 3px;
    padding: 10px 14px;
    overflow-x: auto;
    font-family: 'JetBrains Mono', Consolas, monospace;
    font-size: 8pt;
    line-height: 1.4;
    color: #1e293b;
    break-inside: avoid;
    page-break-inside: avoid;
}
pre code {
    background: none;
    border: none;
    padding: 0;
    color: inherit;
}

/* Hyperlinks */
a {
    color: #1d4ed8;
    text-decoration: none;
}
a:hover {
    text-decoration: underline;
}

hr {
    border: 0;
    border-top: 0.5pt solid #cbd5e1;
    margin: 20px 0;
}

/* MathJax Display Styling */
.MathJax {
    font-size: 105% !important;
}
mjx-container[display="true"] {
    margin: 12px 0 !important;
}
</style>

<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
    displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
  },
  options: {
    enableMenu: false
  }
};
</script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml-full.js"></script>
"""

def generate_paper_html(paper_info):
    md_file = os.path.join(PAPERS_DIR, paper_info["md"])
    with open(md_file, "r", encoding="utf-8") as f:
        md_text = f.read()

    # Create temporary clean markdown with pandoc
    temp_html = os.path.join(OUT_DIR, "temp_" + paper_info["html"])
    
    # Run Pandoc to get HTML body
    cmd = [
        PANDOC,
        md_file,
        "--mathjax",
        "-t", "html5"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, check=True, encoding="utf-8")
    body_html = res.stdout

    # Academic Layout Wrap
    running_header = f"""
    <div class="running-header">
        <span>Salik Shah &middot; Dirgha AI</span>
        <span>{paper_info["short_title"]} &middot; Preprint (Nov 2026)</span>
    </div>
    """

    running_footer = f"""
    <div class="running-footer">
        <span>Dirgha AI Foundational Monograph Series &middot; Open Research &middot; CC-BY-4.0</span>
        <span>https://salikshah.com &middot; github.com/Dirgha-AI</span>
    </div>
    """

    final_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{paper_info["title"]}</title>
    {ACADEMIC_CSS}
</head>
<body>
    {running_header}
    {body_html}
    {running_footer}
</body>
</html>
"""

    html_path = os.path.join(OUT_DIR, paper_info["html"])
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(final_html)

    return html_path

def compile_pdf(html_path, pdf_path):
    cmd = [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        "--virtual-time-budget=8000",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    subprocess.run(cmd, check=True)

PAPERS = [
    {
        "md": "Paper-1-Synthetic-Humanism-Ahimsa-of-Abundance.md",
        "title": "Synthetic Humanism: Intelligence, Non-Harm, and the Ahimsa of Abundance",
        "short_title": "Synthetic Humanism: Intelligence, Non-Harm & Abundance",
        "html": "Monograph-1-Synthetic-Humanism-Ahimsa-of-Abundance.html",
        "pdf": "Monograph-1-Synthetic-Humanism-Ahimsa-of-Abundance.pdf"
    },
    {
        "md": "Paper-2-Ahimsa-as-a-Timeout-Rule-LOKAHI-DPI.md",
        "title": "Ahimsa as a Timeout Rule: Operationalizing Non-Harm in AI Accountability Infrastructure for Digital Public Goods",
        "short_title": "Ahimsa as a Timeout Rule: LOKAHI for DPI",
        "html": "Monograph-2-Ahimsa-as-a-Timeout-Rule-LOKAHI-DPI.html",
        "pdf": "Monograph-2-Ahimsa-as-a-Timeout-Rule-LOKAHI-DPI.pdf"
    },
    {
        "md": "Paper-3-Ahimsa-by-Design-Dual-Axis-AIA.md",
        "title": "Ahimsa-by-Design: Dual-Axis Evaluation of Non-Extraction and Affirmative Flourishing in AI Systems",
        "short_title": "Ahimsa-by-Design: Dual-Axis AIA v1.1",
        "html": "Monograph-3-Ahimsa-by-Design-Dual-Axis-AIA.html",
        "pdf": "Monograph-3-Ahimsa-by-Design-Dual-Axis-AIA.pdf"
    },
    {
        "md": "Paper-4-LOKAHI-Disjoint-Threshold-Consent-Rings.md",
        "title": "LOKAHI: Disjoint Threshold Consent Rings and Cryptographic Boundary Manifests for Multi-Agent Collectives",
        "short_title": "LOKAHI: Disjoint Threshold Consent Rings",
        "html": "Monograph-4-LOKAHI-Disjoint-Threshold-Consent-Rings.html",
        "pdf": "Monograph-4-LOKAHI-Disjoint-Threshold-Consent-Rings.pdf"
    },
    {
        "md": "Paper-5-Ghostproof-Epistemic-Uncertainty.md",
        "title": "Ghostproof: The Somatic Judgment Layer, Epistemic Uncertainty, and Load-Bearing Human Agency in AI Delegation",
        "short_title": "Ghostproof: The Somatic Judgment Layer",
        "html": "Monograph-5-Ghostproof-Somatic-Judgment-Layer.html",
        "pdf": "Monograph-5-Ghostproof-Somatic-Judgment-Layer.pdf"
    },
    {
        "md": "Paper-6-Kinetic-Ahimsa-Embodied-Robotics-Interlocks.md",
        "title": "Kinetic Ahimsa: Pre-Flight Force-Envelope Manifests and Hardware Interlocks for Embodied Robotics",
        "short_title": "Kinetic Ahimsa: Embodied Robotics Interlocks",
        "html": "Monograph-6-Kinetic-Ahimsa-Embodied-Robotics.html",
        "pdf": "Monograph-6-Kinetic-Ahimsa-Embodied-Robotics.pdf"
    }
]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("=== Compiling World-Class Academic PDF Preprints ===")
    for p in PAPERS:
        print(f"[*] Formatting {p['md']}...")
        html_file = generate_paper_html(p)
        pdf_file = os.path.join(OUT_DIR, p["pdf"])
        print(f"[*] Rendering PDF {p['pdf']} via headless Chrome (MathJax + Booktabs)...")
        compile_pdf(html_file, pdf_file)
        size_kb = os.path.getsize(pdf_file) / 1024
        print(f"  [+] SUCCESS: {p['pdf']} ({size_kb:.1f} KB)")
    print("=== All 6 Monographs Compiled Successfully ===")

if __name__ == "__main__":
    main()
