import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

decks = [
    '01_agent_architecture_and_roles_study.html',
    '02_token_exhaustion_and_compute_costs.html',
    '03_business_pricing_and_revenue_model.html',
    '04_market_fit_competitors_and_geolaunch.html',
    '05_ui_ux_visual_experience_blueprint.html'
]

workspace_dir = r"c:\Users\omara\Desktop\new anit"

for deck in decks:
    path = os.path.join(workspace_dir, deck)
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()
    
    # Slides detection
    slides = re.findall(r'<section[^>]*class=["\'][^"\']*(?:slide|view)[^"\']*["\']', c, re.IGNORECASE)
    if not slides:
        slides = re.findall(r'class=["\'][^"\']*(?:slide|card|section)[^"\']*["\']', c, re.IGNORECASE)
        
    # Check key features
    has_slide_nav = 'keydown' in c or 'slide' in c.lower()
    has_fullscreen = 'requestFullscreen' in c or 'fullscreen' in c.lower()
    has_print = '@media print' in c
    has_tables = '<table' in c
    table_count = len(re.findall(r'<table', c))
    
    # Check titles or headings
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', c, re.DOTALL | re.IGNORECASE)
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', c, re.DOTALL | re.IGNORECASE)
    
    clean_h1 = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s]
    clean_h2 = [re.sub(r'<[^>]+>', '', h).strip() for h in h2s]
    
    print(f"\n==========================================")
    print(f"DECK: {deck} ({len(c):,} bytes)")
    print(f"==========================================")
    print(f"  H1 Title: {clean_h1[:1]}")
    print(f"  Total H2 Sections: {len(clean_h2)}")
    print(f"  Sample H2s: {clean_h2[:4]}")
    print(f"  Data Tables: {table_count}")
    print(f"  Print Media CSS: {has_print}")
    print(f"  Fullscreen JS: {has_fullscreen}")
    print(f"  Slide / Keyboard Navigation: {has_slide_nav}")
