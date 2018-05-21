# -*- coding: utf-8 -*-

"""
Shell functions for the module.
"""

import pathlib
import re
import os
import sys
import subprocess

def run_in_shell_with_output(cmd):
    """
    Runs a given command in a subshell and prints the ouput.

    :param cmd: Command to run.
    :returns: Returns the exit code of the subprocess.
    """
    tmp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in tmp.stdout:
        sys.stdout.write(line.decode("utf-8"))
    tmp.communicate()
    return tmp.returncode

def run_in_shell_without_output(cmd):
    """
    Runs a given command in a subshell and does not print the ouput.

    :param cmd: Command to run.
    :returns: Returns the exit code of the subprocess.
    """
    tmp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tmp.communicate()
    return tmp.returncode

def get_default_conda_env_path():
    """
    Get the system's default conda environment path.

    :returns: Returns either the path as a string or "0" in case no path was found.
    """
    tmp = subprocess.Popen("conda info", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = tmp.communicate()[0].decode('utf-8')
    dirs = re.findall("envs directories : (.*)", out)
    if dirs:
        return dirs[0].strip()
    else:
        return "0"

def create_env_dirs(path, name):
    """
    Creates paths for scripts that get automatically executed when the environment gets
    de-/activated. Use these scripts to set/unset environment variables when the conda env is
    de./activated.

    :param path: Path to the conda environment.
    :param name: Name of the conda environment.
    :returns: The path to the folder which contains the de-/activate scripts as a string.
    """
    if not os.path.split(path)[1] == name:
        path = os.path.join(path, name)

    tmp = os.path.join(path, 'etc', 'conda')
    activate_path = os.path.join(tmp, 'activate.d')
    deactivate_path = os.path.join(tmp, 'deactivate.d')

    pathlib.Path(activate_path).mkdir(parents=True, exist_ok=True) 
    pathlib.Path(deactivate_path).mkdir(parents=True, exist_ok=True) 

    with open(os.path.join(activate_path, name + '_env_vars.bat'), 'w') as f:
        f.write("set MY_KEY='secret-key-value'\nset MY_FILE=C:\\path\\to\\my\\file")

    with open(os.path.join(deactivate_path, name + '_env_vars.bat'), 'w') as f:
        f.writelines("set MY_KEY=\nset MY_FILE=")

    return str(tmp)
