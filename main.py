import os

def create_markdown(folder):
    md_content = ''
    for root, _, files in os.walk(folder):
        for file in files:
            try:
                relative_path = os.path.relpath(os.path.join(root, file), folder)
                with open(os.path.join(root, file), 'r') as f:
                    file_contents = f.read()
            except UnicodeDecodeError:
                print(f"Skipping {file}: not a text file.")
                continue
            md_content += f"# {relative_path}\n\n"
            md_content += f"```{file_contents}```\n\n"

    with open('output.md', 'w') as md_file:
        md_file.write(md_content)

if __name__ == "__main__":
    folder_name = os.path.expanduser('~/programming/repo-to-markdown/')
    create_markdown(folder_name)
