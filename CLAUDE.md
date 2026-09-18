# CLAUDE.md — Aethelgard Sovereign Autonomous Multi-Agent OS
> **Everything Claude Code (ECC) Architectural Specification & Coding Standards**

## System Identity & Core Lore
- **Project Designation:** Aethelgard — Sovereign Multi-Agent Atelier & B2B Autonomous Guild
- **Core Mission:** Completely replace traditional $10k–$15k/month human creative agencies, web developers, and front-office executive receptionists with a consecrated guild of 10 autonomous AI agents.
- **Visual Aesthetic:** **Obsidian Verdant Aethelgard** (Sovereign Dark Atelier / Illuminated Medieval-Tech Alchemical).

---

## 1. Visual & Frontend Invariants

### 1.1 Palette Standard (Strict Invariants)
- **Deep Obsidian Void:** `#070B08` (Base canvas background. NEVER use pure black `#000000` or generic gray `#1F2937`).
- **Dark Moss-Slate Glass:** `#111A14` to `#16231B` (Card surfaces, panels, toolbars).
- **Antique Gilded Brass Linework:** `#C5A059` / `#D4AF37` (1px borders, crests, heraldic sigils, primary display accents).
- **Luminous Ethereal Mint:** `#2EE59D` (Active agent pulse runes, verified conversion badges, CTA buttons).
- **Dragon Amber:** `#F59E0B` (High-priority telephony alerts, caller escalation).
- **Parchment Primary Text:** `#E6E4DD` (Strictly maintained at $\ge 7.0:1$ WCAG AAA contrast ratio on dark surfaces).

### 1.2 Typography Hierarchy
- **Headings & Display:** `Cinzel`, `Cormorant Garamond`, or `Trajan Pro` (Roman chiseled serif style).
- **Body & Copy:** `Inter` (High-legibility sans-serif with 4px/8px rhythm).
- **Telemetry & Financials:** `JetBrains Mono` (Cryptographic ledgers, token counts, timestamps).

### 1.3 Apple Design System & Emil Kowalski Interaction Physics
- **Continuous Curvature (Squircle) Law:** $R_{\text{inner}} = R_{\text{outer}} - \text{Padding}$. Master bento: `rounded-[28px]` to `rounded-[32px]`, cards: `rounded-[20px]`, inner buttons: `rounded-[12px]`.
- **Dual Specular Rim Lighting:** Never use flat 1px gray borders. Dark mode surfaces must feature `box-shadow: inset 0 1px 1px 0 rgba(255, 255, 255, 0.15), 0 10px 30px -10px rgba(0, 0, 0, 0.5); border: 1px solid rgba(255, 255, 255, 0.08);`.
- **Spring Physics for Direct Manipulation:** Buttons and cards MUST support Emil Kowalski spring physics (`stiffness: 400-500, damping: 25-30, mass: 0.8`) with `active:scale-[0.98]`.
- **50% Faster Exits:** Entrances 300ms–400ms (`cubic-bezier(0.16, 1, 0.3, 1)`), exits 150ms–200ms (`cubic-bezier(0.4, 0, 1, 1)`).
- **21st.dev Component Patterns:** Bento grids, mouse-following radial cursor spotlight glows, 4-phase scroll-based storylines (`animation-timeline: view()`), and generative 60fps canvas fallbacks for hero video elements.
- **SPA DOM Invariants:** Strictly 0 duplicate IDs and 0 duplicate HTML tag attributes (to prevent browsers dropping classes). Always expose onclick handlers to `window`.
- Use **Anime.js** for SVG stroke drawing (`strokeDashoffset`) of circular seals and numeric metric scrubbing.
- Use **Motion** (`motion.dev` CDN bundle) for vanilla and React spring physics and layout transitions.
- Use **Shape Dividers** (`shapedivider.app`) for smooth curved SVG section transitions.
- Use **Bklit** radial mesh lighting + SVG noise grain dithering to prevent color banding.

### 1.4 Generative UI (Stitch) & Pinned Spatial 3D Scrollytelling
- **Generative UI Prompting Law:** Avoid coordinate micromanagement (`width: 320px`). Guide generative engines via relational spatial hierarchy (60/40 splits, 12-col bento grids), concrete sensory tokens (Obsidian `#070B08`, Warm Platinum `#D4C4B5`, Mint `#2EE59D`), and gravitational anchoring (`sticky top-0 h-screen`, `fixed left-8 top-1/2`).
- **Pinned 3D Spatial Transition Law (Louvre Reference):** Multi-act narrative landings must anchor inside a `sticky top-0 h-screen overflow-hidden` container within a multi-screen track (`h-[400vh]`). The central object remains persistent on stage and reframes via 3D transforms (`translate3d`, `scale3d`, `rotate3d`), backed by parallax vertical hairlines.
- **Synchronized Minimalist Side Rail:** Fixed vertical rail (`fixed left-8 top-1/2 -translate-y-1/2`) with an illuminated active dash indicator tracking spatial camera anchors.
- **Tabular Numeric Invariant:** All count-up metric tickers and financial ledgers MUST specify `font-variant-numeric: tabular-nums` / `font-mono tabular-nums` to eliminate character width shifts and layout jitter.
- **Fluid Splines & Waveforms:** Attribution charts must utilize continuous cubic Bézier splines with magnetic crosshairs, and telephony receptionists must render 60fps dual-color audio waveform frequency visualizers.

