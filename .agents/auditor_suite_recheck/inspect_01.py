import os
import re

with open(r"c:\Users\omara\Desktop\new anit\01_agent_architecture_and_roles_study.html", "r", encoding="utf-8") as f:
    text = f.read()

print("Slides with class='slide':", len(re.findall(r'<div[^>]*class=["\'][^"\']*slide[^"\']*["\']', text)))
matches = re.findall(r'<div[^>]*class=["\'][^"\']*slide[^"\']*["\'][^>]*>', text)
for m in matches[:5]:
    print(" ", m)
