import os

import boto3
import botocore


BUCKET_NAME = "hastatakip"
FILES = ["AH_ISTEK.pdf", "TTF.pdf"]

s3 = boto3.resource("s3")

for f in FILES:
    local_path = os.path.join("src/staticfiles", f)
    s3.Bucket(BUCKET_NAME).download_file(f, local_path)
