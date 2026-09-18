/**
 * verify_suite.js
 * Comprehensive automated verification script for the Autonomous B2B SaaS
 * Multi-Agent Marketing & Web Generation Platform Study Suite.
 * 
 * Verifies all 11 files (01-05 .md, 01-05 .html, index.html):
 * 1. File existence and non-empty status.
 * 2. Markdown structural integrity (>=500 lines, required topics, schemas).
 * 3. HTML standards compliance (DOCTYPE, viewport, title, obsidian theme, @media print, script interactivity).
 * 4. Link & Anchor resolution across all files.
 * 5. Quantitative metrics audit (total lines, total slides, mathematical consistency).
 */

const fs = require('fs');
const path = require('path');

const rootDir = path.resolve(__dirname, '../../');

const EXPECTED_FILES = [
  '01_agent_architecture_and_roles_study.md',
  '01_agent_architecture_and_roles_study.html',
  '02_token_exhaustion_and_compute_costs.md',
  '02_token_exhaustion_and_compute_costs.html',
  '03_business_pricing_and_revenue_model.md',
  '03_business_pricing_and_revenue_model.html',
  '04_market_fit_competitors_and_geolaunch.md',
  '04_market_fit_competitors_and_geolaunch.html',
  '05_ui_ux_visual_experience_blueprint.md',
  '05_ui_ux_visual_experience_blueprint.html',
  'index.html'
];

const REQUIRED_MD_TOPICS = {
  '01_agent_architecture_and_roles_study.md': [
    /temporal/i,
    /langgraph/i,
    /n8n/i,
    /product web builder/i,
    /hierarchy|corporate/i,
    /ast|cro/i,
    /event (?:bus|stream)|sse|websocket/i,
    /companion/i
  ],
  '02_token_exhaustion_and_compute_costs.md': [
    /bill of materials|bom/i,
    /claude|gpt-4o|gemini/i,
    /landing page/i,
    /whatsapp/i,
    /prompt caching/i,
    /light.*average.*power/i
  ],
  '03_business_pricing_and_revenue_model.md': [
    /standard.*pro.*ultra.*enterprise/i,
    /quarterly|semi-annual|yearly/i,
    /credit/i,
    /gross margin/i,
    /cac|ltv/i,
    /pro-forma|breakeven|p&l/i
  ],
  '04_market_fit_competitors_and_geolaunch.md': [
    /competitor|jasper|hubspot/i,
    /framer|v0/i,
    /moat|agency/i,
    /geo-launch|united states|singapore|uae/i,
    /gdpr|soc 2/i
  ],
  '05_ui_ux_visual_experience_blueprint.md': [
    /obsidian/i,
    /command cockpit/i,
    /landing page studio/i,
    /omnichannel calendar/i,
    /telemetry|analytics/i,
    /companion|swiftui|jetpack compose|winui/i
  ]
};

// Summary report data
const results = {
  totalTests: 0,
  passed: 0,
  failed: 0,
  failures: [],
  fileStats: {},
  linkAudit: { checked: 0, resolved: 0, broken: [] },
  metrics: {
    totalMarkdownLines: 0,
    totalHtmlSlides: 0,
    totalByteSize: 0
  }
};

function assert(condition, message, fileContext = '') {
  results.totalTests++;
  if (condition) {
    results.passed++;
  } else {
    results.failed++;
    const err = `[FAIL] ${fileContext ? `[${fileContext}] ` : ''}${message}`;
    results.failures.push(err);
    console.error(err);
  }
}

console.log('================================================================');
console.log('AUTONOMOUS B2B SAAS STUDY SUITE — COMPREHENSIVE AUTOMATED AUDIT');
console.log('================================================================\n');

// 1. Check file existence & non-empty status
console.log('--- Phase 1: Deliverable Files Existence & Non-Empty Check ---');
EXPECTED_FILES.forEach(filename => {
  const filePath = path.join(rootDir, filename);
  const exists = fs.existsSync(filePath);
  assert(exists, `File does not exist: ${filename}`, filename);

  if (exists) {
    const stats = fs.statSync(filePath);
    assert(stats.size > 0, `File is empty (0 bytes): ${filename}`, filename);
    results.fileStats[filename] = {
      sizeBytes: stats.size,
      sizeKB: (stats.size / 1024).toFixed(1)
    };
    results.metrics.totalByteSize += stats.size;
  }
});

// 2. Validate Markdown Specifications
console.log('\n--- Phase 2: Markdown Technical Specifications Rigor Check ---');
const mdFiles = EXPECTED_FILES.filter(f => f.endsWith('.md'));

