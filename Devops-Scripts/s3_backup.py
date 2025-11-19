import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3, bucket_name, region):
    """
    Create an S3 bucket in a specified region.
    """
    if region == "us-east-2":
        # us-east-1 does NOT require LocationConstraint
        s3.create_bucket(Bucket=bucket_name)
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': region}
        )
    print("Bucket created successfully")


def upload_backup(s3, file_name, bucket_name, key_name):
    with open(file_name, "rb") as data:
        s3.Bucket(bucket_name).put_object(
            Key=key_name,
            Body=data
        )
    print("Backup uploaded successfully")


# Your bucket details
bucket_name = "akhil-s3-bucket-demo"   # must be globally unique
region = "us-east-2"

# File to upload
file_name = "/Users/akhilanto/Desktop/git_repo/python-chronicles/python.tar.gz"

# Upload the file
upload_backup(s3, file_name, bucket_name, "python.tar.gz")
