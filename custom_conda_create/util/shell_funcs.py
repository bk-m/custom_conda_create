# -*- coding: utf-8 -*-

"""
Shell functions for the module.
"""

import re
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

    :returns: Returns either the path as a string or False in case no path was found.
    """
    tmp = subprocess.Popen("conda info", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = tmp.communicate()[0].decode('utf-8')
    dirs = re.findall("envs directories : (.*)", out)
    if dirs:
        return dirs[0]
    else:
        return False
