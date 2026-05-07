const fs = require('fs');
const path = require('path');
const JavaScriptObfuscator = require('javascript-obfuscator');

const ROOT = path.resolve(__dirname, '..');
const RAW_DIR = path.join(ROOT, 'js-reverse-raw');
const OUT_DIR = path.join(ROOT, 'frontend', 'JS Reverse', 'js', 'challenges');
const CONFIG_DIR = path.join(__dirname, 'config');

const LEVEL_CONFIGS = {
  basic: loadConfig('tier-basic.json'),
  intermediate: loadConfig('tier-intermediate.json'),
  advanced: loadConfig('tier-advanced.json'),
  boss: loadConfig('tier-boss.json')
};

function loadConfig(filename) {
  return JSON.parse(fs.readFileSync(path.join(CONFIG_DIR, filename), 'utf8'));
}

function tierForLevel(levelNum) {
  if (levelNum <= 8) return 'basic';
  if (levelNum <= 12) return 'intermediate';
  if (levelNum <= 16) return 'advanced';
  return 'boss';
}

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function build() {
  ensureDir(OUT_DIR);
  const files = fs.readdirSync(RAW_DIR).filter((file) => file.endsWith('.src.js'));

  files.forEach((file) => {
    const match = file.match(/^level(\d+)\.src\.js$/);
    if (!match) return;
    const levelNum = Number(match[1]);
    const rawPath = path.join(RAW_DIR, file);
    const outPath = path.join(OUT_DIR, `level${levelNum}.js`);
    const source = fs.readFileSync(rawPath, 'utf8');

    if (levelNum <= 4) {
      fs.writeFileSync(outPath, source, 'utf8');
      return;
    }

    const config = LEVEL_CONFIGS[tierForLevel(levelNum)];
    const result = JavaScriptObfuscator.obfuscate(source, config);
    fs.writeFileSync(outPath, result.getObfuscatedCode(), 'utf8');
  });

  console.log(`JS Reverse challenges built: ${files.length}`);
}

build();
