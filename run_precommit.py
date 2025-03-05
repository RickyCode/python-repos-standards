import subprocess


def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode


if __name__ == '__main__':
    print('Sequence started!')
    run_cmd('pre-commit install')
    run_cmd('git update-index --again')

    i = 0
    continue_flag = True

    while i < 3 and continue_flag:
        print(f'Running pre-commit, iteration {i+1}/3...')

        if run_cmd('pre-commit run') != 1:
            print(f'Pre-commit successful run on iteration {i+1}/3. Stopping...')
            run_cmd('git update-index --again')
            continue_flag = False

        run_cmd('git update-index --again')
        i += 1

    # run_cmd('python ./__scripts__/project_context_generator.py')
    run_cmd('python -m __scripts__.project_context_generator')

    print('Sequence complete!')
    input('Press any key to continue...')
