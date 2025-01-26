import os
import shutil

# Define the base directory of your project
base_dir = r'C:\Users\DeeAnn\Desktop\HRMSPROJECT'

# Define the target directories for different file types
target_dirs = {
    'py': os.path.join(base_dir, 'hrms_app'),
    'pyc': os.path.join(base_dir, 'hrms_app', '__pycache__'),
    'cpp': os.path.join(base_dir, 'src'),
    'h': os.path.join(base_dir, 'src'),
    'json': os.path.join(base_dir, '.vscode'),
    'md': base_dir,  # Markdown files remain in the root directory
    'sln': base_dir,  # Solution files remain in the root directory
    'vcxproj': base_dir  # Project files remain in the root directory
}

# Create target directories if they don't exist
for dir_path in target_dirs.values():
    os.makedirs(dir_path, exist_ok=True)

# Walk through the base directory and move files to their target locations
for root, dirs, files in os.walk(base_dir):
    for file in files:
        file_ext = file.split('.')[-1]
        if file_ext in target_dirs:
            src_path = os.path.join(root, file)
            dest_path = os.path.join(target_dirs[file_ext], file)
            try:
                shutil.move(src_path, dest_path)
                print(f'Moved {src_path} to {dest_path}')
            except Exception as e:
                print(f'Error moving {src_path} to {dest_path}: {e}')
        else:
            print(f'Skipping {file} (no target directory defined)')

print('Cleanup completed.')