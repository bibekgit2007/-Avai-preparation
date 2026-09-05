import re
import json

def test_html():
    content = open("index.html", encoding="utf-8").read()
    
    # 1. Check required elements exist in DOM
    assert '<select id="examSelector"' in content, "Missing examSelector"
    assert '<select id="streamSelector"' in content, "Missing streamSelector"
    assert '<div class="flex items-center gap-1.5 overflow-x-auto no-scrollbar" id="subjectTabs">' in content or 'id="subjectTabs"' in content, "Missing subjectTabs"
    assert 'id="mockModal"' in content, "Missing mockModal"
    assert 'id="mockSubjectCheckboxes"' in content, "Missing mockSubjectCheckboxes"
    
    # 2. Extract main app script block (the largest inline script)
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    assert len(scripts) >= 1, "No script tag found"
    js_code = max(scripts, key=len)
    
    # 3. Check functions are defined
    required_funcs = [
        "function filterByExam()",
        "function switchStream(",
        "function switchSubject(",
        "function populateTopicFilter()",
        "function filterByTopic()",
        "function getFiltered()",
        "function render()",
        "function openMockModal()",
        "function closeMockModal()",
        "function setMockPreset(",
        "function startCustomMockTest()",
        "function showFinalResult()"
    ]
    for fn in required_funcs:
        assert fn in js_code, f"Missing function {fn} in index.html"
        
    # 4. Check EXAM_SUBJECT_COMBINATIONS exists and is structured
    assert "const EXAM_SUBJECT_COMBINATIONS = {" in js_code
    assert "'MHT-CET': [" in js_code
    assert "'WBJEE': [" in js_code
    assert "'UPSC': [" in js_code
    assert "'CUET': [" in js_code
    assert "'NDA': [" in js_code
    assert "'BITSAT': [" in js_code
    assert "'IIT-JAM': [" in js_code
    
    # 5. Check bracket matching for the main script block
    lines = js_code.splitlines()
    raw_bal = 0
    for line in lines:
        clean = re.sub(r'//.*', '', line)
        raw_bal += clean.count('{') - clean.count('}')
    
    assert raw_bal == 0, f"Unbalanced curly braces in script: net balance is {raw_bal}"
    print("[PASSED] HTML structure, stream selectors, required JS functions, and brace balancing verified!")

if __name__ == "__main__":
    test_html()
