# BNW3H Design QA

## Target and comparison

- Visual target: `design/concepts/06-bossa-protocol-central-brand-palette.png`
- Desktop implementation: `design/qa/desktop-morning-1600x1000.png`
- Combined comparison: `design/qa/reference-vs-implementation.png`
- Redesign comparison: `design/qa/reference-vs-redesign.png`
- Mobile states: `design/qa/mobile-morning-390x844.png`, `design/qa/mobile-hifas-390x844.png`, `design/qa/mobile-facilitator-390x844.png`
- Theme states: `design/qa/desktop-morning-1600x1000.png`, `design/qa/desktop-tarde-1600x1000.png`, `design/qa/desktop-noite-1600x1000.png`

## Fidelity and functionality

- The split Capital / Bossa Protocol / Hifas hierarchy matches the selected target.
- The official Bossa Nova3 Hub logo and supplied `[Re]3` signature are used as source assets, not reconstructed.
- Bossa Protocol is central; PCdRC is explicitly the first artifact in formation. QF / Q-ACC, RetroPGF and Governance remain labeled `Em desenho`.
- The compressed sans display system replaces the previous serif-led hierarchy and remains legible across tested breakpoints.
- Morning, afternoon and night tokens retain the orange brand dialogue while keeping capital blue and hifas orange/teal distinct.
- Mobile width 390px has zero horizontal overflow. Header, theme control, CTAs and hifa tabs maintain practical touch sizes.
- The hifa constellation now stays fully inside its frame at 1600px and 390px, with a positive gap from the supporting copy and zero page overflow.
- The global grid wallpaper was removed. Paper grain and non-repeating tonal washes now carry the poster materiality without repeating the Kalma/[Re]3 visual shortcut.
- `/` is semantically and visually Hifas-first; `/capital` is Capital-first. DOM order, heading order, navigation order and final CTA order all follow the selected persona.
- Capital uses Inter Tight as a diligence-led voice; Hifas keeps Barlow Condensed as the public call. Both retain IBM Plex Mono for status and traceability.
- Mobile menu opens, closes on selection and closes with Escape.
- Hifa tabs work with pointer and Left/Right arrow keys; keyboard selection is instantaneous.
- Artifact rows expose one active state at a time.
- No browser console warnings or errors were found.

## Motion review

| Before | After | Why |
| --- | --- | --- |
| Theme changes could flash between palettes | View Transition crossfade using opacity, 180–220ms | The occasional state change gets a short perceptual bridge without animating layout |
| Mobile theme names became cramped | M / T / N visual labels with full accessible names | Preserves 44px-scale controls and clear semantics at narrow widths |
| Nav indicator included an unused color transition | Transform-only indicator at 220ms with the strong ease-out curve | Keeps frequent navigation motion small, interruptible and GPU-friendly |
| Generic all-at-once section appearance | One-time 50ms stagger with transform + opacity | Explains reading order without blocking interaction |
| No reduced-motion path | Movement removed and opacity retained under `prefers-reduced-motion` | Keeps state legible while respecting motion preference |
| Hifa artwork used a negative top margin | Contained square frame, `object-fit: contain`, clipped overflow and positive spacing | Keeps all eight outer emblems visible without colliding with the copy or crossing the column frame |

## Accessibility

- Semantic header, navigation, main, sections and footer.
- Skip link and visible focus styles.
- Accessible names for atmosphere controls and source images.
- Keyboard-operable tabs with managed `tabindex` and `aria-selected`.
- Theme selection uses `aria-pressed`; artifact selection uses `aria-expanded`.
- Reduced-motion behavior is present.

## Redesign responsive pass

- Tested both `/` and `/capital` at 1600×1000, 1024×768, 799×844, 390×844 and 320×568.
- `scrollWidth === innerWidth` for both routes at every tested width.
- First semantic field and sole `<h1>` follow the route: Hifas on `/`, Capital on `/capital`.
- Artwork-to-selector protection measures 104px at 1600px, 73px at 1024px and 58px from 799px down to 320px.
- Hifa controls remain at least 48px high and retain pointer plus Left/Right keyboard operation.
- Morning, afternoon and night states were visually inspected after the grid removal.
- Latest evidence: `14-desktop-hifas-gateway-after-redesign-1600x1000.png`, `15-desktop-hifas-controls-after-redesign-1600x1000.png`, `17-mobile-hifas-night-after-redesign-390x844.png`, `18-desktop-capital-night-after-redesign-1600x1000.png`, `19-desktop-hifas-tarde-after-redesign-1600x1000.png`.

## Final result

final result: passed
