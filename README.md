# GitCheck

Python Command line tool to return results from the Holberton Checker API when a task file is pushed.

---
## Dependencies

[GitPython](https://gitpython.readthedocs.io/en/stable/)

    python -m pip install gitpython

# 
### Things to think about

- What information does the script need?
- Will it be given via argument, environment variable, or config/settings file? 

# 
## What needs to Happen?

### Section 0: Installation
- Can the user run the script without the proper dependencies? If yes, will the script solicit a response to automatically run a setup process?

### Section 1: Who am I?
- How will the script know the GitHub user and the password?

### Section 2: Managing Repos
- Does the script need to initialize a new repo, open a existing one on the local machine, or clone a remote repo from GitHub?

### Section 3: Working in a Repo
- What are the files that changed?
- Want branch is the current working tree connected to?
- Am I pushing?
- How many files will be staged and commited?
- How will the user fill in a commit message?
- Will the user be prompted if the message is to verbose?
