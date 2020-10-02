#!/usr/bin/python3
"""
This is a program to set-up settings variables
for GitHub API and Holberton API and savse to file.
Program also checks current authentication key, if exits,
for Holberton API and creates new key if expired.
"""

import requests
from os import path


def get_auth(email, api, pwrd):
    """
    sends POST request to get new authorization token
    with Holberton credentials as data

    arguments:
        email: user's Holberton email for POST request
        api: user's Holberton API key for POST request
        pwrd: user's Holberton password for POST request
    """
    params = {
        "api_key": '{}'.format(api),
        "email": '{}'.format(email),
        "password": '{}'.format(pwrd),
        "scope": "checker"
    }
    response = requests.post('https://intranet.hbtn.io/users/auth_token.json',
                             params=params)
    return response.json().get('auth_token')


def test_auth():
    """
    imports variables from GitCheck_settings file or
    prompts the user to input their information
    and saves for future use
    """
    if path.exists('GitCheck_settings.py'):
        # imports existing settings variables from file
        from GitCheck_settings import pwrd
        from GitCheck_settings import email
        from GitCheck_settings import api
        from GitCheck_settings import auth
        from GitCheck_settings import gituser
        from GitCheck_settings import gitemail
        from GitCheck_settings import gitpwrd
    else:
        # prompts user to input settings information for API calls
        with open('GitCheck_settings.py', 'w') as f:
            email = input("Enter Holberton email: ")
            pwrd = input("Enter Holberton password: ")
            api = input("Enter Holberton API key: ")
            gituser = input("Enter GitHub username: ")
            gitemail = input("Enter GitHub email: ")
            gitpwrd = input("Enter GitHub password: ")
            auth = get_auth(email, api, pwrd)
            f.write("#!/usr/bin/python3\n \
            email = '{}'\n \
            pwrd = '{}'\n \
            api = '{}'\n \
            auth = '{}'\n \
            gituser = '{}'\n \
            gitemail = '{}'\n \
            gitpwrd = '{}'\n"
                    .format(email, pwrd, api, auth,
                            gituser, gitemail, gitpwrd))

    # determines if Holberton authentication token is valid
    check = requests.get('https://intranet.hbtn.io/users/me.json',
                         params={'auth_token': auth})
    # Optional print for testing: print(check.json())
    if check.status_code == 401:
        # creates new authentication token if expired and saves to file
        auth = get_auth(email, api, pwrd)
        with open('GitCheck_settings.py', 'w') as f:
            f.write("#!/usr/bin/python3\n \
            email = '{}'\n \
            pwrd = '{}'\n \
            api = '{}'\n \
            auth = '{}'\n \
            gituser = '{}'\n \
            gitemail = '{}'\n \
            gitpwrd = '{}'\n"
                    .format(email, pwrd, api, auth,
                            gituser, gitemail, gitpwrd))

# runs test_auth function to initialize variables and check authentication
test_auth()
