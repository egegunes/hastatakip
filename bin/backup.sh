#!/bin/bash

set -eu

source "$HOME/hastatakip/playbooks/env/backup"

echo "Initiated backup at $(date)"

ansible-playbook \
    -c local \
    -i "localhost," \
    "$HOME/hastatakip/playbooks/backup.yml"
