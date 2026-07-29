# Configuration for the Terminal-themed GitHub Profile README Generator

# GitHub Profile Information
USERNAME = "syedfarhan078"
NAME = "Syed Farhan Ahmed"
TITLE = "AI & Machine Learning Engineer"
SUBTITLE = "Full Stack Developer | Open Source Enthusiast | Problem Solver"
LOCATION = "Bengaluru, India"

# Education
EDUCATION = {
    "degree": "B.Tech in Artificial Intelligence & Machine Learning",
    "college": "Atria Institute of Technology"
}

# Terminal Neofetch Information Details
TERMINAL_INFO = {
    "OS": "Windows 11",
    "Editor": "VS Code",
    "Languages": "Python, Java, C++, JavaScript, SQL",
    "Frameworks": "Django, Flask, Streamlit",
    "Database": "MySQL, MongoDB",
    "Learning": "AI Engineering",
    "College": "Atria Institute of Technology",
    "Location": "Bengaluru, India"
}

# Profile Photo Settings
PROFILE_PHOTO_INPUT = "raw_profile.jpg"  # Source image filename
PROFILE_PHOTO_OUTPUT = "assets/profile.png"
PROFILE_GLOW_COLOR = "#89b4fa"  # Overridden dynamically by theme colors

# Custom ASCII Logo (Left Column)
# Beautiful, compact blocks representing "SF"
ASCII_LOGO = """
  ██████  ███████ 
 ██       ██      
  █████   █████   
      ██  ██      
 ██████   ██      
"""

# GitHub Stats (Static local values instead of API fetches)
STATS = {
    "followers": 12,
    "following": 15,
    "repositories": 18,
    "stars": 5,
    "commits": 212,
    "contributions": 284,
    "pull_requests": 14,
    "issues": 8,
    "top_languages": ["Python", "JavaScript", "C++", "Java"]
}

# Featured Projects
PROJECTS = [
    {
        "name": "Career Catalyst",
        "description": "AI-powered career guidance platform built with Django"
    },
    {
        "name": "Eye Controlled Mouse",
        "description": "Computer Vision accessibility project using OpenCV"
    },
    {
        "name": "Air Quality Dashboard",
        "description": "Interactive visualization using Plotly & Streamlit"
    },
    {
        "name": "CFG to CNF Converter",
        "description": "Theory of Computation project in Python"
    }
]

# Tech Stack List
# These will be displayed as clean terminal "badges" / visual items in the README SVGs.
TECH_STACK = [
    "Python", "Java", "C++", "JavaScript", "HTML", "CSS",
    "Django", "Flask", "Streamlit", "MySQL", "MongoDB",
    "Git", "GitHub", "Linux", "Docker", "VS Code"
]

# Optional Live Data Integrations (Set to active=False by default, can be toggled)
INTEGRATIONS = {
    "spotify": {
        "active": False,
        "song": "No Active Playback",
        "artist": "Unknown Artist",
        "album": ""
    },
    "leetcode": {
        "active": False,
        "solved": 150,
        "total": 3100,
        "ranking": "Top 12%"
    },
    "codeforces": {
        "active": False,
        "rating": 1200,
        "rank": "Pupil"
    },
    "wakatime": {
        "active": False,
        "weekly_hours": "32h 15m",
        "editors": ["VS Code", "Terminal"]
    }
}

# Theme Color Palettes
THEMES = {
    "dark": {
        "background": "#0d1117",      # GitHub Dark background
        "terminal_bg": "#161b22",     # Darker window background
        "border": "#30363d",          # Muted gray border
        "text": "#c9d1d9",            # White/grey primary text
        "accent": "#58a6ff",          # Neon Blue accent
        "accent_green": "#3fb950",    # Green accent for active elements
        "accent_yellow": "#d29922",   # Yellow warning/subtle highlight
        "subtext": "#8b949e",         # Secondary grey text
        "prompt": "#58a6ff",          # Prompt symbol ($) color
        "glow": "rgba(88, 166, 255, 0.4)",
        "cursor": "#58a6ff",          # Cursor color
        "window_control": {
            "close": "#ff5f56",
            "minimize": "#ffbd2e",
            "maximize": "#27c93f"
        }
    },
    "light": {
        "background": "#ffffff",      # GitHub Light background
        "terminal_bg": "#f6f8fa",     # Light grey window background
        "border": "#d0d7de",          # Light border
        "text": "#24292f",            # Dark primary text
        "accent": "#0969da",          # Deep Blue accent
        "accent_green": "#1a7f37",    # Green accent
        "accent_yellow": "#9a6700",   # Muted yellow
        "subtext": "#57606a",         # Muted subtext
        "prompt": "#0969da",          # Prompt color
        "glow": "rgba(9, 105, 218, 0.15)",
        "cursor": "#0969da",          # Cursor color
        "window_control": {
            "close": "#ff5f56",
            "minimize": "#ffbd2e",
            "maximize": "#27c93f"
        }
    }
}

# Layout settings
SVG_WIDTH = 950
SVG_HEIGHT = 580
