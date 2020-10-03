#!/usr/bin/python3
"""
Defines functions for git add, git commit, and git push
files using GitPython
"""

from sys import argv
try:
    import git
except ImportError as err:
    # TODO: auto setup dependenicies
    print(err)
    exit()


def get_changes(repo):
    """ get diff of file changes """
    changed = repo.is_dirty(untracked_files=True)
    diff = repo.git.diff(repo.head.commit.tree)

    return changed, diff


def get_commit_msg():
    """ make a message for a commit """
    msg = input("Commit Message:\n")
    if msg is "":
        retry = input("Quit Commit?(y/n)")
        if retry is 'y':
            msg = get_commit_msg()
        else:
            return None
    if len(msg) > 50:
        print("Message too long")
        msg = get_commit_msg()
    return msg


def get_files(args):
    """ get list of files to commit """
    files = args[1:]
    if files == []:
        print("No files given")
        exit()
    if 'README.md' not in files:
        files.append('README.md')
    return files


def git_push():
    """ Commit and push files """
    from cwd import parent_from_cwd

    files = get_files(argv)

    parent, project_dir = parent_from_cwd()
    path = '~/{}'.format(parent)
    repo = git.Repo(path)
    result, diff = get_changes(repo)
    if result is False:
        print("No Files to commit")
        exit()

    msg = get_commit_msg()

    if msg is None:
        exit()
    try:
        import os
        for item in files:
            # print('try',
            #    os.path.join(repo.working_tree_dir, project_dir, item)
            # )
            repo.index.add(
                os.path.join(repo.working_tree_dir, project_dir, item)
            )
    except FileNotFoundError as err:
        print("files", files)
        print("Add error", err)
        exit()

    repo.index.commit(msg)
    repo.remotes.origin.pull()
    repo.remotes.origin.push()
