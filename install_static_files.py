import os
import requests
from pathlib import Path

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent

# Define the URLs for the necessary static files
static_files = {
    "static/admin/base.css": "https://raw.githubusercontent.com/django/django/main/django/contrib/admin/static/admin/css/base.css",
    "static/admin/responsive.css": "https://raw.githubusercontent.com/django/django/main/django/contrib/admin/static/admin/css/responsive.css",
    "static/admin/dark_mode.css": "https://raw.githubusercontent.com/django/django/main/django/contrib/admin/static/admin/css/dark_mode.css",
    "static/admin/theme.js": "https://raw.githubusercontent.com/django/django/main/django/contrib/admin/static/admin/js/theme.js",
}

# Function to download and save a file
def download_file(url, dest):
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    dest.parent.mkdir(parents=True, exist_ok=True)  # Create directories if they don't exist
    with open(dest, "wb") as file:
        file.write(response.content)
    print(f"Downloaded {dest}")

# Download and save each static file
for relative_path, url in static_files.items():
    dest = BASE_DIR / relative_path
    download_file(url, dest)

print("Static files installation complete.")