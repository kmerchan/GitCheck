#!/usr/bin/env python3
from github import git_push
from searching import test_auth
from task_corrections import request_correction

if __name__ == "__main__":
    test_auth()
    git_push()
    request_correction()
