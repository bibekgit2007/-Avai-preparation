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
    assert 'id="examDropdownTrigger"' in content, "Missing examDropdownTrigger in DOM"
    assert 'id="examDropdownMenu"' in content, "Missing examDropdownMenu in DOM"
    assert 'id="examSearchInput"' in content, "Missing examSearchInput in DOM"
    assert 'id="examCategoryChips"' in content, "Missing examCategoryChips in DOM"
    assert 'id="examCardsContainer"' in content, "Missing examCardsContainer in DOM"
    assert 'id="upperRowCategoryNav"' in content, "Missing upperRowCategoryNav in DOM"
    assert 'id="examMegaMenu"' in content, "Missing examMegaMenu in DOM"
    assert 'id="notesStudioModal"' in content, "Missing notesStudioModal in DOM"
    assert 'id="notesStudioBtn"' in content, "Missing notesStudioBtn in DOM"
    assert 'id="notesTextInput"' in content, "Missing notesTextInput in DOM"
    assert 'id="ntaLiveRadarStrip"' in content, "Missing ntaLiveRadarStrip in DOM"
    assert 'id="ntaInstructionsModal"' in content, "Missing ntaInstructionsModal in DOM"
    assert 'id="mockRecoveryModal"' in content, "Missing mockRecoveryModal in DOM"
    assert 'id="recoverProgressText"' in content, "Missing recoverProgressText in DOM"
    assert 'id="notesOcrProgress"' in content, "Missing notesOcrProgress in DOM"
    assert 'id="mistakeNotebookModal"' in content, "Missing mistakeNotebookModal in DOM"
    assert 'id="mistakeNotebookBtn"' in content, "Missing mistakeNotebookBtn in DOM"
    assert 'id="mistakeCountBadge"' in content, "Missing mistakeCountBadge in DOM"
    assert 'id="flagMistakeBtn"' in content, "Missing flagMistakeBtn in DOM"
    assert 'id="mistakeKpiTotal"' in content, "Missing mistakeKpiTotal in DOM"
    assert 'id="mistakeKpiPending"' in content, "Missing mistakeKpiPending in DOM"
    assert 'id="mistakeKpiMastered"' in content, "Missing mistakeKpiMastered in DOM"
    assert 'id="mistakeKpiAvgTime"' in content, "Missing mistakeKpiAvgTime in DOM"
    assert 'id="mistakeNotebookList"' in content, "Missing mistakeNotebookList in DOM"
    assert 'id="startMistakeTestBtn"' in content, "Missing startMistakeTestBtn in DOM"
    assert 'id="ncertModal"' in content, "Missing ncertModal in DOM"
    assert 'id="ncertModalContent"' in content, "Missing ncertModalContent in DOM"
    assert 'id="ncertPracticeChapterBtn"' in content, "Missing ncertPracticeChapterBtn in DOM"
    assert 'id="ntaOfficialHeader"' in content, "Missing ntaOfficialHeader in DOM"
    assert 'id="ntaCBTModeBtn"' in content, "Missing ntaCBTModeBtn in DOM"
    assert 'id="ntaOfficialTimer"' in content, "Missing ntaOfficialTimer in DOM"
    assert 'id="ntaSectionTabs"' in content, "Missing ntaSectionTabs in DOM"
    assert 'id="ntaPaperViewModal"' in content, "Missing ntaPaperViewModal in DOM"
    assert 'id="ntaPaperViewContent"' in content, "Missing ntaPaperViewContent in DOM"
    assert 'id="countAnsweredMarked"' in content, "Missing countAnsweredMarked in DOM"
    assert 'id="diagnosticAnalyticsModal"' in content, "Missing diagnosticAnalyticsModal in DOM"
    assert 'id="diagnosticAnalyticsBtn"' in content, "Missing diagnosticAnalyticsBtn in DOM"
    assert 'id="diagEriValue"' in content, "Missing diagEriValue in DOM"
    assert 'id="diagEriRing"' in content, "Missing diagEriRing in DOM"
    assert 'id="diagEriTierBadge"' in content, "Missing diagEriTierBadge in DOM"
    assert 'id="diagMarksBleed"' in content, "Missing diagMarksBleed in DOM"
    assert 'id="diagPotentialScoreText"' in content, "Missing diagPotentialScoreText in DOM"
    assert 'id="diagAvgSpeed"' in content, "Missing diagAvgSpeed in DOM"
    assert 'id="diagQuadrantGrid"' in content, "Missing diagQuadrantGrid in DOM"
    assert 'id="diagDifficultyGrid"' in content, "Missing diagDifficultyGrid in DOM"
    assert 'id="diagChapterHeatmap"' in content, "Missing diagChapterHeatmap in DOM"
    assert 'id="diagAiDirectives"' in content, "Missing diagAiDirectives in DOM"
    
    assert 'STIX+Two+Text' in content, "Missing STIX Two Text Google Font"
    assert 'katex.min.css' in content, "Missing KaTeX stylesheet inclusion"
    assert '.redox-badge' in content, "Missing .redox-badge CSS in stylesheet"
    assert '.reaction-arrow' in content, "Missing .reaction-arrow CSS in stylesheet"
    assert '.math-vec' in content, "Missing .math-vec CSS in stylesheet"
    assert '.math-hat' in content, "Missing .math-hat CSS in stylesheet"
    assert '.nav-caret' in content, "Missing .nav-caret in stylesheet"
    assert '.rotate-180' in content, "Missing .rotate-180 in stylesheet"
    assert '.upper-row-btn' in content, "Missing .upper-row-btn in stylesheet"
    assert '#examMegaMenu' in content, "Missing #examMegaMenu in stylesheet"
    assert '.nta-answered' in content, "Missing .nta-answered in stylesheet"
    assert '.nta-not-answered' in content, "Missing .nta-not-answered in stylesheet"
    assert '.nta-not-visited' in content, "Missing .nta-not-visited in stylesheet"
    assert '.nta-marked' in content, "Missing .nta-marked in stylesheet"
    assert '.nta-marked-answered' in content, "Missing .nta-marked-answered in stylesheet"
    
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
        "function filterDrawerByNTA(",
        "function renderChapterDirectoryDrawer()",
        "function toggleExamDropdown(",
        "function handleExamDropdownSearch(",
        "function filterExamDropdownCategory(",
        "function renderExamDropdownList()",
        "function selectExamFromDropdown(",
        "function updateExamDropdownUI(",
        "function openExamMegaMenu(",
        "function closeExamMegaMenu()",
        "function renderExamMegaMenuContent(",
        "function selectFromMegaMenu(",
        "function openNotesStudioModal()",
        "function closeNotesStudioModal()",
        "function switchNotesStudioTab(",
        "function loadSampleNotes()",
        "function handleNotesFileUpload(",
        "function processUploadedNotesFile(",
        "function ensurePDFJsLoaded()",
        "function ensureTesseractLoaded()",
        "function extractQuestionsFromNotes(",
        "function generateAndStartNotesTest()",
        "function renderSavedNotesTests()",
        "function loadSavedNotesTest(",
        "function deleteSavedNotesTest(",
        "function exportSavedNotesTest(",
        "function openNTAInstructionsModal()",
        "function closeNTAInstructionsModal()",
        "function switchNTATab(",
        "function saveActiveMockSession()",
        "function clearActiveMockSession()",
        "function checkForResumableMockSession()",
        "function resumeMockSession()",
        "function discardMockSession()",
        "function getMistakeNotebook()",
        "function saveMistakeNotebook(",
        "function updateMistakeBadgeCount()",
        "function isQuestionInMistakeNotebook(",
        "function recordMistake(",
        "function markMistakeMastered(",
        "function toggleMistakeFlagForCurrentQ()",
        "function updateCurrentQMistakeFlagUI()",
        "function openMistakeNotebookModal()",
        "function closeMistakeNotebookModal()",
        "function filterMistakeSubject(",
        "function renderMistakeNotebook()",
        "function toggleMasteredMistake(",
        "function deleteMistake(",
        "function clearMasteredMistakes()",
        "function practiceSingleMistake(",
        "function startMistakeReTest()",
        "function getQuestionPeerBenchmark(",
        "function getQuestionNCERTReference(",
        "function getPaceAnalysis(",
        "function openNCERTModalForCurrentQ()",
        "function closeNCERTModal()",
        "function practiceNCERTChapterFromModal()",
        "function isNTACBTModeActive()",
        "function toggleNTACBTMode()",
        "function initNTACBTModeOnLoad()",
        "function renderNTASectionTabs()",
        "function updateNTATimerDisplay()",
        "function openNTAPaperViewModal()",
        "function closeNTAPaperViewModal()",
        "function openDiagnosticAnalyticsModal()",
        "function closeDiagnosticAnalyticsModal()",
        "function computeDiagnosticMetrics()",
        "function renderDiagnosticAnalytics()",
        "function practiceChapterFromAnalytics("
    ]
    for fn in required_funcs:
        assert fn in js_code, f"Missing function {fn} in index.html"
        
    # 4. Check EXAM_SUBJECT_COMBINATIONS and EXAM_DIRECTORY
    assert "const EXAM_DIRECTORY = [" in js_code, "Missing EXAM_DIRECTORY in script"
    assert "const EXAMSIDE_MEGA_CATEGORIES = {" in js_code, "Missing EXAMSIDE_MEGA_CATEGORIES in script"
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
