/**
 * GLAMOUR CALCULATOR ENGINE
 * Complete Standard, Scientific, Memory, Unit Converter, and Audio Synthesizer
 */

// State Object
const CalcState = {
    expression: '',
    tape: '',
    result: null,
    memory: 0,
    angleMode: 'DEG', // 'DEG' or 'RAD'
    theme: localStorage.getItem('glamour_calc_theme') || 'midnight',
    soundEnabled: localStorage.getItem('glamour_calc_sound') !== 'false',
    history: JSON.parse(localStorage.getItem('glamour_calc_history') || '[]'),
    activeMode: 'standard' // 'standard', 'scientific', 'converter'
};

// DOM Elements
const DOM = {
    body: document.body,
    appContainer: document.getElementById('appContainer'),
    displayTape: document.getElementById('displayTape'),
    displayMain: document.getElementById('displayMain'),
    displayPreview: document.getElementById('displayPreview'),
    angleBadge: document.getElementById('angleBadge'),
    memIndicator: document.getElementById('memIndicator'),
    scientificGrid: document.getElementById('scientificGrid'),
    converterPanel: document.getElementById('converterPanel'),
    standardGrid: document.getElementById('standardGrid'),
    historyDrawer: document.getElementById('historyDrawer'),
    historyList: document.getElementById('historyList'),
    historyToggleBtn: document.getElementById('historyToggleBtn'),
    themeToggleBtn: document.getElementById('themeToggleBtn'),
    themeDropdown: document.getElementById('themeDropdown'),
    soundToggleBtn: document.getElementById('soundToggleBtn'),
    tabStandard: document.getElementById('tabStandard'),
    tabScientific: document.getElementById('tabScientific'),
    tabConverter: document.getElementById('tabConverter'),
    // Converter inputs
    convType: document.getElementById('convType'),
    convUnitFrom: document.getElementById('convUnitFrom'),
    convUnitTo: document.getElementById('convUnitTo'),
    convInputFrom: document.getElementById('convInputFrom'),
    convInputTo: document.getElementById('convInputTo')
};

// ==========================================================================
// WEB AUDIO API SOUND SYNTHESIZER (No external audio files required)
// ==========================================================================
class SoundSynth {
    constructor() {
        this.ctx = null;
    }

    init() {
        if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            this.ctx = new AudioCtx();
        }
    }

    playClick(freq = 600, duration = 0.035, type = 'sine') {
        if (!CalcState.soundEnabled) return;
        try {
            this.init();
            if (this.ctx.state === 'suspended') {
                this.ctx.resume();
            }
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = type;
            osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
            osc.frequency.exponentialRampToValueAtTime(freq * 0.4, this.ctx.currentTime + duration);

            gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);

            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start();
            osc.stop(this.ctx.currentTime + duration);
        } catch (e) {
            // Audio context might be restricted before user gesture
        }
    }

    playSuccess() {
        if (!CalcState.soundEnabled) return;
        try {
            this.init();
            if (this.ctx.state === 'suspended') this.ctx.resume();
            
            const now = this.ctx.currentTime;
            [523.25, 659.25, 783.99].forEach((freq, idx) => {
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.value = freq;
                gain.gain.setValueAtTime(0.04, now + idx * 0.04);
                gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.04 + 0.12);
                osc.connect(gain);
                gain.connect(this.ctx.destination);
                osc.start(now + idx * 0.04);
                osc.stop(now + idx * 0.04 + 0.12);
            });
        } catch(e) {}
    }

    playSpecial() {
        this.playClick(900, 0.045, 'triangle');
    }
}

const AudioPlayer = new SoundSynth();

// ==========================================================================
// CALCULATOR CORE ENGINE
// ==========================================================================

