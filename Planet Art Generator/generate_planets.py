from __future__ import annotations

import argparse
import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


# Each biome has a palette ordered from darkest to lightest.
# Feel free to tweak these RGB values to establish your game's art direction.
BIOMES = {
    "scorched": {
    "palette": [
        (30, 18, 27),     # deep shadow
        (65, 27, 35),     # dark volcanic rock
        (105, 39, 38),    # dark rust
        (155, 58, 39),    # burnt red
        (200, 91, 46),    # orange rust
        (235, 145, 68),   # hot highlights
        (35, 53, 65),     # dark, dried-out lake
        (48, 91, 100),    # rare mineral-rich lake
    ],
    "noise_scale": 0.64,
    "crater_chance": 0,
    "crack_chance": 0,
},
"ocean": {
    "palette": [
        (20, 65, 120),    # deep ocean
        (35, 105, 190),   # ocean blue
        (54, 148, 210),   # shallow water
    ],
    "noise_scale": 0.64,
    "crater_chance": 0,
    "crack_chance": 0,
},
"lush": {
    "palette": [
        (12, 31, 58),     # deep shadow
        (20, 65, 120),    # deep ocean
        (35, 105, 190),   # ocean blue
        (54, 148, 210),   # shallow water
        (30, 85, 42),     # dark forest
        (40, 115, 48),    # forest green
        (75, 155, 61),    # green terrain
        (135, 190, 85),   # lighter land
        (190, 215, 120),  # bright terrain highlights
    ],
    "noise_scale": 0.74,
    "crater_chance": 0,
    "crack_chance": 0,
},
"frozen": {
    "palette": [
        (10, 24, 47),     # deep shadow
        (19, 43, 75),     # deep frozen ocean
        (35, 76, 119),    # dark blue ice
        (59, 112, 157),   # icy blue
        (220, 239, 244),  # pale blue ice
        (220, 239, 244),  # light green
        (220, 239, 244),  # snow and ice highlights
    ],
    "noise_scale": 0.80,
    "crater_chance": 0,
    "crack_chance": 0,
},
"barren": {
    "palette": [
        (29, 31, 36),     # deep shadow
        (57, 58, 59),     # dark stone
        (88, 84, 79),     # grey rock
        (124, 115, 99),   # dusty terrain
        (163, 148, 121),  # sandy rock
        (201, 184, 151),  # pale surface
        (35, 54, 66),     # dark, isolated lake
        (48, 91, 99),     # rare mineral lake
    ],
    "noise_scale": 0.34,
    "crater_chance": 0,
    "crack_chance": 0,
},
"Neutron_star": {
    "palette": [
        (45, 65, 105),    # deep blue shadow
        (105, 145, 210),   # blue shadow
        (165, 200, 245),   # blue highlight
        (210, 230, 255),   # pale blue
        (240, 247, 255),   # near white
        (255, 255, 255),   # bright white
        (255, 255, 255),   # white
        (255, 255, 255),   # white highlight
    ],
    "noise_scale": 0.5,
    "crater_chance": 0,
    "crack_chance": 0,
    },
"M-type": {
    "palette": [
        (50, 20, 20),     # deep shadow
        (100, 40, 40),    # dark red
        (150, 60, 60),    # red
        (200, 80, 80),    # light red
        (255, 100, 100),  # bright red
        (255, 150, 150),  # pinkish red
        (255, 200, 200),  # pale pink
        (255, 220, 220),  # very pale pink
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
    },
"G-type": {
    "palette": [
        (50, 50, 20),     # deep shadow
        (100, 100, 40),   # dark yellow
        (150, 150, 60),   # yellow
        (200, 200, 80),   # light yellow
        (255, 255, 100),  # bright yellow
        (255, 255, 150),  # pale yellow
        (255, 255, 200),  # very pale yellow
        (255, 255, 220),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
"K-type": {
    "palette": [
        (50, 30, 20),     # deep shadow
        (100, 60, 40),    # dark orange
        (150, 90, 60),    # orange
        (200, 120, 80),   # light orange
        (255, 150, 100),  # bright orange
        (255, 180, 140),  # pale orange
        (255, 210, 180),  # very pale orange
        (255, 230, 210),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
    },
"F-type": {
    "palette": [
        (50, 50, 30),     # deep shadow
        (100, 100, 60),   # dark yellow
        (150, 150, 90),   # yellow
        (200, 200, 120),  # light yellow
        (255, 255, 150),  # bright yellow
        (255, 255, 180),  # pale yellow
        (255, 255, 210),  # very pale yellow
        (255, 255, 230),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
    },
"A-type": {
    "palette": [
        (50, 50, 50),     # deep shadow
        (100, 100, 100),  # dark gray
        (150, 150, 150),  # gray
        (200, 200, 200),  # light gray
        (255, 255, 255),  # bright white
        (255, 255, 255),  # pale white
        (255, 255, 255),  # very pale white
        (255, 255, 255),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
"B-type": {
    "palette": [
        (50, 50, 100),    # deep shadow
        (100, 100, 200),  # dark blue
        (150, 150, 255),  # blue
        (200, 200, 255),  # light blue
        (255, 255, 255),  # bright white
        (255, 255, 255),  # pale white
        (255, 255, 255),  # very pale white
        (255, 255, 255),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
"O-type": {
    "palette": [
        (10, 25, 75),     # deep blue shadow
        (20, 65, 150),    # dark blue
        (45, 110, 220),   # vivid blue
        (86, 145, 255),   # blue
        (140, 190, 255),  # light blue
        (190, 220, 255),  # pale blue
        (225, 240, 255),  # very pale blue
        (255, 255, 255),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
"Red_dwarf": {
    "palette": [
        (50, 20, 20),     # deep shadow
        (100, 40, 40),    # dark red
        (150, 60, 60),    # red
        (200, 80, 80),    # light red
        (255, 100, 100),  # bright red
        (255, 150, 150),  # pinkish red
        (255, 200, 200),  # pale pink
        (255, 220, 220),  # very pale pink
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
"White_dwarf": {
    "palette": [
        (50, 50, 50),     # deep shadow
        (100, 100, 100),  # dark gray
        (150, 150, 150),  # gray
        (200, 200, 200),  # light gray
        (255, 255, 255),  # bright white
        (255, 255, 255),  # pale white
        (255, 255, 255),  # very pale white
        (255, 255, 255),  # almost white
    ],
    "noise_scale": 0.6,
    "crater_chance": 0,
    "crack_chance": 0,
},
}


def smooth_noise(rng: np.random.Generator, width: int, height: int,
                 grid_size: int = 12) -> np.ndarray:
    """Create smooth terrain noise, then resize it to the requested resolution."""
    small_w = max(2, grid_size)
    small_h = max(2, round(grid_size * height / width))
    small = rng.random((small_h, small_w), dtype=np.float32)
    noise_img = Image.fromarray(np.uint8(small * 255), mode="L")
    noise_img = noise_img.resize((width, height), Image.Resampling.BILINEAR)
    return np.asarray(noise_img, dtype=np.float32) / 255.0


def make_planet(biome: str, seed: int, size: int = 128) -> Image.Image:
    """Generate one seeded RGBA pixel-art planet."""
    if biome not in BIOMES:
        raise ValueError(f"Unknown biome {biome!r}. Available: {', '.join(BIOMES)}")

    config = BIOMES[biome]
    palette = config["palette"]
    rng = np.random.default_rng(seed)
    py_rng = random.Random(seed)

    # Generate terrain at a lower resolution and enlarge with nearest-neighbour
    # interpolation to keep the image looking pixelated.
    work_size = 64
    broad = smooth_noise(rng, work_size, work_size, grid_size=8)
    medium = smooth_noise(rng, work_size, work_size, grid_size=20)
    fine = rng.random((work_size, work_size), dtype=np.float32)

    # A subtle directional lighting term: top-left is brighter, bottom-right darker.
    yy, xx = np.mgrid[0:work_size, 0:work_size]
    nx = (xx - (work_size - 1) / 2) / (work_size / 2)
    ny = (yy - (work_size - 1) / 2) / (work_size / 2)
    radius = np.sqrt(nx * nx + ny * ny)
    lighting = np.clip(0.62 - 0.27 * nx - 0.30 * ny, 0.12, 1.0)

    terrain = 0.57 * broad + 0.30 * medium + 0.13 * fine
    terrain = np.clip(terrain * 0.88 + lighting * 0.20, 0, 1)

    # Map terrain values to a small discrete palette.
    palette_array = np.asarray(palette, dtype=np.uint8)
    indices = np.minimum((terrain * len(palette)).astype(np.int32), len(palette) - 1)
    rgb = palette_array[indices]

    # Add a few hand-sized pixel clusters/craters at the working resolution.
    surface = Image.fromarray(rgb, mode="RGB")
    draw = ImageDraw.Draw(surface)
    for _ in range(max(3, int(size * config["crater_chance"] / 2))):
        cx = py_rng.randint(8, work_size - 9)
        cy = py_rng.randint(8, work_size - 9)
        r = py_rng.choice([1, 2, 3, 4])
        if py_rng.random() < config["crater_chance"]:
            draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=palette[0])
            if r >= 2:
                draw.point((cx-1, cy-1), fill=palette[-1])

    # Add occasional short dark marks to suggest cracks or rocky features.
    crack_count = int(size * config["crack_chance"] / 2)
    for _ in range(crack_count):
        x = py_rng.randint(5, work_size - 6)
        y = py_rng.randint(5, work_size - 6)
        length = py_rng.randint(2, 6)
        draw.line((x, y, x + py_rng.randint(-2, 2), y + length),
                  fill=palette[0], width=1)

    # Upscale without smoothing for a crisp pixel-art look.
    surface = surface.resize((size, size), Image.Resampling.NEAREST)

    # Apply a circular mask with a little margin so the silhouette isn't clipped.
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    margin = 3
    mask_draw.ellipse((margin, margin, size - margin - 1, size - margin - 1), fill=255)

    # Keep only pixels inside the circle; transparent outside.
    rgba = surface.convert("RGBA")
    rgba.putalpha(mask)

    return rgba


def generate_batch(output_dir: Path, count: int, size: int, base_seed: int,
                   biomes: list[str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    for biome in biomes:
        if biome not in BIOMES:
            raise ValueError(f"Unknown biome {biome!r}. Available: {', '.join(BIOMES)}")

        biome_dir = output_dir / biome
        biome_dir.mkdir(parents=True, exist_ok=True)

        for variant in range(count):
            # Stable, distinct seed for each biome/variant pair.
            seed = base_seed + list(BIOMES).index(biome) * 100_000 + variant
            image = make_planet(biome, seed, size)
            filename = biome_dir / f"{biome}_{variant + 1:03d}.png"
            image.save(filename, format="PNG")

        print(f"Generated {count} {biome} planets in {biome_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate seeded pixel-art planet PNGs.")
    parser.add_argument("--count", type=int, default=10,
                        help="Number of variants to generate per biome (default: 10)")
    parser.add_argument("--size", type=int, default=128,
                        help="Output image width and height (default: 128)")
    parser.add_argument("--seed", type=int, default=12345,
                        help="Base seed for repeatable output (default: 12345)")
    parser.add_argument("--output", type=Path, default=Path("output"),
                        help="Output folder (default: ./output)")
    parser.add_argument("--biomes", nargs="+", default=list(BIOMES),
                        help=f"Biomes to generate (available: {', '.join(BIOMES)})")
    args = parser.parse_args()

    if args.count < 1:
        parser.error("--count must be at least 1")
    if args.size < 16:
        parser.error("--size must be at least 16")

    generate_batch(args.output, args.count, args.size, args.seed, args.biomes)


if __name__ == "__main__":
    main()
