#!/usr/bin/env python3
"""
Terminal-themed GitHub Profile README SVG Generator.
Generates beautiful, responsive SVGs representing a futuristic terminal / fastfetch dashboard.
Compatible with dark and light themes, completely self-contained and zero-API dependent.
"""

import os
import base64
import sys
import re
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader

try:
    from PIL import Image, ImageOps
except ImportError:
    print("Error: Pillow is required to run this script. Please install it using 'pip install Pillow'.")
    sys.exit(1)

import config


def process_ascii_image(input_path: str, output_path: str, invert: bool = False, target_size: tuple = (120, 130)) -> Optional[str]:
    """
    Loads your custom ASCII image, resizes it to target_size (default 120x130 for centering),
    converts it to grayscale (L), inverts colors if needed, and saves it as an optimized PNG.
    Returns the base64 encoded data URI of the processed PNG.
    """
    if not os.path.exists(input_path):
        print(f"Warning: Photo '{input_path}' not found. Profile image will be blank.")
        return None

    try:
        # Open and transpose based on EXIF orientation if it exists
        img = Image.open(input_path)
        img = ImageOps.exif_transpose(img)

        # Convert to grayscale
        img_gray = img.convert("L")

        # Resize to exactly the target width and height to fit the SVG feed window
        img_resized = img_gray.resize(target_size, Image.Resampling.LANCZOS)

        if invert:
            # For light theme: invert so background is white and characters are dark
            img_processed = ImageOps.invert(img_resized)
        else:
            img_processed = img_resized

        # Ensure assets directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save output image with maximum PNG optimization
        img_processed.save(output_path, "PNG", optimize=True)
        print(f"Successfully processed ASCII image: '{output_path}'")

        # Read bytes and encode to base64
        with open(output_path, "rb") as f:
            encoded_bytes = base64.b64encode(f.read())
            return f"data:image/png;base64,{encoded_bytes.decode('utf-8')}"

    except Exception as e:
        print(f"Error processing ASCII image: {e}")
        return None


def get_default_avatar_base64() -> str:
    """
    Returns a default fallback transparent 1x1 PNG base64 string if the image processing fails.
    """
    pixel_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
    return f"data:image/png;base64,{pixel_b64}"


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


def generate_svg(theme_name: str, theme_config: Dict[str, Any], profile_b64: str) -> None:
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
        "profile_image_b64": profile_b64,
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
    
    # Locate raw profile picture (must be the newly copied raw_profile.png)
    raw_img = os.path.join("assets", config.PROFILE["photo_input"])
    if not os.path.exists(raw_img) and os.path.exists(config.PROFILE["photo_input"]):
        raw_img = config.PROFILE["photo_input"]

    print(f"Raw image path: '{raw_img}'")

    # Generate SVGs for each theme
    for theme_name, theme_config in config.THEMES.items():
        print(f"Processing ASCII image for theme: '{theme_name}'...")
        # For dark mode, keep black background (invert=False).
        # For light mode, invert to white background (invert=True).
        invert_map = (theme_name == "light")
        
        theme_photo_output = f"assets/profile_{theme_name}.png"
        
        # Process and retrieve base64 string
        profile_b64 = process_ascii_image(
            raw_img, 
            theme_photo_output, 
            invert=invert_map, 
            target_size=(120, 130)
        )

        if not profile_b64:
            print("No profile image found. Using default placeholder.")
            profile_b64 = get_default_avatar_base64()
        
        print(f"Generating SVG for theme: '{theme_name}'...")
        generate_svg(theme_name, theme_config, profile_b64)

    print("SVG Generation completed successfully!")


if __name__ == "__main__":
    main()