function updateDisplay() {
    // Format Display Main
    if (CalcState.expression === '') {
        DOM.displayMain.innerText = '0';
    } else {
        // Pretty format operators for view
        const prettyExpr = CalcState.expression
            .replace(/\*/g, ' × ')
            .replace(/\//g, ' ÷ ')
            .replace(/\+/g, ' + ')
            .replace(/(?<!\d)-(?!\d)/g, '-')
            .replace(/(?<=\d)-(?=\d)/g, ' - ')
            .replace(/\^/g, ' ^ ');
        DOM.displayMain.innerText = prettyExpr;
    }

    // Auto resize text if long
    if (DOM.displayMain.innerText.length > 14) {
        DOM.displayMain.style.fontSize = '26px';
    } else if (DOM.displayMain.innerText.length > 9) {
        DOM.displayMain.style.fontSize = '34px';
    } else {
        DOM.displayMain.style.fontSize = '42px';
    }

    // Live preview
    if (CalcState.expression && !isOperator(CalcState.expression.slice(-1))) {
        try {
            const val = evaluateExpression(CalcState.expression);
            if (val !== null && !isNaN(val) && isFinite(val) && String(val) !== CalcState.expression) {
                DOM.displayPreview.innerText = `= ${formatNumber(val)}`;
            } else {
                DOM.displayPreview.innerText = '';
            }
        } catch (e) {
            DOM.displayPreview.innerText = '';
        }
    } else {
        DOM.displayPreview.innerText = '';
    }

    // Memory Indicator
    if (CalcState.memory !== 0) {
        DOM.memIndicator.classList.add('active');
    } else {
        DOM.memIndicator.classList.remove('active');
    }
}

function appendValue(val) {
    AudioPlayer.playClick(500 + Math.random() * 80);
    
    // Clear if previous calculation just completed and user starts entering a new number
    if (CalcState.result !== null && !isOperator(val) && !isFunctionSymbol(val)) {
        CalcState.expression = '';
        CalcState.result = null;
    } else if (CalcState.result !== null && (isOperator(val) || isFunctionSymbol(val))) {
        CalcState.result = null;
    }

    // Prevent consecutive invalid operators
    const lastChar = CalcState.expression.slice(-1);
    if (isOperator(val)) {
        if (CalcState.expression === '' && val !== '-') return;
        if (isOperator(lastChar)) {
            CalcState.expression = CalcState.expression.slice(0, -1) + val;
            updateDisplay();
            return;
        }
    }

    // Decimal point handling
    if (val === '.') {
        const parts = CalcState.expression.split(/[\+\-\*\/\^\(\)]/);
        const lastPart = parts[parts.length - 1];
        if (lastPart.includes('.')) return;
        if (lastPart === '') val = '0.';
    }

    CalcState.expression += val;
    updateDisplay();
}

function appendFunction(fnName) {
    AudioPlayer.playSpecial();
    if (CalcState.result !== null) {
        CalcState.result = null;
    }

    switch (fnName) {
        case 'sin':
        case 'cos':
        case 'tan':
        case 'asin':
        case 'acos':
        case 'atan':
        case 'log':
        case 'ln':
        case 'sqrt':
            CalcState.expression += `${fnName}(`;
            break;
        case 'sqr':
            CalcState.expression += '^2';
            break;
        case 'cube':
            CalcState.expression += '^3';
            break;
        case 'power':
            CalcState.expression += '^';
            break;
        case 'fact':
            CalcState.expression += '!';
            break;
        case 'inv':
            if (CalcState.expression) {
                CalcState.expression = `(1/(${CalcState.expression}))`;
            }
            break;
        case 'abs':
            CalcState.expression += 'abs(';
            break;
        case 'pi':
            CalcState.expression += 'π';
            break;
        case 'e':
            CalcState.expression += 'e';
            break;
        default:
            break;
    }
    updateDisplay();
}

function clearAll() {
    AudioPlayer.playSpecial();
    CalcState.expression = '';
    CalcState.tape = '';
    CalcState.result = null;
    DOM.displayTape.innerText = '';
    DOM.displayPreview.innerText = '';
    updateDisplay();
}

function deleteLast() {
    AudioPlayer.playClick(350, 0.04);
    if (CalcState.expression.length > 0) {
        // If ends with function like "sin(", delete whole function
        const fnMatches = CalcState.expression.match(/(sin|cos|tan|asin|acos|atan|log|ln|sqrt|abs)\($/);
        if (fnMatches) {
            CalcState.expression = CalcState.expression.slice(0, -fnMatches[0].length);
        } else {
            CalcState.expression = CalcState.expression.slice(0, -1);
        }
        updateDisplay();
    }
}

function toggleSign() {
    AudioPlayer.playClick();
    if (!CalcState.expression) return;
    try {
        if (CalcState.expression.startsWith('-(') && CalcState.expression.endsWith(')')) {
            CalcState.expression = CalcState.expression.slice(2, -1);
        } else {
            CalcState.expression = `-(${CalcState.expression})`;
        }
        updateDisplay();
    } catch (e) {}
}

function calculate() {
    if (!CalcState.expression) return;
    
    try {
        const sanitizedExpr = CalcState.expression;
        const res = evaluateExpression(sanitizedExpr);

        if (res === null || isNaN(res) || !isFinite(res)) {
            DOM.displayMain.innerText = 'Error';
            AudioPlayer.playClick(200, 0.15, 'sawtooth');
            return;
        }

        AudioPlayer.playSuccess();
        const formattedRes = formatNumber(res);

        // Add pulse animation
        DOM.displayMain.classList.remove('pulse-anim');
        void DOM.displayMain.offsetWidth; // Trigger reflow
        DOM.displayMain.classList.add('pulse-anim');

        DOM.displayTape.innerText = `${sanitizedExpr} =`;
        
        // Save to History
        addHistoryItem(sanitizedExpr, formattedRes);

        CalcState.tape = sanitizedExpr;
        CalcState.expression = String(res);
        CalcState.result = res;
        DOM.displayPreview.innerText = '';
        updateDisplay();

    } catch (err) {
        DOM.displayMain.innerText = 'Error';
        AudioPlayer.playClick(200, 0.15, 'sawtooth');
    }
}

// Memory Functions
function handleMemory(action) {
    AudioPlayer.playSpecial();
    const currentVal = CalcState.expression ? (evaluateExpression(CalcState.expression) || 0) : 0;

    switch (action) {
        case 'MC':
            CalcState.memory = 0;
            break;
        case 'MR':
            if (CalcState.memory !== 0) {
                CalcState.expression += String(CalcState.memory);
                updateDisplay();
            }
            break;
        case 'M+':
            CalcState.memory += currentVal;
            break;
        case 'M-':
            CalcState.memory -= currentVal;
            break;
        case 'MS':
            CalcState.memory = currentVal;
            break;
    }
    updateDisplay();
}

// Angle Mode Toggle (DEG / RAD)
function toggleAngleMode() {
    AudioPlayer.playSpecial();
    CalcState.angleMode = CalcState.angleMode === 'DEG' ? 'RAD' : 'DEG';
    DOM.angleBadge.innerText = CalcState.angleMode;
    updateDisplay();
}

// ==========================================================================
// MATHEMATICAL PARSER & EVALUATOR
// ==========================================================================

function evaluateExpression(expr) {
    if (!expr) return null;

    let parsed = expr;

    // Replace Constants
    parsed = parsed.replace(/π/g, `${Math.PI}`);
    parsed = parsed.replace(/(?<![a-zA-Z])e(?![a-zA-Z])/g, `${Math.E}`);

    // Handle Factorials: e.g. 5! or (3+2)!
    parsed = parsed.replace(/(\d+(\.\d+)?|\([^\)]+\))!/g, (match, n) => {
        const num = evalSafe(n);
        return factorial(num);
    });

    // Handle Functions
    const isDeg = CalcState.angleMode === 'DEG';
    const toRad = (angle) => (isDeg ? (angle * Math.PI) / 180 : angle);
    const toDeg = (rad) => (isDeg ? (rad * 180) / Math.PI : rad);

    // Custom function definitions for evaluator
    const funcs = {
        sin: (x) => Math.sin(toRad(x)),
        cos: (x) => Math.cos(toRad(x)),
        tan: (x) => {
            const rad = toRad(x);
            if (Math.abs(Math.cos(rad)) < 1e-15) throw new Error('Undefined');
            return Math.tan(rad);
        },
        asin: (x) => toDeg(Math.asin(x)),
        acos: (x) => toDeg(Math.acos(x)),
        atan: (x) => toDeg(Math.atan(x)),
        log: (x) => Math.log10(x),
        ln: (x) => Math.log(x),
        sqrt: (x) => Math.sqrt(x),
        abs: (x) => Math.abs(x)
    };

    // Replace power operator `^` with `**`
    parsed = parsed.replace(/\^/g, '**');

    // Replace function calls with Math functions or custom mapped
    parsed = parsed.replace(/(sin|cos|tan|asin|acos|atan|log|ln|sqrt|abs)\(/g, (m, fn) => {
        return `funcs.${fn}(`;
    });

    // Safely evaluate with Function constructor without pollution
    try {
        const computeFn = new Function('funcs', `"use strict"; return (${parsed});`);
        const res = computeFn(funcs);
        return res;
    } catch (e) {
        return null;
    }
}

function evalSafe(expr) {
    try {
        return new Function(`"use strict"; return (${expr});`)();
    } catch (e) {
        return 0;
    }
}

function factorial(n) {
    if (n < 0 || n !== Math.floor(n)) return NaN;
    if (n === 0 || n === 1) return 1;
    if (n > 170) return Infinity; // Limit for standard float
    let r = 1;
    for (let i = 2; i <= n; i++) r *= i;
    return r;
}

function formatNumber(num) {
    if (num === null || isNaN(num)) return '0';
    if (!isFinite(num)) return num > 0 ? 'Infinity' : '-Infinity';
    
    // Round floating precision errors like 0.1 + 0.2
    const precision = 10;
    const rounded = parseFloat(num.toPrecision(precision));
    
    // Use scientific notation for extremely large/small values
    if (Math.abs(rounded) >= 1e12 || (Math.abs(rounded) > 0 && Math.abs(rounded) < 1e-7)) {
        return rounded.toExponential(6);
    }
    
    return String(rounded);
}

function isOperator(char) {
    return ['+', '-', '*', '/', '%', '^'].includes(char);
}

function isFunctionSymbol(str) {
    return ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', '(', ')'].some(fn => str.includes(fn));
}

// ==========================================================================
// HISTORY SYSTEM
// ==========================================================================

function addHistoryItem(expr, res) {
    const item = {
        id: Date.now(),
        expr,
        res,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };
    CalcState.history.unshift(item);
    if (CalcState.history.length > 50) CalcState.history.pop();
    localStorage.setItem('glamour_calc_history', JSON.stringify(CalcState.history));
    renderHistory();
}

function renderHistory() {
    if (CalcState.history.length === 0) {
        DOM.historyList.innerHTML = '<div class="history-empty">No calculations yet.<br>Do some math to see history!</div>';
        return;
    }

    DOM.historyList.innerHTML = CalcState.history.map(item => `
        <div class="history-item" onclick="useHistoryItem('${item.res}')">
            <div class="hist-expr">${item.expr} =</div>
            <div class="hist-res">${item.res}</div>
        </div>
    `).join('');
}

function useHistoryItem(val) {
    AudioPlayer.playClick();
    CalcState.expression = String(val);
    CalcState.result = parseFloat(val);
    updateDisplay();
    toggleHistoryDrawer(false);
}

function clearHistory() {
    AudioPlayer.playSpecial();
    CalcState.history = [];
    localStorage.removeItem('glamour_calc_history');
    renderHistory();
}

function toggleHistoryDrawer(forceState) {
    AudioPlayer.playClick();
    const isOpen = forceState !== undefined ? forceState : !DOM.historyDrawer.classList.contains('open');
    if (isOpen) {
        renderHistory();
        DOM.historyDrawer.classList.add('open');
        DOM.historyToggleBtn.classList.add('active');
    } else {
        DOM.historyDrawer.classList.remove('open');
        DOM.historyToggleBtn.classList.remove('active');
    }
}

// ==========================================================================
// THEME & SOUND MANAGEMENT
// ==========================================================================

function setTheme(themeName) {
    CalcState.theme = themeName;
    DOM.body.setAttribute('data-theme', themeName);
    localStorage.setItem('glamour_calc_theme', themeName);
    DOM.themeDropdown.classList.remove('show');
}

function toggleThemeDropdown() {
    AudioPlayer.playClick();
    DOM.themeDropdown.classList.toggle('show');
}

function toggleSound() {
    CalcState.soundEnabled = !CalcState.soundEnabled;
    localStorage.setItem('glamour_calc_sound', CalcState.soundEnabled);
    DOM.soundToggleBtn.innerHTML = CalcState.soundEnabled ? 
        `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>` :
        `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></svg>`;
    DOM.soundToggleBtn.classList.toggle('active', CalcState.soundEnabled);
    if (CalcState.soundEnabled) AudioPlayer.playSuccess();
}

// ==========================================================================
// MODE SWITCHING (Standard / Scientific / Converter)
// ==========================================================================

function switchMode(mode) {
    AudioPlayer.playClick();
    CalcState.activeMode = mode;

    DOM.tabStandard.classList.toggle('active', mode === 'standard');
    DOM.tabScientific.classList.toggle('active', mode === 'scientific');
    DOM.tabConverter.classList.toggle('active', mode === 'converter');

    if (mode === 'standard') {
        DOM.appContainer.classList.remove('scientific-mode');
        DOM.scientificGrid.classList.add('hidden');
        DOM.standardGrid.style.display = 'grid';
        DOM.converterPanel.classList.remove('active');
        document.querySelector('.display-panel').style.display = 'flex';
    } else if (mode === 'scientific') {
        DOM.appContainer.classList.add('scientific-mode');
        DOM.scientificGrid.classList.remove('hidden');
        DOM.standardGrid.style.display = 'grid';
        DOM.converterPanel.classList.remove('active');
        document.querySelector('.display-panel').style.display = 'flex';
    } else if (mode === 'converter') {
        DOM.appContainer.classList.remove('scientific-mode');
        DOM.scientificGrid.classList.add('hidden');
        DOM.standardGrid.style.display = 'none';
        DOM.converterPanel.classList.add('active');
        document.querySelector('.display-panel').style.display = 'none';
        updateConverterUnits();
        runConversion();
    }
}

// ==========================================================================
// UNIT CONVERTER ENGINE
// ==========================================================================

const UnitConversions = {
    length: {
        units: ['Meters (m)', 'Kilometers (km)', 'Centimeters (cm)', 'Millimeters (mm)', 'Miles (mi)', 'Feet (ft)', 'Inches (in)'],
        rates: {
            'Meters (m)': 1,
            'Kilometers (km)': 1000,
            'Centimeters (cm)': 0.01,
            'Millimeters (mm)': 0.001,
            'Miles (mi)': 1609.344,
            'Feet (ft)': 0.3048,
            'Inches (in)': 0.0254
        }
    },
    weight: {
        units: ['Kilograms (kg)', 'Grams (g)', 'Milligrams (mg)', 'Pounds (lb)', 'Ounces (oz)', 'Tonnes (t)'],
        rates: {
            'Kilograms (kg)': 1,
            'Grams (g)': 0.001,
            'Milligrams (mg)': 0.000001,
            'Pounds (lb)': 0.45359237,
            'Ounces (oz)': 0.0283495,
            'Tonnes (t)': 1000
        }
    },
    temperature: {
        units: ['Celsius (°C)', 'Fahrenheit (°F)', 'Kelvin (K)'],
        convert: (val, from, to) => {
            let celsius;
            if (from === 'Celsius (°C)') celsius = val;
            else if (from === 'Fahrenheit (°F)') celsius = (val - 32) * 5 / 9;
            else if (from === 'Kelvin (K)') celsius = val - 273.15;

            if (to === 'Celsius (°C)') return celsius;
            if (to === 'Fahrenheit (°F)') return (celsius * 9 / 5) + 32;
            if (to === 'Kelvin (K)') return celsius + 273.15;
            return celsius;
        }
    },
    data: {
        units: ['Bytes (B)', 'Kilobytes (KB)', 'Megabytes (MB)', 'Gigabytes (GB)', 'Terabytes (TB)'],
        rates: {
            'Bytes (B)': 1,
            'Kilobytes (KB)': 1024,
            'Megabytes (MB)': 1024 * 1024,
            'Gigabytes (GB)': 1024 * 1024 * 1024,
            'Terabytes (TB)': 1024 * 1024 * 1024 * 1024
        }
    },
    speed: {
        units: ['m/s', 'km/h', 'mph', 'knot', 'ft/s'],
        rates: {
            'm/s': 1,
            'km/h': 0.277778,
            'mph': 0.44704,
            'knot': 0.514444,
            'ft/s': 0.3048
        }
    }
};

function updateConverterUnits() {
    const type = DOM.convType.value;
    const conf = UnitConversions[type];
    if (!conf) return;

    DOM.convUnitFrom.innerHTML = conf.units.map(u => `<option value="${u}">${u}</option>`).join('');
    DOM.convUnitTo.innerHTML = conf.units.map(u => `<option value="${u}">${u}</option>`).join('');
    
    if (conf.units.length > 1) {
        DOM.convUnitTo.selectedIndex = 1;
    }
}

function runConversion(direction = 'from') {
    const type = DOM.convType.value;
    const conf = UnitConversions[type];
    if (!conf) return;

    const fromUnit = DOM.convUnitFrom.value;
    const toUnit = DOM.convUnitTo.value;

    if (direction === 'from') {
        const val = parseFloat(DOM.convInputFrom.value) || 0;
        let res = 0;
        if (conf.convert) {
            res = conf.convert(val, fromUnit, toUnit);
        } else {
            const inBase = val * conf.rates[fromUnit];
            res = inBase / conf.rates[toUnit];
        }
        DOM.convInputTo.value = formatNumber(res);
    } else {
        const val = parseFloat(DOM.convInputTo.value) || 0;
        let res = 0;
        if (conf.convert) {
            res = conf.convert(val, toUnit, fromUnit);
        } else {
            const inBase = val * conf.rates[toUnit];
            res = inBase / conf.rates[fromUnit];
        }
        DOM.convInputFrom.value = formatNumber(res);
    }
}

// ==========================================================================
// KEYBOARD EVENT LISTENERS & SHORTCUTS
// ==========================================================================

document.addEventListener('keydown', (e) => {
    // Disable shortcuts if typing inside converter inputs
    if (document.activeElement === DOM.convInputFrom || document.activeElement === DOM.convInputTo) {
        return;
    }

    const key = e.key;

    if (key >= '0' && key <= '9') {
        highlightKey(`btn-${key}`);
        appendValue(key);
    } else if (key === '.') {
        highlightKey('btn-dot');
        appendValue('.');
    } else if (key === '+') {
        highlightKey('btn-plus');
        appendValue('+');
    } else if (key === '-') {
        highlightKey('btn-minus');
        appendValue('-');
    } else if (key === '*') {
        highlightKey('btn-mult');
        appendValue('*');
    } else if (key === '/') {
        e.preventDefault();
        highlightKey('btn-div');
        appendValue('/');
    } else if (key === '%') {
        highlightKey('btn-mod');
        appendValue('%');
    } else if (key === '^') {
        appendFunction('power');
    } else if (key === '(' || key === ')') {
        appendValue(key);
    } else if (key === 'Enter' || key === '=') {
        e.preventDefault();
        highlightKey('btn-equals');
        calculate();
    } else if (key === 'Backspace') {
        highlightKey('btn-del');
        deleteLast();
    } else if (key === 'Escape') {
        highlightKey('btn-ac');
        clearAll();
    }
});

function highlightKey(id) {
    const el = document.getElementById(id);
    if (el) {
        el.classList.add('pressed');
        setTimeout(() => el.classList.remove('pressed'), 120);
    }
}

// Close Dropdowns on Click Outside
document.addEventListener('click', (e) => {
    if (!DOM.themePickerContainer?.contains(e.target) && !DOM.themeToggleBtn?.contains(e.target)) {
        DOM.themeDropdown?.classList.remove('show');
    }
});

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    setTheme(CalcState.theme);
    DOM.angleBadge.innerText = CalcState.angleMode;
    DOM.soundToggleBtn.classList.toggle('active', CalcState.soundEnabled);
    updateDisplay();
});
