#!/bin/bash

set -eu

source "$HOME/hastatakip/playbooks/env/backup"

ansible-playbook \
    -c local \
    -i "localhost," \
    "$HOME/hastatakip/playbooks/backup.yml"
