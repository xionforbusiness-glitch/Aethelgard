import os
import re
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MARKDOWN_FILES = [
    "01_agent_architecture_and_roles_study.md",
    "02_token_exhaustion_and_compute_costs.md",
    "03_business_pricing_and_revenue_model.md",
    "04_market_fit_competitors_and_geolaunch.md",
    "05_ui_ux_visual_experience_blueprint.md"
]

class TestMarkdownDeliverables(unittest.TestCase):

    def test_all_markdown_files_exist_and_non_empty(self):
        for f in MARKDOWN_FILES:
            p = os.path.join(BASE_DIR, f)
            self.assertTrue(os.path.exists(p), f"File {f} is missing")
            size = os.path.getsize(p)
            self.assertGreater(size, 40000, f"File {f} is smaller than 40KB ({size} bytes)")

    def test_r1_architecture_study_contracts(self):
        p = os.path.join(BASE_DIR, "01_agent_architecture_and_roles_study.md")
        with open(p, "r", encoding="utf-8") as fh:
            text = fh.read()

        # Agents required
        agents = [
            "Project Planner", "Product Web Builder", "Content Creator",
            "Social & Messaging Orchestrator", "Marketing Performance Manager",
            "Brand & Compliance Gatekeeper", "Media Synthesizer"
        ]
        for ag in agents:
            self.assertIn(ag, text, f"Study 01 missing agent: {ag}")

        # Frameworks evaluated
        for fw in ["n8n", "LangGraph", "CrewAI", "Temporal"]:
            self.assertIn(fw, text, f"Study 01 missing benchmark for: {fw}")

        # Headless API-first and companion apps
        self.assertTrue("WebSockets" in text or "SSE" in text, "Study 01 missing event stream spec")
        for platform in ["iOS", "Android", "macOS", "Windows"]:
            self.assertIn(platform, text, f"Study 01 missing companion platform: {platform}")

    def test_r2_token_compute_study_contracts(self):
        p = os.path.join(BASE_DIR, "02_token_exhaustion_and_compute_costs.md")
        with open(p, "r", encoding="utf-8") as fh:
            text = fh.read()

        # BOM deliverables
        self.assertIn("Text Post", text)
        self.assertIn("Carousel", text)
        self.assertIn("AI Video", text)
        self.assertIn("Landing Page", text)
        self.assertIn("WhatsApp", text)

        # Optimization & caching
        self.assertIn("Prompt Caching", text)
        self.assertIn("Context Window", text)
        self.assertTrue("Light" in text and "Average" in text and "Power" in text, "Study 02 missing usage intensities")

    def test_r3_pricing_model_contracts(self):
        p = os.path.join(BASE_DIR, "03_business_pricing_and_revenue_model.md")
        with open(p, "r", encoding="utf-8") as fh:
            text = fh.read()

        # Tiers
        for t in ["Standard", "Pro", "Ultra", "Enterprise"]:
            self.assertIn(t, text, f"Study 03 missing tier: {t}")

        # Multi-billing
        for b in ["Quarterly", "Semi-Annual", "Yearly"]:
            self.assertIn(b, text, f"Study 03 missing billing cycle: {b}")

        # Margins >70%
        self.assertIn(">70%", text)
        self.assertIn("LTV", text)
        self.assertIn("CAC", text)

    def test_r4_market_fit_contracts(self):
        p = os.path.join(BASE_DIR, "04_market_fit_competitors_and_geolaunch.md")
        with open(p, "r", encoding="utf-8") as fh:
            text = fh.read()

        # Competitors
        for c in ["Jasper", "HubSpot", "Copy.ai", "Sprinklr", "Taplio", "Framer", "v0"]:
            self.assertIn(c, text, f"Study 04 missing competitor: {c}")

        # Top countries
        for country in ["United States", "United Kingdom", "UAE", "Singapore", "Germany"]:
            self.assertIn(country, text, f"Study 04 missing country: {country}")

    def test_r5_ui_ux_blueprint_contracts(self):
        p = os.path.join(BASE_DIR, "05_ui_ux_visual_experience_blueprint.md")
        with open(p, "r", encoding="utf-8") as fh:
            text = fh.read()

        # Core cockpit components
        self.assertIn("Cockpit", text)
        self.assertIn("Studio", text)
        self.assertIn("Calendar", text)
        self.assertIn("Analytics", text)
        for platform in ["iOS", "Android", "macOS", "Windows"]:
            self.assertIn(platform, text, f"Study 05 missing wireframe platform: {platform}")

if __name__ == "__main__":
    unittest.main()
