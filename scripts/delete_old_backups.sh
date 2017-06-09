#!/bin/bash

set -euo pipefail

PERIOD=$1
BACKUPDIR="/home/hastatakip/backups/backups.never"

case "$PERIOD" in
    "daily")
        BACKUPDIR="/home/hastatakip/backups/backups.hourly"
        MOVEDIR="/home/hastatakip/backups/backups.daily"
        ;;
    "weekly")
        BACKUPDIR="/home/hastatakip/backups/backups.daily"
        MOVEDIR="/home/hastatakip/backups/backups.weekly"
        ;;
    "monthly")
        BACKUPDIR="/home/hastatakip/backups/backups.weekly"
        MOVEDIR="/home/hastatakip/backups/backups.monthly"
        ;;
    *)
        exit 1
        ;;
esac

LASTBACKUP=$(ls -t $BACKUPDIR | head -1)
NAME=$(date +%Y-%m-%d)
NEWFILE="$NAME.sqlite3"

mv $BACKUPDIR/$LASTBACKUP $MOVEDIR/$NEWFILE

rm $BACKUPDIR/*

python /home/hastatakip/bin/dropbox_delete_old.py $PERIOD
