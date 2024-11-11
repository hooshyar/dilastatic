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
    if new_path != path:
        if os.path.exists(new_path):
            if os.path.isdir(new_path):
                # Merge directories
                for item in os.listdir(path):
                    s = os.path.join(path, item)
                    d = os.path.join(new_path, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, dirs_exist_ok=True)
                    else:
                        shutil.copy2(s, d)
                shutil.rmtree(path)
            else:
                # Merge files by appending content
                with open(new_path, 'a', encoding='utf-8') as new_file:
                    with open(path, 'r', encoding='utf-8') as old_file:
                        new_file.write(old_file.read())
                os.remove(path)
        else:
            shutil.move(path, new_path)
    return new_path

def process_directory(root_dir, replacements):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip the wp-content directory if it's in the root
        if 'wp-content' in dirnames and dirpath == root_dir:
            dirnames.remove('wp-content')
        
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