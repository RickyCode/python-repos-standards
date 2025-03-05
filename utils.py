import subprocess


def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode
