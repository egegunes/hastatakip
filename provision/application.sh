#!/bin/bash

cat /dev/urandom | tr -cd "0-9a-zA-Z" | fold -w 128 | head -n 1 | sudo tee /etc/secret

mkdir -p /home/hastatakip/logs
touch /home/hastatakip/logs/django.log
chown vagrant:vagrant /home/hastatakip/logs/django.log

mkdir -p /home/hastatakip/db

[ -d "environment" ] && rm -rf environment

pyvenv-3.5 environment
source environment/bin/activate

pip3.5 install --upgrade pip
pip3.5 install -r hastatakip/requirements.txt

cd hastatakip/src

python3.5 manage.py makemigrations
python3.5 manage.py migrate
