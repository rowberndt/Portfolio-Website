"""Generate the public PDF, HTML resume, and editable Markdown from one source.

Run with Python 3 and reportlab installed. No personal source files are required.
"""
import json
from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'content/resume.json').read_text(encoding='utf-8'))
assets = ROOT / 'assets'
assets.mkdir(exist_ok=True)
ink = colors.HexColor('#1f352d')
styles = {
    'name': ParagraphStyle('name', fontName='Helvetica-Bold', fontSize=24, leading=29, textColor=colors.black, spaceAfter=3),
    'headline': ParagraphStyle('headline', fontName='Helvetica', fontSize=10.5, leading=14, textColor=ink, spaceAfter=5),
    'contact': ParagraphStyle('contact', fontName='Helvetica', fontSize=9, leading=12, spaceAfter=10),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.5, leading=14, textColor=colors.HexColor('#242424')),
    'heading': ParagraphStyle('heading', fontName='Helvetica-Bold', fontSize=10, leading=13, spaceBefore=12, spaceAfter=6, textColor=ink, keepWithNext=True),
    'entry': ParagraphStyle('entry', fontName='Helvetica-Bold', fontSize=10.5, leading=14, spaceAfter=2, keepWithNext=True),
    'sub': ParagraphStyle('sub', fontName='Helvetica', fontSize=9, leading=12, textColor=colors.HexColor('#4c514e'), spaceAfter=4, keepWithNext=True),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=10.5, leading=14, textColor=colors.HexColor('#242424'), leftIndent=10, firstLineIndent=-10, spaceAfter=4),
    'skill': ParagraphStyle('skill', fontName='Helvetica', fontSize=10, leading=13, spaceAfter=3),
}
def p(text, style='body'):
    return Paragraph(text, styles[style])

story = [p(escape(data['name']).upper(), 'name'), p(escape(data['headline']), 'headline')]
story.append(p(f'<link href="mailto:{data["email"]}">{data["email"]}</link> | {data["phone"]} | <link href="{data["github"]}">github.com/rowberndt</link>', 'contact'))
story.append(p(escape(data['summary'])))
story.append(p('TECHNICAL SKILLS', 'heading'))
for skill in data['skills']:
    story.append(p(f'<b>{escape(skill["label"])}:</b> {escape(skill["text"])}', 'skill'))
story.append(p('TECHNICAL PROJECTS', 'heading'))
for project in data['projects']:
    block = [p(escape(project['name']), 'entry'), p(escape(project['subtitle']), 'sub')]
    block.extend(p('- ' + escape(bullet), 'bullet') for bullet in project['bullets'])
    story.append(KeepTogether(block))
story.append(p('EDUCATION AND TRAINING', 'heading'))
for school in data['education']:
    story.append(KeepTogether([p(f'{escape(school["name"])} <font name="Helvetica" size="9">| {escape(school["dates"])}</font>', 'entry'), p(escape(school['detail']), 'sub')]))
story.append(p('EXPERIENCE', 'heading'))
for job in data['experience']:
    block = [p(f'{escape(job["role"])} | {escape(job["organization"])}', 'entry'), p(escape(job['dates']), 'sub')]
    block.extend(p('- ' + escape(bullet), 'bullet') for bullet in job['bullets'])
    story.append(KeepTogether(block))
pdf_path = assets / 'Rowen-Berndt-Resume.pdf'
doc = SimpleDocTemplate(str(pdf_path), pagesize=letter, leftMargin=40, rightMargin=40, topMargin=33, bottomMargin=30, title='Rowen Berndt - AI and Machine Learning Resume', author='Rowen Berndt')
doc.build(story)

parts = [f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="Rowen Berndt's resume: AI/ML training at TripleTen, Python and PyTorch projects, data systems, and experience."><meta name="theme-color" content="#f7f6f0"><title>Resume | Rowen Berndt</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><link rel="stylesheet" href="resume.css"><script src="resume.js" defer></script></head>
<body><a class="skip-link" href="#resume-content">Skip to resume</a><main class="resume-page"><nav class="resume-toolbar" aria-label="Resume actions"><a href="index.html#resume">← Back to portfolio</a><div class="button-row"><button class="button print-button" type="button" id="print-resume" hidden>Print</button><a class="button primary" href="assets/Rowen-Berndt-Resume.pdf" download>Download PDF <span aria-hidden="true">↓</span></a></div></nav><article class="resume-document" id="resume-content"><header><h1>{escape(data['name'])}</h1><p class="resume-headline">{escape(data['headline'])}</p><div class="resume-contact"><a href="mailto:{data['email']}">{data['email']}</a><a href="tel:+16038673325">{data['phone']}</a><a href="{data['github']}" target="_blank" rel="noopener noreferrer">github.com/rowberndt</a></div><p class="resume-summary">{escape(data['summary'])}</p></header><section aria-labelledby="technical-skills"><h2 id="technical-skills">Technical skills</h2>''']
for skill in data['skills']:
    parts.append(f'<p class="skill-line"><strong>{escape(skill["label"])}:</strong> {escape(skill["text"])}</p>')
parts.append('</section><section aria-labelledby="technical-projects"><h2 id="technical-projects">Technical projects</h2>')
for project in data['projects']:
    parts.append(f'<div class="resume-entry"><h3>{escape(project["name"])}</h3><p class="resume-subtitle">{escape(project["subtitle"])}</p><ul>')
    parts.extend(f'<li>{escape(bullet)}</li>' for bullet in project['bullets'])
    parts.append('</ul></div>')
parts.append('</section><section aria-labelledby="education-training"><h2 id="education-training">Education and training</h2>')
for school in data['education']:
    parts.append(f'<div class="resume-entry"><div class="entry-heading"><h3>{escape(school["name"])}</h3><span class="resume-subtitle">{escape(school["dates"])}</span></div><p class="school-detail">{escape(school["detail"])}</p></div>')
parts.append('</section><section aria-labelledby="experience"><h2 id="experience">Experience</h2>')
for job in data['experience']:
    parts.append(f'<div class="resume-entry"><div class="entry-heading"><h3>{escape(job["role"])}</h3><span class="resume-subtitle">{escape(job["dates"])}</span></div><p class="resume-subtitle">{escape(job["organization"])}</p><ul>')
    parts.extend(f'<li>{escape(bullet)}</li>' for bullet in job['bullets'])
    parts.append('</ul></div>')
parts.append('</section></article><a class="resume-source-link" href="assets/Rowen-Berndt-Resume.md" download>Download editable text (Markdown)</a></main></body></html>')
(ROOT / 'resume.html').write_text('\n'.join(parts), encoding='utf-8')

md = [f'# {data["name"]}', data['headline'], f'{data["email"]} | {data["phone"]} | {data["github"]}', data['summary'], '## Technical skills']
md.extend(f'**{s["label"]}:** {s["text"]}' for s in data['skills'])
md.append('## Technical projects')
for project in data['projects']:
    md.extend([f'### {project["name"]}', project['subtitle'], '\n'.join('- ' + b for b in project['bullets'])])
md.append('## Education and training')
for school in data['education']:
    md.extend([f'**{school["name"]}** | {school["dates"]}', school['detail']])
md.append('## Experience')
for job in data['experience']:
    md.extend([f'### {job["role"]} | {job["organization"]}', job['dates'], '\n'.join('- ' + b for b in job['bullets'])])
(assets / 'Rowen-Berndt-Resume.md').write_text('\n\n'.join(md) + '\n', encoding='utf-8')
print('Generated assets/Rowen-Berndt-Resume.pdf, assets/Rowen-Berndt-Resume.md, and resume.html')
