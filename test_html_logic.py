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
    assert '<script src="data/syllabus.js' in content, "Missing syllabus.js script inclusion"
    assert 'id="chapterNavStrip"' in content, "Missing chapterNavStrip in DOM"
    assert 'id="unitSelector"' in content, "Missing unitSelector in DOM"
    assert 'id="chapterPillsContainer"' in content, "Missing chapterPillsContainer in DOM"
    assert 'id="chapterDirectoryDrawer"' in content, "Missing chapterDirectoryDrawer in DOM"
    assert 'id="drawerSearchInput"' in content, "Missing drawerSearchInput in DOM"
    assert 'id="drawerContentList"' in content, "Missing drawerContentList in DOM"
    
    assert 'STIX+Two+Text' in content, "Missing STIX Two Text Google Font"
    assert 'katex.min.css' in content, "Missing KaTeX stylesheet inclusion"
    assert '.redox-badge' in content, "Missing .redox-badge CSS in stylesheet"
    assert '.reaction-arrow' in content, "Missing .reaction-arrow CSS in stylesheet"
    
    # 2. Extract main app script block (the largest inline script)
    scripts = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
    assert len(scripts) >= 1, "No script tag found"
    js_code = max(scripts, key=len)
    
    # 3. Check functions are defined
    required_funcs = [
        "function formatScienceAndMath(",
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
        "function showFinalResult()",
        "function renderChapterNavStrip()",
        "function scrollChapterPills(",
        "function filterByChapter(",
        "function filterByUnit(",
        "function toggleChapterDirectoryDrawer(",
        "function handleDrawerSearch(",
        "function renderChapterDirectoryDrawer()"
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

    # 6. Check syllabus.js structure and sub-chapters
    syl_content = open("data/syllabus.js", encoding="utf-8").read()
    assert "window.AVAI_SYLLABUS = " in syl_content
    assert "EXAM_SYLLABUS_REGISTRY = {" in syl_content
    assert "BIO_UNIT_04" in syl_content, "Missing Plant Physiology unit"
    assert "BIO_CH_11" in syl_content, "Missing Photosynthesis sub-chapter"
    assert "BIO_CH_12" in syl_content, "Missing Respiration sub-chapter"
    assert "BIO_CH_13" in syl_content, "Missing Plant Growth sub-chapter"
    assert "BIO_UNIT_05" in syl_content, "Missing Human Physiology unit"
    assert "BIO_CH_16" in syl_content, "Missing Breathing sub-chapter"
    assert "BIO_CH_17" in syl_content, "Missing Circulation sub-chapter"
    assert "BIO_CH_18" in syl_content, "Missing Excretion sub-chapter"
    assert "BIO_CH_19" in syl_content, "Missing Locomotion sub-chapter"
    assert "BIO_CH_20" in syl_content, "Missing Neural sub-chapter"
    assert "BIO_CH_21" in syl_content, "Missing Chemical Coordination sub-chapter"
    assert "getExamSyllabus" in syl_content
    assert "mapQuestionToSyllabus" in syl_content
    assert "getChapterQuestionStats" in syl_content
    print("[PASSED] HTML structure, chapter navigation strip, directory drawer, syllabus sub-chapters & JS logic verified!")

if __name__ == "__main__":
    test_html()
