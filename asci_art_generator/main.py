# main.py
from PIL import Image, ImageDraw, ImageOps
import os

# === Configurable parameters ===
INPUT_FILE = "img.png"        # input image (must be in same folder as main.py)
OUTPUT_HALFTONE = "halftone_dots.png"
OUTPUT_ASCII = "halftone_ascii.txt"

cell_size = 8                  # grid cell size (smaller = more detail, larger = bigger dots)
max_radius = cell_size * 0.25 # maximum dot radius
invert = False                 # invert brightness mapping
dot_color = (215, 230, 240)          # dot color (black)
background_color = (0,0,0)  # background color (light)

# ASCII characters (light -> dark)
ASCII_CHARS = [" ", ".", ":", "-", "=", "+", "*", "#", "%", "@"]

# === Load image ===
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, INPUT_FILE)

if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image not found: {img_path}")

img = Image.open(img_path).convert("L")
orig_w, orig_h = img.size

# Resize so width/height are multiples of cell_size
new_w = (orig_w // cell_size) * cell_size
new_h = (orig_h // cell_size) * cell_size
img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

# Create halftone canvas
halftone = Image.new("RGB", (new_w, new_h), background_color)
draw = ImageDraw.Draw(halftone)
pixels = img.load()

ascii_lines = []

for gy in range(0, new_h, cell_size):
    row_chars = []
    for gx in range(0, new_w, cell_size):
        # Average brightness in this cell
        total = 0
        for yy in range(gy, gy + cell_size):
            for xx in range(gx, gx + cell_size):
                total += pixels[xx, yy]
        avg = total / (cell_size * cell_size)

        # Brightness → radius
        t = avg / 255.0
        if invert:
            t = 1 - t
        radius = (1 - t) * max_radius

        # Draw dot
        if radius > 0.3:
            cx = gx + cell_size // 2
            cy = gy + cell_size // 2
            bbox = [cx - radius, cy - radius, cx + radius, cy + radius]
            draw.ellipse(bbox, fill=dot_color)

        # Brightness → ASCII char
        norm = radius / max_radius if max_radius > 0 else 0
        idx = min(len(ASCII_CHARS) - 1, int(norm * (len(ASCII_CHARS) - 1)))
        row_chars.append(ASCII_CHARS[idx])
    ascii_lines.append("".join(row_chars))

# === Save results ===
halftone.save(os.path.join(script_dir, OUTPUT_HALFTONE))
with open(os.path.join(script_dir, OUTPUT_ASCII), "w", encoding="utf8") as f:
    f.write("\n".join(ascii_lines))
