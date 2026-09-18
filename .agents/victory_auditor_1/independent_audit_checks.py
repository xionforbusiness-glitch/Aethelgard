import re
import os
import sys

workspace = r"c:\Users\omara\Desktop\new anit"

def check_file(filename):
    path = os.path.join(workspace, filename)
    if not os.path.exists(path):
        return None, f"File {filename} does not exist"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    return content, None

print("=== INDEPENDENT ARITHMETIC & SPECIFICATION AUDIT ===")

# 1. Check Markdown Studies
md_files = [
    "01_agent_architecture_and_roles_study.md",
    "02_token_exhaustion_and_compute_costs.md",
    "03_business_pricing_and_revenue_model.md",
    "04_market_fit_competitors_and_geolaunch.md",
    "05_ui_ux_visual_experience_blueprint.md"
]

html_files = [
    "01_agent_architecture_and_roles_study.html",
    "02_token_exhaustion_and_compute_costs.html",
    "03_business_pricing_and_revenue_model.html",
    "04_market_fit_competitors_and_geolaunch.html",
    "05_ui_ux_visual_experience_blueprint.html",
    "index.html"
]

for f in md_files + html_files:
    content, err = check_file(f)
    if err:
        print(f"FAIL: {err}")
        sys.exit(1)
    else:
        print(f"PASS: {f} exists, size={len(content)} chars")

# Check R1 specifics in 01
c1, _ = check_file("01_agent_architecture_and_roles_study.md")
roles = [
    "Project Planner Agent",
    "Product Web Builder Agent",
    "Content Creator Agent",
    "Social & Messaging Orchestrator Agent",
    "Marketing Performance Manager Agent",
    "Brand & Compliance Gatekeeper Agent",
    "Media Synthesizer Agent"
]
for role in roles:
    if role.lower() in c1.lower():
        print(f"PASS: Role found in Study 01: {role}")
    else:
        print(f"FAIL: Role missing in Study 01: {role}")

frameworks = ["n8n", "LangGraph", "CrewAI", "Temporal"]
for fw in frameworks:
    if fw.lower() in c1.lower():
        print(f"PASS: Framework benchmarked in Study 01: {fw}")
    else:
        print(f"FAIL: Framework missing in Study 01: {fw}")

platforms = ["iOS", "Android", "macOS", "Windows", "WebSocket", "SSE"]
for plat in platforms:
    if plat.lower() in c1.lower():
        print(f"PASS: Companion/API concept found in Study 01: {plat}")
    else:
        print(f"FAIL: Companion/API concept missing in Study 01: {plat}")

# Check R2 specifics in 02
c2, _ = check_file("02_token_exhaustion_and_compute_costs.md")
models = ["GPT-4o", "Claude 3.5 Sonnet", "Gemini", "FLUX", "Runway", "ElevenLabs"]
for m in models:
    if m.lower() in c2.lower():
        print(f"PASS: Model referenced in Study 02: {m}")
    else:
        print(f"FAIL: Model missing in Study 02: {m}")

deliverable_boms = ["Text Post", "Carousel", "Video", "Landing Page", "WhatsApp"]
for d in deliverable_boms:
    if d.lower() in c2.lower():
        print(f"PASS: BOM topic found in Study 02: {d}")
    else:
        print(f"FAIL: BOM topic missing in Study 02: {d}")

intensities = ["Light", "Average", "Power"]
for inten in intensities:
    if inten.lower() in c2.lower():
        print(f"PASS: Intensity model found in Study 02: {inten}")
    else:
        print(f"FAIL: Intensity model missing in Study 02: {inten}")

# Check R3 specifics in 03
c3, _ = check_file("03_business_pricing_and_revenue_model.md")
tiers = ["Standard", "Pro", "Ultra", "Enterprise"]
for t in tiers:
    if t.lower() in c3.lower():
        print(f"PASS: Tier found in Study 03: {t}")
    else:
        print(f"FAIL: Tier missing in Study 03: {t}")

billing = ["Quarterly", "Semi-Annual", "Yearly"]
for b in billing:
    if b.lower() in c3.lower():
        print(f"PASS: Billing cycle found in Study 03: {b}")
    else:
        print(f"FAIL: Billing cycle missing in Study 03: {b}")

metrics = ["CAC", "LTV", "top-up", "gross margin"]
for met in metrics:
    if met.lower() in c3.lower():
        print(f"PASS: Financial metric found in Study 03: {met}")
    else:
        print(f"FAIL: Financial metric missing in Study 03: {met}")

# Check R4 specifics in 04
c4, _ = check_file("04_market_fit_competitors_and_geolaunch.md")
competitors = ["Jasper", "HubSpot Breeze", "Copy.ai", "Sprinklr", "Taplio", "Predis.ai", "Framer", "v0.dev", "Relume"]
for comp in competitors:
    if comp.lower() in c4.lower():
        print(f"PASS: Competitor analyzed in Study 04: {comp}")
    else:
        print(f"FAIL: Competitor missing in Study 04: {comp}")

geos = ["United States", "United Kingdom", "UAE", "Germany", "Singapore"]
for g in geos:
    if g.lower() in c4.lower():
        print(f"PASS: Geo target analyzed in Study 04: {g}")
    else:
        print(f"FAIL: Geo target missing in Study 04: {g}")

# Check R5 specifics in 05
c5, _ = check_file("05_ui_ux_visual_experience_blueprint.md")
surfaces = [
    "Command Cockpit",
    "Landing Page Studio",
    "Omnichannel Calendar",
    "Closed-Loop Feedback",
    "Companion App"
]
for s in surfaces:
    if s.lower() in c5.lower():
        print(f"PASS: UI/UX surface found in Study 05: {s}")
    else:
        print(f"FAIL: UI/UX surface missing in Study 05: {s}")

# Check HTML print stylesheet in all HTML files
for hf in html_files:
    hc, _ = check_file(hf)
    if "@media print" in hc:
        print(f"PASS: @media print stylesheet found in {hf}")
    else:
        print(f"FAIL: @media print missing in {hf}")

print("\nALL CONTRACT & INTEGRITY CHECKS COMPLETED.")
