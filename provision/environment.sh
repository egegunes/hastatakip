#!/bin/bash

cat <<EOF > /home/vagrant/.bash_profile
source ~/.bashrc
export DJANGO_SECRET_KEY=$(cat /dev/urandom | tr -cd "0-9a-zA-Z" | fold -w 128 | head -n 1)
export DJANGO_DB_PATH="/home/vagrant/db.sqlite3"
export DJANGO_LOG_FILE="/home/vagrant/django.log"
export DJANGO_LOG_LEVEL="DEBUG"
export DJANGO_STATIC_ROOT="/home/vagrant/static/"
export DJANGO_MEDIA_ROOT="/home/vagrant/media/"
EOF
