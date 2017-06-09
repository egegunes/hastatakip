#!/usr/bin/env python3.5

import dropbox
import datetime
import sys
from dropbox_token import ACCESS_TOKEN


dbx = dropbox.Dropbox(ACCESS_TOKEN)

today = str(datetime.date.today())

if sys.argv[1] == "daily":
    dbfolder = '/backups/db/hourly'
    new_path = '/backups/db/daily/%s.sqlite3' % today
elif sys.argv[1] == "weekly":
    dbfolder = '/backups/db/daily'
    new_path = '/backups/db/weekly/%s.sqlite3' % today
elif sys.argv[1] == "monthly":
    dbfolder = '/backups/db/weekly'
    new_path = '/backups/db/monthly/%s.sqlite3' % today

for entry in dbx.files_list_folder(dbfolder).entries:
    tmp = datetime.datetime(2016,10,9,0,0,0)
    server_modified = entry.server_modified
    if server_modified > tmp:
        tmp = server_modified 
        f = entry

current_path = f.path_lower

dbx.files_move(current_path, new_path)

dbx.files_delete(dbfolder)
