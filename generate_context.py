# import fnmatch
import os
from pathlib import Path

# def parse_gitignore(base_dir):
#     """Parse the .gitignore file and return a list of ignored patterns."""
#     gitignore_path = os.path.join(base_dir, ".gitignore")
#     patterns = []
#     # while not os.path.exists(gitignore_path) and os.path.dirname(base_dir) != base_dir:
#     #     base_dir = os.path.dirname(base_dir)
#     #     gitignore_path = os.path.join(base_dir, ".gitignore")
#     if os.path.exists(gitignore_path):
#         with open(gitignore_path, 'r', encoding='utf-8') as f:
#             for line in f:
#                 line = line.strip()
#                 if line and not line.startswith('#'):
#                     patterns.append(line)
#     return patterns

# def is_ignored(path, patterns, base_dir):
#     """Check if a path matches any pattern in the .gitignore."""
#     relative_path = os.path.relpath(path, base_dir)
#     for pattern in patterns:
#         # Match directories explicitly
#         if fnmatch.fnmatch(relative_path, pattern) or fnmatch.fnmatch(os.path.join(relative_path, ''), pattern):
#             return True
#         # Match files explicitly
#         if fnmatch.fnmatch(os.path.basename(relative_path), pattern):
#             return True
#     return False

# def list_files_in_directory(base_dir):
#     """List all files in a directory and its subdirectories."""
#     file_list = []
#     for root, _, files in os.walk(base_dir):
#         for file in files:
#             file_list.append(os.path.join(root, file).replace('\\', '/'))
#     return file_list

# def has_hidden_entries(path):
#     """Returns True if any file or directory within the given path starts with '.'."""
#     for root, dirs, files in os.walk(path):
#         for name in dirs + files:
#             if name.startswith('.'):
#                 return True
#     return False


def is_ignored(path, patterns, base_dir):
    relative_path = str(Path(path)).split(Path(os.getcwd()).name)[-1]
    # relative_path = str(os.path.relpath(path, base_dir)) # falla por algún motivo
    if relative_path.startswith('.') or f'{os.sep}.' in relative_path:

        return True

    for ignore in patterns:
        if ignore in path:

            return True

    return False


# def filter_files(file_list):
#     """Filter out files that should be ignored."""
#     return [file for file in file_list if not is_ignored(file)]


# def generate_file_structure(base_dir, ignored_patterns):
#     """Generates a nested representation of the file structure."""
#     file_structure = []
#     for root, dirs, files in os.walk(base_dir):
#         relative_path = os.path.relpath(root, base_dir)
#         if is_ignored(root, ignored_patterns, base_dir):
#             dirs[:] = []  # Skip this directory
#             continue
#         filtered_files = [
#             f
#             for f in files
#             if not is_ignored(os.path.join(root, f), ignored_patterns, base_dir)
#         ]
#         file_structure.append(
#             {
#                 'path': relative_path,
#                 'files': filtered_files,
#                 'dirs': dirs,
#             }
#         )
#     return file_structure


def generate_file_structure(base_dir, ignored_patterns):
    """Generates a nested recursive representation of the file structure."""

    def build_structure(current_dir):
        if is_ignored(current_dir, ignored_patterns, base_dir):

            return None

        dirs = []
        files = []
        for entry in sorted(os.listdir(current_dir)):
            full_path = os.path.join(current_dir, entry)
            if is_ignored(full_path, ignored_patterns, base_dir):
                continue

            if os.path.isdir(full_path):
                subdir = build_structure(full_path)
                if subdir:
                    dirs.append(subdir)

            else:
                files.append(entry)

        return {
            'name': os.path.basename(current_dir),
            'path': os.path.relpath(current_dir, base_dir),
            'dirs': dirs,
            'files': files,
        }

    # print(json.dumps(build_structure(base_dir), indent=2))  # Debug print

    return build_structure(base_dir)


def remove_comments(content):
    """Removes comments from the given content."""
    lines = content.split('\n')
    cleaned_lines = [line.split('#')[0] for line in lines if line.split('#')[0].strip()]

    return '\n'.join(cleaned_lines)


