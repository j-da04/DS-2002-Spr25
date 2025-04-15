import requests
import boto3
import sys
import os

def fetch_file(url, local_filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {local_filename}")
    else:
        print(f"Failed to download file: {response.status_code}")
        sys.exit(1)

def upload_to_s3(file_path, bucket, key):
    s3 = boto3.client('s3')
    with open(file_path, 'rb') as f:
        s3.upload_fileobj(f, bucket, key)
    print(f"Uploaded to S3: s3://{bucket}/{key}")

def generate_presigned_url(bucket, key, expiration):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=expiration
    )
    return url

if __name__ == "__main__":
    # You can replace this with any small public file
    file_url = "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif"
    local_filename = "funny.gif"
    bucket_name = "ds2002-cwj8uw"  # <-- Replace with your bucket
    expiration_seconds = 604800  # 7 days

    fetch_file(file_url, local_filename)
    upload_to_s3(local_filename, bucket_name, local_filename)
    url = generate_presigned_url(bucket_name, local_filename, expiration_seconds)

    print("Presigned URL (valid for 7 days):")
    print(url)

    # Clean up local file (optional)
    os.remove(local_filename)
