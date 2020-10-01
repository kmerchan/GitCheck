# GitCheck

Python Command line tool to return results from the Holberton Checker API when a task file is pushed.

---
## Requirements
- Python >= 3.4
- Git 1.7.0 or newer

## Dependencies

[GitPython](https://gitpython.readthedocs.io/en/stable/)

    python -m pip install gitpython

[gitdb](https://pypi.org/project/gitdb/)

    python -m pip install gitdb

[requests](https://requests.readthedocs.io/en/master/)

    python -m pip install requests

# 
### Things to think about

- What information does the script need?
- Will it be given via argument, environment variable, or config/settings file? 

# 
## What needs to Happen with Git?

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
- How many files will be staged and committed?
- How will the user fill in a commit message?
- Will the user be prompted if the message is to verbose?

# 
## What needs to Happen with Checker API?

### Section 0: Installation
- Can the user run the script without the proper dependencies? If yes, will the script solicit a response to automatically run a setup process?

### Section 1: Respect mAH Authorita!
- Check user authorization with auth_token.

### Section 2: Do I even?
- Is the checker available?
- Do we check with API yet?

### Section 3: Get tasks to check
- Use Holberton Checker API to get a list of tasks.
- Get file names of recently staged/committed files.
- Do we check all tasks? Recently pushed tasks? Recently push and previously push tasks?

### Section 4: Request corrections for tasks
- Use Holberton Checker API to request a correction for a task or list of tasks.

### Section 5: Compile results of corrections
- Store relevant data from correction responses into data structures.

### Section 6: Display results
- Parse and Display relevant data from correction responses
