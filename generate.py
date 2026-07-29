#!/usr/bin/env python3
"""
Terminal-themed GitHub Profile README SVG Generator.
Generates beautiful, responsive SVGs representing a futuristic terminal / fastfetch dashboard.
Compatible with dark and light themes, completely self-contained and zero-API dependent.
"""

import os
import base64
import sys
from typing import Dict, Any, Optional
from jinja2 import Environment, FileSystemLoader

try:
    from PIL import Image, ImageOps, ImageDraw
except ImportError:
    print("Error: Pillow is required to run this script. Please install it using 'pip install Pillow'.")
    sys.exit(1)

import config


def crop_profile_image(input_path: str, output_path: str, size: tuple = (180, 180)) -> Optional[str]:
    """
    Crops the input image to a perfect circle, resizes it, and saves it as a PNG.
    Returns the base64 encoded string of the processed PNG.
    """
    if not os.path.exists(input_path):
        print(f"Warning: Input image '{input_path}' not found. Profile image processing will be skipped.")
        return None

    try:
        # Open and transpose based on EXIF orientation if it exists
        img = Image.open(input_path)
        img = ImageOps.exif_transpose(img)

        # Center crop to a square
        width, height = img.size
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        img_cropped = img.crop((left, top, right, bottom))

        # Resize to target dimension
        img_resized = img_cropped.resize(size, Image.Resampling.LANCZOS)

        # Create alpha mask for the circle
        mask = Image.new("L", size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)

        # Apply mask and convert to RGBA
        output_img = Image.new("RGBA", size, (0, 0, 0, 0))
        output_img.paste(img_resized, (0, 0), mask=mask)

        # Ensure assets directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Save output image
        output_img.save(output_path, "PNG")
        print(f"Successfully processed profile image: '{output_path}'")

        # Read output image bytes and encode to base64
        with open(output_path, "rb") as f:
            encoded_bytes = base64.b64encode(f.read())
            return f"data:image/png;base64,{encoded_bytes.decode('utf-8')}"

    except Exception as e:
        print(f"Error processing profile image: {e}")
        return None


def get_default_avatar_base64() -> str:
    """
    Returns a default fallback SVG/PNG circle avatar base64 string if the image processing fails.
    """
    # A tiny inline transparent/gray 1x1 PNG as placeholder
    pixel_b64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
    return f"data:image/png;base64,{pixel_b64}"


def generate_svg(theme_name: str, theme_config: Dict[str, Any], profile_b64: str) -> None:
    """
    Renders the SVG template with the given theme configurations and saves the file.
    """
    template_file = f"{theme_name}.svg.jinja"
    output_file = f"{theme_name}_mode.svg"

    # Set up Jinja2 environment
    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
    if not os.path.exists(template_dir):
        os.makedirs(template_dir, exist_ok=True)
        print(f"Created templates directory at '{template_dir}'")

    env = Environment(loader=FileSystemLoader(template_dir))

    try:
        template = env.get_template(template_file)
    except Exception as e:
        print(f"Error loading template '{template_file}': {e}")
        print("Creating placeholder templates because they do not exist yet.")
        return

    # Prep the rendering context
    context = {
        "username": config.USERNAME,
        "name": config.NAME,
        "title": config.TITLE,
        "subtitle": config.SUBTITLE,
        "location": config.LOCATION,
        "education": config.EDUCATION,
        "terminal_info": config.TERMINAL_INFO,
        "ascii_logo": config.ASCII_LOGO.strip("\n"),
        "stats": config.STATS,
        "projects": config.PROJECTS,
        "tech_stack": config.TECH_STACK,
        "integrations": config.INTEGRATIONS,
        "theme": theme_config,
        "profile_image_b64": profile_b64,
        "svg_width": config.SVG_WIDTH,
        "svg_height": config.SVG_HEIGHT,
    }

    try:
        rendered_svg = template.render(context)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered_svg)
        print(f"Successfully generated '{output_file}'")
    except Exception as e:
        print(f"Error rendering template '{template_file}': {e}")


def main() -> None:
    """
    Main entry point for generating SVGs.
    """
    print("Starting GitHub Profile Terminal SVG Generation...")
    
    # Process profile image
    raw_img = os.path.join("assets", config.PROFILE_PHOTO_INPUT)
    # Check if raw_img exists in root instead (during some local testing runs)
    if not os.path.exists(raw_img) and os.path.exists(config.PROFILE_PHOTO_INPUT):
        raw_img = config.PROFILE_PHOTO_INPUT

    processed_img = config.PROFILE_PHOTO_OUTPUT

    print(f"Looking for raw profile image at: '{raw_img}'")
    profile_b64 = crop_profile_image(raw_img, processed_img)

    if not profile_b64:
        # Check if already processed image exists
        if os.path.exists(processed_img):
            print(f"Using already processed image: '{processed_img}'")
            with open(processed_img, "rb") as f:
                encoded_bytes = base64.b64encode(f.read())
                profile_b64 = f"data:image/png;base64,{encoded_bytes.decode('utf-8')}"
        else:
            print("No profile image found. Using default placeholder.")
            profile_b64 = get_default_avatar_base64()

    # Generate SVGs for each theme
    for theme_name, theme_config in config.THEMES.items():
        print(f"Generating SVG for theme: '{theme_name}'")
        generate_svg(theme_name, theme_config, profile_b64)

    print("SVG Generation completed successfully!")


if __name__ == "__main__":
    main()
