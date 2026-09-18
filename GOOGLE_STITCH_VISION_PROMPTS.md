# AETHELGARD — GOOGLE STITCH Generative UI Prompts Suite
> **Enterprise Vision, Sensory Aesthetic Architecture & Modular Screen Prompts**  
> *Ready to Copy-Paste Directly into Google Stitch / Generative UI Studios*

---

## Table of Contents
1. [Master Aesthetic Architecture & Global Design Tokens](#1-master-aesthetic-architecture--global-design-tokens)
2. [Prompt 01: Flagship Sovereign Landing Page](#2-prompt-01-flagship-sovereign-landing-page)
3. [Prompt 02: Sovereign Command Cockpit (Master CRM Dashboard)](#3-prompt-02-sovereign-command-cockpit-master-crm-dashboard)
4. [Prompt 03: Valerius the Herald — AI Telephony & Voice Studio](#4-prompt-03-valerius-the-herald--ai-telephony--voice-studio)
5. [Prompt 04: Daedalus the Architect — Autonomous Product Web Studio](#5-prompt-04-daedalus-the-architect--autonomous-product-web-studio)
6. [Prompt 05: Aurelius the Scribe — Thought Leadership & Carousel Studio](#6-prompt-05-aurelius-the-scribe--thought-leadership--carousel-studio)
7. [Prompt 06: Argus the Watcher — Closed-Loop Telemetry & Attribution Radar](#7-prompt-06-argus-the-watcher--closed-loop-telemetry--attribution-radar)
8. [Prompt 07: Agent SLAs, Guardrails & Tone Matrix Studio (ECC)](#8-prompt-07-agent-slas-guardrails--tone-matrix-studio-ecc)
9. [Prompt 08: The Omnichannel Chronicle — Booked Audiences Calendar](#9-prompt-08-the-omnichannel-chronicle--booked-audiences-calendar)
10. [Prompt 09: Client Onboarding & Product DNA Intake Portal](#10-prompt-09-client-onboarding--product-dna-intake-portal)
11. [Prompt 10: Mobile Executive Companion App (iOS Native Luxury)](#11-prompt-10-mobile-executive-companion-app-ios-native-luxury)

---

## 1. Master Aesthetic Architecture & Global Design Tokens

> **Copy-Paste this section into Google Stitch as your "Global Design System" or "Master Theme Guidelines" before generating individual screens.**

### Aesthetic Persona: "Obsidian Verdant Citadel"
An ultra-luxurious, futuristic neoclassical B2B SaaS interface fusing **Apple Pro Hardware industrial precision**, **high-end Swiss watchmaking**, and **ancient royal cartography**. Dark, luminous, authoritative, and whisper-quiet. Not a toy, not generic SaaS; a high-ticket $100,000/year sovereign intelligence sanctuary.

### Color Palette Tokens
- **Deep Void Base:** `#070B08` (Darkest obsidian abyss, rich green undertones, non-fatiguing)
- **Moss & Citadel Glass:** `#0B130E` (Surface card backgrounds), `#111A14` (Elevated modals), `#16241C` (Hover active states)
- **Celestial Gold (Accents & Heraldry):** `#C5A059` (Primary gold), `#EAD7A6` (Illuminated text highlights), `#8A6926` (Filigree borders)
- **Sovereign Mint (Action & Telemetry):** `#2EE59D` (Vibrant electric mint), `#75F5C6` (Data pulses), `#059669` (Deep green pills)
- **Atmospheric Border & Glass Highlights:** `rgba(197, 160, 89, 0.22)` (Subtle gold hairline strokes), `rgba(255, 255, 255, 0.08)` (Specular top edge rims)

### Typography Hierarchy
- **Display & Heraldic Titles:** Neoclassical High-Contrast Serif (e.g. *Cinzel*, *Cormorant Garamond*, or *Editorial New*). Tracking: Wide (`tracking-widest` to `tracking-tight`), uppercase accents.
- **Ergonomic Reading & Body UI:** Precision Modern Sans (e.g. *Plus Jakarta Sans*, *Inter*, or *SF Pro Display*). Weight: 300 to 500. Crisp readability on deep obsidian backgrounds.
- **Telemetry, Code & Metrics:** Monospaced High-Tech Sans (e.g. *JetBrains Mono*, *Space Mono*). Used for latency, token rates, hashes, and mathematical figures.

### Apple UI/UX Mathematical Laws
- **Continuous Squircle Curvature:**
  $$\text{Radius}_{\text{inner}} = \text{Radius}_{\text{outer}} - \text{Padding}$$
  - Master Bento Grid Containers: `rounded-[28px]` to `rounded-[32px]`
  - Standard Interior Cards: `rounded-[20px]` to `rounded-[24px]`
  - Nested Controls & Badges: `rounded-[10px]` to `rounded-[14px]`
- **Dual Specular Rim Lighting:** Every card must feature an ultra-subtle top-inner highlight simulating real optical glass:
  ```css
  box-shadow: inset 0 1px 1px 0 rgba(255, 255, 255, 0.15), 0 20px 50px rgba(0, 0, 0, 0.7);
  border: 1px solid rgba(197, 160, 89, 0.22);
  ```
- **Emil Kowalski Physics:** All springs feel weighted and responsive. Snappy buttons (`stiffness: 450, damping: 35`), fluid cards (`stiffness: 280, damping: 28`), and exit animations that vanish 50% faster than entrances.

---

## 2. Prompt 01: Flagship Sovereign Landing Page

```markdown
Role & Context:
Design a world-class, ultra-luxury B2B SaaS landing page for "Aethelgard" — an autonomous AI Agency Platform where a guild of 9 specialized autonomous agents replace traditional human agencies ($10k-$25k/mo retainers) with instant product web synthesis, 24/7 inbound duplex phone call answering, and closed-loop ROI attribution.

Visual Atmosphere & Theme:
- Theme: Obsidian Verdant Citadel (Deep obsidian void #070B08, dark moss glass #0B130E, celestial gold #C5A059, vibrant mint #2EE59D).
- Header: Floating glassmorphic navigation with heraldic crest, executive nav items ("Storyline", "Voice Engine", "3D Architecture", "Deep Inspection", "Economics"), live status indicator ("IX Swarm Nodes Active"), and a glowing action button "Enter Sanctum".

Section 1: Hero Stage & 4K Sovereign Video Player
- An expansive, cinematic hero header with monumental typography: "Autonomous Intelligence. Cast in Sovereign Loyalty."
- Floating luxury CTA buttons: "Consecrate Your Guild Tier" (mint glow), "Launch Command Cockpit" (gold border), and "Live Inbound Telephony Demo".
- The Hero Visual Showcase: A 16:9 cinematic video viewport framed in dark brushed obsidian with golden corner filigree accents.
  - Video content: Dark high-resolution system visualization showing real-time network graphs and glowing nodes.
  - Ambient Glow Reflection: Behind the video frame, a soft, blurred dynamic ambient canvas radiates glowing emerald and gold light reflecting video highlights.
  - Glassmorphic HUD Player Controls:
    - Top Status Bar: "● SOVEREIGN SYSTEM REEL // 4K 60FPS" with "2160p HDR" and live token throughput ("1,420 Tokens/sec").
    - Center Overlay: Floating glass play/pause trigger with glowing pulsing aura.
    - Bottom Deck: Play/pause button, animated sound equalizer waves next to audio toggle, progress scrubber bar, live duration (00:14 / 01:30), 4 chapter navigation pills ([01 Inbound Call], [02 Web Generation], [03 Conclave], [04 Closed-Loop ROI]), and fullscreen icon.
- Trust Ticker Bar: 4 executive badges ("100% Zero Prompt Drift", "<60s Edge Deploy", "24/7/365 Vigilant Telephony", "10x Retainer Cost Arbitrage").

Section 2: Scroll-Driven Operational Storyline ("4 Acts")
- An interactive two-column scroll experience tracking a lead from raw ingestion to closed-loop scale.
- Left Column (Sticky Pinned Cockpit):
  - A glowing circular Astrolabe Dial with a rotating celestial needle indicator, current act badge ("ACT 01 // INTAKE"), and a vertical progress rail tracking depth (25% to 100%).
- Right Column (Narrative Milestone Cards connected by an illuminated vertical circuit line):
  - Act I: Product DNA Vectorization (85,000 Tokens/s parsing pitch decks and whitepapers into Qdrant vault in 4.2s).
  - Act II: Daedalus Autonomous Web Compilation (<60s Edge deploy with 100/100 Lighthouse score).
  - Act III: Valerius Duplex SIP Voice Concierge (142ms phone answer speed, natural British Baritone voice, direct Google Calendar booking).
  - Act IV: Argus Attribution Radar & Prompt Optimization (Continuous Bayesian gradient tuning, +38.4% conversion lift).

Section 3: Hover-Based Reveal Bento Grid (21st.dev Spotlight & 3D Tilt)
- An asymmetric bento grid of the 4 core AI studios with mouse-following radial cursor spotlight glows and 3D card perspective tilt.
- Top Toggle: "Executive Surface" vs "Under-The-Hood Peel" mode.
- Each bento card has an executive front face that peels upward on hover to reveal an under-the-hood technical inspection drawer:
  - Studio I (Valerius Voice): Peels to reveal live SIP audio packet hex buffer (4F 12 AA 99...) and Deepgram Nova-2 streaming JSON transcript.
  - Studio II (Daedalus Web): Peels to reveal live Tailwind AST compilation tree with zero CLS score.
  - Studio III (Vector Vault): Peels to reveal an interactive 3D Cosine Affinity Matrix with AES-256 cryptographic seal.
  - Studio IV (Attribution Radar): Peels to reveal live Bayesian loss optimization equations and gradient descent feed.

Section 4: 5-Layer 3D Isometric Exploded Object Breakdown
- An interactive 3D architectural deconstruction of the deterministic agent engine.
- Visual Stage: An isometric chassis showing 5 stacked subsystem plates floating along the vertical Z-axis:
  - Plate 1 (Top): Valerius Duplex SIP Telephony Transceiver (142ms)
  - Plate 2: Daedalus Neural Web Layout Compiler (48s)
  - Plate 3: Hermes Event Stream Multiplexer (Kafka/WebSockets 8ms)
  - Plate 4: Qdrant Ontological Vector Vault (AES-256)
  - Plate 5 (Base): Argus Bayesian Loss Arbiter (Real-time gradient optimization)
- Interactive Controls:
  - Z-Axis Explosion Depth Slider (0% assembled solid block to 100% fully exploded).
  - 3D Angle Preset Buttons: "Isometric 3D", "Front Elevation", "Top-Down Plan".
  - Subsystem Spec Sheet: Displays real-time Bill of Materials (BOM) economics ($0.0084/call, $0.0210/deploy), latency SLAs, and tunable runtime parameter sliders.

Section 5: Interactive Enterprise ROI Arbitrage Calculator & Tier Pricing
- Dynamic sliders for "Current Agency Retainers" ($5k - $50k/mo) and "Inbound Call Volume".
- Real-time calculator showing estimated monthly savings (e.g. "$142,800 Annual Net Savings, 96.8% Gross Margin").
- Tiers: Sanctum Pro ($349/mo), Citadel Sovereign ($899/mo), and Sovereign Enterprise Conclave (Custom BYOK / Dedicated VPC).
```

---

## 3. Prompt 02: Sovereign Command Cockpit (Master CRM Dashboard)

```markdown
Role & Context:
Design the master executive command dashboard ("The Sovereign Command Cockpit") for C-suite executives and agency founders to monitor their fleet of autonomous AI agents, live telephone calls, active pipeline deals, and system health in real-time.

Visual Topology & Layout:
- Left Navigation Sidebar: Fixed 72-width obsidian glass bar with heraldic crest, workspace switcher ("Aethelgard Prime"), quick status badge ("● All 9 Nodes Consecrated"), and navigation menu with active gold indicator pills:
  - 01 The Sovereign Cockpit (Active)
  - 02 Valerius the Herald (Voice Concierge)
  - 03 Daedalus the Architect (Web Studio)
  - 04 The Chronicle (Omnichannel Calendar)
  - 05 Aurelius the Scribe (Thought Leadership)
  - 06 Argus the Watcher (Attribution Radar)
  - 07 Agent SLAs & Tone Tuning (ECC Spec)
  - Consecrate New Task CTA (+ button)
  - User profile with encrypted tenant key ("Vault: AES-256")
- Top Header Bar: Search bar with keyboard shortcut (⌘K), real-time token throughput counter ("1,420 Tok/s"), active carrier SIP status ("Duplex Active"), and notification center with pending calendar booking badges.

Core Dashboard Modules:
1. Executive KPI Runes (4 Bento Cards):
   - Inbound Telephony Intercepts: "148 calls" (+34% vs baseline, 142ms average answer latency).
   - Autonomous Web Landers: "12 live portals" (100/100 Lighthouse, deployed to Cloudflare Edge).
   - Qualified Pipeline Sealed: "$348,000" (42 Google Calendar slots consecrated).
   - Retainer Arbitrage Lift: "$42,800/mo saved" (vs traditional agency overhead).

2. Live Swarm Operational Canvas:
   - A multi-node agent orchestration visualizer showing real-time pulses between Valerius, Daedalus, Aurelius, and Argus.
   - Status indicators: Active generation, listening, compiling, recalibrating.

3. Enterprise Covenant Pipeline (Active Deals Table):
   - Columns: Client Organization, Assigned Autonomous Agent, Deal Value, Touchpoint Channel (WhatsApp, SIP Phone, Web Form), Telephony Sentiment Score, and Status Pill ("Sealed", "In Negotiation", "Escrow Consecrated").
   - Realistic deals: "Apex Capital ($180k)", "CloudShield Global ($340k)", "Solaria Energy ($95k)".

4. Real-time Telephony & System Event Stream:
   - Live streaming terminal log showing timestamped micro-actions:
     - "[14:22:04] Valerius answered incoming SIP trunk (+1 415 882-9011) — 138ms TTFB"
     - "[14:22:18] Prospect qualified: Budget > $50k • Google Calendar token generated"
     - "[14:22:42] Argus recalibrated upstream prompt vector #892 (+4.2% dwell lift)"
```

---

## 4. Prompt 03: Valerius the Herald — AI Telephony & Voice Studio

```markdown
Role & Context:
Design an ultra-modern, high-ticket AI Voice & Inbound Telephony Control Center for "Valerius the Herald" — an autonomous voice concierge that intercepts inbound phone calls, WhatsApp voice notes, and carrier SIP trunks with sub-150ms latency, handles intricate qualification, and books calendar appointments.

Visual Style:
- Dark emerald glass, brushed obsidian steel, and warm amber gold signal lines.
- Dual-pane layout: Live Telephony Call Console on the left; Deep Session Debrief, Transcript & Audio Spectrum on the right.

Module 1: Live Voice Telephony Transceiver
- Carrier status header: "SIP Duplex Protocol v4.2 • ElevenLabs British Baritone Turbo • Deepgram Nova-2 STT".
- Active Call Card:
  - Caller ID: "Julian Sterling — Managing Partner, Sterling & Vance Capital"
  - Live Call Timer: "02:44" with subtle pulse ring.
  - Interactive Duplex Audio Spectrum: Real-time animated vertical wave bars tracking caller audio (gold) vs agent response audio (mint).
  - Live Interruption Sensitivity & VAD Threshold indicator ("Silero VAD: 24ms").
  - Actions: "Mute Agent", "Force Escalate to Human", "Trigger Calendar Seal", "End Session".

Module 2: Real-time Streaming Transcript & Intent Graph
- Chat-style speech bubble stream with millisecond latency stamps:
  - Prospect: "Can your system handle high-volume inbound leads from our London campaign without drop-off?"
  - Valerius (142ms response): "Indeed, Julian. Our edge infrastructure concurrently terminates up to 5,000 carrier SIP trunks with zero latency degradation. Shall I secure Thursday at 2 PM GMT on your calendar to review our SLA benchmarks?"
- Entity & Qualification Extraction Box:
  - Extracted Budget: "$50,000 - $100,000" (Badge: High Intent)
  - Timezone: "GMT+1 (London)"
  - Sentiment Score: "98.4% Confidence"
  - Calendar Slot Proposed: "Thursday, Oct 24 @ 14:00 GMT" (Badge: Consecrated)

Module 3: Omnichannel Lead Interceptor (WhatsApp Audio & SIP Trunks)
- Switcher tabs: "Direct SIP Cellular Trunks", "WhatsApp Business Audio API", "WebRTC Web Widget".
- Configurable Voice Persona Controls:
  - Voice Model Selector (British Baritone Executive, Silicon Valley Challenger, Institutional Advisor).
  - Latency Budget Slider (120ms - 350ms).
  - Guardrail Strictness Slider (95.0% - 99.99% zero-hallucination threshold).
```

---

## 5. Prompt 04: Daedalus the Architect — Autonomous Product Web Studio

```markdown
Role & Context:
Design the creative and technical workstation for "Daedalus the Architect" — an autonomous AI web studio that ingests raw product whitepapers, Figma URLs, or plain-text specifications and compiles complete, edge-rendered, high-converting Astro + Tailwind landing pages in under 60 seconds.

Layout & Workspace:
- Three-column IDE-style layout: Prompt & Spec Intake Drawer (Left), Live Interactive Responsive Canvas (Center), Technical AST & Edge Inspector (Right).

Module 1: Spec Intake & Neural Layout Engine (Left Panel)
- Client Brand Spec input field: "Paste product URL, raw PDF whitepaper, or brand guidelines...".
- Extracted DNA Summary: Color tokens, target ICP (Enterprise B2B), core value proposition, key objections.
- Autonomous Design System Generator: Visual swatch cards showing generated palette, typography pairing, and component style.
- "Compile & Deploy to Edge" monumental action button with estimated build time ("48.2s").

Module 2: Live Responsive Canvas (Center Viewport)
- Top Viewport Switcher Toolbar: Desktop (1920px), Tablet (768px), Mobile (375px), and Zoom level controls.
- Interactive rendered iframe / preview card displaying the live-generated landing page with working navigation, hero section, bento cards, and interactive forms.
- Interactive hover inspectors allowing the user to click any section to view autonomous design rationale.

Module 3: Edge Build & Lighthouse Telemetry (Right Panel)
- Core Web Vitals Scorecard:
  - Performance: 100 / 100
  - Accessibility: 100 / 100
  - Best Practices: 100 / 100
  - SEO: 100 / 100
  - Cumulative Layout Shift (CLS): 0.000 (Pure Zero)
- Cloudflare Edge Global Deployment Status: 284 PoPs worldwide, SSL certified, custom domain routing (`portal.clientbrand.com`).
- Live Tailwind AST Code Stream: A collapsible syntax-highlighted code drawer showing clean semantic HTML and Tailwind tokens.
```

---

## 6. Prompt 05: Aurelius the Scribe — Thought Leadership & Carousel Studio

```markdown
Role & Context:
Design the luxury thought leadership workstation for "Aurelius the Scribe" — an autonomous AI agent that analyzes industry trends and customer telemetry to generate high-converting LinkedIn 7-slide PDF carousels, contrarian executive epistles, and teleprompter video scripts.

Layout & Visual Structure:
- Split-screen studio: Pillar & Strategy Selection on the left; Live 7-Slide Carousel Visual Previewer in the center; Executive Markdown & Teleprompter Editor on the right.

Module 1: Strategic Content Pillar Selector
- 4 Clickable Strategic Pillars:
  - 01 The Contrarian Paradigm Shift (Market Disruption)
  - 02 Architectural Teardown (Cyclical State Machines vs Human Agencies)
  - 03 Unit Economics & ROI Arbitrage ($14 Acquisition vs $180 Baseline)
  - 04 Zero-Human Operational Autonomy (Duplex SIP Telephony)
- Format Selector Tabs: "LinkedIn 7-Slide Carousel (PDF)", "Executive Epistle / Long-form Post", "Video Script & Teleprompter", "X Autonomous Thread".

Module 2: Interactive 7-Slide Carousel Previewer (Center Stage)
- A realistic, presentation-grade dark emerald & gold slide viewer displaying Slide 3 of 7:
  - Slide dimensions: 1080x1350 (4:5 LinkedIn vertical aspect ratio).
  - Slide styling: Deep moss green background, gold foil header typography, crisp explanatory body copy, custom data diagram, and author avatar pill ("Aurelius Conclave AI").
  - Navigation Controls: Previous Slide (‹), Next Slide (›), Scrubber dots, and "Export Vector PDF" button.

Module 3: Executive Post Editor & Teleprompter
- Clean markdown editor displaying the accompanying LinkedIn text hook and formatted post.
- Estimated dwell score: "94.2% High Engagement".
- Action Deck: "Copy Markdown", "Generate Voiceover (ElevenLabs)", "Schedule in Chronicle Calendar".
```

---

## 7. Prompt 06: Argus the Watcher — Closed-Loop Telemetry & Attribution Radar

```markdown
Role & Context:
Design an ultra-sophisticated closed-loop telemetry analytics radar for "Argus the Watcher" — the sensory intelligence engine that tracks visitor dwell time, phone conversation sentiment, and closed revenue, then uses Bayesian loss gradients to autonomously recalibrate upstream agent prompts.

Visual & Graphical Language:
- Silky smooth, glowing cubic spline curves on an obsidian coordinate grid.
- No rigid clunky line charts. Apple Health / TradingView precision aesthetic with soft gradient area fills.

Module 1: Silky Multi-Channel Spline Attribution Radar
- Timeframe Switcher: "Last 7 Days", "Last 30 Days", "Quarterly Arc".
- 4 Glowing Spline Curves with interactive clickable toggles:
  - Emerald Mint Curve: Aurelius Content & Carousels (Impressions & Dwell Time)
  - Amber Gold Curve: Valerius Voice Inbound Telephony (Call Volume & Converted Demos)
  - Cyan Teal Curve: Daedalus Web Portals (Visitor Traffic & Conversion Rates)
  - Violet Purple Curve: Closed-Loop Revenue Attribution ($ ARR)
- Interactive Magnetic Crosshair:
  - Hovering across the chart tracks mouse position with a vertical dashed line snapping to days (Mon - Sun).
  - Floating Glassmorphic Tooltip displaying exact day metrics and peak calibration markers.

Module 2: Closed-Loop Bayesian Prompt Recalibration Engine
- Prominent Recalibration Trigger: "Recalibrate All Prompts Now" button with animated gradient border and live toast feedback.
- Live Recalibration Telemetry Feed:
  - Shows real-time vector adjustments: "ΔW_prompt = α × (∇Dwell - λLatency) • 9 Prompts Updated in 0.08s".
  - Vector Drift Guard: "99.98% Fidelity Preserved".

Module 3: Executive Conversion Metric Runes
- Dwell Time Index: "+43.2% Lift"
- Voice-to-Calendar Conversion: "35.6% Conversion Rate" (42 booked / 118 calls)
- Acquisition Cost: "$14.20 vs $180 industry baseline" (92% reduction)
```

---

## 8. Prompt 07: Agent SLAs, Guardrails & Tone Matrix Studio (ECC)

```markdown
Role & Context:
Design the governance and guardrail studio for managing autonomous agent invariants, SLAs, and personality archetypes, powered by the Everything Claude Code (affaan-m/ecc) specification.

Layout & Modules:
1. Live Tunable Behavioral Sliders:
   - Slider 1: Deterministic Rigor / Temperature (0.00 Strict to 1.00 Creative) with live numeric readout.
   - Slider 2: Guardrail Strictness (95.0% to 99.99% Zero-Hallucination Threshold) with citation requirement toggle.
   - Slider 3: SIP Voice Latency Budget (120ms to 450ms) controlling telephony interruption sensitivity.

2. Tone Matrix Archetype Selector (4 Radio Pill Cards):
   - Archetype A: "Sovereign Heraldic" (Elevated, authoritative, precision Latin-infused executive English).
   - Archetype B: "Silicon Valley Challenger" (Punchy, contrarian, high-velocity SaaS founder tone).
   - Archetype C: "Institutional Enterprise" (Risk-averse, Fortune 500 compliant, conservative).
   - Archetype D: "Technical Systems Architect" (Deep technical specifications, zero fluff, AST-focused).

3. Dynamic CLAUDE.md Code Inspector:
   - A dark syntax-highlighted code container showing the auto-generated CLAUDE.md rules and invariants in real time as the user adjusts sliders and archetypes.
   - Action: "Copy CLAUDE.md Specification" with live toast alert.

4. Interactive Sandbox Guardrail Boundary Tester:
   - Input simulation field: "Test agent boundaries with adversarial prompts...".
   - Quick preset test chips: "Guarantee 100% discount", "Ask for non-NDA financials", "Book outside business hours".
   - "Evaluate Guardrail" button showing real-time agent refusal and compliance redirection upholding strict SLA boundaries.
```

---

## 9. Prompt 08: The Omnichannel Chronicle — Booked Audiences Calendar

```markdown
Role & Context:
Design an executive drop schedule and calendar control center ("The Omnichannel Chronicle") where automated social drops (LinkedIn, X), inbound phone consultations, and product web updates are scheduled and visualized across an intuitive weekly and monthly grid.

Visual Design:
- Top Toolbar: View switcher ("Weekly Matrix", "Monthly Cadence", "Gantt Timeline"), Date range selector ("Oct 21 - Oct 27"), and Channel filter chips (LinkedIn Carousels, Inbound Telephony Demos, Web Drops, WhatsApp Sequences).
- Calendar Grid:
  - Crisp columns for Monday through Sunday.
  - Event Cards styled with dark moss backgrounds and colored left accent bars:
    - Gold Cards: Booked Executive Consultations (e.g. "Julian Sterling — $180k Deal Demo").
    - Mint Cards: Aurelius LinkedIn Carousels (e.g. "Drop: The 4-Act Agency Replacement Model").
    - Cyan Cards: Daedalus Portal Deployments (e.g. "Staging: CloudShield Enterprise Lander").
  - Hover states showing detailed attendee info, calendar RSVP status, and direct call recording links.
- Sidebar Drawer: "Unscheduled Drafts & Incoming Leads" ready to drag-and-drop directly onto the calendar.
```

---

## 10. Prompt 09: Client Onboarding & Product DNA Intake Portal

```markdown
Role & Context:
Design an elegant 4-Rite interactive onboarding wizard for enterprise clients to consecrate their brand DNA into the Aethelgard platform in under 3 minutes.

Visual Experience:
- Dual-tier header with sanctuary breadcrumbs: "Rite I: Product DNA", "Rite II: Voice Invariants", "Rite III: Channel Consecration", "Rite IV: Deployment".
- Step-by-Step Interactive Form:
  - Rite I: Brand & Product Ingestion — Drag-and-drop file uploader for pitch decks (PDF), whitepapers, or URL field for live site scraping with automated vectorization progress bar ("85k tokens/s").
  - Rite II: Brand Voice & Persona Tuning — Interactive tone sliders, forbidden phrase inputs, and SLA boundary toggles.
  - Rite III: Omnichannel Connection Hub — 1-click connectors for WhatsApp Business API, Twilio SIP trunks, LinkedIn Organization, and Cloudflare DNS.
  - Rite IV: Sovereign Consecration — Summary audit card, cryptographic tenant signature, and "Launch Guild Swarm" monumental button with animated particle celebration.
```

---

## 11. Prompt 10: Mobile Executive Companion App (iOS Native Luxury)

```markdown
Role & Context:
Design a luxury native iOS/Android mobile companion app for C-suite executives to monitor their Aethelgard autonomous agency platform on the go.

Visual Layout & Mobile Constraints:
- 393px width mobile viewport with native iOS Dynamic Island, status bar, and home indicator.
- Dynamic Island Pill: Displays live active phone call ("Valerius: Live Call (01:42) • Deal Qualified").
- Executive Hero Feed:
  - Greeting: "Good evening, Lord Chancellor."
  - Daily Revenue Lift Card: "$14,280 captured today across 6 inbound consultations".
- Instant Telephony Alert Feed:
  - Compact cards for recent inbound calls with quick play buttons for audio recordings, AI-generated call summaries, and "Accept Calendar Booking" buttons.
- Bottom Navigation Dock: 4 icons with tactile haptic glow ("Cockpit", "Voice Radar", "Chronicle", "Vault").
```

---

## How to Use These Prompts in Google Stitch

1. **Step 1:** Copy and paste the **Master Aesthetic Architecture & Global Design Tokens** (Section 1) into Stitch's project context or styling settings to lock in the Obsidian Verdant palette, typography, and squircle math.
2. **Step 2:** Choose the specific screen you want to generate (e.g., [Prompt 01: Flagship Sovereign Landing Page](#2-prompt-01-flagship-sovereign-landing-page) or [Prompt 03: Valerius Telephony Studio](#4-prompt-03-valerius-the-herald--ai-telephony--voice-studio)).
3. **Step 3:** Paste the full prompt text into Google Stitch's prompt box and trigger generation.
4. **Step 4:** Stitch will generate the high-fidelity UI components matching the Apple Pro luxury aesthetic, without being constrained by rigid pixel micromanagement.
