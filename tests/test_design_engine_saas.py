import os
import re
import unittest
from collections import Counter


class TestDesignEngineSaasSovereignty(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.saas_dir = os.path.join(cls.root_dir, "design_engine_saas")
        cls.session12_path = os.path.join(cls.saas_dir, "session12.html")
        cls.flagship_path = os.path.join(cls.saas_dir, "index.html")
        cls.root_index_path = os.path.join(cls.root_dir, "index.html")
        cls.research_log_path = os.path.join(cls.root_dir, "DESIGN_ENGINE_RESEARCH_LOG.md")

        with open(cls.session12_path, "r", encoding="utf-8") as f:
            cls.s12_content = f.read()
        with open(cls.flagship_path, "r", encoding="utf-8") as f:
            cls.flagship_content = f.read()
        with open(cls.root_index_path, "r", encoding="utf-8") as f:
            cls.root_index_content = f.read()
        with open(cls.research_log_path, "r", encoding="utf-8") as f:
            cls.research_log_content = f.read()

    def test_session_files_exist(self):
        """Verify all sessions from session02 to session12 exist in design_engine_saas."""
        for i in range(2, 13):
            fname = f"session{i:02d}.html"
            fpath = os.path.join(self.saas_dir, fname)
            self.assertTrue(os.path.exists(fpath), f"Missing milestone file: {fname}")

    def test_zero_duplicate_ids_in_session12(self):
        """Session 12 must satisfy strict 0 duplicate IDs invariant."""
        content_no_scripts = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', self.s12_content, flags=re.IGNORECASE)
        content_no_styles = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', content_no_scripts, flags=re.IGNORECASE)
        ids = re.findall(r'\bid=["\']([^"\']+)["\']', content_no_styles)
        counts = Counter(ids)
        duplicates = {k: v for k, v in counts.items() if v > 1}
        self.assertEqual(duplicates, {}, f"Duplicate IDs in session12.html: {duplicates}")

    def test_zero_duplicate_ids_in_flagship(self):
        """Active flagship must satisfy strict 0 duplicate IDs invariant."""
        content_no_scripts = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', self.flagship_content, flags=re.IGNORECASE)
        content_no_styles = re.sub(r'<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>', '', content_no_scripts, flags=re.IGNORECASE)
        ids = re.findall(r'\bid=["\']([^"\']+)["\']', content_no_styles)
        counts = Counter(ids)
        duplicates = {k: v for k, v in counts.items() if v > 1}
        self.assertEqual(duplicates, {}, f"Duplicate IDs in flagship index.html: {duplicates}")

    def test_session12_features_present(self):
        """Ensure Session 12 key architectural breakthroughs are embedded."""
        # 1. Magnetic Spring Vector Field
        self.assertIn('id="magneticFieldSection"', self.s12_content)
        self.assertIn('id="magneticCanvas"', self.s12_content)
        self.assertIn('id="magneticPrimaryBtn"', self.s12_content)
        self.assertIn('triggerMagneticWarpSingularity', self.s12_content)

        # 2. Web Audio HRTF 3D Spatial Soundstage
        self.assertIn('id="spatialAudioSection"', self.s12_content)
        self.assertIn('id="spatialStageCanvas"', self.s12_content)
        self.assertIn('id="spatialToggleAllBtn"', self.s12_content)
        self.assertIn('toggleSpatialMasterAudio', self.s12_content)
        self.assertIn('AudioListener', self.s12_content)
        self.assertIn('PannerNode', self.s12_content)

        # 3. 12-Milestone Chrono Expansion
        self.assertIn('commit 0xCE12FB40', self.s12_content)
        self.assertIn('chronoMilestone12', self.s12_content)

    def test_root_index_crown_points_to_session12(self):
        """Ensure Master Cockpit Hub crowns Session 12 with historical session links."""
        self.assertIn('Session 12 Sovereign Flagship Active', self.root_index_content)
        self.assertIn('Launch Session 12 Flagship', self.root_index_content)
        self.assertIn('design_engine_saas/session11.html', self.root_index_content)

    def test_research_log_documents_session12(self):
        """Ensure DESIGN_ENGINE_RESEARCH_LOG.md contains Session 12 deconstruction."""
        self.assertIn('Session 12', self.research_log_content)
        self.assertIn('Magnetic Spring Vector Field Studio', self.research_log_content)
        self.assertIn('Web Audio HRTF 3D Spatial Soundstage', self.research_log_content)
        self.assertIn('0xCE12FB40', self.research_log_content)


if __name__ == "__main__":
    unittest.main()
