import os
import re

# Define the base directory of your project
base_dir = r'C:\Users\DeeAnn\Desktop\HRMSPROJECT'

# Define the patterns to search for and the replacement texts
patterns = {
    re.compile(r'from custom_typing import'): 'from custom_typing import',
    re.compile(r'from custom_types import'): 'from custom_types import',
    re.compile(r'from custom_functools import'): 'from custom_functools import',
    re.compile(r'from custom_inspect import'): 'from custom_inspect import',
    re.compile(r'from custom_logging import'): 'from custom_logging import',
    re.compile(r'from custom_warnings import'): 'from custom_warnings import',
    re.compile(r'from custom_collections import'): 'from custom_collections import'
}

# Walk through the base directory and update imports in .py files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            updated_content = content
            for pattern, replacement in patterns.items():
                updated_content = pattern.sub(replacement, updated_content)
            if updated_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f'Updated imports in {file_path}')

print('Import update completed.')