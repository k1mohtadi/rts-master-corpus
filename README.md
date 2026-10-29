# RTS Master Corpus & Universal Glossary
### Rhizomatique Translation Studio (RTS) — Directed by Keyvan Mohtadi

This repository is the cross-project **Living Editorial Memory** and **Universal Glossary** of the Rhizomatique Translation Studio (RTS). It is updated continuously at the conclusion of each chapter or entry across our translation and editing projects.

Rather than hardcoding static rules into every prompt, this repository accumulates empirical editorial decisions over time so that both human collaborators and our AI pipeline can study, audit, and learn from our evolving translation praxis.

---

## 📂 Repository Contents

### 1. Contrastive Sentence Decision Log (`English` $\to$ `RTS Invalid` $\to$ `Human Edited`)
Tracks specific sentences where the RTS draft was judged invalid, mechanical, calqued, or rhythmically flawed, alongside Keyvan Mohtadi's final human edit and the distilled rationale.
- 📊 **CSV (Excel / Google Sheets / Data Pipeline):** [`sentence_decisions.csv`](./sentence_decisions.csv)
- 📖 **Browsable Markdown Table:** [`SENTENCE_DECISIONS.md`](./SENTENCE_DECISIONS.md) *(Currently logging **38** verified sentence-level decisions)*

### 2. Universal Glossary & Attribution Database
Records our preferred Persian translations for core concepts across sociology, political economy, philosophy, and cultural studies—explicitly documenting **who used or coined the term** (whether from reference dictionaries like Dariush Ashouri's *Dictionary of Humanities*, established Persian translators, project translators like Dr. Saeed Madani, or RTS editorial decisions).
- 📊 **CSV (Excel / Google Sheets / Data Pipeline):** [`universal_glossary.csv`](./universal_glossary.csv)
- 📖 **Browsable Markdown Table:** [`UNIVERSAL_GLOSSARY.md`](./UNIVERSAL_GLOSSARY.md) *(Currently logging **51** core conceptual terms)*

---

## 📚 Projects Currently Logged
1. **Encyclopedia of Social & Political Movements (Vols. 1–2)** — Entry 871 (*Food Riots*), Entry 899 (*Gezi Park Protests (Istanbul)*), Entry 901 (*Global Austerity Protests*), Entry 1009 (*Hunger Strikes*), Entry 1037 (*Independentism (Catalonia)*), Entry 1051 (*Indigenous Protest in Bolivia Against Evo Morales*).
2. **Social Histories of Modern Iran (Stephanie Cronin / تاریخ‌های اجتماعی ایران مدرن)** — *Introduction: Subalterns, politics and society in Iran* & *Chapter 1: The Iranian Revolution of the 1970s in Global Perspective*.

---

## 🔄 How We Update This Repository (End-of-Chapter Workflow)

1. **Human Editorial Pass:** At the end of each chapter/entry, the human editor finalizes the Persian text.
2. **Automated Diff Extraction:** We compare the **RTS Draft** against the **Human Final Version**, extracting sentences with substantive syntactic, lexical, chronological, or stylistic revisions.
3. **Corpus & Glossary Update:** New sentence pairs and newly settled terminology (with their reference/translator attributions) are appended to `sentence_decisions.csv` and `universal_glossary.csv`.
4. **Markdown Sync:** Running `python scripts/build_corpus.py` regenerates the GitHub Markdown tables (`SENTENCE_DECISIONS.md` and `UNIVERSAL_GLOSSARY.md`) so collaborators can browse everything directly on GitHub or download the CSVs.
