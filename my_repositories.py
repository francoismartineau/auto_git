import os, sys, subprocess
from auto_git import git_commands

"""
    The goal of this script is to automatically keep remote repositories synced
    with their local counterparts. Change the path of REPORITORIES_FILE to a file
    that contains all the paths of the repositories you want to automatically sync.
    The content could look like this:
    C:\folder\repositoy
    C:\folder\folder\repository
    etc
"""

REPORITORIES_FILE = "C:\\_util\\auto_git\\my_repositories.txt"

with open(REPORITORIES_FILE) as f:
    repositories = f.read().splitlines()


# Will keep the shell hidden
si = subprocess.STARTUPINFO() 
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW


for r in repositories:
    os.chdir(r)
    for c in git_commands(r):
        subprocess.call(c, startupinfo=si)
