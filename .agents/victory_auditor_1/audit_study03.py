import os

md_path = r"c:\Users\omara\Desktop\new anit\03_business_pricing_and_revenue_model.md"
html_path = r"c:\Users\omara\Desktop\new anit\03_business_pricing_and_revenue_model.html"

with open(md_path, "r", encoding="utf-8") as f:
    md = f.read()

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

required_strings = [
    "Standard", "Pro", "Ultra", "Enterprise",
    "$129", "$349", "$899", "$2,499",
    "96.9%", "95.8%", "93.3%",
    "Quarterly", "Semi-Annual", "Yearly",
    "1 Text Post = 1 credit", "1 Carousel = 5 credits",
    "1 Video = 25 credits", "1 Landing Page = 50 credits",
    "CAC", "LTV"
]

print("=== VERIFYING STUDY 03 (MARKDOWN) ===")
for s in required_strings:
    if s.lower() in md.lower():
        print(f"PASS: Found '{s}' in Markdown")
    else:
        print(f"FAIL: Missing '{s}' in Markdown")

print("\n=== VERIFYING STUDY 03 (HTML) ===")
for s in required_strings:
    if s.lower() in html.lower():
        print(f"PASS: Found '{s}' in HTML")
    else:
        print(f"FAIL: Missing '{s}' in HTML")
