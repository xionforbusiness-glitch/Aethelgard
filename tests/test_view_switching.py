import re
import unittest

portal_path = r"stitch_ai_agency_platform_website\the_sovereign_command_cockpit_master_executive_dashboard\code.html"

class TestViewSwitchingIntegrity(unittest.TestCase):
    def setUp(self):
        with open(portal_path, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_all_seven_views_exist_as_crm_views(self):
        views = ['cockpit', 'valerius', 'daedalus', 'chronicle', 'aurelius', 'argus', 'slas']
        for v in views:
            # Check pattern: <(div|section) id="view-{v}" class="[^"]*crm-view[^"]*"
            pattern = rf'<(?:div|section)[^>]*id="view-{v}"[^>]*class="[^"]*crm-view[^"]*"'
            match = re.search(pattern, self.content)
            self.assertIsNotNone(match, f"View id='view-{v}' must have class 'crm-view'")

    def test_no_duplicate_ids_in_code_html(self):
        ids = re.findall(r'id=[\'"]([^\'"]+)[\'"]', self.content)
        seen = set()
        duplicates = []
        for id_val in ids:
            if id_val in seen:
                duplicates.append(id_val)
            seen.add(id_val)
        self.assertEqual(duplicates, [], f"Found duplicate IDs in code.html: {duplicates}")

    def test_hero_video_present(self):
        self.assertIn('id="hero-sovereign-video"', self.content)
        self.assertIn('SOVEREIGN REEL', self.content)
        self.assertIn('heroVideoPlayBtn', self.content)

    def test_scroll_storyline_present(self):
        self.assertIn('id="storyline-section"', self.content)
        self.assertIn('Scroll-Based Storyline', self.content)
        self.assertIn('Phase I // Inception', self.content)
        self.assertIn('Phase II // Dispatch', self.content)
        self.assertIn('Phase III // Synthesis', self.content)
        self.assertIn('Phase IV // The Moat', self.content)

    def test_object_breakdown_present(self):
        self.assertIn('id="object-breakdown-section"', self.content)
        self.assertIn('Sovereign Architecture Object Breakdown', self.content)
        self.assertIn('selectBreakdownObject', self.content)
        self.assertIn('OBJECT_DATA', self.content)
        self.assertIn('BOM Unit Economics', self.content)

    def test_enterprise_lead_table_present(self):
        self.assertIn('Enterprise Covenant Pipeline &amp; Active Deals', self.content)
        self.assertIn('Apex Capital Partners', self.content)
        self.assertIn('CloudShield Global Systems', self.content)
        self.assertIn('Solaria Energy Infrastructure', self.content)

    def test_motion_library_included(self):
        self.assertIn('https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js', self.content)
        self.assertIn('window.Motion', self.content)

    def test_each_view_has_rich_content(self):
        views = {
            'view-cockpit': ['Sovereign Command Cockpit', 'Executive Command Center', 'storyline-section'],
            'view-valerius': ['Valerius the Herald', 'Lead Telephony Agent', 'drawerTranscript'],
            'view-daedalus': ['Daedalus the Architect', 'canvas-frame', 'Summon Valerius'],
            'view-chronicle': ['The Chronicle', 'Upcoming Chronicle Dispatch', 'slideTitle'],
            'view-aurelius': ['Aurelius the Scribe', 'LinkedIn 7-Slide Carousel', 'Contrarian Take'],
            'view-argus': ['Argus the Watcher', 'Recalibrate All Prompts Now', 'telemetry-ticker-console', 'card-vector-valerius'],
            'view-slas': ['Agent SLAs', 'affaan-m/ecc', 'Deterministic Rigor', 'CLAUDE.md']
        }
        for vid, tokens in views.items():
            for tok in tokens:
                self.assertIn(tok, self.content, f"View {vid} missing essential token: {tok}")

    def test_all_onclick_functions_globally_bound_to_window(self):
        onclicks = re.findall(r'onclick=[\'"]([^\'"]+)[\'"]', self.content)
        called_funcs = set()
        for oc in onclicks:
            m = re.match(r'([a-zA-Z0-9_$]+)\s*\(', oc)
            if m:
                called_funcs.add(m.group(1))

        for fn in sorted(called_funcs):
            has_window = f'window.{fn}' in self.content
            has_decl = bool(re.search(rf'function\s+{fn}\b', self.content))
            self.assertTrue(has_window or has_decl, f"Onclick handler function '{fn}' is missing or not exposed to window!")

    def test_no_duplicate_attributes_on_html_tags(self):
        lines = self.content.splitlines()
        for line_idx, line in enumerate(lines, 1):
            tag_matches = re.finditer(r'<([a-zA-Z0-9\-]+)([^>]*)>', line)
            for tm in tag_matches:
                tag_name = tm.group(1)
                attr_str = tm.group(2)
                attrs = re.findall(r'([a-zA-Z0-9\-]+)\s*=', attr_str)
                seen = set()
                dups = set()
                for a in attrs:
                    if a in seen:
                        dups.add(a)
                    seen.add(a)
                if dups and tag_name != 'link':
                    self.fail(f"Line {line_idx}: Tag <{tag_name}> has duplicate attributes: {dups}")

    def test_no_rogue_init_hash_router_collisions(self):
        self.assertNotIn("initHashRouter", self.content, "Dead legacy initHashRouter must be removed to prevent router collisions")
        self.assertIn("initAppRouter", self.content, "Robust initAppRouter must handle document readyState and view switching")

    def test_hero_ambient_canvas_and_scroll_observer_present(self):
        self.assertIn('id="hero-ambient-canvas"', self.content)
        self.assertIn('initStorylineScroll', self.content)
        self.assertIn('initHeroCanvas', self.content)

if __name__ == '__main__':
    unittest.main()
