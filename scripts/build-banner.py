"""Assemble the imagegen sprite sheet into a looping GIF; requires Pillow."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
COLUMNS, ROWS = 2, 4
FRAME_DURATION_MS = 180
COLORS = 256

sheet = Image.open(ROOT / 'artwork/midnight-mint-spritesheet.png').convert('RGB')
assert sheet.width % COLUMNS == 0 and sheet.height % ROWS == 0, 'Uneven frame grid'
width, height = sheet.width // COLUMNS, sheet.height // ROWS
palette = sheet.quantize(colors=COLORS)
frames = []
for row in range(ROWS):
    for column in range(COLUMNS):
        frame = sheet.crop((column * width, row * height,
                            (column + 1) * width, (row + 1) * height))
        frames.append(frame.quantize(palette=palette, dither=Image.Dither.NONE))

asset = ROOT / 'asset'
asset.mkdir(exist_ok=True)
frames[0].convert('RGB').save(asset / 'coding-studio-still.png', optimize=True)
output = asset / 'coding-studio.gif'
frames[0].save(output, save_all=True, append_images=frames[1:],
               duration=FRAME_DURATION_MS, loop=0, disposal=2, optimize=True)

with Image.open(output) as animation:
    assert animation.n_frames == COLUMNS * ROWS, 'GIF lost its animation frames'
    assert animation.info['loop'] == 0, 'GIF must repeat indefinitely'
    hashes = set()
    for index in range(animation.n_frames):
        animation.seek(index)
        assert animation.size == (width, height)
        assert animation.info['duration'] == FRAME_DURATION_MS
        hashes.add(animation.convert('RGB').tobytes())
    assert len(hashes) == COLUMNS * ROWS, 'Each animation frame must be distinct'
print(f'{output.name}: {COLUMNS * ROWS} frames, {width}x{height}, '
      f'{FRAME_DURATION_MS} ms/frame, {output.stat().st_size:,} bytes')
