---
name: apple-uiux-pro
description: Apple design tokens, continuous squircle curvature math, Emil Kowalski interaction physics, 21st.dev modern component patterns, and Framer Motion integration.
---

# Apple UI/UX Pro & Motion Interaction Skill

Use this skill when building or upgrading frontend interfaces to Apple/Linear/Stripe-tier visual quality and interactive smoothness.

## Core Tokens & Mathematical Rules

### 1. Continuous Curvature (Squircle) Law
$$R_{\text{inner}} = R_{\text{outer}} - \text{Padding}$$
- Master Bento: `rounded-[28px]` to `rounded-[32px]`
- Standard Card: `rounded-[20px]` to `rounded-[24px]`
- Inner Items: `rounded-[12px]` to `rounded-[14px]`

### 2. Dual Specular Rim Lighting
```css
box-shadow: 
  inset 0 1px 1px 0 rgba(255, 255, 255, 0.15),
  0 10px 30px -10px rgba(0, 0, 0, 0.5);
border: 1px solid rgba(255, 255, 255, 0.08);
```

### 3. Emil Kowalski Interaction Constants
- **Snappy Micro (Buttons, Toggles):** `{ stiffness: 450, damping: 35, mass: 0.8 }`
- **Fluid Gentle (Drawers, Modals):** `{ stiffness: 280, damping: 28, mass: 1.0 }`
- **Hover Tilt / Bento Follow:** `{ stiffness: 220, damping: 22, mass: 0.5 }`
- **Exit Transitions:** Must be 50% faster than entrance transitions (150ms-200ms vs 300ms-400ms).

### 4. 21st.dev Component Patterns
- **Cursor Spotlight Glow:** Project smooth radial gradients centered at mouse `(x, y)`.
- **Scroll Storyline:** Sticky stacking cards or CSS `animation-timeline: view()` with intersection observer fallback.
- **Hero Video & Canvas:** Ambient 60fps particle mesh fallback when video fails or network is offline.

### 5. Vanilla Motion Integration
Include standalone production bundle:
```html
<script src="https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js"></script>
```
Use `window.Motion.animate(el, keyframes, options)`.
