import sys, os, subprocess, datetime

"""
    \Brief: Automatically push origin master a given repository. The
    \Brief: origin remote will be used by default.
    \Argument [repository]: string that represents the path to the repository

"""
def auto_git(repository):
    now = datetime.datetime.now()
    date = "{0}/{1:02d}/{2:02d}".format(now.year,
                                        now.month,
                                        now.day)
    
    os.chdir(repository)
    subprocess.call(["git", "add", "."])
    subprocess.call(["git", "commit", "-m", "AutoCommit{0}".format(date)])
    subprocess.call(["git", "push", "origin", "master"])
