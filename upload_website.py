
import boto3
import os
import sys
from mimetypes import guess_type

# AWS Mumbai region
REGION = "ap-south-1"

# Read bucket name from command line
if len(sys.argv) != 2:
    print("Usage: python upload_website.py YOUR_BUCKET_NAME")
    sys.exit(1)

BUCKET_NAME = sys.argv[1]
WEBSITE_FOLDER = "website"

def upload_website():
    s3 = boto3.client("s3", region_name=REGION)

    if not os.path.isdir(WEBSITE_FOLDER):
        print("Error: website folder not found.")
        return

    files_uploaded = 0

    for root, dirs, files in os.walk(WEBSITE_FOLDER):
        for filename in files:
            file_path = os.path.join(root, filename)
            s3_key = os.path.relpath(
                file_path, WEBSITE_FOLDER
            ).replace("\\", "/")

            content_type, _ = guess_type(file_path)

            extra_args = {}
            if content_type:
                extra_args["ContentType"] = content_type

            s3.upload_file(
                file_path,
                BUCKET_NAME,
                s3_key,
                ExtraArgs=extra_args
            )

            print(f"Uploaded: {s3_key}")
            files_uploaded += 1

    print(f"\nSuccess! Uploaded {files_uploaded} file(s).")
    print(f"S3 bucket: {BUCKET_NAME}")

if __name__ == "__main__":
    try:
        upload_website()
    except Exception as error:
        print("Upload failed:", error)
