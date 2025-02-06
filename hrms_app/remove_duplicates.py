import os
import hashlib
from collections import defaultdict

def hash_file(file_path):
    """Generate a hash for a file."""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except PermissionError:
        print(f"Permission denied: {file_path}")
        return None
    return hasher.hexdigest()

def find_duplicates(directory):
    """Find and remove duplicate files in a directory."""
    files_by_hash = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash:
                files_by_hash[file_hash].append(file_path)

    duplicates = [files for files in files_by_hash.values() if len(files) > 1]
    return duplicates

def remove_duplicates(duplicates):
    """Remove duplicate files, keeping only the first occurrence."""
    for files in duplicates:
        for file in files[1:]:
            try:
                os.remove(file)
                print(f"Removed duplicate file: {file}")
            except FileNotFoundError:
                print(f"File not found: {file}")
            except PermissionError:
                print(f"Permission denied: {file}")

if __name__ == "__main__":
    project_dir = "C:\\Users\\DeeAnn\\Desktop\\HRMSPROJECT"
    duplicates = find_duplicates(project_dir)
    remove_duplicates(duplicates)