#!/usr/bin/env python3.5

import sys
import dropbox
from dropbox_token import ACCESS_TOKEN


dropbox = dropbox.Dropbox(ACCESS_TOKEN)

filename = str(sys.argv[1])

with open(filename, "rb") as db:
    dropbox.files_upload(db.read(), "/backups/db/hourly/%s" % filename)
