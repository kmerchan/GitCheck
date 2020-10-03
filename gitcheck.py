#!/usr/bin/env python3
"""
main program uses functions to
(1) verify or get authentication token,
(2) add, commit, and push files passed in as arguments,
and (3) request correction and return check results
"""

from github import git_push
from searching import test_auth
from task_corrections import request_correction

if __name__ == "__main__":
    test_auth()
    git_push()
    request_correction()
