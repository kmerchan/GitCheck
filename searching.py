#!/usr/bin/python3
"""
This is a program to mess with the Holberton API
"""

import requests
from os import path


def get_auth(email, api, pwrd):
    params = {
        "api_key": '{}'.format(api),
        "email": '{}'.format(email),
        "password": '{}'.format(pwrd),
        "scope": "checker"
    }
    nada = requests.post('https://intranet.hbtn.io/users/auth_token.json',
                         params=params)
    return nada.json().get('auth_token')

def test_auth():
    if path.exists('settings.py'):
        from settings import pwrd
        from settings import email
        from settings import api
        from settings import auth
    else:
        with open('settings.py', 'w') as f:
            email = input("Enter Holberton email: ")
            pwrd = input("Enter Holberton password: ")
            api = input("Enter Holberton API key: ")
            auth = get_auth(email, api, pwrd)
            f.write("#!/usr/bin/python3\nemail = '{}'\npwrd = '{}'\napi = '{}'\nauth = '{}'\n".format(email, pwrd, api, auth))
    check = requests.get('https://intranet.hbtn.io/users/me.json', params={'auth_token': auth})
    if check.status_code == 401:
        auth = get_auth(email, api, pwrd)
        with open('settings.py', 'w') as f:
            f.write("#!/usr/bin/python3\nemail = '{}'\npwrd = '{}'\napi = '{}'\nauth = '{}'\n".format(email, pwrd, api, auth))
test_auth()
