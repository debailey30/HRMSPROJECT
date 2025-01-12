import os

def generate_tree(directory, prefix=''):
    files = []
    directories = []

    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            files.append(item)
        else:
            directories.append(item)

    for idx, dir_name in enumerate(sorted(directories)):
        is_last_dir = (idx == len(directories) - 1)
        print(f"{prefix}{'└── ' if is_last_dir else '├── '}{dir_name}")
        new_prefix = prefix + ('    ' if is_last_dir else '│   ')
        generate_tree(os.path.join(directory, dir_name), new_prefix)

    for idx, file_name in enumerate(sorted(files)):
        is_last_file = (idx == len(files) - 1)
        print(f"{prefix}{'└── ' if is_last_file else '├── '}{file_name}")

if __name__ == '__main__':
    project_dir = '.'  # Change this to the specific directory you want to inspect
    print(f"{os.path.basename(os.path.abspath(project_dir))}/")
    generate_tree(project_dir)