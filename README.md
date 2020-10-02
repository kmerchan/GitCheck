# GitCheck

Python Command line tool to add, commit, and push files to GitHub and return results from the Holberton Checker API in one program.

---
### Table of Contents
* [Installation and Usage](## Installation and Usage)
* [Code Description](## Code Description)
* [Authors](## Authors)

## Installation and Usage
To use the GitCheck program:
* Get a copy of this repository with `git clone https://github.com/scan3ls/GitCheck.git`
* Ensure you have the [basic requirements](### Requirements) to run the program
* To install dependencies, run the program `~/GitCheck/install.sh`
* Move into the directory with files to add, commit, push, and check and run the program with `~/GitCheck/gitcheck.py <files>`, where <files> is the list of files to check
* The first time running the program, the user will be prompted to input their Holberton credentials to request an authentication token. Users will only need to provide their credentials once.
* If there are changes to credentials, please remove the settings file with `rm GitClone_settings.py` in the GitCheck respository. This will re-prompt the user for credentials the next time the program is run.

### Requirements
- Python >= 3.4
- Git 1.7.0 or newer

#### Dependencies

[GitPython](https://gitpython.readthedocs.io/en/stable/)

    python -m pip install gitpython

[gitdb](https://pypi.org/project/gitdb/)

    python -m pip install gitdb

[requests](https://requests.readthedocs.io/en/master/)

    python -m pip install requests


## Code Description
[searching.py](/searching.py) - accesses Holberton credentials or prompts user for credentials to validate and/or get authorization token for Holberton API
* `get_auth` method - gets authorization token through POST request with Holberton credentials as data
* `test_auth` method - imports variables from saved file or promps user to input credentials, authorizes authentication token, and saves current credentials to file

[cwd.py](/cwd.py) - gets project id, project directory name, and project repository name from current working directory
* `pid_from_cwd` method - returns project's id based on the current working directory
* `parent_from_cwd` method - returns both the parent repository name and parent project directory based on the current working directory

[github.py](/github.py) - handles adding, commiting, and pushing files to GitHub with GitPython
* 

## Bugs
If project names or ids are changed, or new projects are added, the repository lists of current projects and project ids will need to be manually updated. In the future, this can be optimized by adding a Holberton API endpoint that returns all projects for a repository.

## Authors
* Colson Scott - [GitHub](https://github.com/octopusHugz) / [email](colson.scott@holbertonschool.com)
* Gunter Pearson - [GitHub](https://github.com/GunterPearson) / [email](gunter.pearson@holbertonschool.com)
* Kelsie Merchant - [GitHub](https://github.com/kmerchan) / [email](kelsie.merchant@holbertonschool.com)
* Lance Burklin - [GitHub](https://github.com/Lancewburklin) / [email](lance.burklin@holbertonschool.com)
* Logan Scanlon - [GitHub](https://github.com/scan3ls) / [email](logan.scanlon@holbertonschool.com)