def merge_files(base_dir, ignored_patterns):
    """Merges all files in the directory into a single string with markers for each file."""
    merged_content = []
    script_name = os.path.basename(__file__)
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file == script_name:
                continue  # Skip the script itself

            file_path = os.path.join(root, file)
            if is_ignored(file_path, ignored_patterns, base_dir):
                continue

            relative_path = os.path.relpath(file_path, base_dir)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                content = remove_comments(content).strip()

                if file_path.endswith('.md'):
                    merged_content.append(
                        f'\n=============================== \\< BEGIN FILE: {relative_path} \\>\n'
                        f'{content}\n'
                        f'=============================== \\< END FILE: {relative_path} \\>\n'
                    )

                elif file_path.endswith('.py'):
                    merged_content.append(
                        f'\n=============================== \\< BEGIN FILE: {relative_path} \\>\n'
                        f'```python\n{content}\n```\n'
                        f'=============================== \\< END FILE: {relative_path} \\>\n'
                    )

                else:
                    merged_content.append(
                        f'\n=============================== \\< BEGIN FILE: {relative_path} \\>\n'
                        f'```\n{content}\n```\n'
                        f'=============================== \\< END FILE: {relative_path} \\>\n'
                    )

            except Exception as e:
                print(f'Could not read file {file}: {e}')

    return '\n'.join(merged_content)


def detect_key_files(base_dir, ignored_patterns):
    """Detect key configuration files in the project."""
    key_files = []
    common_files = [
        'README.md',
        'requirements.txt',
        'package.json',
        'pyproject.toml',
        'Dockerfile',
        '.env',
    ]
    for root, _, files in os.walk(base_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file in common_files and not is_ignored(file_path, ignored_patterns, base_dir):
                key_files.append(os.path.relpath(file_path, base_dir))

    return key_files


def render_tree(structure, prefix=''):
    """Renders the recursive file structure as a formatted tree diagram."""
    if not structure:

        return ''

    lines = []
    name = structure['name'] or '.'
    lines.append(f'{name}/')

    def _render(node, current_prefix):
        dirs = sorted(node['dirs'], key=lambda d: d['name'])
        files = sorted(node['files'])
        entries = dirs + files

        for i, entry in enumerate(entries):
            connector = '└── ' if i == len(entries) - 1 else '├── '
            if isinstance(entry, dict):  # directory
                lines.append(f'{current_prefix}{connector}{entry["name"]}/')
                new_prefix = current_prefix + ('    ' if i == len(entries) - 1 else '│   ')
                _render(entry, new_prefix)

            else:  # file
                lines.append(f'{current_prefix}{connector}{entry}')

    _render(structure, '')

    return '\n'.join(lines)


def generate_markdown(base_dir, file_structure, merged_content, key_files):
    """Generates a Markdown document with the project context."""
    markdown = ['# Project Context']

    markdown.append('## File Structure')
    markdown.append('\n```')
    tree_representation = render_tree(file_structure, os.path.basename(base_dir))
    markdown.append(tree_representation)
    markdown.append('```')

    markdown.append('## Key Configuration Files')
    if key_files:
        markdown.append('The following key configuration files were detected:')
        for file in key_files:
            markdown.append(f'- {file}')

    else:
        markdown.append('No key configuration files detected.')

    markdown.append('\n## Files Content')
    markdown.append(merged_content)

    return '\n'.join(markdown)


def analyze_project(base_dir, ignored_patterns):
    """Perform a basic analysis of the project."""
    analysis = ['# Basic Analysis']
    total_files = 0
    total_lines = 0
    script_name = os.path.basename(__file__)
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file == script_name:
                continue

            file_path = os.path.join(root, file)
            if is_ignored(file_path, ignored_patterns, base_dir):
                continue

            total_files += 1
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    total_lines += sum(1 for _ in f)

            except Exception:
                pass

    analysis.append(f'- Total files: {total_files}')
    analysis.append(f'- Total lines of code: {total_lines}')

    return '\n'.join(analysis)


def main():
    base_dir = os.getcwd()

    print(f'Generating context for directory: {base_dir}')

    # ignored_patterns = parse_gitignore(base_dir)

    ignored_patterns = [
        # '.git',
        '__pycache__',
        'flask_session',
        'project_context_generator.py',
        'results.txt',
        'project_context.md',
        # 'playground.ipynb',
        # 'learn.ipynb',
        '.ipynb',
        # '.pre-commit-config.yaml',
        # '.vscode',
    ]

    file_structure = generate_file_structure(base_dir, ignored_patterns)
    merged_content = merge_files(base_dir, ignored_patterns)
    key_files = detect_key_files(base_dir, ignored_patterns)
    analysis = analyze_project(base_dir, ignored_patterns)
    markdown = generate_markdown(base_dir, file_structure, merged_content, key_files)

    output_file = os.path.join(base_dir, 'project_context.md')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)
        f.write('\n\n')
        f.write(analysis)

    print(f'Project context saved to {output_file}')


if __name__ == '__main__':
    main()
