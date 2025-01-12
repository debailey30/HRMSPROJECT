import os

def remove_compiled_files(directory):
    """
    Remove all .pyc files recursively in the given directory.
    
    Args:
        directory (str): The root directory to start the search.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")

if __name__ == "__main__":
    project_dir = '.'  # Change this to the root directory of your project
    remove_compiled_files(project_dir)