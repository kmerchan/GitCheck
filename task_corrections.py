#!/usr/bin/python3
"""
Utilizes Holberton checker API to request correction
for all files recently added, committed, and pushed
"""

from cwd import pid_from_cwd
import requests
from sys import argv
from GitCheck_settings import auth


def request_correction():
    """Requests a correction given a task ID"""
    checks_dict = {}
    project_id = pid_from_cwd()
    base_url = 'https://intranet.hbtn.io/projects/'
    task_url = '{}{}.json?auth_token={}'.format(base_url, project_id, auth)
    payload = {'Content-Type': 'application/json'}
    project = requests.get(task_url, params=payload).json()
    tasks = project.get('tasks')
    for task in tasks:
        task_id = task.get('id')
        task_file = task.get('github_file')
        if task_file in argv:
            correction_base_url = 'https://intranet.hbtn.io/tasks/'
            correction_url = '{}{}/start_correction.json?auth_token={}'.format(
                correction_base_url, task_id, auth)
            correction_res_id = requests.post(
                correction_url, params=payload).json().get('id')
            result_base_url = 'https://intranet.hbtn.io/correction_requests/'
            correction_result_url = '{}{}.json?auth_token={}'.format(
                result_base_url, correction_res_id, auth)
            # static route to return a correction result we know
            # correction_result_url = '{}3591396.json?auth_token={}'.format(
            #     correction_base_url, auth)
            correction_result = requests.get(
                correction_result_url, params=payload).json()
            checks = correction_result.get('result_display').get('checks')
            checks_dict.update({task_id: checks})
    print(checks_dict)
