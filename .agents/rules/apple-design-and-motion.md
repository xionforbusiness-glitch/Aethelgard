---
description: Enterprise Apple Design system tokens, Emil Kowalski interaction physics, 21st.dev patterns, and Motion integration rules.
always_on: true
---

# Apple Design Tokens, Interaction Physics & Modern Web Rules

## 1. Apple Continuous Curvature (Squircle) Law
When nesting containers and inner elements, never arbitrarily assign border radii. Always apply the optical squircle padding formula:
R_{\text{inner}} = R_{\text{outer}} - \text{Padding}
- **Master Bento Container / Modals:** rounded-[28px] to rounded-[32px]
- **Standard Cards:** rounded-[20px] to rounded-[24px]
- **Buttons & Inputs inside Cards:** rounded-[12px] to rounded-[14px] (or rounded-full)
- Mismatched radii cause corner pinching and visual amateurism.

## 2. Dual Specular Rim Lighting (Dark Mode Luxury)
Never use plain flat 1px solid gray borders. Dark mode realism requires specular edge reflections:
\\css
box-shadow: 
  inset 0 1px 1px 0 rgba(255, 255, 255, 0.15),
  0 10px 30px -10px rgba(0, 0, 0, 0.5);
border: 1px solid rgba(255, 255, 255, 0.08);
\
## 3. Emil Kowalski Interaction Physics (emilkowalski/skills)
1. **Springs for Direct Manipulation, Curves for Non-Interruptibles:**
   - Hovers, button presses, and tabs MUST use springs (stiffness: 400-500, damping: 25-30, mass: 0.8).
   - Springs never hitch or stutter when interrupted mid-flight by rapid clicks.
2. **50% Faster Exits:**
   - Entrances: 300ms-400ms (cubic-bezier(0.16, 1, 0.3, 1)).
   - Exits: 150ms-200ms (cubic-bezier(0.4, 0, 1, 1)). Fast exits respect user momentum.
3. **Active Press States:**
   - Active press scale should be subtle: scale(0.975) or scale(0.98) with transition: transform 80ms cubic-bezier(0.2, 0, 0, 1).

## 4. 21st.dev Modern Component Patterns
- **Hover Spotlight Glow:** Track cursor coordinates (x, y) relative to the card bounding box and project a smooth radial gradient.
- **Scroll-Based Storyline:** Use sticky stacking cards or CSS scroll-driven animations (animation-timeline: view()) with IntersectionObserver spring fallbacks.
- **Hero Video with Generative Canvas Fallback:** Pair hero video elements with a 60fps HTML5 particle constellation canvas fallback to guarantee 100% visual uptime in air-gapped or offline environments.

## 5. Single-Page Application (SPA) DOM Invariants
- **Zero Duplicate Tag Attributes:** Browsers silently discard subsequent attributes if an element defines duplicates. Keep attributes strictly unified.
- **Global Function Binding:** In vanilla SPAs, expose onclick handlers explicitly to window (window.switchView = switchView) to avoid scope isolation errors.
- **WCAG AAA Contrast:** Primary text >= 7:1, tabular figures must use font-mono tabular-nums.
