#!/bin/bash

# Check for 3 arguments
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <file-to-upload> <bucket-name> <expiration-in-seconds>"
    exit 1
fi

FILE=$1
BUCKET=$2
EXPIRATION=$3
KEY=$(basename "$FILE")  # Use filename as object key

# Upload the file to the S3 bucket (private by default)
aws s3 cp "$FILE" "s3://$BUCKET/$KEY" --acl private

# Generate a presigned URL
aws s3 presign "s3://$BUCKET/$KEY" --expires-in "$EXPIRATION"
