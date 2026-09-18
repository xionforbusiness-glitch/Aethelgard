const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '../../');
const files = fs.readdirSync(root).filter(f => f.startsWith('0') && (f.endsWith('.html') || f.endsWith('.md')));

console.log('--- Detailed Workspace Deliverables Inspection ---');
files.forEach(f => {
  const filePath = path.join(root, f);
  const content = fs.readFileSync(filePath, 'utf8');
  const lines = content.split('\n').length;
  const size = fs.statSync(filePath).size;
  
  if (f.endsWith('.html')) {
    const titleMatch = content.match(/<title>([^<]+)<\/title>/i);
    let slideCount = 0;
    if (f.includes('01_agent')) {
      slideCount = (content.match(/class=["'][^"']*slide-card[^"']*["']/g) || []).length;
    } else if (f.includes('02_token')) {
      slideCount = (content.match(/<div[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (f.includes('03_business')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (f.includes('04_market')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    } else if (f.includes('05_ui_ux')) {
      slideCount = (content.match(/<section[^>]*class=["'][^"']*\bslide\b(?![^"']*-)[^"']*["']/g) || []).length;
    }
    console.log(`[HTML] ${f}: exact slides = ${slideCount}`);
  } else {
    const titleMatch = content.match(/^#\s+(.+)$/m);
    const h2s = (content.match(/^##\s+(.+)$/gm) || []).slice(0, 5);
    console.log(`[MD] ${f}:`);
    console.log(`  Lines: ${lines}, Size: ${(size/1024).toFixed(1)} KB`);
    console.log(`  Title: ${titleMatch ? titleMatch[1].trim() : 'N/A'}`);
    console.log(`  First H2s: ${h2s.map(h => h.replace(/^##\s+/, '')).join(' | ')}`);
  }
});

