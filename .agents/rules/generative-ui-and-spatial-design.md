---
description: Generative UI prompt engineering (Google Stitch), pinned spatial 3D scrollytelling architecture, and synchronized tactile interface patterns.
always_on: true
---

# Generative UI & Spatial 3D Scrollytelling Rules

## 1. Generative UI Prompting Architecture (Google Stitch)
When authoring prompts for generative UI engines such as Google Stitch, never micromanage pixel coordinates or rigid dimensions (e.g. `width: 320px`, `top: 145px`). Models produce stiff, broken, non-responsive layouts under coordinate constraints.

Instead, adhere strictly to the **3 Pillars of Generative UI Prompts**:
1. **Relational Spatial Hierarchy:**
   - Define macro layout relationships: asymmetric 60/40 hero splits, 12-column bento grids, sticky viewport anchoring (`sticky top-0 h-screen`), and fixed edge rails (`fixed left-8 top-1/2`).
   - Allow the generative engine's CSS flexbox/grid engine to compute responsive fluid boundaries.
2. **Concrete Sensory & Materiality Tokens:**
   - Always supply exact hexadecimal tokens and surface behaviors:
     - Obsidian Void `#070B08` (base background)
     - Warm Platinum `#D4C4B5` (architectural hairlines and typography)
     - Ethereal Mint `#2EE59D` (active status runes and verified badges)
     - Gilded Brass `#C5A059` (heraldic accents)
     - Dual specular rim lighting (`box-shadow: inset 0 1px 1px rgba(255,255,255,0.15)`)
3. **Behavioral Invariants & State Transitions:**
   - Describe interactive states as functional behaviors: hover depth lift (`scale(1.02)`), active press damping (`scale(0.98)`), synchronized side rail tracking, and magnetic crosshair snapping.

---

## 2. Pinned Spatial 3D Scrollytelling (Louvre Exhibition Pattern)
When designing narrative multi-act landing pages, elements must NOT scroll off-screen like a standard flat document. The viewport must feel like a museum camera orbiting an anchored 3D spatial artifact:

1. **The Anchored Viewport Stage:**
   - Outer track: `relative h-[400vh]` (allocating 100vh per narrative act).
   - Inner stage: `sticky top-0 h-screen w-full overflow-hidden flex items-center justify-center`.
   - Perspective container: `perspective: 1200px; transform-style: preserve-3d;`.
2. **Persistent 3D Artifact Reframing:**
   - Centerpiece remains continuously on stage, transitioning smoothly between camera coordinates based on scroll progress:
     - **Act I (Hero):** Centered macro stance: `translate3d(0, 0, 0) scale(1.0) rotateY(0deg)`.
     - **Act II (Voice):** Shifts right into 3/4 profile: `translate3d(24vw, -2vh, 40px) scale(0.92) rotateY(-18deg)`.
     - **Act III (Studio):** Shifts left to reveal interactive canvas: `translate3d(-26vw, 0, 20px) scale(0.88) rotateY(14deg)`.
     - **Act IV (Attribution):** Recedes into high-elevation dramatic angle: `translate3d(0, -6vh, -80px) scale(0.82) rotateX(8deg)`.
3. **Parallax Architectural Hairlines:**
   - Subtle vertical hairlines (`border-r border-white/[0.04]`) translate at $0.3\times$ scroll velocity to provide cinematic spatial depth behind the artifact.

---

## 3. Tactile Synchronized Interface Components

### 3.1 Synchronized Minimalist Vertical Side Rail
- Positioned fixed along the left or right margin (`fixed left-8 top-1/2 -translate-y-1/2 z-40`).
- Features numbered nodes (`01`, `02`, `03`, `04`) with an illuminated active dash indicator (`h-6 w-0.5 bg-emerald-400`).
- Tracks scroll progress or viewport intersections bidirectionally with smooth spring interpolation.

### 3.2 Tabular Numerics for Metric Tickers
- Count-up numbers, token throughput counters, and financial ledgers MUST apply:
  ```css
  font-variant-numeric: tabular-nums;
  /* Tailwind: */
  font-mono tabular-nums
  ```
- Failure to set `tabular-nums` causes character width oscillations during numeric tweening, resulting in severe parent card jitter.

