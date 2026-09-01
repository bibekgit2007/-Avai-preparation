# 🎯 AVAI Preparation — Premier Multi-Subject Online Mock Examination & PYQ Portal

[![Live App](https://img.shields.io/badge/Live%20Portal-Online-blue?style=for-the-badge&logo=vercel)](https://avai-prep.vercel.app)
[![PWA Ready](https://img.shields.io/badge/PWA-Offline%20Ready-emerald?style=for-the-badge&logo=pwa)](https://bibekgit2007.github.io/-Avai-preparation/)
[![Exams](https://img.shields.io/badge/Exams-NEET%20%7C%20JEE%20%7C%20WBJEE%20%7C%20UPSC%20%7C%20SSC%20%7C%20CUET%20%7C%20NDA-purple?style=for-the-badge)](https://avai-prep.vercel.app)
[![Languages](https://img.shields.io/badge/Bilingual-English%20%26%20বাংলা-amber?style=for-the-badge)](https://avai-prep.vercel.app)

**AVAI Preparation** (`AVAI_PREP`) is a cutting-edge, responsive, and feature-rich online mock test and examination portal tailored for Indian competitive exams (**NEET, JEE Main, WBJEE, UPSC Civil Services, SSC CGL/CHSL, CUET, and NDA**).

Equipped with real-time **Google Sheet live sync**, intelligent **PYQ year recognition**, **per-question stopwatch timing**, and a built-in **floating scientific calculator**, AVAI Prep delivers a full-fledged NTA/CBT test simulation directly in your browser.

---

## 🌟 Key Features

### 1. 📚 Multi-Subject & Multi-Exam Question Bank
- Comprehensive subject coverage:
  - **Physics** (Mechanics, Electromagnetism, Modern Physics, Optics, Thermodynamics)
  - **Chemistry** (Physical, Organic, Inorganic & Coordination Chemistry)
  - **Biology** (Cell Biology, Genetics, Physiology, Ecology, Botany, Zoology)
  - **Mathematics** (Calculus, Algebra, Coordinate Geometry, Matrices & Determinants)
  - **General Knowledge & Current Affairs**
  - **General Science**
  - **History & Indian Polity**
  - **Geography**
  - **Reasoning & Aptitude**
  - **English Language**
- Dynamic exam filtering for **NEET**, **JEE Main**, **WBJEE**, **UPSC**, **SSC**, **CUET**, and **NDA**.

---

### 2. ⏱️ Dual Timer & Live Per-Question Stopwatch
- **Overall Test Countdown Timer**: Displays remaining time with visual urgency indicators (warning yellow under 30 mins, pulsing red under 10 mins).
- **Live Per-Question Stopwatch (`⏱️ 00:00`)**: Real-time timer on each question card recording exact seconds spent per question.
- **Pace Analytics**: Average speed per question (`Avg Speed: 00:45 / Q`) and subject-wise time breakdowns in final reports.

---

### 3. 🎯 Intelligent PYQ Recognition & Year Badges
- Auto-detects Previous Year Questions (PYQs) from the database or question text (e.g. `2024`, `2023`, `2022`).
- Displays jewel-toned glowing badges:
  - `🎯 NEET 2024 PYQ`
  - `🎯 JEE 2023 PYQ`
  - `🎯 UPSC 2024 PYQ`
  - `🎯 WBJEE 2023 PYQ`

---

### 4. 📊 NTA-Standard CBT Question Palette
- Color-coded candidate status indicator:
  - 🟢 **Answered**
  - 🔴 **Not Answered**
  - 🟣 **Marked for Review**
  - 🟣🟢 **Answered & Marked for Review**
  - ⚪ **Not Visited**
- Instant question jumping with mobile drawer support.

---

### 5. 🌐 Instant Bilingual Toggle (English & বাংলা)
- Seamless one-click toggle between **English** and **বাংলা** for:
  - Question Prompts
  - Multiple-Choice Options
  - Step-by-step Solution Derivations & Explanations

---

### 6. ✦ Built-In Floating Scientific Calculator
- Draggable and side-dockable luxury scientific calculator accessible directly inside the exam interface.
- Complete trigonometry (`sin`, `cos`, `tan`), logarithms (`ln`, `log`), roots, powers, factorials, memory registers (`M+`, `M-`, `MR`), and unit converters.
- Toggle anytime with keyboard shortcut <kbd>C</kbd> or the floating action button.

---

### 7. 🔄 Real-Time Google Sheet & File Sync
- **Live Cloud Sync**: Connect any Google Sheet (Viewer link) for real-time question bank updates without modifying application code.
- **Direct File Uploader**: Drag and drop `.csv`, `.tsv`, or `.json` question bank files.
- **Zero-Risk Permissions**: Works safely with read-only viewer links.

---

### 8. 📈 Comprehensive Scorecard & Analytics
- Automated scoring with customizable negative marking presets:
  - **NEET / JEE**: `+4` Correct / `-1` Wrong
  - **UPSC**: `+2` Correct / `-0.66` Wrong
  - **SSC**: `+2` Correct / `-0.50` Wrong
  - **Custom / Zero Negative Marking**
- Detailed metrics for Final Score, Accuracy %, Subject-wise Progress, Time Spent per Subject, and Full Solution Review.

---

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
| :--- | :--- |
| <kbd>1</kbd> / <kbd>2</kbd> / <kbd>3</kbd> / <kbd>4</kbd> | Select Option A, B, C, or D |
| <kbd>→</kbd> or <kbd>Enter</kbd> | Save Answer & Move to Next Question |
| <kbd>←</kbd> | Previous Question |
| <kbd>S</kbd> | Toggle Step-by-Step Solution & Derivation |
| <kbd>M</kbd> | Mark / Unmark for Review |
| <kbd>C</kbd> | Toggle Floating Scientific Calculator |
| <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>A</kbd> | Open Admin Question Bank Sync Center |

---

## 📋 Google Sheet / CSV Question Schema

To add your own questions via Google Sheets or CSV, use the following column headers:

| Column Header | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `Exam` | Text | Target examination | `NEET`, `JEE`, `WBJEE`, `UPSC`, `SSC` |
| `Subject` | Text | Primary subject | `Physics`, `Chemistry`, `Biology`, `Mathematics` |
| `Topic` | Text | Chapter or topic name | `Units and Measurement`, `Kinematics` |
| `Difficulty` | Text | Difficulty pill | `Easy`, `Medium`, `Hard` |
| `Year` | Text / Num | PYQ exam year | `2024`, `2023`, `2022` |
| `Question_EN` | Text | Question in English | *What is the least count...?* |
| `Question_BN` | Text | Question in Bengali | *ভার্নিয়ার ধ্রুবক কত?* |
| `Opt1_EN` - `Opt4_EN` | Text | Options A, B, C, D in English | `0.02 cm`, `0.01 cm`, `0.2 mm`, `0.02 mm` |
| `Opt1_BN` - `Opt4_BN` | Text | Options A, B, C, D in Bengali | `০.০২ সেমি`, `০.০১ সেমি`, `০.২ মিমি` |
| `Correct` | Num / Char | Correct option index (1-4 or A-D) | `1` or `A` |
| `Expl_EN` | Text | Detailed solution in English | *LC = 1 MSD - 1 VSD...* |
| `Expl_BN` | Text | Detailed solution in Bengali | *ধাপ ভিত্তিক বিস্তারিত ব্যাখ্যা...* |

---

## 🚀 Quick Start & Local Development

### 1. Clone the repository
```bash
git clone https://github.com/bibekgit2007/-Avai-preparation.git
cd -Avai-preparation
```

### 2. Run locally
You can open `index.html` directly in any web browser or use a local static server:

```bash
# Using Python
python -m http.server 8080

# Or using Node.js
npx serve .
```

Open `http://localhost:8080` in your browser.

---

## 📱 Progressive Web App (PWA) & Offline Access

AVAI Preparation is configured with service worker caching (`sw.js` and `manifest.json`). You can install it on **Android**, **iOS**, **Windows**, or **macOS** as a standalone application:
1. Open the portal in Chrome, Edge, or Safari.
2. Click **"Install App"** or **"Add to Home Screen"**.
3. Practice mock tests anywhere, even without an internet connection!

---

## 📄 License & Credits

Developed with ❤️ for aspirants preparing for competitive examinations across India.
© 2026 AVAI Preparation. All rights reserved.
