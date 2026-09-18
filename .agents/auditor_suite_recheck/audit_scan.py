import os
import re

BASE_DIR = r"c:\Users\omara\Desktop\new anit"

HTML_DECKS = [
    ("01_agent_architecture_and_roles_study.html", 12),
    ("02_token_exhaustion_and_compute_costs.html", 13),
    ("03_business_pricing_and_revenue_model.html", 10),
    ("04_market_fit_competitors_and_geolaunch.html", 12),
    ("05_ui_ux_visual_experience_blueprint.html", 13),
]

print("=== SLIDE COUNT & STRUCTURE AUDIT ===")
total_slides = 0
for fname, exp in HTML_DECKS:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    slides = re.findall(r'<div[^>]*class=["\'][^"\']*slide[^"\']*["\']', content)
    # filter for top-level slides (id="slide-X")
    slide_ids = re.findall(r'id=["\']slide-\d+["\']', content)
    print(f"  {fname}: {len(slide_ids)} slide IDs found (expected {exp})")
    total_slides += len(slide_ids)
    assert len(slide_ids) == exp, f"Mismatch in {fname}: found {len(slide_ids)}, expected {exp}"

print(f"Total verified presentation slides across all decks: {total_slides}")

print("\n=== VERIFYING PRINT CSS RULES ===")
for fname, _ in HTML_DECKS:
    fpath = os.path.join(BASE_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    has_page_rule = bool(re.search(r"@page\s*\{[^}]*size:\s*16in\s+9in", content))
    has_break = "page-break-after" in content or "break-after" in content
    print(f"  {fname}: @page 16in 9in = {has_page_rule}, slide break rule = {has_break}")
    assert has_page_rule, f"Missing 16in 9in landscape @page in {fname}"
    assert has_break, f"Missing page break rule in {fname}"

print("All print CSS rules verified.")