### 3.3 Silky Cubic Spline Telemetry Charts
- Telemetry curves must use continuous cubic Bézier splines (`d="M... C... S..."`), never rigid jagged polylines.
- Hover states require an interactive vertical crosshair line that magnetically snaps to discrete time increments (e.g. days), displaying an anchored glassmorphic metric card.
- Channel toggles must smoothly animate path opacity and recalculate aggregate metrics without page reloads.

### 3.4 Live Audio Waveform Visualizers
- Real-time voice concierge states (Valerius) must render dynamic dual-color frequency equalizer bars (`h-1` to `h-8`) that oscillate with randomized organic harmonic rhythms (60fps) during active speech.

---

## 4. 1300s Gothic AI Mechanical Architecture & Taste-Skill Anti-Slop Invariants

### 4.1 1300s Gothic AI 3D Clockwork (The Astrarium Pattern)
When synthesizing an AI agent visualization conceived as if engineered in the 1300s (14th century medieval alchemy and clockwork):
1. **Historical Precedents:**
   - Ground the 3D model in Ramon Llull's *Ars Magna* (concentric calculating discs, c. 1305) and Giovanni Dondi dall'Orologio's *Astrarium* (7-faced planetary astronomical clock, Padua 1364).
2. **Procedural Three.js Scene Composition (Zero External GLTF Dependencies):**
   - **Central Neural Lumen:** A faceted icosahedron (`IcosahedronGeometry`) with warm ivory interior lighting (`#F1E0D0`) pulsing gently at alchemical thought frequencies.
   - **Tri-Axial Astrolabe Rings:** Three concentric nested rings rotating in gyroscopic counter-orbits:
     - Gilded brass equator ring (`#D4C4B5`, `TorusGeometry`)
     - Tilted zodiac rete ring (23.5° ecliptic tilt, roman hour markers)
     - Forged dark iron meridian colure (`#1C1B1B`)
   - **Clockwork Gear Train:** Interlocking spur gears with brass cross-spokes and extruded spur teeth driving at precise harmonic ratios (2:1 gear reduction).
   - **Gothic Cathedral Flying Buttresses:** Six pointed cathedral arch buttresses with trefoil finials (`CylinderGeometry` + `BoxGeometry`) encasing the core like a holy mechanical reliquary.
   - **Stardust Particle Field:** Fine golden dust floating gently in the ambient space.

### 4.2 Container-Locked Three.js Invariant (No Canvas Drift)
In generative UI and preview environments (e.g. Google Stitch, nested iframes):
- **NEVER append Three.js canvas to `document.body`:** This causes canvas displacement, zero-width bounds, or z-index collisions.
- **Strict Container Binding:** Always render to an explicit `<canvas id="...">` scoped inside a parent container with:
  ```css
  position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none;
  ```
- **Guaranteed Initial State at 0px Scroll:** On page load or `scrollY < 80px`, Act I must be explicitly enforced active (`opacity-100`, `pointer-events-auto`, `display: flex`), preventing blank dark voids when generative previewers capture screenshots.
- **Responsive Resize Observers:** Attach `ResizeObserver` to the stage container to update Three.js `camera.aspect` and `renderer.setSize(w, h, false)` dynamically.

### 4.3 Taste-Skill Anti-Slop Heuristics (Anti-Generic Discipline)
Adhere to the rigorous design and typography discipline derived from `leonxlnx/taste-skill`:
1. **Hard Viewport Hero Enclosure:**
   - The primary headline, value proposition, and CTAs must all comfortably fit within the initial 100vh desktop viewport.
   - Hero explanatory subtext must be concise and disciplined: $\le 20$ words maximum.
2. **Strict Em-Dash (`—`) Ban:**
   - Never use the em-dash (`—` or `&mdash;`) in headlines, subheadings, or testimonials. Use natural sentence structure or crisp punctuation (periods, commas, colons).
3. **1-in-3 Eyebrow Restraint:**
   - Uppercase tracking labels (`text-xs uppercase tracking-[0.2em]`) must appear at most once per 3 sections. Overusing eyebrows is a signature marker of generic AI templates.
4. **Italic Descender Clearance:**
   - When using italic serif display fonts (`Cinzel`, `Cormorant Garamond`), always provide bottom clearance (`leading-[1.18] pb-1`) to prevent descenders on characters like `g`, `y`, `p`, and `q` from being clipped.
5. **Tactile Spring Compressions:**
   - Buttons and interactive cards must implement Emil Kowalski micro-spring physics (`stiffness: 120, damping: 18, mass: 0.8`) with tactile active press feedback (`active:scale-[0.98]`).

