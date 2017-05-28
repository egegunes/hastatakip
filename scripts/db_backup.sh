DATABASE=/home/hastatakip/db/db.sqlite3
BACKUPDIR=/home/hastatakip/backups/backups.hourly
BACKUPDB="db-$(date +%d-%m-%y-%H-%M).sqlite3"
DAY=$(date +%d-%m-%y)
TIME=$(date +%H:%M)

BACKUP=$(sqlite3 $DATABASE ".backup $BACKUPDIR/$BACKUPDB")

if [ $? -ne 0 ]; then
	python /home/egegunes/bin/push "DB backup error (local)"
fi
	
cd $BACKUPDIR

UPLOAD=$(python ~/bin/dropbox_upload.py $BACKUPDB)

if [ $? -ne 0 ]; then
	python /home/egegunes/bin/push "DB backup error (cloud)"
fi
