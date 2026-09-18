import glob
import re

html_files = glob.glob(r"c:\Users\omara\Desktop\new anit\*.html")
for hf in sorted(html_files):
    fname = hf.split("\\")[-1]
    with open(hf, "r", encoding="utf-8") as f:
        content = f.read()
    scripts = re.findall(r'<script[^>]*src=["\'](.*?)["\']', content, re.IGNORECASE)
    styles = re.findall(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\'](.*?)["\']', content, re.IGNORECASE)
    images = re.findall(r'<img[^>]*src=["\'](.*?)["\']', content, re.IGNORECASE)
    print(f"{fname:45} | Ext scripts: {len(scripts)} | Ext styles: {len(styles)} | Img: {len(images)}")
    if styles:
        print(f"   Styles: {styles}")
    if scripts:
        print(f"   Scripts: {scripts}")
