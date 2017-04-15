#!/bin/bash

sudo postgresql-setup initdb
sudo -u postgres -g postgres psql <<EOF
DROP DATABASE IF EXISTS hastatakip;
DROP ROLE IF EXISTS hastatakip;
CREATE ROLE hastatakip PASSWORD 'afahfl1471947ada91ndan1e209j1j' NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT LOGIN;
CREATE DATABASE hastatakip OWNER hastatakip;
EOF
sed -i 's/^local\s\+all\s\+all\s\+peer/local all all md5/g' /var/lib/pgsql/data/pg_hba.conf
systemctl restart postgresql.service