mdFiles.forEach(filename => {
  const filePath = path.join(rootDir, filename);
  if (!fs.existsSync(filePath)) return;

  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  const lineCount = lines.length;

  results.fileStats[filename].lineCount = lineCount;
  results.metrics.totalMarkdownLines += lineCount;

  // Check >= 500 lines
  assert(lineCount >= 500, `Markdown file has fewer than 500 lines (${lineCount} lines found)`, filename);

  // Check H1 header exists
  const hasH1 = /^#\s+.+/m.test(content);
  assert(hasH1, `Missing top-level H1 title header`, filename);

  // Check multiple major section headers (minimum 4 major sections)
  const majorSections = content.match(/^#{2,3}\s+(?:\d+\.|\b[A-Z]).+/gm) || [];
  assert(majorSections.length >= 4, `Insufficient major sections (${majorSections.length} found, minimum 4 required)`, filename);

  // Check required architectural and domain topics
  const topics = REQUIRED_MD_TOPICS[filename] || [];
  topics.forEach(pattern => {
    const matched = pattern.test(content);
    assert(matched, `Required technical topic missing: ${pattern}`, filename);
  });

  // Check markdown links inside MD files
  const mdLinkRegex = /\[([^\]]+)\]\(([^)]+)\)/g;
  let match;
  while ((match = mdLinkRegex.exec(content)) !== null) {
    const linkUrl = match[2].trim();
    if (!linkUrl.startsWith('http') && !linkUrl.startsWith('#') && !linkUrl.startsWith('mailto:')) {
      results.linkAudit.checked++;
      const cleanPath = linkUrl.split('#')[0];
      const targetPath = path.resolve(rootDir, cleanPath);
      if (fs.existsSync(targetPath)) {
        results.linkAudit.resolved++;
      } else {
        results.linkAudit.broken.push({ source: filename, target: linkUrl });
        assert(false, `Broken relative link to '${linkUrl}'`, filename);
      }
    }
  }

  console.log(`✓ ${filename}: ${lineCount} lines, ${results.fileStats[filename].sizeKB} KB, ${majorSections.length} major sections verified.`);
});

// 3. Validate HTML Presentation Decks and Master Hub
console.log('\n--- Phase 3: HTML5/CSS3 Presentation Decks & Master Hub Audit ---');
const htmlFiles = EXPECTED_FILES.filter(f => f.endsWith('.html'));

