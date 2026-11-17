# Midnight Mint animation

Original frames generated with the built-in imagegen tool, then assembled into a GIF with Pillow.
The main profile README intentionally contains only the animation, language badges, and contribution snake.

## Customize the banner

- Source: `midnight-mint-spritesheet.png`, 1536 × 1024, two columns and four rows.
- Output: `../asset/coding-studio.gif`, eight frames at 768 × 256.
- Timing: 180 ms per frame, a 1.44-second infinite loop.
- Change `FRAME_DURATION_MS` in `../scripts/build-banner.py` to adjust playback speed.
- Replace the sprite sheet with another evenly divided 2 × 4 sheet to change the room, colors, or motion.
- Rebuild with `python -m pip install Pillow` followed by `python scripts/build-banner.py` from the repository root.
- `coding-studio-still.png` is shown when the visitor prefers reduced motion.

## Contribution snake

`../.github/workflows/snake.yml` generates the snake from this account's actual contribution calendar every day at approximately 03:17 WIB (GitHub may delay scheduled jobs).
It can also be run through Actions → Update contribution snake → Run workflow.
The generated light and dark SVG files are published to the `output` branch.
Change the `color_snake` and `color_dots` values in the workflow to adjust its palette.

Generator: [Platane/snk](https://github.com/Platane/snk).

## Image generation prompt

Generate a SINGLE SPRITE SHEET for an animated pixel-art GIF. The ENTIRE canvas must have aspect ratio 3:2 (1536 pixels wide by 1024 pixels tall). It MUST NOT be an ultrawide canvas.
LAYOUT: a precise regular grid with TWO columns and FOUR rows, exactly EIGHT panels. Each panel is 768 wide by 256 tall, a 3:1 landscape panorama. No panel labels, NO borders, NO gutters. Every panel touches its neighbors and fills its entire grid cell.
Scene within EVERY panel: the same original 16-bit pixel-art cozy coding room at night. Dark forest green studio, right-side desk with mint-screen monitor showing abstract code lines and a wireframe torus, keyboard, small plant and warm cream lamp. Rainy Indonesian city rooftops through the window. Left third is a dark wall with a small mint orbital planet emblem. No people. Restrained mint green, sage and cream lighting. Crisp square pixel clusters. No readable text or logos. Wide view, not a close-up.
ANIMATION: these are eight consecutive frames of ONE identical scene with a LOCKED CAMERA. Identical geometry, identical lighting positions, identical furniture and identical crop across all eight tiles. Only rain lines fall a few pixels per frame, a tiny code cursor blinks, two mint dots rotate around the orbital emblem, lamp glow subtly pulses. Avoid all movement of the furniture, window, shelves or camera. Seamless loop. Reading order: left to right, then top to bottom.
The final delivered image is the 3:2 rectangular SPRITE SHEET of eight 3:1 frames, not one panorama.
