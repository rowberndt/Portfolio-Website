# Rowen Berndt portfolio

A responsive, static portfolio focused on AI/ML internships. Includes project case studies, a small interactive neural-network forward pass, and a one-page resume in PDF, HTML, and editable Markdown.

## Preview

No build step or runtime packages are required. From this directory:

```sh
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173 in a browser. Core content, project disclosures, and resume links work without JavaScript. JavaScript enables the demo, email copying, and print button.

## Update the resume

Edit `content/resume.json`, then regenerate all three versions:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/build_resume.py
python scripts/check_site.py
```

The generated outputs are `assets/Rowen-Berndt-Resume.pdf`, `assets/Rowen-Berndt-Resume.md`, and `resume.html`. Keep these outputs in version control so visitors do not need Python. The editable Markdown is an export; future regenerations overwrite changes made directly to it.

The short bio and resume preview in `index.html` are hand-authored. Update them when education, training, or project status changes. The PDF is the canonical one-page application resume; browser printing of the HTML can vary with browser settings.

## Checks

```sh
python scripts/check_site.py
node scripts/check_demo.cjs
```

Checks validate local assets and fragment links, duplicate IDs, resume content extraction, one-page PDF output, and the demo's probability bounds and normalization. Browser review should also cover widths of 320, 390, 768, 1024, and 1440 pixels; keyboard sliders and project disclosures; resume download; and email copy feedback.

## Hosting

Serve `index.html`, `styles.css`, `script.js`, `resume.html`, `resume.css`, `resume.js`, and the `assets/` directory using any static web host. Relative links support a project subdirectory. There are no third-party fonts, analytics, runtime CDNs, API keys, or form backends.

Contact actions open the visitor's email app. The GitHub link points to the profile; featured repositories are currently private, so case studies provide context without sending visitors to inaccessible repository pages. Source visibility is a separate repository setting.

## Content provenance

See `docs/content-notes.md` for the factual basis of the rewritten material and the limits on project claims.
