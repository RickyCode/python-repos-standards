import os

gitignore_path = '.gitignore'
file_to_ignore = 'project_context.md'


def update_gitignore():
    if not os.path.exists(gitignore_path):
        with open(gitignore_path, 'w') as gitignore_file:
            gitignore_file.write('')

    with open(gitignore_path, 'r') as gitignore_file:
        lines = gitignore_file.readlines()

    if file_to_ignore not in [line.strip() for line in lines]:
        with open(gitignore_path, 'a') as gitignore_file:
            gitignore_file.write(f'\n{file_to_ignore}\n')


if __name__ == '__main__':
    update_gitignore()
