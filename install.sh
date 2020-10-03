#!/usr/bin/env bash
# script to install dependencies to run GitCheck program
sudo apt-get -y install python3-git
sudo python -m pip install gitpython
sudo python -m pip install gitdb
sudo python -m pip install requests
