#!/bin/bash

set -eu

source "$HOME/environment/bin/activate"
source "$HOME/hastatakip/playbooks/env/backup"

echo "Initiated restore at $(date)"

ansible-playbook \
    -c local \
    -i "localhost," \
    "$HOME/hastatakip/playbooks/restore.yml"
