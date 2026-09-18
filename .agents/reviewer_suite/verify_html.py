import glob
import os
import re
from html.parser import HTMLParser

workspace_dir = r"c:\Users\omara\Desktop\new anit"
html_files = sorted([f for f in os.listdir(workspace_dir) if f.endswith(".html")])
print(f"Found {len(html_files)} HTML files:")

class TagCounter(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.open_tags = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if tag not in ['br', 'hr', 'img', 'input', 'meta', 'link', 'col', 'base']:
            self.open_tags.append(tag)
    def handle_endtag(self, tag):
        if tag in self.open_tags:
            self.open_tags.reverse()
            self.open_tags.remove(tag)
            self.open_tags.reverse()

for hf in html_files:
    path = os.path.join(workspace_dir, hf)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    has_doctype = bool(re.search(r"<!DOCTYPE html>", content, re.IGNORECASE))
    has_viewport = "viewport" in content.lower()
    has_print = "@media print" in content
    has_style = "<style" in content
    has_script = "<script" in content
    title_match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "NO TITLE"
    
    links = re.findall(r'href=["\'](.*?)["\']', content)
    internal_doc_links = [l for l in links if l.endswith(".html")]
    
    parser = TagCounter()
    try:
        parser.feed(content)
        parse_status = "Valid HTML structure"
    except Exception as e:
        parse_status = f"Parser Error: {e}"
        
    print(f"\n--- {hf} ({len(content)} bytes) ---")
    print(f"  Title: {title}")
    print(f"  Doctype: {has_doctype} | Viewport: {has_viewport} | Print CSS: {has_print} | Style: {has_style} | Script: {has_script}")
    print(f"  HTML doc links found: {set(internal_doc_links)}")
    print(f"  Parse status: {parse_status} (Total tags parsed: {len(parser.tags)})")
