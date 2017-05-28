#!/bin/bash

PERIOD=$1
BACKUPDIR="/home/hastatakip/backups/backups.never"

if [ "$PERIOD" == "daily" ]; then
    BACKUPDIR="/home/hastatakip/backups/backups.hourly"
    MOVEDIR="/home/hastatakip/backups/backups.daily"
elif [ "$PERIOD" == "weekly" ]; then
    BACKUPDIR="/home/hastatakip/backups/backups.daily"
    MOVEDIR="/home/hastatakip/backups/backups.weekly"
elif [ "$PERIOD" == "monthly" ]; then
    BACKUPDIR="/home/hastatakip/backups/backups.weekly"
    MOVEDIR="/home/hastatakip/backups/backups.monthly"
fi

LASTBACKUP=$(ls -t $BACKUPDIR | head -1)
NAME=$(date +%d-%m-%y)
NEWFILE="$NAME.sqlite3"

mv $BACKUPDIR/$LASTBACKUP $MOVEDIR/$NEWFILE

if [ $? -ne 0 ]; then
	python /home/hastatakip/bin/push "Local error while deleting old backups $PERIOD"
fi

rm $BACKUPDIR/*

if [ $? -ne 0 ]; then
	python /home/hastatakip/bin/push "Local error while deleting old backups $PERIOD"
fi

python /home/hastatakip/bin/dropbox_delete_old.py $PERIOD

if [ $? -ne 0 ]; then
	python /home/hastatakip/bin/push "Cloud error while deleting old backups $PERIOD"
fi
