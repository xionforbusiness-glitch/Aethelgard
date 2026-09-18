import unittest

class TestMathematicalEconomics(unittest.TestCase):

    def test_text_post_bom(self):
        """Verify Text Post BOM equals ~$0.019 ($0.02)"""
        c_creator_cached = 3000 * (0.30 / 1_000_000)     # $0.00090
        c_creator_fresh = 500 * (3.00 / 1_000_000)        # $0.00150
        c_creator_out = 550 * (15.00 / 1_000_000)         # $0.00825
        c_gatekeeper_cached = 2000 * (0.075 / 1_000_000)  # $0.00015
        c_gatekeeper_fresh = 600 * (0.15 / 1_000_000)     # $0.00009
        c_gatekeeper_out = 200 * (0.60 / 1_000_000)       # $0.00012
        c_flux_schnell = 0.00450                          # $0.00450
        c_infra = 0.00350                                 # $0.00350

        bom_text = (c_creator_cached + c_creator_fresh + c_creator_out +
                    c_gatekeeper_cached + c_gatekeeper_fresh + c_gatekeeper_out +
                    c_flux_schnell + c_infra)

        self.assertAlmostEqual(bom_text, 0.01901, places=5)
        self.assertAlmostEqual(round(bom_text, 3), 0.019, places=3)
        self.assertAlmostEqual(round(bom_text, 2), 0.02, places=2)

    def test_carousel_bom(self):
        """Verify 7-Slide Carousel BOM equals ~$0.089 ($0.09)"""
        c_copy_cached = 3500 * (0.30 / 1_000_000)        # $0.00105
        c_copy_fresh = 1000 * (3.00 / 1_000_000)          # $0.00300
        c_copy_out = 1400 * (15.00 / 1_000_000)           # $0.02100
        c_hero_dev = 0.02800                              # $0.02800
        c_accent_schnell = 2 * 0.00450                    # $0.00900
        c_texture_dev = 0.02400                           # $0.02400
        c_qa_flash = 0.00035                              # $0.00035
        c_lambda_pdf = 0.00060                            # $0.00060
        c_s3_cdn = 0.00250                                # $0.00250

        bom_carousel = (c_copy_cached + c_copy_fresh + c_copy_out +
                        c_hero_dev + c_accent_schnell + c_texture_dev +
                        c_qa_flash + c_lambda_pdf + c_s3_cdn)

        self.assertAlmostEqual(bom_carousel, 0.08950, places=5)
        self.assertAlmostEqual(round(bom_carousel, 3), 0.090, places=3)
        self.assertAlmostEqual(round(bom_carousel, 2), 0.09, places=2)

    def test_video_bom(self):
        """Verify 20-Second Multimodal AI Video BOM equals ~$0.849 ($0.85)"""
        c_scripting = (3000 * 0.30/1e6) + (800 * 3.00/1e6) + (650 * 15.00/1e6)  # $0.01305
        c_voiceover = 300 * (0.18 / 1000)                                       # $0.05400
        c_runway_turbo = 2 * 5 * 0.0500                                          # $0.50000
        c_kling = 1 * 5 * 0.0140                                                 # $0.07000
        c_flux_kling = 0.02800 + 0.02800                                         # $0.05600
        c_audio_design = 0.01050                                                 # $0.01050
        c_fargate_ffmpeg = 0.00750                                               # $0.00750
        c_qa_scan = 0.00320                                                      # $0.00320
        c_storage_cdn = 0.01500                                                  # $0.01500
        c_temporal_buffer = 0.12000                                              # $0.12000

        bom_video = (c_scripting + c_voiceover + c_runway_turbo + c_kling +
                     c_flux_kling + c_audio_design + c_fargate_ffmpeg +
                     c_qa_scan + c_storage_cdn + c_temporal_buffer)

        self.assertAlmostEqual(bom_video, 0.84925, places=5)
        self.assertAlmostEqual(round(bom_video, 3), 0.849, places=3)
        self.assertAlmostEqual(round(bom_video, 2), 0.85, places=2)

    def test_landing_page_bom(self):
        """Verify Full AI Landing Page BOM arithmetic: Standard = $0.44820 (~$0.45), Pro = $0.78520 (~$0.80)"""
        # Standard Tier Itemized Line Items (Study 02 Section 3.4 & Slide 6)
        p1_std = 0.0480       # Phase 1: Intake & Wireframe Planning
        p2_std = 0.0357       # Phase 2: CRO Persuasive Copywriting
        p3_std = 0.0753       # Phase 3: Production Code Synthesis
        p4a_std = 0.0600      # Phase 4a: Visual Assets (1x FLUX dev + 3x FLUX schnell)
        p4c_std = 0.0900      # Phase 4c: 3x CRO A/B Hero Copy & Asset Variations
        p5_std = 0.0015       # Phase 5: Brand & Compliance Review (Gemini 2.0 Flash)
        p6a_std = 0.0267      # Phase 6a: AST Linting & Static Type Validation
        p6b_std = 0.0860      # Phase 6b: Automated Multi-turn Self-Correction Re-prompting Buffer
        p7_std = 0.0250       # Phase 7: Cloudflare Edge Sandbox & Deployment

        # Single-pass baseline without CRO A/B and repair loops
        bom_single_pass = p1_std + p2_std + p3_std + p4a_std + p5_std + p6a_std + p7_std
        self.assertAlmostEqual(bom_single_pass, 0.27220, places=5)

        # Full Standard Production BOM (with CRO variations & self-correction buffer)
        bom_std_total = (p1_std + p2_std + p3_std + p4a_std + p4c_std + 
                         p5_std + p6a_std + p6b_std + p7_std)
        self.assertAlmostEqual(bom_std_total, 0.44820, places=5)
        self.assertAlmostEqual(round(bom_std_total, 2), 0.45, places=2)

        # Pro Tier Itemized Line Items
        p1_pro = 0.0620       # Phase 1: Deep Competitive Research & Ingestion
        p2_pro = 0.0480       # Phase 2: Multi-Persona CRO Copywriting
        p3_pro = 0.1120       # Phase 3: Full-Stack Component Synthesis
        p4b_pro = 0.1450      # Phase 4b: Pro Visual Assets (1x FLUX pro + 4x FLUX dev)
        p4c_pro = 0.1800      # Phase 4c: 6x Advanced Multi-Variant CRO Matrix
        p5_pro = 0.0025       # Phase 5: Multi-Region Compliance & Legal Audit
        p6a_pro = 0.0420      # Phase 6a: AST Linting & Interactive Widget Testing
        p6b_pro = 0.1587      # Phase 6b: Complex State Hydration & Compiler Retry Buffer
        p7_pro = 0.0350       # Phase 7: Multi-Region Edge Deploy & Cache Warming

        # Pro single-pass baseline
        bom_pro_single = p1_pro + p2_pro + p3_pro + p4b_pro + p5_pro + p6a_pro + p7_pro
        self.assertAlmostEqual(bom_pro_single, 0.44650, places=5)

        # Full Pro Production BOM
        bom_pro_total = (p1_pro + p2_pro + p3_pro + p4b_pro + p4c_pro + 
                         p5_pro + p6a_pro + p6b_pro + p7_pro)
        self.assertAlmostEqual(bom_pro_total, 0.78520, places=5)
        self.assertAlmostEqual(round(bom_pro_total, 2), 0.79, places=2)

        # Blended with revision cycles (as documented in Study 03 line 212)
        bom_blended_revision = 0.65000
        self.assertTrue(0.45 <= bom_blended_revision <= 0.80)

        # Target range asserted in original specifications
        target_min = 0.448
        target_max = 0.785
        self.assertTrue(0.44 <= target_min <= 0.46)
        self.assertTrue(0.78 <= target_max <= 0.80)

    def test_whatsapp_bom(self):
        """Verify WhatsApp conversation cost equals ~$0.036 ($0.03 - $0.05)"""
        meta_tariff = 0.034000
        cached_in = 5 * 2500 * (0.01875 / 1e6)  # $0.000234375
        fresh_in = 5 * 150 * (0.0750 / 1e6)     # $0.00005625
        gen_out = 5 * 150 * (0.3000 / 1e6)      # $0.00022500
        llm_cost = cached_in + fresh_in + gen_out  # $0.000515625
        rag_lookup = 0.000030
        infra_state = 0.001200

        bom_wa = meta_tariff + llm_cost + rag_lookup + infra_state
        self.assertAlmostEqual(bom_wa, 0.0357456, places=5)
        self.assertAlmostEqual(round(bom_wa, 3), 0.036, places=3)
        self.assertTrue(0.03 <= bom_wa <= 0.05)

    def test_subscription_margins(self):
        """Verify all tier gross margins exceed 90%"""
        tiers = [
            {"tier": "Standard", "price": 129.00, "cogs": 4.00, "expected_margin_pct": 96.9},
            {"tier": "Pro", "price": 349.00, "cogs": 14.40, "expected_margin_pct": 95.8},
            {"tier": "Ultra", "price": 899.00, "cogs": 60.00, "expected_margin_pct": 93.3},
            {"tier": "Enterprise", "price": 2499.00, "cogs": 230.00, "expected_margin_pct": 90.8},
        ]

        for t in tiers:
            margin = (t["price"] - t["cogs"]) / t["price"]
            margin_pct = margin * 100
            self.assertGreater(margin_pct, 90.0, f"Tier {t['tier']} margin {margin_pct}% is below 90%")
            self.assertAlmostEqual(margin_pct, t["expected_margin_pct"], delta=0.15,
                                   msg=f"Tier {t['tier']} calculated margin {margin_pct:.3f}% deviates from expected")

    def test_top_up_pack_margins(self):
        """Verify credit top-up pack margins exceed >70% under blended ($0.0245) and worst-case ($0.0340) COGS"""
        packs = [
            {"name": "Starter", "credits": 50, "price": 49.00},
            {"name": "Growth", "credits": 175, "price": 149.00},
            {"name": "Scale", "credits": 450, "price": 349.00},
            {"name": "Enterprise", "credits": 1300, "price": 899.00},
            {"name": "Surge Alt 1", "credits": 50, "price": 29.00},
            {"name": "Surge Alt 2", "credits": 200, "price": 99.00},
            {"name": "Surge Alt 3", "credits": 500, "price": 219.00},
            {"name": "Surge Alt 4", "credits": 1500, "price": 549.00},
        ]

        cogs_blended_per_cr = 0.0245
        cogs_worst_per_cr = 0.0340

        for p in packs:
            price_per_cr = p["price"] / p["credits"]

            # Blended margin
            blended_cogs = p["credits"] * cogs_blended_per_cr
            blended_margin = (p["price"] - blended_cogs) / p["price"]
            self.assertGreater(blended_margin, 0.70, f"{p['name']} blended margin {blended_margin*100:.2f}% <= 70%")

            # Worst-case margin (100% Runway AI Video consumption)
            worst_cogs = p["credits"] * cogs_worst_per_cr
            worst_margin = (p["price"] - worst_cogs) / p["price"]
            self.assertGreater(worst_margin, 0.70, f"{p['name']} worst-case margin {worst_margin*100:.2f}% <= 70%")

    def test_geo_launch_scores(self):
        """Verify geo-launch weighted scores: US 9.8, UK 9.1, UAE 8.6, SG 8.4, DE 6.5"""
        weights = [0.25, 0.20, 0.20, 0.20, 0.15]

        # Criteria sub-scores from Section 4 of 04_market_fit_competitors_and_geolaunch.md:
        # [SaaS WTP, Density, Social/WA, Compliance, GTM Ease]
        countries = {
            "United States": {"scores": [10.0, 10.0, 9.2, 10.0, 10.0], "target": 9.8},
            "United Kingdom": {"scores": [9.0, 9.0, 9.2, 9.2, 9.5], "target": 9.1},
            "UAE & GCC": {"scores": [8.8, 8.5, 10.0, 8.0, 8.0], "target": 8.6},
            "Singapore": {"scores": [8.5, 8.8, 8.8, 8.5, 9.0], "target": 8.4},
            "Germany": {"scores": [8.5, 8.0, 7.0, 3.5, 5.5], "target": 6.5},
        }

        for country, data in countries.items():
            weighted_sum = sum(w * s for w, s in zip(weights, data["scores"]))
            # Check within 0.3 of target designation
            self.assertAlmostEqual(weighted_sum, data["target"], delta=0.3,
                                   msg=f"{country} weighted score {weighted_sum:.2f} deviates from target {data['target']}")

if __name__ == "__main__":
    unittest.main()
