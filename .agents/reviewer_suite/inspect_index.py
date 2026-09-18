import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r"c:\Users\omara\Desktop\new anit\index.html", "r", encoding="utf-8") as f:
    content = f.read()

print("--- index.html Overview ---")
print(f"Total length: {len(content)} characters")

# Check section headings or card titles
cards = re.findall(r'<article[^>]*class=["\']([^"\']+)["\']|<div[^>]*class=["\']([^"\']*(?:card|study|grid)[^"\']*)["\']', content)
print(f"Card / container elements found: {len(cards)}")
for c in cards[:10]:
    print(f"  Class match: {c}")

# Check links to all 5 studies
studies = [
    '01_agent_architecture_and_roles_study.html',
    '02_token_exhaustion_and_compute_costs.html',
    '03_business_pricing_and_revenue_model.html',
    '04_market_fit_competitors_and_geolaunch.html',
    '05_ui_ux_visual_experience_blueprint.html'
]

print("\nVerifying links to 5 deliverables in index.html:")
for s in studies:
    found = s in content
    print(f"  {s}: {'FOUND' if found else 'MISSING'}")

# Check key UI features in index.html
print("\nInteractive features in index.html:")
print(f"  Search/Filter input: {'input' in content.lower()}")
print(f"  Filter buttons: {'filter' in content.lower()}")
print(f"  Keyboard shortcuts: {'keydown' in content or 'keyup' in content or 'keypress' in content}")
print(f"  Print media styling: {'@media print' in content}")
print(f"  Modal / quick view: {'modal' in content.lower()}")

