# Project Instructions & Agent Guidelines

## 1. Storage & PDF Processing Rules (CRITICAL)
- **Do NOT Save PDF Images to Disk**: Never dump or render PDF pages as `.png`, `.jpg`, or other raster images to the project filesystem.
- **Immediate Cleanup Obligation**: If any temporary image is ever generated for inspection or OCR, it MUST be kept in memory (`io.BytesIO`) or deleted immediately upon completion of the task. Never leave directories like `scratch_pages/` or scratch render files behind.
- **Prefer In-Memory Text Extraction**: Use direct text and layer extraction (`fitz` / PyMuPDF `page.get_text()`, stream parsers) to extract questions, options, and solutions directly into memory.

## 2. Diagram & Illustration Standards
- **Vector SVGs Only**: When a question requires a circuit diagram, ray optics diagram, chemical reaction flow, or biological pathway, craft lightweight, responsive **inline vector SVGs** (`<svg>...</svg>`).
- **Zero Raster Asset Bloat**: Never use `.png` or `.jpg` raster screenshots for diagrams. SVGs ensure crisp scaling on mobile and desktop while remaining under 2 KB each.

## 3. Question Bank Synchronization & Bilingual Parity
- All questions must be synchronized across:
  - `data/physics_questions.js` (`window.PHYSICS_QUESTIONS_DATA`)
  - `data/physics_for_you_master_questions.csv`
  - `data/master_questions_copy_paste.tsv`
- Maintain 100% dual-language parity with accurate, authentic English (`en`) and Bengali (`bn`) translations for questions, options, and step-by-step explanations.
- Tag authentic target exams and streams without inventing historical PYQ years.
