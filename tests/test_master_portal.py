import os
import re
import unittest

class TestUnifiedMasterPortal(unittest.TestCase):
    def setUp(self):
        self.portal_path = r"c:\Users\omara\Desktop\new anit\stitch_ai_agency_platform_website\the_sovereign_command_cockpit_master_executive_dashboard\code.html"
        self.assertTrue(os.path.exists(self.portal_path), "Master portal file must exist")
        with open(self.portal_path, "r", encoding="utf-8") as f:
            self.content = f.read()

    def test_all_seven_views_present(self):
        views = ['view-cockpit', 'view-valerius', 'view-daedalus', 'view-chronicle', 'view-aurelius', 'view-argus', 'view-slas']
        for v in views:
            self.assertIn(f'id="{v}"', self.content, f"View #{v} must be present in master HTML")

    def test_all_seven_nav_buttons_present(self):
        targets = ['cockpit', 'valerius', 'daedalus', 'chronicle', 'aurelius', 'argus', 'slas']
        for t in targets:
            self.assertIn(f'data-target="{t}"', self.content, f"Nav button data-target='{t}' must exist")

    def test_sidebar_is_unified_and_consistent(self):
        self.assertIn("House of ScaleTech", self.content)
        self.assertIn("Zero-Knowledge Vault", self.content)
        self.assertIn("AES-256 Quantum Sealed", self.content)
        self.assertIn("Aethelgard", self.content)
        self.assertIn("Command Cockpit", self.content)

    def test_autohiding_top_header(self):
        self.assertIn('id="crm-top-header"', self.content)
        self.assertIn('9 Autonomous Agents Active', self.content)
        self.assertIn('Fuel Ledger', self.content)
        self.assertIn('lastScrollTop', self.content)
        self.assertIn('-translate-y-full', self.content)

    def test_aurelius_studio_features(self):
        self.assertIn("Aurelius the Scribe", self.content)
        self.assertIn("Contrarian Take", self.content)
        self.assertIn("Architecture Breakdown", self.content)
        self.assertIn("ROI & Unit Economics", self.content)
        self.assertIn("Technical Teardown", self.content)
        self.assertIn("Generate with Aurelius", self.content)
        self.assertIn("LinkedIn 7-Slide Carousel", self.content)

    def test_argus_spline_chart_features(self):
        self.assertIn("generateCubicBezierSpline", self.content)
        self.assertIn("telemetryData", self.content)
        self.assertIn("Recalibrate All Prompts Now", self.content)
        self.assertIn("spline-glow-mint", self.content)
        self.assertIn("spline-glow-amber", self.content)
        self.assertIn("Last 7 Days", self.content)
        self.assertIn("Last 30 Days", self.content)

    def test_slas_and_ecc_features(self):
        self.assertTrue("Agent SLAs, Guardrails &amp; Tone Matrix" in self.content or "Agent SLAs, Guardrails & Tone Matrix" in self.content)
        self.assertIn("affaan-m/ecc", self.content)
        self.assertIn("Deterministic Rigor", self.content)
        self.assertIn("Guardrail Strictness", self.content)
        self.assertIn("SIP Voice Latency Budget", self.content)
        self.assertIn("CLAUDE.md", self.content)

    def test_router_and_toasts(self):
        self.assertIn("function switchView", self.content)
        self.assertIn("function showToast", self.content)
        self.assertIn("crm-toast-container", self.content)

if __name__ == "__main__":
    unittest.main()
