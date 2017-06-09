#!/bin/bash

set -euo pipefail

DATABASE=/home/hastatakip/db/db.sqlite3
BACKUPDIR=/home/hastatakip/backups/backups.hourly
BACKUPDB="db-$(date +%Y-%m-%d-%H%M).sqlite3"

sqlite3 $DATABASE ".backup $BACKUPDIR/$BACKUPDB"

cd $BACKUPDIR

/home/hastatakip/bin/dropbox_upload.py $BACKUPDB
