from generate_context import main as generate_context
from run_precommit import run_precommit
from sync import sync_files, update_submodule
from update_gitignore import update_gitignore


def prepare_repo():
    update_submodule()
    sync_files()
    run_precommit()
    update_gitignore()
    generate_context()


if __name__ == '__main__':
    prepare_repo()