### 1.5 1300s Gothic AI Aesthetic, Medieval Agent Iconography & Taste-Skill Heuristics
- **1300s Illuminated Manuscript Agent Artworks:**
  - **Valerius the Herald:** 14th-century herald blowing a long golden trumpet bearing a pennon inscribed *"AUDITE! ET ANUNCIO PACEM"*, standing in an illuminated archway (`assets/images/valerius_the_herald_1300.png`).
  - **Solon & The Conclave:** 1300s monastic magistrate holding the scales of justice and *"CODEX IURIS CANONICI"* alongside an enthroned crowned monarch (`assets/images/solon_and_the_conclave_1300.png`).
  - **Daedalus the Master Mason:** 1300s medieval architect with drafting compass and parchment scroll of *"GEOMETRIA SACRA"* against a soaring Gothic cathedral (`assets/images/daedalus_the_architect_1300.png`).
- **Procedural 1364 Giovanni Dondi *Astrarium* 3D Scene:**
  - Built purely in Three.js procedural geometry (0 external `.gltf` asset dependencies) to eliminate preview canvas crashes.
  - Composed of: central warm ivory neural lumen (`IcosahedronGeometry`), tri-axial astrolabe rings (`TorusGeometry` in gilded brass `#D4C4B5` and dark iron `#1C1B1B`), interlocking spur gears (2:1 ratio), 6 pointed Gothic cathedral arches, and stardust field.
  - Strictly container-locked: `<canvas>` scoped inside `#threejs-spatial-stage` with `position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none;`. Never append to `document.body`.
  - Initial state enforcement: At `scrollY < 80px`, Act I is strictly active (`opacity-100`, `pointer-events-auto`, `display: flex`) to prevent blank void capture during Stitch screenshots.
- **Taste-Skill Anti-Slop Heuristics (`leonxlnx/taste-skill`):**
  - **Hard Viewport Hero:** Complete hero message and primary CTAs enclosed inside 100vh. Subtext strictly $\le 20$ words.
  - **Em-Dash Ban:** The em-dash (`—`) is completely forbidden across headlines, subtitles, and pull quotes.
  - **1-in-3 Eyebrow Rule:** Limit uppercase tracking tags to at most 1 every 3 sections.
  - **Italic Descender Clearance:** Always specify `leading-[1.18] pb-1` on italic serif headings so descenders on `g, y, p` are never clipped.
  - **Emil Kowalski Micro-Interactions:** Fast spring compressions (`stiffness: 120, damping: 18, mass: 0.8`) with tactile `active:scale-[0.98]`.

---

## 2. The 10 Sovereign Agents & Responsibilities

1. **Daedalus the Architect:** Autonomous product intake; generates high-converting landing pages and websites in Tailwind/React in 60s.
2. **Valerius the Herald:** 24/7 AI Voice Concierge & Telephony Receptionist; handles WhatsApp Voice, Telegram, and phone calls; qualifies callers and books calendar appointments.
3. **Aurelius the Scribe:** Omnichannel content generation (LinkedIn carousels, articles, thought leadership).
4. **Hephaestus the Artificer:** Media synthesis (FLUX image assets, ElevenLabs audio, Runway Gen-3 video).
5. **Solon the Lawgiver:** Brand voice enforcement, compliance verification, claim substantiation.
6. **Pythagoras the Arbiter:** Marketing performance telemetry, CTR/CPA tracking, closed-loop prompt optimization.
7. **Hermes the Courier:** Omnichannel publishing schedule and dispatch pipeline.
8. **Argus the Sentinel:** Real-time system health, API uptime monitoring, anomaly detection.
9. **Justinian the Steward:** Token ledger auditing, subscription billing, credit replenishment.
10. **The Conclave Conductor:** Meta-orchestrator coordinating all sovereign agents.

---

## 3. Telephony & WhatsApp Protocol Invariants (OpenWA)

- **Library:** `@open-wa/wa-automate` (OpenWA headless multi-device client).
- **Inbound Call Handling:**
  1. Inbound voice calls must be intercepted immediately.
  2. Valerius declines the call gracefully and triggers an automated priority ring sequence.
  3. Valerius dispatches an instant Push-to-Talk (PTT) Opus audio note synthesized via ElevenLabs Turbo v2.5 ("Marcus" British Baritone).
- **Transcription:** Inbound voice notes and caller speech are transcribed via **Deepgram Nova-2** with $<300\text{ms}$ latency.
- **Calendar Consecration:** Confirmed demo or consultation slots must immediately write to the executive Google Calendar with client phone and notes.

---

## 4. Custom Slash Commands

- `/consecrate-page <product-url-or-spec>`: Triggers Daedalus to synthesize a live landing page blueprint in Obsidian Verdant styling.
- `/telephony-audit`: Audits Valerius's OpenWA connection status, recent call transcripts, and calendar bookings.
- `/token-ledger`: Computes live token burn rate and remaining runway across Gemini, Claude, and ElevenLabs APIs.
- `/contrast-check`: Runs WCAG 2.1 AAA luminance checks on all active CSS color variables.

---

## 5. Development & Verification Commands

```bash
# Install all required frontend, animation, and telephony packages
npm install @open-wa/wa-automate @deepgram/sdk elevenlabs-node motion animejs tailwindcss lucide-react googleapis

# Run local development server
npm run dev

# Run unit and contract tests
npm test

# Build production artifacts
npm run build
```
