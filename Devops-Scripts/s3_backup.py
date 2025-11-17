import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket_name)

def create_bucket(s3, bucket_name, region):
    """
    Create an S3 bucket in a specified region.
    """
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
    print("Bucket created successfully")


def upload_backup(s3, file_name, bucket_name, key_name):
    """
    Upload a file (backup) to the specified S3 bucket.
    """
    data = (file_name, 'rb')   # read in binary mode
    s3.Bucket(bucket_name).put_object(
            Key=key_name,
            Body=data
        )
    print("Backup uploaded successfully")



# Your bucket details
bucket_name = "Akhil-S3-Bucket"
region = "us-east-2"

# File to upload
file_name = "Give file path here"

# Upload the file
upload_backup(s3, file_name, bucket_name, "my-backup.tar.gz")
