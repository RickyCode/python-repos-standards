import os
import shutil
from utils import run_cmd

source_path = '.standards/'
# destination_file = '.pre-commit-config.yaml'

files = [
    '.pre-commit-config.yaml',
    'PULL_REQUEST_TEMPLATE.md',
    # 'CONTRIBUTING.md',
    # 'CODE_OF_CONDUCT.md',
    # 'LICENSE',
]


def update_submodule():
    run_cmd('git submodule update --remote')


def sync_files():
    for file_name in files:

        source_file = source_path + file_name
        destination_file = file_name

        if not os.path.exists(source_file):
            raise FileNotFoundError(f'The source file {source_file} does not exist.')

        shutil.copy2(source_file, destination_file)
        print(f'Copied {source_file} to {destination_file}')

        run_cmd(f'git add {destination_file}')
        print(f'Added {destination_file} to git')

    # run_cmd(f'git commit -m "CHORE: Update files from standards"')


if __name__ == '__main__':
    sync_files()
