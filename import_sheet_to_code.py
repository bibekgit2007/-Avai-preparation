"""
AVAI Preparation - Sheet to Code Importer
Converts questions from a Google Sheet URL or CSV/TSV file into permanent coded questions
in data/physics_questions.js, data/physics_for_you_master_questions.csv, and data/master_questions_copy_paste.tsv.
"""

import sys
import os
import re
import csv
import json
import urllib.request
import argparse

def extract_sheet_id(url):
    m = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
    if m:
        val = m.group(1)
        if val == 'e' or len(val) <= 5:
            return None
        return val
    return None

def fetch_google_sheet(url):
    sheet_id = extract_sheet_id(url)
    if not sheet_id:
        # Check if /d/e/ published link
        if '/d/e/' in url:
            pub_url = url.split('?')[0] + '?output=csv'
            req = urllib.request.Request(pub_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req) as resp:
                return resp.read().decode('utf-8')
        raise ValueError(f"Could not extract a valid Google Sheet ID from URL: {url}")

    gviz_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"
    req = urllib.request.Request(gviz_url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.read().decode('utf-8')
    except Exception as e:
        # Fallback to json endpoint
        json_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:json"
        req = urllib.request.Request(json_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode('utf-8')
            start = raw.find('{')
            end = raw.rfind('}')
            data = json.loads(raw[start:end+1])
            # Reconstruct CSV from gviz json table
            lines = []
            rows = data['table']['rows']
            for r in rows:
                row_vals = []
                for c in r.get('c', []):
                    v = c.get('v', '') if c else ''
                    row_vals.append(str(v) if v is not None else '')
                lines.append(','.join(f'"{v}"' for v in row_vals))
            return '\n'.join(lines)

def parse_sheet_content(csv_text):
    # Detect if single-column raw CSV
    reader = list(csv.reader(csv_text.splitlines()))
    if not reader:
        return []

    first_row = reader[0]
    if len(first_row) <= 1 and ',' in first_row[0]:
        # User pasted entire CSV into column A
        lines = [r[0] for r in reader if r]
        reader = list(csv.reader(lines))

    if not reader or len(reader) < 2:
        return []

    headers = [h.strip() for h in reader[0]]
    header_lower = [h.lower().replace(' ', '_').replace('-', '_') for h in headers]

    # Map column names
    col_map = {}
    for i, h in enumerate(header_lower):
        if any(k in h for k in ['question_id', 'id']): col_map['id'] = i
        elif any(k in h for k in ['exam', 'stream']): col_map['exam'] = i
        elif any(k in h for k in ['subject']): col_map['subject'] = i
        elif any(k in h for k in ['topic', 'chapter']): col_map['topic'] = i
        elif any(k in h for k in ['difficulty']): col_map['difficulty'] = i
        elif any(k in h for k in ['question_en', 'en_question', 'question']):
            if 'bn' not in h and 'id' not in h: col_map['en'] = i
        elif any(k in h for k in ['question_bn', 'bn_question']): col_map['bn'] = i
        elif any(k in h for k in ['opt1_en', 'opta_en', 'opt1']): 
            if 'bn' not in h: col_map['opt1_en'] = i
        elif any(k in h for k in ['opt2_en', 'optb_en', 'opt2']): 
            if 'bn' not in h: col_map['opt2_en'] = i
        elif any(k in h for k in ['opt3_en', 'optc_en', 'opt3']): 
            if 'bn' not in h: col_map['opt3_en'] = i
        elif any(k in h for k in ['opt4_en', 'optd_en', 'opt4']): 
            if 'bn' not in h: col_map['opt4_en'] = i
        elif any(k in h for k in ['opt1_bn', 'opta_bn']): col_map['opt1_bn'] = i
        elif any(k in h for k in ['opt2_bn', 'optb_bn']): col_map['opt2_bn'] = i
        elif any(k in h for k in ['opt3_bn', 'optc_bn']): col_map['opt3_bn'] = i
        elif any(k in h for k in ['opt4_bn', 'optd_bn']): col_map['opt4_bn'] = i
        elif any(k in h for k in ['correct', 'ans', 'answer']): col_map['correct'] = i
        elif any(k in h for k in ['expl_en', 'explanation_en', 'solution_en']): col_map['expl_en'] = i
        elif any(k in h for k in ['expl_bn', 'explanation_bn', 'solution_bn']): col_map['expl_bn'] = i

    parsed_questions = []
    for row_idx, row in enumerate(reader[1:], start=1):
        if not row or not any(row):
            continue

        def get_val(key, default=''):
            idx = col_map.get(key)
            if idx is not None and idx < len(row):
                return row[idx].strip()
            return default

        en_text = get_val('en')
        if not en_text:
            continue

        # Correct answer normalization (1-indexed 1..4 or A..D to 0..3)
        raw_ans = get_val('correct', '1').upper()
        if raw_ans in ['A', '1']: ans_idx = 0
        elif raw_ans in ['B', '2']: ans_idx = 1
        elif raw_ans in ['C', '3']: ans_idx = 2
        elif raw_ans in ['D', '4']: ans_idx = 3
        else:
            try:
                ans_idx = max(0, min(3, int(raw_ans) - 1))
            except:
                ans_idx = 0

        opt1_en = get_val('opt1_en', 'Option A')
        opt2_en = get_val('opt2_en', 'Option B')
        opt3_en = get_val('opt3_en', 'Option C')
        opt4_en = get_val('opt4_en', 'Option D')

        opt1_bn = get_val('opt1_bn', opt1_en)
        opt2_bn = get_val('opt2_bn', opt2_en)
        opt3_bn = get_val('opt3_bn', opt3_en)
        opt4_bn = get_val('opt4_bn', opt4_en)

        q_id = get_val('id', f"Q-{row_idx:03d}")
        subject = get_val('subject', 'Physics')
        topic = get_val('topic', 'General')
        exam = get_val('exam', 'NEET, JEE, WBJEE')
        difficulty = get_val('difficulty', 'Medium')
        bn_text = get_val('bn', en_text)
        expl_en = get_val('expl_en', 'Standard step-by-step solution.')
        expl_bn = get_val('expl_bn', expl_en)

        parsed_questions.append({
            "id": q_id,
            "exam": exam,
            "subject": subject,
            "topic": topic,
            "difficulty": difficulty,
            "en": en_text,
            "bn": bn_text,
            "opts": {
                "en": [opt1_en, opt2_en, opt3_en, opt4_en],
                "bn": [opt1_bn, opt2_bn, opt3_bn, opt4_bn]
            },
            "correct": ans_idx,
            "expl_en": expl_en,
            "expl_bn": expl_bn
        })

    return parsed_questions

def merge_and_export(new_questions, mode='append'):
    # Load existing questions from data/physics_questions.json
    existing_path = os.path.join("data", "physics_questions.json")
    existing_questions = []
    if os.path.exists(existing_path):
        with open(existing_path, "r", encoding="utf-8") as f:
            existing_questions = json.load(f)

    if mode == 'replace':
        final_questions = new_questions
    else:
        existing_ids = {q['id']: idx for idx, q in enumerate(existing_questions)}
        for nq in new_questions:
            if nq['id'] in existing_ids:
                # Update existing
                existing_questions[existing_ids[nq['id']]] = nq
            else:
                existing_questions.append(nq)
        final_questions = existing_questions

    # Export JS
    js_content = "window.PHYSICS_QUESTIONS_DATA = " + json.dumps(final_questions, indent=4, ensure_ascii=False) + ";\n"
    with open("data/physics_questions.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    # Export JSON
    with open("data/physics_questions.json", "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=4, ensure_ascii=False)

    # Export CSV
    csv_headers = [
        "Question_ID", "Exam", "Subject", "Topic", "Difficulty",
        "Question_EN", "Question_BN",
        "Opt1_EN", "Opt2_EN", "Opt3_EN", "Opt4_EN",
        "Opt1_BN", "Opt2_BN", "Opt3_BN", "Opt4_BN",
        "Correct_Answer", "Explanation_EN", "Explanation_BN"
    ]
    with open("data/physics_for_you_master_questions.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for q in final_questions:
            writer.writerow([
                q["id"], q["exam"], q["subject"], q["topic"], q["difficulty"],
                q["en"], q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"], q["expl_bn"]
            ])

    # Export TSV
    with open("data/master_questions_copy_paste.tsv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(csv_headers)
        for q in final_questions:
            writer.writerow([
                q["id"], q["exam"], q["subject"], q["topic"], q["difficulty"],
                q["en"], q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"], q["expl_bn"]
            ])

    print(f"[SUCCESS] Exported {len(final_questions)} coded questions to:")
    print("  - data/physics_questions.js (window.PHYSICS_QUESTIONS_DATA)")
    print("  - data/physics_questions.json")
    print("  - data/physics_for_you_master_questions.csv")
    print("  - data/master_questions_copy_paste.tsv")

def main():
    parser = argparse.ArgumentParser(description="Import Google Sheet questions into permanent coded questions.")
    parser.add_argument("--url", help="Google Sheet URL (Viewer or edit link)")
    parser.add_argument("--file", help="Local CSV/TSV file path")
    parser.add_argument("--mode", choices=['append', 'replace'], default='append', help="Merge mode (default: append/update)")

    args = parser.parse_args()

    if not args.url and not args.file:
        print("Usage: python import_sheet_to_code.py --url <google_sheet_url>")
        print("   or: python import_sheet_to_code.py --file <path_to_csv>")
        sys.exit(1)

    if args.url:
        print(f"[*] Fetching questions from Google Sheet: {args.url} ...")
        content = fetch_google_sheet(args.url)
    else:
        print(f"[*] Reading questions from local file: {args.file} ...")
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

    questions = parse_sheet_content(content)
    print(f"[OK] Parsed {len(questions)} questions.")

    if not questions:
        print("[ERROR] No valid questions found.")
        sys.exit(1)

    merge_and_export(questions, mode=args.mode)

if __name__ == "__main__":
    main()
