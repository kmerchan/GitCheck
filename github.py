#!/usr/bin/python3
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
    from sys import argv
    
    files = args[2:] 
    if files == []:
        print("No files given")
        exit()
    if 'README.md' not in files:
        files.append('README.md')

# Define argument structure
# assume projID file_list or directory
def git_push():
    """ Commit and push files """
    from projects import parent_from_cwd

    files = get_files(argv)

    # TODO: change path to return of a funcion call
    path = '~/{}'.format(parent_from_cwd())
    repo = git.Repo(path)
    result, files = get_changes(repo)
    if result is False:
        print("No Files to commit")
        exit()

    msg = get_commit_msg()

    if msg is None:
        exit()
    try:
        repo.index.add(files)
    except FileNotFoundError as err:
        print(err)
        exit()

    repo.index.commit(msg)
    repo.remotes.origin.push()
