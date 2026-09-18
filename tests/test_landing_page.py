"""
Unit tests for the Aethelgard 1300s Gothic AI Sovereign Landing Page.
Validates the presence and structural integrity of:
1. Floating Minimalist Capsule Pill Header (Version 3 reference)
2. 1300s Gothic AI Celestial Clockwork Astrarium 3D Scene (Three.js procedural scene)
3. 4-Act Pinned Spatial Storyline & Synchronized Side Rail
4. Embedded 1300s Medieval Illuminated Agent Artworks (Valerius, Solon, Daedalus)
5. Four Core Swarm Sanctums (Audio Waveform, Lighthouse 100/100, Vector Vault, Cubic Spline Chart)
6. Sovereign Pantheon & Economic Treaty Tiers ($349, $899, Custom)
7. Taste-Skill Anti-Slop Guardrails (no em-dashes in headings, tabular-nums on tickers)
"""

import os
import re
import unittest
from collections import Counter


class TestLandingPageElevation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.landing_path = os.path.join(
            cls.root_dir,
            "stitch_ai_agency_platform_website",
            "aethelgard_product_sovereign_vision_landing_page_celestial_astrolabe_animated",
            "code.html"
        )
        with open(cls.landing_path, "r", encoding="utf-8") as f:
            cls.content = f.read()

    def test_file_exists_and_substantial(self):
        """Ensure landing page file exists and is substantial (>20KB)."""
        self.assertTrue(os.path.exists(self.landing_path))
        self.assertGreater(len(self.content), 20000)

    def test_zero_duplicate_ids(self):
        """DOM integrity: every ID in the landing page must be unique."""
        ids = re.findall(r'\bid=["\']([a-zA-Z0-9_\-]+)["\']', self.content)
        counts = Counter(ids)
        duplicates = {k: v for k, v in counts.items() if v > 1}
        self.assertEqual(duplicates, {}, f"Found duplicate IDs: {duplicates}")

    def test_floating_capsule_pill_header(self):
        """Floating Capsule Pill Header matching user's red circle reference."""
        self.assertIn('Aethelgard', self.content)
        self.assertIn('PLATFORM', self.content)
        self.assertIn('ARCHITECTURE', self.content)
        self.assertIn('DATA PIPELINE', self.content)
        self.assertIn('SOLUTIONS', self.content)
        self.assertIn('AGENTS', self.content)
        self.assertIn('PRICING', self.content)
        self.assertIn('9 ACTIVE AGENTS', self.content)
        self.assertIn('GET STARTED', self.content)

    def test_3d_sovereign_knight_scene(self):
        """3D Sovereign Three.js scene, GLTFLoader, and masterKnightGroup setup."""
        self.assertIn('id="threejs-spatial-stage"', self.content)
        self.assertIn('three.min.js', self.content)
        self.assertIn('GLTFLoader.js', self.content)
        self.assertIn('sovereign_celestial_relic_4k.glb', self.content)
        self.assertIn('masterKnightGroup', self.content)

    def test_4_act_spatial_camera_storyline(self):
        """4-Act Pinned Spatial Storyline & Synchronized Side Rail."""
        self.assertIn('id="storyline-stage"', self.content)
        self.assertIn('id="act-1-view"', self.content)
        self.assertIn('id="act-2-view"', self.content)
        self.assertIn('id="act-3-view"', self.content)
        self.assertIn('id="act-4-view"', self.content)
        self.assertIn('act-nav', self.content)
        self.assertIn('01 // INCEPTION', self.content)
        self.assertIn('02 // SPECS', self.content)
        self.assertIn('03 // ATTRIBUTION', self.content)
        self.assertIn('04 // SECURITY', self.content)

    def test_clean_vector_icons_and_smart_navbar(self):
        """Clean vector luxury icons on cards, smart scroll navbar, and animated timeline."""
        self.assertIn('id="smart-navbar-container"', self.content)
        self.assertIn('id="storyline-side-rail"', self.content)
        self.assertIn('animate-timeline-laser', self.content)
        self.assertIn('query_stats', self.content)

    def test_four_core_swarm_sanctums(self):
        """Four Core Swarm Sanctums (Audio Waveform, Lighthouse, Vector Vault, Spline)."""
        self.assertIn('id="sanctums"', self.content)
        self.assertIn('id="audio-waveform"', self.content)
        self.assertIn('142ms DUPLEX', self.content)
        self.assertIn('CLOUDFLARE WORKERS', self.content)
        self.assertIn('3,072 DIMS', self.content)
        self.assertIn('id="chart-container"', self.content)
        self.assertIn('id="crosshair"', self.content)

    def test_anti_slop_and_taste_skill_guardrails(self):
        """Taste-Skill & Apple UI/UX Pro: no em-dashes in headings, tabular-nums on counters."""
        self.assertNotIn('—', self.content.split('<h1')[1].split('</h1>')[0])
        self.assertIn('tabular-nums', self.content)
        self.assertIn('tactile-slab-3d', self.content)

    def test_alternating_spatial_choreography(self):
        """Alternating Knight-Text Spatial Choreography: Act II left flank, Act III right flank, Centered Knight."""
        # Act II container aligned to left flank with generous margin
        self.assertIn('id="act-2-view"', self.content)
        self.assertIn('justify-start', self.content)
        self.assertIn('pl-20', self.content)
        # Act III container aligned to right flank
        self.assertIn('id="act-3-view"', self.content)
        self.assertIn('justify-end', self.content)
        self.assertIn('ml-auto', self.content)
        # 3D Cinematic Camera Choreography & Centered Knight Physics
        self.assertIn('actCamTargets', self.content)
        self.assertIn('masterKnightGroup.position.set(0, 0, 0);', self.content)
        self.assertIn('masterKnightGroup.rotation.y = curKnightRotY;', self.content)

    def test_letter_by_letter_reveal_animation(self):
        """Letter-by-letter staggered character reveal animation."""
        self.assertIn('letterReveal', self.content)
        self.assertIn('letter-char', self.content)
        self.assertIn('data-reveal-title="true"', self.content)
        self.assertIn('triggerLetterReveal', self.content)

    def test_side_rail_overlap_prevention(self):
        """Whisper-thin side rail with hover-only tooltips and ample card clearance."""
        self.assertIn('id="storyline-side-rail"', self.content)
        self.assertIn('group-hover:opacity-100', self.content)
        self.assertIn('w-10', self.content)

    def test_scroll_driven_timeline_milestones(self):
        """Scroll-activated timeline milestones with IntersectionObserver and halo ignition."""
        self.assertIn('timeline-milestone', self.content)
        self.assertIn('timeline-dot', self.content)
        self.assertIn('timeline-dot-active', self.content)
        self.assertIn('timeline-ping-active', self.content)
        self.assertIn('milestoneObserver', self.content)

    def test_enterprise_ai_telephony_console(self):
        """Practical B2B AI Telephony console with live SIP route, caller ID, and transcript."""
        self.assertIn('+1 (415) 890-2140', self.content)
        self.assertIn('SIP ACTIVE', self.content)
        self.assertIn('Deepgram Nova-2 Streaming Transcript', self.content)
        self.assertIn('CALLER CHANNEL', self.content)
        self.assertIn('NEURAL VOICE ENGINE', self.content)

    def test_billing_interval_switcher_and_neon_laser_card(self):
        """Monthly / Quarterly / Yearly billing interval toggle and spinning neon border beam."""
        self.assertIn('id="btn-billing-monthly"', self.content)
        self.assertIn('id="btn-billing-quarterly"', self.content)
        self.assertIn('id="btn-billing-yearly"', self.content)
        self.assertIn('data-monthly="349"', self.content)
        self.assertIn('data-quarterly="314"', self.content)
        self.assertIn('data-yearly="279"', self.content)
        self.assertIn('data-monthly="899"', self.content)
        self.assertIn('data-quarterly="809"', self.content)
        self.assertIn('data-yearly="719"', self.content)
        self.assertIn('animatePriceDeceleration', self.content)
        self.assertIn('neon-laser-card', self.content)
        self.assertIn('spinLaser', self.content)
        
    def test_knight_model_scaling_and_breathing_isolation(self):
        """Verify knight model scaling math (3.8 / maxDim) and that animate() does not overwrite knightModel.scale."""
        self.assertIn("const knightScale = 3.8 / maxDim;", self.content)
        self.assertIn("knightModel.scale.set(knightScale, knightScale, knightScale);", self.content)
        # Animate loop should modulate masterKnightGroup, never knightModel
        self.assertIn("masterKnightGroup.scale.set(1.0, 1.0, 1.0);", self.content)
        animate_body = re.search(r'function animate\(\)\s*\{([\s\S]*?)\n\s*animate\(\);', self.content)
        self.assertIsNotNone(animate_body)
        self.assertNotIn("knightModel.scale", animate_body.group(1))

    def test_camera_choreography_coordinates(self):
        """Verify camera positions and target vectors for Acts I, II, III, and IV."""
        self.assertIn("const actCamTargets = [", self.content)
        self.assertIn("{ camX: 0, camY: 0.15, camZ: 5.6, tarX: 0, tarY: 0.15, tarZ: 0, rotY: 0, rotX: 0 }", self.content)
        self.assertIn("{ camX: -3.6, camY: 0.12, camZ: 5.4, tarX: -1.8, tarY: 0.12, tarZ: 0, rotY: -0.88, rotX: 0.08 }", self.content)
        self.assertIn("{ camX: 3.6, camY: 0.05, camZ: 5.4, tarX: 1.8, tarY: 0.05, tarZ: 0, rotY: 0.88, rotX: 0.08 }", self.content)
        self.assertIn("{ camX: -2.8, camY: 0.0, camZ: 5.8, tarX: -1.2, tarY: 0.0, tarZ: 0, rotY: -0.55, rotX: 0.04 }", self.content)

    def test_global_stardust_canvas_and_threejs_isolation(self):
        """Verify 2D context for global stardust and WebGL context isolation for Three.js."""
        self.assertIn("id=\"global-stardust-canvas\"", self.content)
        self.assertIn("id=\"gothic-astrarium-canvas\"", self.content)
        self.assertIn("globalStardustCanvas.getContext('2d')", self.content)
        self.assertIn("new THREE.WebGLRenderer({ canvas: canvas", self.content)

    def test_storyline_side_rail_sticky_containment(self):
        """Verify storyline side rail is encapsulated inside storyline-stage sticky viewport container."""
        stage_match = re.search(r'<section[^>]+id=["\']storyline-stage["\'][\s\S]*?</section>', self.content)
        self.assertIsNotNone(stage_match)
        stage_html = stage_match.group(0)
        self.assertIn('id="storyline-side-rail"', stage_html)
        self.assertIn('sticky top-0', stage_html)

    def test_html_tag_balance(self):
        """Ensure all HTML elements are strictly balanced with zero unclosed tags."""
        from html.parser import HTMLParser
        class TagAudit(HTMLParser):
            def __init__(self):
                super().__init__()
                self.stack = []
                self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
                self.errors = []
            def handle_starttag(self, tag, attrs):
                if tag not in self.void_elements:
                    self.stack.append(tag)
            def handle_endtag(self, tag):
                if tag in self.void_elements:
                    return
                if not self.stack:
                    self.errors.append(f'Unexpected </{tag}>')
                    return
                if self.stack[-1] == tag:
                    self.stack.pop()
                else:
                    self.errors.append(f'Mismatched closing tag </{tag}>, expected </{self.stack[-1]}>')
        audit = TagAudit()
        audit.feed(self.content)
        self.assertEqual(audit.errors, [], f"HTML tag syntax errors: {audit.errors}")

    def test_knight_forward_orientation(self):
        """Verify knight model is reoriented to face forward toward user/camera (+Z)."""
        self.assertIn("knightModel.rotation.y = -Math.PI / 2;", self.content)

    def test_mouse_gaze_decoupled_parallax(self):
        """Verify camera position and model remain steady without mouse parallax jitter."""
        self.assertIn("masterKnightGroup.rotation.y = curKnightRotY;", self.content)
        self.assertIn("camera.position.set(curCamX, curCamY, curCamZ);", self.content)
        self.assertNotIn("curCamX + mouse.x", self.content)

    def test_neon_laser_card_stacking_hierarchy(self):
        """Verify CSS stacking context: border beam ::before at z-index 2 and badge at z-30."""
        self.assertIn("isolation: isolate;", self.content)
        self.assertIn("z-index: 2;", self.content)
        self.assertIn("z-30", self.content)
        self.assertIn("Most Popular", self.content)

    def test_tri_spectral_engine_waterfall_stagger(self):
        """Verify Tri-Spectral Engine waterfall animation with staggered transition delays."""
        tri_cards = re.findall(r'class="[^"]*tri-card[^"]*"[^>]*style="transition-delay:\s*(\d+)ms;"', self.content)
        self.assertEqual(tri_cards, ['120', '360', '600'])
        self.assertIn("const triCards = document.querySelectorAll('.tri-card');", self.content)
        self.assertIn("c.classList.add('translate-y-0', 'opacity-100');", self.content)
    def test_background_grid_elimination(self):
        """Verify architectural grid is eliminated for pure dark cosmic atmosphere."""
        self.assertNotIn("bg-architectural-grid", self.content.split('<body')[1].split('>')[0])
        self.assertIn("background-image: none;", self.content)

    def test_drop_down_waterfall_cascade(self):
        """Verify tri-card uses descending drop-down starting position -translate-y-12."""
        self.assertIn("-translate-y-12", self.content)
        self.assertIn("c.classList.remove('-translate-y-12', 'opacity-0');", self.content)

    def test_under_the_hood_peel_toggle(self):
        """Verify real DOM switching between executive and technical views."""
        self.assertIn("sanctum-exec-view", self.content)
        self.assertIn("sanctum-tech-view", self.content)
        self.assertIn("RAW CARRIER SIP TRACE", self.content)
        self.assertIn("SWC RUST AST ENGINE", self.content)
        self.assertIn("document.querySelectorAll('.sanctum-exec-view')", self.content)

    def test_4k_celestial_relic_integration(self):
        """Verify 4K PBR model direct registration and removal of obsolete switcher."""
        self.assertIn("sovereign_celestial_relic_4k.glb", self.content)
        self.assertNotIn("id=\"btn-model-relic\"", self.content)
        self.assertNotIn("id=\"btn-model-knight\"", self.content)
        self.assertIn("load3DModel", self.content)

    def test_zero_breathing_stability(self):
        """Verify model breathing oscillation is set to 0 for rock-solid stability."""
        self.assertIn("masterKnightGroup.scale.set(1.0, 1.0, 1.0);", self.content)
        self.assertIn("masterKnightGroup.position.set(0, 0, 0);", self.content)

    def test_optimistic_glare_and_bloom(self):
        """Verify 4K PBR celestial chiaroscuro, subtle corona sprite, and glare calibration matching reference image 2."""
        self.assertIn("coronaSprite", self.content)
        self.assertIn("THREE.AdditiveBlending", self.content)
        self.assertIn("renderer.toneMappingExposure = 1.18;", self.content)
        self.assertIn("keyLight = new THREE.DirectionalLight(0xfff3db, 2.6);", self.content)
        self.assertIn("rimLight = new THREE.DirectionalLight(0xf1e0d0, 2.2);", self.content)
        self.assertIn("shieldFill = new THREE.PointLight(0x2ee59d, 1.4, 15);", self.content)
        self.assertIn("gearLight = new THREE.PointLight(0xf1d2a9, 1.8, 5);", self.content)
        self.assertIn("coronaSprite.scale.set(5.5, 5.5, 1);", self.content)
        self.assertIn("opacity: 0.35", self.content)
        self.assertNotIn("drop-shadow(0 0 35px", self.content)

    def test_official_brand_logo(self):
        """Verify official company logo and favicon integration."""
        self.assertIn("aethelgard_official_logo_transparent.png", self.content)
        self.assertIn("aethelgard_favicon_64.png", self.content)

    def test_bottom_feathering_mask(self):
        """Verify sticky stage has linear gradient bottom feathering mask."""
        self.assertIn("mask-image:linear-gradient(to_bottom,black_85%,transparent_100%)", self.content)
        self.assertIn("-webkit-mask-image:linear-gradient(to_bottom,black_85%,transparent_100%)", self.content)

    def test_shadcn_area_chart_integration(self):
        """Verify shadcn/ui-grade area chart with dual gradients, dotted Cartesian grid, and floating tooltip."""
        self.assertIn('id="chart-svg-wrapper"', self.content)
        self.assertIn('id="area-chart-svg"', self.content)
        self.assertIn('id="areaGradientPrimary"', self.content)
        self.assertIn('id="areaGradientSecondary"', self.content)
        self.assertIn('stroke-dasharray="3,4"', self.content)
        self.assertIn('id="crosshair-point"', self.content)
        self.assertIn('id="chart-tooltip-card"', self.content)
        self.assertIn('id="tooltip-day"', self.content)
        self.assertIn('id="tooltip-lift"', self.content)
        self.assertIn('id="tooltip-roas"', self.content)
        self.assertIn('id="tooltip-cac"', self.content)
        self.assertIn('translate3d(', self.content)

    def test_enterprise_security_and_act1_unoccluded_layout(self):
        """Verify unoccluded Act I typography, left-flanked Act IV security slab, and zero 3D overlap."""
        self.assertIn('Aethelgard replaces bloated agency retainers', self.content)
        self.assertIn('Enterprise Security &amp; Sovereignty', self.content)
        self.assertIn('id="act-4-view"', self.content)
        self.assertIn('justify-start', self.content)
        self.assertIn('pl-20', self.content)
        self.assertIn('SOC 2 Type II', self.content)
        self.assertIn('Private VPC', self.content)

    def test_threejs_performance_flags(self):
        """Verify performance optimizations: shadowMap disabled for 1.86M poly model and high-performance context."""
        self.assertIn("renderer.shadowMap.enabled = false;", self.content)
        self.assertIn("powerPreference: 'high-performance'", self.content)
        self.assertIn("isScrollTicking", self.content)

    def test_medieval_nomenclature_purge(self):
        """Verify complete elimination of archaic/medieval character names and terms."""
        forbidden_terms = [
            'Sanctum I: Valerius',
            'Valerius SIP Fabric',
            'Daedalus AST Edge',
            'Solon the Arbiter',
            'Consecrate Guild',
            'Consecrate Sentinel',
            'Consecrate Guild Viceroy',
            'Commission Crown Treaty',
            'MMXXV AETHELGARD ATELIER',
            'Parchment #0941'
        ]
        for term in forbidden_terms:
            self.assertNotIn(term, self.content, f"Forbidden medieval term found: {term}")

    def test_header_pill_boundary_clearance(self):
        """Verify max-w-6xl header width, px-10 padding, and GET STARTED CTA with clearance."""
        self.assertIn('max-w-6xl', self.content)
        self.assertIn('GET STARTED', self.content)
        self.assertIn('px-6 md:px-10', self.content)
        self.assertIn('mr-1 sm:mr-2', self.content)

    def test_threejs_container_act_opacity_transition(self):
        """Verify Three.js stage is hidden in Act I and smoothly fades in during subsequent Acts."""
        self.assertIn('id="threejs-spatial-stage" style="opacity: 0;"', self.content)
        self.assertIn('transition-opacity duration-700 ease-out', self.content)
        self.assertIn("container.style.opacity = currentActIndex === 0 ? '0' : '1';", self.content)

    def test_viewport_meta_tag_present(self):
        """Verify standard responsive viewport meta tag is present to configure mobile screen scaling."""
        has_vp = bool(re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*content=["\'][^"\']*width=device-width[^"\']*["\']', self.content, re.IGNORECASE) or
                     re.search(r'<meta[^>]+content=["\'][^"\']*width=device-width[^"\']*["\'][^>]*name=["\']viewport["\']', self.content, re.IGNORECASE))
        self.assertTrue(has_vp, "Mobile viewport meta tag missing or invalid.")

    def test_mobile_overflow_prevention(self):
        """Verify overflow-x-hidden is enforced on body to prevent horizontal wobble across mobile devices."""
        body_match = re.search(r'<body[^>]*>', self.content)
        self.assertIsNotNone(body_match, "<body> tag not found.")
        self.assertIn("overflow-x-hidden", body_match.group(0), "Body tag must enforce overflow-x-hidden.")

    def test_mobile_responsive_layout_breakpoints(self):
        """Verify responsive breakpoints (hidden md:flex, sm:, md:, lg:) exist for adaptive mobile layout."""
        self.assertIn("hidden md:flex", self.content, "Header desktop nav should hide on mobile screens.")
        self.assertIn("grid-cols-2 md:grid-cols-4", self.content, "Hero metric bar should scale down to 2 columns on mobile.")
        self.assertIn("text-4xl sm:text-5xl md:text-6xl", self.content, "Headline should scale responsively across mobile/desktop.")

    def test_touch_target_accessibility_minimums(self):
        """Verify primary mobile CTAs have generous padding ensuring >=44px touch target compliance."""
        self.assertIn("py-3.5", self.content, "Hero buttons should utilize py-3.5 for >=44px touch target height.")
        self.assertIn("px-7", self.content, "Hero buttons should utilize px-7 for wide accessible tap zone.")
        self.assertIn("py-3", self.content, "Pricing CTAs should utilize py-3 for accessible touch area.")

    def test_mobile_camera_framing_and_resize_handler(self):
        """Verify onWindowResize adapts camera aspect, projection matrix, FOV, and mobileCameraZOffset."""
        self.assertIn("function onWindowResize()", self.content)
        self.assertIn("mobileCameraZOffset", self.content)
        self.assertIn("camera.aspect = aspect;", self.content)
        self.assertIn("camera.updateProjectionMatrix();", self.content)
        self.assertIn("Math.min(window.devicePixelRatio, 2)", self.content)

    def test_mobile_render_loop_framing(self):
        """Verify render loop dynamically frames celestial clockwork head in upper portion on mobile."""
        self.assertIn("const isMobile = window.innerWidth < 768;", self.content)
        self.assertIn("targetCamY = isMobile ? (currentActIndex === 0 ? 0.15 : -0.75) : t.camY;", self.content)
        self.assertIn("targetCamZ = t.camZ + mobileCameraZOffset;", self.content)
        self.assertIn("targetCamX = isMobile ? 0 : t.camX;", self.content)

    def test_passive_touch_event_listeners(self):
        """Verify touch event listeners use passive: true for 60fps/120fps touch scroll performance."""
        self.assertIn("window.addEventListener('touchstart', () => {}, { passive: true });", self.content)
        self.assertIn("window.addEventListener('touchmove', () => {}, { passive: true });", self.content)
        self.assertIn("chartWrapper.addEventListener('touchstart'", self.content)
        self.assertIn("chartWrapper.addEventListener('touchmove'", self.content)

    def test_lighting_and_material_integrity(self):
        """Verify 4K PBR lighting and specular traversal matching reference image 2."""
        self.assertIn("renderer.toneMappingExposure = 1.18;", self.content)
        self.assertIn("ambientLight = new THREE.AmbientLight(0xfffaed, 0.9);", self.content)
        self.assertIn("keyLight = new THREE.DirectionalLight(0xfff3db, 2.6);", self.content)
        self.assertIn("rimLight = new THREE.DirectionalLight(0xf1e0d0, 2.2);", self.content)
        self.assertIn("shieldFill = new THREE.PointLight(0x2ee59d, 1.4, 15);", self.content)
        self.assertIn("gearLight = new THREE.PointLight(0xf1d2a9, 1.8, 5);", self.content)
        self.assertIn("child.material.roughness = Math.max(child.material.roughness, 0.32);", self.content)
        self.assertIn("child.material.metalness = Math.min(child.material.metalness, 0.88);", self.content)

    def test_mobile_navigation_drawer_and_overlay(self):
        """Verify mobile navigation toggle button and backdrop-blurred quick-menu overlay."""
        self.assertIn('id="mobile-menu-toggle"', self.content)
        self.assertIn('id="mobile-nav-overlay"', self.content)
        self.assertIn('id="mobile-nav-panel"', self.content)
        self.assertIn('id="mobile-nav-close"', self.content)
        self.assertIn('id="mobile-menu-icon"', self.content)
        self.assertIn('openMobileMenu', self.content)
        self.assertIn('closeMobileMenu', self.content)
        # Verify quick links to all 6 core destinations
        overlay_match = re.search(r'id=["\']mobile-nav-overlay["\'][\s\S]*?</div>\s*</div>', self.content)
        self.assertIsNotNone(overlay_match)
        overlay_html = overlay_match.group(0)
        self.assertIn('href="#storyline-stage"', overlay_html)
        self.assertIn('href="#architecture"', overlay_html)
        self.assertIn('href="#ingestion"', overlay_html)
        self.assertIn('href="#solutions"', overlay_html)
        self.assertIn('href="#agents"', overlay_html)
        self.assertIn('href="#pricing"', overlay_html)

    def test_act4_mobile_centering_and_backdrop_blur(self):
        """Verify Act IV card is centered on mobile with px-4 md:pl-20 and max-w-md mx-auto md:mx-0."""
        self.assertIn('id="act-4-view"', self.content)
        act4_match = re.search(r'<div[^>]+id=["\']act-4-view["\'][\s\S]*?</div>\s*</div>', self.content)
        self.assertIsNotNone(act4_match)
        act4_html = act4_match.group(0)
        self.assertIn('px-4 md:pl-20', act4_html)
        self.assertIn('max-w-md', act4_html)
        self.assertIn('mx-auto md:mx-0', act4_html)
        self.assertIn('backdrop-blur-2xl', act4_html)

    def test_pricing_cards_mobile_stacking_and_padding(self):
        """Verify pricing cards stack naturally on mobile with flex-col lg:flex-row and generous padding."""
        self.assertIn('flex-col lg:flex-row', self.content)
        self.assertIn('p-6 sm:p-8', self.content)

    def test_apple_hig_44px_touch_targets(self):
        """Verify Apple HIG 44px+ touch target classes across mobile interactive elements."""
        self.assertIn('min-h-[44px]', self.content)
        self.assertIn('min-w-[44px]', self.content)
        self.assertIn('min-h-[48px]', self.content)


class TestRootLandingPageElevation(TestLandingPageElevation):
    """Ensure stitch_ai_agency_platform_website/aethelgard_1300s_gothic_ai_sovereign_landing_page.html passes all tests."""
    @classmethod
    def setUpClass(cls):
        cls.root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.landing_path = os.path.join(
            cls.root_dir,
            "stitch_ai_agency_platform_website",
            "aethelgard_1300s_gothic_ai_sovereign_landing_page.html"
        )
        with open(cls.landing_path, "r", encoding="utf-8") as f:
            cls.content = f.read()


if __name__ == '__main__':
    unittest.main()
