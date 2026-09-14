"""Check local links, resume consistency, and PDF extraction without a browser."""
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = []
        self.references = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.append(attrs['id'])
        for attr in ['href', 'src']:
            if attr in attrs:
                self.references.append(attrs[attr])

pages = {name: Page((ROOT / name).read_text(encoding='utf-8')) for name in ['index.html', 'resume.html']}
for name, page in pages.items():
    assert len(page.ids) == len(set(page.ids)), f'Duplicate IDs in {name}'
    for reference in page.references:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        target = unquote(url.path) or name
        assert (ROOT / target).is_file(), f'Missing asset: {reference} in {name}'
        if url.fragment:
            assert target in pages and unquote(url.fragment) in pages[target].ids, f'Missing anchor: {reference}'

resume = json.loads((ROOT / 'content/resume.json').read_text(encoding='utf-8'))
pdf = PdfReader(ROOT / 'assets/Rowen-Berndt-Resume.pdf')
assert len(pdf.pages) == 1, 'Resume must fit on one page'
text = ' '.join(pdf.pages[0].extract_text().split())
assert resume['name'].upper() in text
for section in ['skills', 'projects', 'education', 'experience']:
    for entry in resume[section]:
        for value in entry.values():
            for phrase in (value if isinstance(value, list) else [value]):
                assert ' '.join(phrase.split()) in text, f'Missing PDF content: {phrase}'
assert 'One year completed' in text
assert 'Aug 2026 - Present' in text
assert '2029' not in text
assert len(pdf.pages[0].get('/Annots', [])) >= 2, 'Expected clickable contact links'
print('PASS: links, anchors, unique IDs, all resume content, contact links, and one-page PDF')
