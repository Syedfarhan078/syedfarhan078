#!/usr/bin/env python3
"""
Terminal-themed GitHub Profile README SVG Generator.
Generates beautiful, responsive SVGs representing a futuristic terminal / fastfetch dashboard.
Compatible with dark and light themes, completely self-contained and zero-API dependent.
"""

import os
import sys
import re
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader

try:
    from PIL import Image, ImageOps, ImageDraw
except ImportError:
    print("Error: Pillow is required to run this script. Please install it using 'pip install Pillow'.")
    sys.exit(1)

import config


def image_to_ascii(image_path: str, cols: int = 28, invert: bool = False) -> str:
    """
    Converts a raw image to a square-cropped ASCII art block.
    Compensates for the aspect ratio of monospace characters (~0.55).
    """
    if not os.path.exists(image_path):
        print(f"Warning: Photo '{image_path}' not found. ASCII photo will be blank.")
        return ""

    try:
        img = Image.open(image_path)
        img = ImageOps.exif_transpose(img)

        # Center crop to a perfect square
        width, height = img.size
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        img_cropped = img.crop((left, top, right, bottom))

        # monospaced character aspect ratio correction (taller than wide)
        rows = int(cols * 0.55)

        # Resize to columns x rows
        img_resized = img_cropped.resize((cols, rows), Image.Resampling.BILINEAR)
        img_gray = img_resized.convert("L")

        # ASCII character density ramp
        chars = " .:-=+*#%@"
        if invert:
            # Invert for light background (where dark ink maps to dense chars)
            chars = chars[::-1]

        pixels = img_gray.getdata()
        ascii_chars = []
        for pixel in pixels:
            # Scale 0-255 to character indices
            idx = int(pixel * (len(chars) - 1) / 255)
            ascii_chars.append(chars[idx])

        # Group character lists into lines
        lines = []
        for i in range(0, len(ascii_chars), cols):
            lines.append("".join(ascii_chars[i:i+cols]))

        return "\n".join(lines)

    except Exception as e:
        print(f"Error converting image to ASCII: {e}")
        return ""


def minify_svg(svg_content: str) -> str:
    """
    Minifies the SVG content by removing XML comments, extra spaces, and empty lines.
    """
    # Remove XML comments
    clean_svg = re.sub(r"<!--(?!.*?Generated).*?-->", "", svg_content, flags=re.DOTALL)
    
    # Strip whitespaces and empty lines
    minified_lines = []
    for line in clean_svg.splitlines():
        stripped_line = line.strip()
        if stripped_line:
            minified_lines.append(stripped_line)
            
    return "\n".join(minified_lines)


def generate_svg(theme_name: str, theme_config: Dict[str, Any], ascii_photo: str) -> None:
    """
    Renders the SVG template with the given theme configurations, minifies the output,
    and writes the final SVG file.
    """
    template_file = f"{theme_name}.svg.jinja"
    output_file = f"{theme_name}_mode.svg"

    # Set up Jinja2 environment with autoescape enabled
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)

    try:
        template = env.get_template(template_file)
    except Exception as e:
        print(f"Error loading template '{template_file}': {e}")
        return

    # Prep context
    context = {
        "profile": config.PROFILE,
        "terminal_info": config.TERMINAL_INFO,
        "ascii_logo": config.ASCII_LOGO.strip("\n"),
        "projects": config.PROJECTS,
        "tech_stack": config.TECH_STACK,
        "socials": config.SOCIALS,
        "integrations": config.INTEGRATIONS,
        "theme": theme_config,
        "profile_ascii": ascii_photo,
        "svg_width": config.SVG_WIDTH,
        "svg_height": config.SVG_HEIGHT,
    }

    try:
        rendered_svg = template.render(context)
        minified_svg_content = minify_svg(rendered_svg)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(minified_svg_content)
        print(f"Successfully generated '{output_file}' (Size: {len(minified_svg_content)/1024:.2f} KB)")
    except Exception as e:
        print(f"Error rendering template '{template_file}': {e}")


def main() -> None:
    """
    Main entry point.
    """
    print("Starting GitHub Profile Terminal SVG Generation...")
    
    # Locate raw profile picture
    raw_img = os.path.join("assets", config.PROFILE["photo_input"])
    if not os.path.exists(raw_img) and os.path.exists(config.PROFILE["photo_input"]):
        raw_img = config.PROFILE["photo_input"]

    print(f"Raw image path: '{raw_img}'")

    # Generate SVGs for each theme
    for theme_name, theme_config in config.THEMES.items():
        print(f"Converting image to ASCII for theme: '{theme_name}'...")
        # Dark theme renders on a dark background: light parts of the image should map to denser chars.
        # Light theme renders on a white background: dark parts of the image should map to denser chars.
        invert_map = (theme_name == "light")
        
        # cols = 28 maps to ~126px width, fitting beautifully in the sub-window
        ascii_photo = image_to_ascii(raw_img, cols=28, invert=invert_map)
        
        print(f"Generating SVG for theme: '{theme_name}'...")
        generate_svg(theme_name, theme_config, ascii_photo)

    print("SVG Generation completed successfully!")


if __name__ == "__main__":
    main()
