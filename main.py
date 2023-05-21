import os
import sys

skip_list = ['.git', 'output.md']

def skip_file(relative_path):
    for skip in skip_list:
        if skip in relative_path:
            return True
    return False

def create_markdown(folder):
    md_content = ''
    for root, _, files in os.walk(folder):
        for file in files:
            relative_path = os.path.relpath(os.path.join(root, file), folder)
            if skip_file(relative_path):
                print('skipping this path: ', relative_path)
                continue

            try:
                with open(os.path.join(root, file), 'r') as f:
                    file_contents = f.read()
            except UnicodeDecodeError:
                print(f"Skipping {file}: not a text file.")
                continue

            md_content += f"# {relative_path}\n\n"
            md_content += f"```\n{file_contents}\n```\n\n"

    with open('output.md', 'w') as md_file:
        md_file.write(md_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = '~/programming/repo-to-markdown/'
    folder_name = os.path.expanduser(path)
    create_markdown(folder_name)
