import os

def replace_text_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(file_path, 'w') as file:
        file.write(content)

replacements = {
    'wordpress': 'dilacms',
    'dilacode': 'datacode',
    'wp-': 'dc-'
}

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.js') or file.endswith('.css'):
            replace_text_in_file(os.path.join(root, file), replacements)