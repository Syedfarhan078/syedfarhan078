# Setup and Customization Guide

This repository contains a terminal-themed GitHub Profile README generator. It is designed to look like a futuristic Linux terminal (Fastfetch/Neofetch style) that runs entirely locally from your configuration details—requiring **zero API tokens, keys, or external authentications**.

---

## 🛠️ Getting Started (Local Run)

Follow these steps to run the project and generate your profile SVGs locally:

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your computer.

### 2. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/syedfarhan078/syedfarhan078.git
cd syedfarhan078
```

### 3. Install Dependencies
Install the required packages (`Pillow` for image processing and `Jinja2` for SVG rendering):
```bash
pip install -r requirements.txt
```

### 4. Run the Generator
Run the python script:
```bash
python generate.py
```
This will:
- Read `assets/raw_profile.jpg`.
- Crop it to a perfect circle and output it to `assets/profile.png`.
- Base64-encode the profile image and embed it directly into the SVG templates.
- Compile and generate `light_mode.svg` and `dark_mode.svg` in the root folder.

---

## ✍️ How to Customize Your Details

All profile values are managed in [config.py](file:///c:/Users/SYED%20FARHAN%20AHMED/Desktop/Syed%20Farhan/config.py). You don't need to change any SVG code to update your info!

Open `config.py` and modify the fields:

### 1. General Profile Info
Update `NAME`, `TITLE`, `SUBTITLE`, and `LOCATION` variables.

### 2. Terminal Info Box (Neofetch)
Modify the `TERMINAL_INFO` dictionary to list your OS, preferred editor, coding languages, frameworks, database, college, etc.
```python
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
```

### 3. Custom GitHub Stats
Edit the `STATS` dictionary to reflect your actual GitHub followers, repositories, stars, commits, contributions, etc.

### 4. Featured Projects
Under the `PROJECTS` list, add or modify up to 4 featured projects. Provide their name and a brief description:
```python
PROJECTS = [
    {
        "name": "Career Catalyst",
        "description": "AI-powered career guidance platform built with Django"
    },
    ...
]
```

### 5. Tech Stack Badges
Modify the `TECH_STACK` list. The templates will automatically arrange them in a neat col-by-row grid at the bottom.

---

## 🖼️ How to Replace the Profile Photo
1. Place your new portrait image (JPG or PNG) in the `assets/` folder.
2. Name it `raw_profile.jpg` (or update `PROFILE_PHOTO_INPUT` in `config.py`).
3. Run `python generate.py`.
The script will center-crop the photo to a square, apply a circular mask, resize it to an optimized 180x180 pixels (keeping SVG size under 80KB), and generate the new SVGs.

---

## 🎨 How to Change Colors and Themes
Themes are configured in the `THEMES` dictionary inside `config.py`.
You can customize colors for both `dark` and `light` modes independently:
- `background`: Overall container background.
- `terminal_bg`: Window body color.
- `border`: Window border and gridlines.
- `text`: Primary text color.
- `accent`: Highlights, names, and titles.
- `glow`: Color of the neon glow dropshadow (CSS/SVG filter).

---

## 🧩 How to Add New Widgets

If you want to add new widgets (e.g. now-playing music stats or WakaTime trackers):
1. Enable them in `config.py` under the `INTEGRATIONS` dictionary.
2. Open the SVG templates:
   - [templates/dark.svg.jinja](file:///c:/Users/SYED%20FARHAN%20AHMED/Desktop/Syed%20Farhan/templates/dark.svg.jinja)
   - [templates/light.svg.jinja](file:///c:/Users/SYED%20FARHAN%20AHMED/Desktop/Syed%20Farhan/templates/light.svg.jinja)
3. Write standard SVG XML elements inside the column templates using Jinja tags, referencing `{{ integrations.spotify }}` or other values.

---

## 🤖 How GitHub Actions Work

An automated workflow is configured in [.github/workflows/update.yml](file:///c:/Users/SYED%20FARHAN%20AHMED/Desktop/Syed%20Farhan/.github/workflows/update.yml):
1. Whenever you push changes to `main` (like editing `config.py` directly on GitHub Web), the GitHub Actions Runner will spin up a lightweight Ubuntu container.
2. It sets up Python, installs dependencies, and runs `generate.py`.
3. If new `dark_mode.svg` or `light_mode.svg` files are created, it automatically commits and pushes them back to your repository.
4. Your GitHub Profile will automatically reflect the updates!
