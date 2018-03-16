import datetime

"""
    \Brief: Automatically creates commands to push origin master a given repository.
    \Brief: The origin remote will be used by default.
    \Argument [repository]: string that represents the path to the repository
    \Return: A string list list of all the commands. Perfect to pass to subprocess.call
"""
def git_commands(repository):
    now = datetime.datetime.now()
    date = "{0}/{1:02d}/{2:02d}".format(now.year,
                                        now.month,
                                        now.day)
    commands = []
    commands.append(["git", "add", "."])
    commands.append(["git", "commit", "-m", "AutoCommit{0} ".format(date)])
    commands.append(["git", "push", "origin", "master"])
    return commands
