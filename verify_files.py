import os
from pathlib import Path

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent

# Define the expected directories and files
expected_directories = [
    BASE_DIR / "static",
    BASE_DIR / "static/admin",
    BASE_DIR / "static/css",
    BASE_DIR / "static/js",
    BASE_DIR / "static/images",
    BASE_DIR / "staticfiles",
]

expected_files = [
    BASE_DIR / "static/admin/base.css",
    BASE_DIR / "static/admin/responsive.css",
    BASE_DIR / "static/admin/dark_mode.css",
    BASE_DIR / "static/admin/theme.js",
    BASE_DIR / "static/css/styles.css",
    BASE_DIR / "static/js/scripts.js",
    BASE_DIR / "static/images/logo.png",
]

# Function to check if directories exist
def check_directories(directories):
    for directory in directories:
        if not directory.exists():
            print(f"Missing directory: {directory}")

# Function to check if files exist
def check_files(files):
    for file in files:
        if not file.exists():
            print(f"Missing file: {file}")

# Run the checks
if __name__ == "__main__":
    check_directories(expected_directories)
    check_files(expected_files)
    print("Verification complete.")