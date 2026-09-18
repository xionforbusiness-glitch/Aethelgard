const fs = require('fs');
const path = require('path');

const mdPath = path.resolve('02_token_exhaustion_and_compute_costs.md');
const htmlPath = path.resolve('02_token_exhaustion_and_compute_costs.html');

console.log('--- Checking 02_token_exhaustion_and_compute_costs.md ---');
if (!fs.existsSync(mdPath)) {
  console.error('FAIL: Markdown file does not exist');
  process.exit(1);
}
const mdContent = fs.readFileSync(mdPath, 'utf8');
const mdLines = mdContent.split('\n').length;
console.log(`Lines: ${mdLines}`);
if (mdLines < 500) {
  console.error(`FAIL: Markdown file has fewer than 500 lines (${mdLines})`);
  process.exit(1);
}
const requiredMdTerms = [
  '$0.019',
  '$0.089',
  '$0.849',
  '$0.448',
  '$0.785',
  '$0.036',
  '76.5%',
  'Claude 3.5 Sonnet',
  'Gemini 2.0 Flash',
  'GPT-4o',
  'FLUX',
  'Runway',
  'ElevenLabs',
  'Meta WhatsApp',
  'Tri-Tier Memory Topology',
  'Light Usage',
  'Average Usage',
  'Power Usage',
  '$3.82',
  '$17.86',
  '$77.45'
];

let mdMissing = [];
for (const term of requiredMdTerms) {
  if (!mdContent.includes(term)) {
    mdMissing.push(term);
  }
}
if (mdMissing.length > 0) {
  console.error('FAIL: Markdown missing required terms:', mdMissing);
  process.exit(1);
}
console.log('PASS: All required terms present in markdown.');

console.log('\n--- Checking 02_token_exhaustion_and_compute_costs.html ---');
if (!fs.existsSync(htmlPath)) {
  console.error('FAIL: HTML file does not exist');
  process.exit(1);
}
const htmlContent = fs.readFileSync(htmlPath, 'utf8');
const htmlLines = htmlContent.split('\n').length;
console.log(`Lines: ${htmlLines}`);

const idMatches = htmlContent.match(/id=["']slide-\d+["']/g) || [];
console.log(`Exact slide IDs count: ${idMatches.length}`);
console.log(`Slide IDs: ${idMatches.join(', ')}`);
if (idMatches.length !== 13) {
  console.error(`FAIL: Expected 13 slides, found ${idMatches.length}`);
  process.exit(1);
}


const requiredHtmlFeatures = [
  '@media print',
  '16in 9in landscape',
  'navigateSlide',
  'toggleOverview',
  '#0B0F19',
  '#111827',
  '#6366F1',
  '#10B981',
  'aspect-ratio',
  'progressBar',
  'keydown'
];

let htmlMissing = [];
for (const feat of requiredHtmlFeatures) {
  if (!htmlContent.includes(feat)) {
    htmlMissing.push(feat);
  }
}
if (htmlMissing.length > 0) {
  console.error('FAIL: HTML missing required features:', htmlMissing);
  process.exit(1);
}
console.log('PASS: All required features present in HTML.');
console.log('\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY!');
