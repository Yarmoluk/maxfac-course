# Modern Oral & Maxillofacial Surgery

[![MkDocs](https://img.shields.io/badge/Built_with-MkDocs_Material-blue)](https://squidfunk.github.io/mkdocs-material/)
[![Learning Graph](https://img.shields.io/badge/Concepts-270-green)](https://yarmoluk.github.io/maxfac-course/learning-graph/concept-list/)
[![Chapters](https://img.shields.io/badge/Chapters-20-orange)](https://yarmoluk.github.io/maxfac-course/chapters/)
[![Chatbot](https://img.shields.io/badge/AI_Chatbot-Streamlit-red)](https://yarmoluk.github.io/maxfac-course/)

**Live Site:** [yarmoluk.github.io/maxfac-course](https://yarmoluk.github.io/maxfac-course/)

An intelligent clinical reference for the full-scope oral and maxillofacial surgery practitioner. 20 chapters covering all 11 AAOMS ParCare areas plus surgical technology, practice operations, and emerging frontiers.

Generated in approximately one hour using Claude Code and Dan McCreary's intelligent textbook methodology. From a blank directory to a 20-chapter, 270-concept clinical reference with AI chatbot — demonstrating that structured knowledge graph pipelines can produce domain-expert-level content at unprecedented speed.

Built as part of coursework for SEIS 666: Digital Transformation with AI at the University of St. Thomas.

## What This Covers

Six parts organized by clinical workflow:

### Part I — Clinical Foundations
| Ch | Topic |
|----|-------|
| 1 | Surgical Anatomy |
| 2 | Imaging & Diagnosis |
| 3 | Anesthesia & Sedation |
| 4 | Pharmacology & Pain Management |

### Part II — Core Procedures
| Ch | Topic |
|----|-------|
| 5 | Dentoalveolar Surgery |
| 6 | Dental Implantology |
| 7 | Pathology & Oncology |
| 8 | Facial Trauma |
| 9 | Orthognathic Surgery |
| 10 | TMJ Surgery |

### Part III — Advanced Clinical
| Ch | Topic |
|----|-------|
| 11 | Craniofacial & Cleft |
| 12 | Cosmetic & Aesthetic |
| 13 | Sleep Apnea Surgery |

### Part IV — Surgical Technology
| Ch | Topic |
|----|-------|
| 14 | Robotic Surgery (Yomi) |
| 15 | Navigation & Digital Workflows |
| 16 | 3D Printing & Virtual Surgical Planning |

### Part V — Practice Operations
| Ch | Topic |
|----|-------|
| 17 | Billing & Coding (CPT/CDT/ICD-10) |
| 18 | Practice Management |
| 19 | Telemedicine |

### Part VI — Frontiers
| Ch | Topic |
|----|-------|
| 20 | Emerging Frontiers |

## Knowledge Architecture

- **270 concepts** across 14 taxonomy categories
- **457 dependency edges** in the learning graph
- **Longest learning path:** Maxillofacial Bone Anatomy through Free Flap Reconstruction (9 concepts deep)
- **Course description quality score:** 96/100
- Every answer is verifiable — cites AAOMS ParCare, CPT/CDT codes, peer-reviewed literature

### Key Taxonomy Categories

| Category | Concepts |
|----------|----------|
| Anatomy | 25 |
| Implants | 25 |
| Surgical Technology | 25 |
| Practice Operations | 25 |
| Dentoalveolar | 20 |
| Imaging | 20 |
| Anesthesia/Pharmacology | 20 |
| Trauma | 20 |
| Orthognathic | 20 |
| Pathology/Oncology | 20 |
| Frontiers | 20 |
| Advanced Clinical | 15 |
| TMJ | 15 |

## AI Chatbot

Includes a Streamlit-powered clinical reference chatbot backed by Claude Sonnet 4.5:

- Every response must cite verifiable sources (AAOMS ParCare, journal references, CPT/CDT codes)
- 20 clinical topic categories for guided queries
- Query logging for usage analytics
- Mobile-first interface

```bash
cd chatbot
pip install -r requirements.txt
python build_knowledge_base.py
streamlit run app.py
```

## Technology Stack

- **MkDocs Material** — Static site with MathJax equations, Mermaid diagrams, dark/light mode
- **Streamlit + Anthropic Claude** — AI-powered clinical chatbot
- **vis-network.js** — Interactive knowledge graph
- **GitHub Actions** — Automated deployment
- **Python 3.12** — Graph analysis and knowledge base building

## Methodology

Generated using a structured pipeline that starts with a course description, builds a 270-concept learning graph, structures 20 chapters respecting prerequisite dependencies, then generates content at a clinical professional reading level with embedded CPT/CDT code references throughout.

Part of an ongoing exploration testing whether knowledge graph methodology can structure complex medical domains with the same rigor as engineering or legal domains.

## Authoritative Sources

- AAOMS Parameters of Care 2023
- ADA CDT Manual / AMA CPT Manual / CMS ICD-10
- JOMS, IJOMS, OOO journals
- Peterson's Principles, Fonseca, Miloro textbooks
- FDA Device Classification Database
- ABOMS Certification Requirements

## Getting Started

```bash
git clone https://github.com/Yarmoluk/maxfac-course.git
cd maxfac-course
pip install -r requirements.txt
mkdocs serve
```

## License

(c) 2026 Daniel Yarmoluk. For authorized use only.
