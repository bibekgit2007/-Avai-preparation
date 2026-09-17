"""
Master Dataset Builder for AVAI Preparation Platform
Compiles 322 high-yield, authentic bilingual questions across Physics, Chemistry, Biology, Mathematics, and General Studies.
Synchronizes across:
  - data/physics_questions.js (window.PHYSICS_QUESTIONS_DATA)
  - data/physics_for_you_master_questions.csv
  - data/master_questions_copy_paste.tsv
"""

import json
import csv
import os
import sys

# Import SVG definitions from bank modules for backward compatibility
from data.bank.physics import (
    physics_questions,
    SVG_SCREW_GAUGE, SVG_LCR_CIRCUIT, SVG_MECHANICAL_EQUILIBRIUM,
    SVG_SPHERE_CAVITY, SVG_PRISM_TIR, SVG_WHEATSTONE_BRIDGE,
    SVG_CARNOT_CYCLE, SVG_TWO_CONDUCTORS_SERIES, SVG_COIL_MAGNETIC_MOMENT
)
from data.bank.chemistry import (
    chemistry_questions,
    SVG_CHEM_REACTION_FLOW, SVG_CFT_SPLITTING,
    SVG_ARRHENIUS_PLOT, SVG_CANNIZZARO_FLOW
)
from data.bank.biology import (
    biology_questions,
    SVG_ANTIBODY_STRUCTURE, SVG_IMMUNE_RESPONSE,
    SVG_LAC_OPERON, SVG_KRANZ_ANATOMY,
    SVG_SARCOMERE_STRUCTURE, SVG_GEL_ELECTROPHORESIS,
    SVG_HORMONAL_CYCLE
)
from data.bank.math import (
    math_questions,
    SVG_CONIC_COMMON_TANGENT, SVG_PARABOLAS_AREA, SVG_SKEW_LINES
)
from data.bank.general import general_questions

# Aggregate all modular question banks
all_questions = (
    physics_questions +
    chemistry_questions +
    biology_questions +
    math_questions +
    general_questions
)

def export_all():
    os.makedirs("data", exist_ok=True)
    
    # 1. Export data/physics_questions.js and data/physics_questions.json
    js_content = "window.PHYSICS_QUESTIONS_DATA = " + json.dumps(all_questions, indent=4, ensure_ascii=False) + ";\n"
    with open("data/physics_questions.js", "w", encoding="utf-8") as f:
        f.write(js_content)
    with open("data/physics_questions.json", "w", encoding="utf-8") as f:
        json.dump(all_questions, f, indent=4, ensure_ascii=False)
    print(f"[OK] Exported {len(all_questions)} questions to data/physics_questions.js and data/physics_questions.json")

    # 2. Export data/physics_for_you_master_questions.csv
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
        for q in all_questions:
            writer.writerow([
                q["id"],
                q["exam"],
                q["subject"],
                q["topic"],
                q["difficulty"],
                q["en"],
                q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"],
                q["expl_bn"]
            ])
    print(f"[OK] Exported {len(all_questions)} questions to data/physics_for_you_master_questions.csv")

    # 3. Export data/master_questions_copy_paste.tsv
    with open("data/master_questions_copy_paste.tsv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(csv_headers)
        for q in all_questions:
            writer.writerow([
                q["id"],
                q["exam"],
                q["subject"],
                q["topic"],
                q["difficulty"],
                q["en"],
                q["bn"],
                q["opts"]["en"][0], q["opts"]["en"][1], q["opts"]["en"][2], q["opts"]["en"][3],
                q["opts"]["bn"][0], q["opts"]["bn"][1], q["opts"]["bn"][2], q["opts"]["bn"][3],
                q["correct"] + 1,
                q["expl_en"],
                q["expl_bn"]
            ])
    print(f"[OK] Exported {len(all_questions)} questions to data/master_questions_copy_paste.tsv")

if __name__ == "__main__":
    export_all()
