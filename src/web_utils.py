import os
import re
import shutil
from markdown_to_html import markdown_to_html_node

def copy_static_files(source_dir, dest_dir):

    shutil.rmtree(dest_dir, ignore_errors=True)

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(dest_dir, item)

        if os.path.isfile(source_item):
            shutil.copy(source_item, dest_item)
        else:
            copy_static_files(source_item, dest_item)


def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise Exception('No title found')
        
def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    with open(from_path, 'r') as f:
        content = f.read()
    with open(template_path, 'r') as f:
        temp_content = f.read()
    title = extract_title(content)
    html_content = markdown_to_html_node(content)
    html_content = html_content.to_html()
    final_content = re.sub(r"\{\{\s*title\s*\}\}", title, temp_content, flags=re.IGNORECASE)
    final_content = re.sub(r"\{\{\s*content\s*\}\}", html_content, final_content, flags=re.IGNORECASE)
    final_content = final_content.replace('href="/', f'href="{basepath}')
    final_content = final_content.replace('src="/', f'src="{basepath}')
    with open(dest_path, 'w') as out:
        out.write(final_content)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content):
        content_item = os.path.join(dir_path_content, item)
        dest_item = os.path.join(dest_dir_path, item)

        if os.path.isfile(content_item) and content_item.endswith('.md'):
            dest_item = dest_item[:-3] + '.html'
            generate_page(content_item, template_path, dest_item, basepath)
        elif os.path.isdir(content_item):
            if not os.path.exists(dest_item):
                os.mkdir(dest_item)
            generate_pages_recursive(content_item, template_path, dest_item, basepath)
        