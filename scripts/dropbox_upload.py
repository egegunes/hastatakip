#!/usr/bin/env python3.5

import dropbox, sys

dropbox = dropbox.Dropbox("EHv0uS6gWRMAAAAAAAA-4kIp0Q_xOMEnyC2w4TpvSL0EU-e9RU71ve0wf4rKUMIq")

filename = str(sys.argv[1])

with open(filename, "rb") as db:
    dropbox.files_upload(db.read(), "/backups/db/hourly/%s" % filename)
