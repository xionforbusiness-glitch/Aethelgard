import os
import glob

workspace = r"c:\Users\omara\Desktop\new anit"
files = sorted(glob.glob(os.path.join(workspace, "*.md")) + glob.glob(os.path.join(workspace, "*.html")))

print(f"{'Filename':45} | {'Lines':>6} | {'Words':>7} | {'Bytes':>8}")
print("-" * 75)
for f in files:
    fname = os.path.basename(f)
    with open(f, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
        text = "".join(lines)
        words = len(text.split())
        byte_size = len(text.encode("utf-8"))
        print(f"{fname:45} | {len(lines):6} | {words:7} | {byte_size:8}")
