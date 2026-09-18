import os
import re

html_path = r"c:\Users\omara\Desktop\new anit\02_token_exhaustion_and_compute_costs.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Look for slide 6 or landing page
matches = [m.start() for m in re.finditer(r"SLIDE 6", html, re.IGNORECASE)]
print(f"Slide 6 matches: {len(matches)}")
for idx in matches:
    print("--- SLIDE 6 SNIPPET ---")
    print(html[idx:idx+2000])

# Check numbers in HTML
checks = [
    ("Landing Page Standard Target", "$0.448"),
    ("Landing Page Pro Target", "$0.785"),
    ("Baseline Standard", "$0.272"),
    ("Baseline Pro", "$0.446"),
    ("Text Post BOM", "$0.019"),
    ("Carousel BOM", "$0.089"),
    ("Video BOM", "$0.849"),
    ("WhatsApp BOM", "$0.035")
]

for label, val in checks:
    count = html.count(val)
    print(f"Check {label} ({val}): {count} occurrences in HTML deck 02")
