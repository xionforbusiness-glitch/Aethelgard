import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"c:\Users\omara\Desktop\new anit"
html_files = [f"0{i}_" for i in range(1, 6)]

for f in os.listdir(workspace_dir):
    if f.endswith(".html"):
        path = os.path.join(workspace_dir, f)
        with open(path, "r", encoding="utf-8") as file:
            c = file.read()
        
        # Check for navigation, back to index, or slide controls
        buttons = re.findall(r'<button[^>]*>(.*?)</button>', c, re.DOTALL | re.IGNORECASE)
        nav_elements = re.findall(r'<nav[^>]*>(.*?)</nav>', c, re.DOTALL | re.IGNORECASE)
        print(f"\n=== {f} ===")
        print(f"  Buttons count: {len(buttons)}")
        if buttons:
            print(f"  Sample buttons: {[re.sub(r'<[^>]+>', '', b).strip() for b in buttons[:6]]}")
        print(f"  Nav bars count: {len(nav_elements)}")
        print(f"  Has 'index.html' reference: {'index.html' in c}")
        print(f"  Print button exists: {'window.print' in c}")
