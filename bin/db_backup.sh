#!/bin/bash

set -eu

echo "Initiated backup at $(date)"

DATABASE="$HOME/db/db.sqlite3"
BACKUPDIR="$HOME/backups/db"
BACKUPDB="db-$(date +%Y-%m-%d-%H%M).sqlite3"

sqlite3 $DATABASE ".backup $BACKUPDIR/$BACKUPDB"
