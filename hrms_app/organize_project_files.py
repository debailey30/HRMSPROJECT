import os
import shutil

def move_files_to_directories(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            dest_dir = None
            if file_path.endswith('.py'):
                dest_dir = os.path.join(directory, 'hrms_app')  # Example: Move .py files to hrms_app
            elif file_path.endswith('.html'):
                dest_dir = os.path.join(directory, 'hrms_app', 'templates')  # Example: Move .html files to templates
            elif file_path.endswith('.css') or file_path.endswith('.js'):
                dest_dir = os.path.join(directory, 'hrms_app', 'static')  # Example: Move .css and .js to static

            if dest_dir:
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(file_path, os.path.join(dest_dir, file))
                print(f"Moved: {file_path} to {dest_dir}")

if __name__ == "__main__":
    project_dir = '.'  # Change this to the root directory of your project
    move_files_to_directories(project_dir)