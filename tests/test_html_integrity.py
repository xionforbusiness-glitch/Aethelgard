import os
import re
import unittest
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DECK_FILES = [
    "01_agent_architecture_and_roles_study.html",
    "02_token_exhaustion_and_compute_costs.html",
    "03_business_pricing_and_revenue_model.html",
    "04_market_fit_competitors_and_geolaunch.html",
    "05_ui_ux_visual_experience_blueprint.html",
]
ALL_HTML_FILES = DECK_FILES + ["index.html"]

VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
OPTIONAL_CLOSE = {"p", "li", "dt", "dd", "tr", "th", "td", "option"}

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.has_doctype = False
        self.has_charset = False
        self.has_viewport = False
        self.has_title = False
        self.external_links = []
        self.external_scripts = []
        self.external_images = []
        self.ids = set()
        self.duplicate_ids = []
        self.tag_stack = []
        self.errors = []
        self.style_content = []
        self.in_style = False

    def handle_decl(self, decl):
        if "DOCTYPE" in decl.upper() and "HTML" in decl.upper():
            self.has_doctype = True

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        tag_lower = tag.lower()

        if "id" in attr_dict:
            id_val = attr_dict["id"]
            if id_val in self.ids:
                self.duplicate_ids.append(id_val)
            else:
                self.ids.add(id_val)

        if tag_lower == "meta":
            if "charset" in attr_dict:
                self.has_charset = True
            if attr_dict.get("name", "").lower() == "viewport":
                self.has_viewport = True

        if tag_lower == "title":
            self.has_title = True

        if tag_lower == "link":
            href = attr_dict.get("href", "")
            rel = attr_dict.get("rel", "")
            if href.startswith("http://") or href.startswith("https://") or href.startswith("//"):
                self.external_links.append((rel, href))

        if tag_lower == "script":
            src = attr_dict.get("src", "")
            if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
                self.external_scripts.append(src)

        if tag_lower == "img":
            src = attr_dict.get("src", "")
            if src.startswith("http://") or src.startswith("https://") or src.startswith("//"):
                self.external_images.append(src)

        if tag_lower == "style":
            self.in_style = True

        if tag_lower not in VOID_TAGS:
            self.tag_stack.append((tag_lower, self.getpos()))

    def handle_endtag(self, tag):
        tag_lower = tag.lower()
        if tag_lower == "style":
            self.in_style = False

        if tag_lower in VOID_TAGS:
            return

        if not self.tag_stack:
            self.errors.append(f"Unexpected closing tag </{tag_lower}> at {self.getpos()}")
            return

        last_tag, pos = self.tag_stack[-1]
        if last_tag == tag_lower:
            self.tag_stack.pop()
        else:
            found = False
            for idx in range(len(self.tag_stack) - 1, -1, -1):
                if self.tag_stack[idx][0] == tag_lower:
                    found = True
                    break
            if found:
                while self.tag_stack and self.tag_stack[-1][0] != tag_lower:
                    unclosed, u_pos = self.tag_stack.pop()
                    if unclosed not in OPTIONAL_CLOSE:
                        self.errors.append(f"Unclosed tag <{unclosed}> at {u_pos} before </{tag_lower}>")
                if self.tag_stack:
                    self.tag_stack.pop()
            else:
                self.errors.append(f"Spurious closing tag </{tag_lower}> at {self.getpos()}")

    def handle_data(self, data):
        if self.in_style:
            self.style_content.append(data)


class TestHTMLIntegrity(unittest.TestCase):

    def test_all_html_files_exist_and_non_empty(self):
        for f in ALL_HTML_FILES:
            path = os.path.join(BASE_DIR, f)
            self.assertTrue(os.path.exists(path), f"File {f} does not exist")
            size = os.path.getsize(path)
            self.assertGreater(size, 20000, f"File {f} is suspiciously small ({size} bytes)")

    def test_core_html_structure_and_no_remote_scripts_or_images(self):
        for f in ALL_HTML_FILES:
            path = os.path.join(BASE_DIR, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()

            parser = HTMLValidator()
            parser.feed(content)

            with self.subTest(file=f):
                self.assertTrue(parser.has_doctype, f"{f} missing <!DOCTYPE html>")
                self.assertTrue(parser.has_charset, f"{f} missing <meta charset>")
                self.assertTrue(parser.has_viewport, f"{f} missing <meta name='viewport'>")
                self.assertTrue(parser.has_title, f"{f} missing <title>")

                # Zero external scripts and images allowed
                self.assertEqual(len(parser.external_scripts), 0, f"{f} has external scripts: {parser.external_scripts}")
                self.assertEqual(len(parser.external_images), 0, f"{f} has external images: {parser.external_images}")

                # Check for @import url(http...) in internal CSS
                all_css = "".join(parser.style_content)
                external_imports = re.findall(r"@import\s+url\([\'\"]?(https?:)?//", all_css, re.IGNORECASE)
                self.assertEqual(len(external_imports), 0, f"{f} has external CSS @import: {external_imports}")

                # Check unclosed non-optional tags
                unclosed_critical = [t for t, p in parser.tag_stack if t not in OPTIONAL_CLOSE]
                self.assertEqual(len(unclosed_critical), 0, f"{f} has unclosed critical tags: {unclosed_critical}")

    def test_deck_standalone_asset_integrity(self):
        """Studies 02, 03, 04, 05 must have 0 external links. Studies 01 & index have font links."""
        fully_airgapped_files = [
            "02_token_exhaustion_and_compute_costs.html",
            "03_business_pricing_and_revenue_model.html",
            "04_market_fit_competitors_and_geolaunch.html",
            "05_ui_ux_visual_experience_blueprint.html",
        ]
        for f in fully_airgapped_files:
            path = os.path.join(BASE_DIR, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()
            parser = HTMLValidator()
            parser.feed(content)
            self.assertEqual(len(parser.external_links), 0, f"{f} should have 0 external links, found {parser.external_links}")

    def test_print_stylesheet_rules(self):
        for f in ALL_HTML_FILES:
            path = os.path.join(BASE_DIR, f)
            with open(path, "r", encoding="utf-8") as fh:
                content = fh.read()

            with self.subTest(file=f):
                # Must contain @media print
                self.assertIn("@media print", content, f"{f} missing @media print stylesheet")

                # Decks must contain @page rule with landscape dimension
                if f in DECK_FILES:
                    self.assertIn("@page", content, f"{f} missing @page rule")
                    self.assertTrue("page-break-after" in content or "break-after" in content,
                                    f"{f} missing slide page break rule")
                    self.assertTrue("print-color-adjust" in content or "-webkit-print-color-adjust" in content,
                                    f"{f} missing print color adjustment")
                else:
                    # index.html is executive report
                    self.assertTrue("break-inside" in content or "page-break-inside" in content,
                                    f"{f} missing card break avoidance rule")

if __name__ == "__main__":
    unittest.main()
