import os

def replace_text_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(file_path, 'w') as file:
        file.write(content)

def replace_text_in_directory_names(root, replacements):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        for dirname in dirnames:
            new_dirname = dirname
            for old, new in replacements.items():
                new_dirname = new_dirname.replace(old, new)
            if new_dirname != dirname:
                os.rename(os.path.join(dirpath, dirname), os.path.join(dirpath, new_dirname))

replacements = {
    'wordpress': 'dilacms',
    'dilacode': 'datacode',
    'wp-': 'dc-',
    'elementor': 'dilamentor',
    'wp-content': 'content'
}

# Replace text in files
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.css'):
            replace_text_in_file(os.path.join(root, file), replacements)

# Replace text in directory names
replace_text_in_directory_names('.', replacements)