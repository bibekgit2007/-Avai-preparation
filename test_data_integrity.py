import json
import csv
import xml.etree.ElementTree as ET

def test_data():
    print("=== STARTING DATA INTEGRITY & SYNCHRONIZATION AUDIT ===")
    
    # 1. Test physics_questions.js
    with open("data/physics_questions.js", "r", encoding="utf-8") as f:
        js_content = f.read()
    assert js_content.startswith("window.PHYSICS_QUESTIONS_DATA = "), "Invalid JS header"
    json_str = js_content.replace("window.PHYSICS_QUESTIONS_DATA = ", "").rstrip(";\n ")
    questions = json.loads(json_str)
    print(f"[PASSED] physics_questions.js is valid JSON with {len(questions)} questions.")

    # 2. Check each question structure
    ids = set()
    subjects = set()
    diagram_count = 0
    for idx, q in enumerate(questions):
        # Check required fields
        for field in ["id", "exam", "subject", "topic", "difficulty", "en", "bn", "opts", "correct", "expl_en", "expl_bn"]:
            assert field in q, f"Missing {field} in question {idx}"
        
        assert q["id"] not in ids, f"Duplicate ID {q['id']}"
        ids.add(q["id"])
        subjects.add(q["subject"])

        # Check options
        assert len(q["opts"]["en"]) == 4, f"Question {q['id']} EN options length != 4"
        assert len(q["opts"]["bn"]) == 4, f"Question {q['id']} BN options length != 4"
        assert 0 <= q["correct"] < 4, f"Question {q['id']} correct key out of range: {q['correct']}"

        # Check diagram if present
        if q.get("diagram"):
            diagram_count += 1
            # Check valid XML/SVG
            try:
                ET.fromstring(q["diagram"])
            except Exception as e:
                raise AssertionError(f"Invalid SVG in question {q['id']}: {e}")

    print(f"[PASSED] All {len(questions)} questions have verified keys, bilingual parity, and valid options.")
    print(f"[INFO] Subjects present: {sorted(list(subjects))}")
    print(f"[INFO] Questions with verified vector SVG diagrams/circuits/flows: {diagram_count}")

    # 3. Test CSV format
    with open("data/physics_for_you_master_questions.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        csv_rows = list(reader)
    assert len(csv_rows) == len(questions) + 1, f"CSV row count mismatch: {len(csv_rows)} vs {len(questions)+1}"
    print(f"[PASSED] CSV file verified ({len(csv_rows)-1} data rows + 1 header).")

    # 4. Test TSV format
    with open("data/master_questions_copy_paste.tsv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        tsv_rows = list(reader)
    assert len(tsv_rows) == len(questions) + 1, f"TSV row count mismatch: {len(tsv_rows)} vs {len(questions)+1}"
    print(f"[PASSED] Google Sheets TSV verified ({len(tsv_rows)-1} data rows + 1 header).")

    print("=== ALL INTEGRITY TESTS PASSED SUCCESSFULLY! ===")

if __name__ == "__main__":
    test_data()
