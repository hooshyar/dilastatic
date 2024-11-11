import os
import shutil

replacements = {
    'wp-content': 'dc-content',
    'elementor': 'dilamentor',
    'http://montoya.clapat-themes.com': 'https://datacode.app',
    'montoya': 'dilacode'
}

def replace_text_in_file(file_path, replacements):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        original_content = content
        for old, new in replacements.items():
            content = content.replace(old, new)
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
    except (UnicodeDecodeError, IsADirectoryError):
        pass  # Skip binary files and directories

def rename_item(path, replacements):
    new_path = path
    for old, new in replacements.items():
        new_path = new_path.replace(old, new)
    if new_path != path and not os.path.exists(new_path):
        shutil.move(path, new_path)
        return new_path
    return path

def process_directory(root_dir, replacements):
    # Walk the directory tree and replace text in files
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Replace text in files
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            replace_text_in_file(file_path, replacements)
        # Rename files
        for filename in filenames:
            old_file_path = os.path.join(dirpath, filename)
            new_file_path = rename_item(old_file_path, replacements)
        # Rename directories
        for dirname in dirnames:
            old_dir_path = os.path.join(dirpath, dirname)
            new_dir_path = rename_item(old_dir_path, replacements)

if __name__ == '__main__':
    process_directory('.', replacements)