import sys, os, subprocess, datetime

"""
    Automatically push origin master a given repository.
"""
repository = sys.argv[1]
now = datetime.datetime.now()
date = "{0}/{1:02d}/{2:02d}".format(now.year,
                                    now.month,
                                    now.day)

os.chdir(repository)
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "AutoCommit{0}".format(date)])
subprocess.call(["git", "push", "origin", "master"])
