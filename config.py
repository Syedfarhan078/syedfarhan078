# Configuration for the Terminal-themed GitHub Profile README Generator

# Custom Cyberpunk / Fastfetch-style ASCII Art Logo (representing initials "SF")
ASCII_LOGO = """
  ▄████████    ▄████████ 
 ▄███▄▄▄▄██▀  ▄███▀▀▀▀▀  
 ▀███▀▀▀▀▀    ███▀       
 ▀███████████ ███▄▄▄▄▄▄  
          ███ ▀███▀▀▀▀▀  
 ▄▄▄▄▄▄▄▄███▀  ███       
 ▀▀▀▀▀▀▀▀▀     ███       
"""

# Profile details and focus areas
PROFILE = {
    "username": "syedfarhan078",
    "name": "Syed Farhan Ahmed",
    "title": "AI & Machine Learning Engineer",
    "subtitle": "Full Stack Developer | Open Source Enthusiast | Problem Solver",
    "location": "Bengaluru, India",
    "focus": [
        "AI Engineering",
        "Django Development",
        "System Design",
        "Open Source"
    ],
    "photo_input": "raw_profile.jpg",
    "photo_output": "assets/profile.png"
}

# Terminal Neofetch Information Details
TERMINAL_INFO = {
    "OS": "Windows 11",
    "Editor": "VS Code",
    "Languages": "Python, Java, C++, JavaScript, SQL",
    "Frameworks": "Django, Flask, Streamlit",
    "Database": "MySQL, MongoDB",
    "College": "Atria Institute of Technology",
    "Location": "Bengaluru, India"
}

# Featured Projects in a clean terminal style list
PROJECTS = [
    {
        "name": "Career Catalyst",
        "tech": "Django • AI • Career Guidance"
    },
    {
        "name": "Eye Controlled Mouse",
        "tech": "OpenCV • MediaPipe"
    },
    {
        "name": "CFG → CNF Converter",
        "tech": "Flask • TOC"
    },
    {
        "name": "Air Quality Dashboard",
        "tech": "Plotly • Streamlit"
    }
]

# Tech Stack List
TECH_STACK = [
    "Python", "Java", "C++", "JavaScript", "HTML", "CSS",
    "Django", "Flask", "Streamlit", "MySQL", "MongoDB",
    "Git", "GitHub", "Linux", "Docker", "VS Code"
]

# Social Links (embedded in the clickable elements of the SVG)
SOCIALS = {
    "github": "https://github.com/syedfarhan078",
    "linkedin": "https://linkedin.com/in/syedfarhan078",
    "email": "mailto:syedfarhan078@gmail.com"
}

# Optional Live Data Integrations (Set to active=False by default)
INTEGRATIONS = {
    "spotify": {
        "active": False,
        "song": "No Active Playback",
        "artist": "Unknown Artist"
    },
    "leetcode": {
        "active": False,
        "solved": 150,
        "total": 3100
    },
    "codeforces": {
        "active": False,
        "rating": 1200,
        "rank": "Pupil"
    },
    "wakatime": {
        "active": False,
        "weekly_hours": "32h 15m"
    }
}

# Theme Color Palettes (Tailored monospace design system)
THEMES = {
    "dark": {
        "background": "#0d1117",      # GitHub Dark background
        "terminal_bg": "#161b22",     # Darker window background
        "border": "#30363d",          # Muted gray border
        "text": "#c9d1d9",            # White/grey primary text
        "accent": "#58a6ff",          # Neon Blue accent
        "accent_green": "#3fb950",    # Green accent
        "accent_yellow": "#d29922",   # Yellow highlight
        "subtext": "#8b949e",         # Secondary grey text
        "prompt": "#58a6ff",          # Prompt symbol ($) color
        "glow": "rgba(88, 166, 255, 0.45)",
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
        "glow": "rgba(9, 105, 218, 0.2)",
        "cursor": "#0969da",          # Cursor color
        "window_control": {
            "close": "#ff5f56",
            "minimize": "#ffbd2e",
            "maximize": "#27c93f"
        }
    }
}

# Responsive Canvas dimensions
SVG_WIDTH = 950
SVG_HEIGHT = 580
