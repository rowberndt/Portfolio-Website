# Content notes

Updated September 14, 2026. This file is maintenance context, not resume copy.

## Education and training

- User confirmed they completed one year at UNH and are no longer enrolled. Listed as Data Science coursework, 2025-2026; no completed degree or future UNH graduation is claimed.
- User confirmed current participation in TripleTen's AI/ML Bootcamp, started August 14 and in progress. The resume uses month-level dates, Aug 2026-Present, interpreting August as the current year.
- User requested priority on AI/ML internships. No specific internship season, availability date, or location preference was supplied.
- The old planned Analytical Economics degree was omitted because current enrollment was not confirmed.

## Resume and experience

- Original source: `resume25-26.pdf`, provided through the user's local Downloads folder. The original was not modified or copied into this repository.
- Name, professional contact details, internship dates, shop experience, and interests came from that resume. Its embedded portrait was extracted unchanged for the About section.
- Technical work now precedes earlier service jobs. The summary and technical skills replace the original empty profile and investing-oriented skills section.
- Engrain Market remains as concise evidence of ownership and teamwork. The older Chipotle job and high-school activities were omitted to prioritize relevant work on one page.

## Project evidence

GitHub connection verified the account `rowberndt` and the private repositories `Portfolio-Website`, `Foundations`, and `First-Neural-Net`. The local working copies contain more recent Foundations work than the GitHub default branch, so the current local implementation and documentation were also reviewed read-only.

- **Foundations:** `ingest/README.md`, `train/README.md`, `train/model.py`, and `train/JOINT_MODEL.md` support data ingestion, SQLite journaling, replay, Parquet exports, regularized logistic regression, chronological evaluation, and an experimental attention architecture. These files describe research software; no production deployment quality, commercial use, trading profit, or completed joint-model training is claimed.
- **Computer vision:** `First-Neural-Net/pytorchbasics.ipynb` implements an MNIST classifier with 784-64-64-64-10 layers, Adam, and negative log-likelihood loss. Its saved output reports `Accuracy: 0.972`. This is identified as one recorded run, not a freshly reproduced benchmark. `pytorch5.ipynb` contains cat-versus-dog image preprocessing, three convolutional layers, CUDA training, a 10% validation split, and metric logging. `pytorchgraph.py` plots the logged metrics. No cat-versus-dog accuracy is claimed.
- **Neural network fundamentals:** `First-Neural-Net/nnfs-learning.py` implements dense layers, ReLU, stable softmax, and categorical cross-entropy on the NNFS spiral dataset. It does not implement backpropagation or optimization; the site makes that scope explicit and labels the work as a learning exercise.
- **Interactive demo:** `script.js` performs real calculations with fixed illustrative weights. It is an educational example, not a trained model, and does not reuse benchmark results.

## Verification

- PDF rendered and visually inspected; verified one page and complete selectable text.
- Desktop/mobile visual inspection and overflow checks at widths 320, 390, 768, 1024, and 1440 pixels through the in-app browser.
- Keyboard-operated demo and project disclosure, PDF download, and email-copy success checked in browser.
- Local link, anchor, resume-content, and probability checks are reproducible through the scripts in `scripts/`.

## Future application edits

Add TripleTen project names, techniques, and results when those projects are completed and can be reviewed. For each application, adjust the headline, summary, skills ordering, and project emphasis to match the actual role. Keep accomplishments tied to work that can be explained and demonstrated.