htmlFiles.forEach(filename => {
  const filePath = path.join(rootDir, filename);
  if (!fs.existsSync(filePath)) return;

  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n');
  const lineCount = lines.length;

  results.fileStats[filename].lineCount = lineCount;

  // 1. DOCTYPE check
  assert(/<!DOCTYPE\s+html>/i.test(content), `Missing <!DOCTYPE html>`, filename);

  // 2. Viewport meta check
  assert(/<meta[^>]+name=["']viewport["']/i.test(content), `Missing viewport meta tag`, filename);

  // 3. Character encoding
  assert(/<meta[^>]+charset=["']utf-8["']/i.test(content), `Missing UTF-8 charset meta tag`, filename);

  // 4. Non-empty title tag
  const titleMatch = content.match(/<title>([^<]+)<\/title>/i);
  assert(titleMatch && titleMatch[1].trim().length > 0, `Missing or empty <title> tag`, filename);

  // 5. Obsidian dark theme color token check
  const hasObsidianBg = content.includes('#0B0F19') || content.includes('--bg-base');
  assert(hasObsidianBg, `Missing obsidian dark theme base color (#0B0F19 or --bg-base)`, filename);

  // 6. Card / elevated surface styling
  const hasSurfaceBg = content.includes('#111827') || content.includes('--bg-surface');
  assert(hasSurfaceBg, `Missing obsidian surface color (#111827 or --bg-surface)`, filename);

  // 7. Glassmorphism backdrop blur check
  const hasBackdropFilter = /backdrop-filter:\s*blur/i.test(content);
  assert(hasBackdropFilter, `Missing backdrop-filter blur glassmorphism effect`, filename);

  // 8. @media print stylesheet check
  const hasMediaPrint = /@media\s+print/i.test(content);
  assert(hasMediaPrint, `Missing @media print stylesheet for zero-bleed PDF export`, filename);

  // 9. JavaScript interactive controls
  assert(/<script[\s>]/i.test(content), `Missing <script> interactive controller`, filename);

  // Slide count detection for presentation decks
  if (filename !== 'index.html') {
    let slideCount = 0;
    if (filename.includes('01_agent')) {
      slideCount = (content.match(/class=["'][^"']*slide-card[^"']*["']/g) || []).length;
    } else if (filename.includes('02_token')) {
      slideCount = (content.match(/<div[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (filename.includes('03_business')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (filename.includes('04_market')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (filename.includes('05_ui_ux')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    }

    assert(slideCount >= 10, `Slide count is below minimum threshold of 10 (${slideCount} slides found)`, filename);
    results.fileStats[filename].slideCount = slideCount;
    results.metrics.totalHtmlSlides += slideCount;

    // Check keyboard navigation listener
    const hasKeyboardNav = /keydown/i.test(content) && (/ArrowRight|nextSlide|goToSlide/i.test(content));
    assert(hasKeyboardNav, `Missing keyboard slide navigation event handler`, filename);

    console.log(`✓ ${filename}: ${slideCount} slides, ${lineCount} lines, ${results.fileStats[filename].sizeKB} KB, interactive navigation & print styles verified.`);
  } else {
    // index.html specific checks
    assert(content.includes('01_agent_architecture_and_roles_study.html'), `index.html missing link to Study 01 HTML`, filename);
    assert(content.includes('02_token_exhaustion_and_compute_costs.html'), `index.html missing link to Study 02 HTML`, filename);
    assert(content.includes('03_business_pricing_and_revenue_model.html'), `index.html missing link to Study 03 HTML`, filename);
    assert(content.includes('04_market_fit_competitors_and_geolaunch.html'), `index.html missing link to Study 04 HTML`, filename);
    assert(content.includes('05_ui_ux_visual_experience_blueprint.html'), `index.html missing link to Study 05 HTML`, filename);

    assert(content.includes('01_agent_architecture_and_roles_study.md'), `index.html missing link to Study 01 MD`, filename);
    assert(content.includes('02_token_exhaustion_and_compute_costs.md'), `index.html missing link to Study 02 MD`, filename);
    assert(content.includes('03_business_pricing_and_revenue_model.md'), `index.html missing link to Study 03 MD`, filename);
    assert(content.includes('04_market_fit_competitors_and_geolaunch.md'), `index.html missing link to Study 04 MD`, filename);
    assert(content.includes('05_ui_ux_visual_experience_blueprint.md'), `index.html missing link to Study 05 MD`, filename);

    // Search and filter inputs check
    assert(/id=["']searchInput["']/i.test(content), `index.html missing #searchInput`, filename);
    assert(/filterStudies/i.test(content), `index.html missing filterStudies() search handler`, filename);

    console.log(`✓ index.html: Master navigation hub, ${lineCount} lines, ${results.fileStats[filename].sizeKB} KB, 10 cross-links verified.`);
  }

  // 10. Extract all href links in HTML and verify existence
  const hrefRegex = /href=["']([^"']+)["']/g;
  let hrefMatch;
  while ((hrefMatch = hrefRegex.exec(content)) !== null) {
    const url = hrefMatch[1].trim();
    if (!url.startsWith('http') && !url.startsWith('#') && !url.startsWith('mailto:') && !url.startsWith('javascript:')) {
      results.linkAudit.checked++;
      const cleanPath = url.split('#')[0];
      const targetPath = path.resolve(rootDir, cleanPath);
      if (fs.existsSync(targetPath)) {
        results.linkAudit.resolved++;
      } else {
        results.linkAudit.broken.push({ source: filename, target: url });
        assert(false, `Broken link to target file '${url}'`, filename);
      }
    }
  }
});

// 4. Overall Suite Summary & Results
console.log('\n================================================================');
console.log('AUDIT VERIFICATION SUMMARY');
console.log('================================================================');
console.log(`Total Automated Tests Executed: ${results.totalTests}`);
console.log(`Tests Passed:                  ${results.passed}`);
console.log(`Tests Failed:                  ${results.failed}`);
console.log(`Link Integrity Checks:         ${results.linkAudit.checked} checked, ${results.linkAudit.resolved} resolved, ${results.linkAudit.broken.length} broken`);
console.log(`Total Technical Markdown:      ${results.metrics.totalMarkdownLines} lines across 5 studies`);
console.log(`Total Presentation Slides:     ${results.metrics.totalHtmlSlides} slides across 5 decks`);
console.log(`Total Suite Footprint:         ${(results.metrics.totalByteSize / 1024).toFixed(1)} KB`);

if (results.failed === 0) {
  console.log('\n>>> SUITE INTEGRITY STATUS: 100% VERIFIED & PRODUCTION READY <<<\n');
} else {
  console.error('\n>>> SUITE INTEGRITY STATUS: VERIFICATION FAILURES DETECTED <<<\n');
  results.failures.forEach(f => console.error(f));
}

// Write out JSON verification results for handoff documentation
const summaryJsonPath = path.join(__dirname, 'verification_results.json');
fs.writeFileSync(summaryJsonPath, JSON.stringify(results, null, 2), 'utf8');
console.log(`Verification results saved to: ${summaryJsonPath}`);

process.exit(results.failed === 0 ? 0 : 1);
