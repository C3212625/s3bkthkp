**S3 Bucket Details Script**

This repository contains a Python script to list out all unused and empty S3 buckets in your AWS account. The script generates an Excel file containing details such as the bucket name, creation date, object count, and the last access date of each bucket.
Features

    Lists all S3 buckets in your AWS account.
    Identifies and lists empty buckets.
    Retrieves the object count for each bucket.
    Fetches the last modified date of objects in each bucket to estimate the last access date.
    Exports the information to an Excel file (bucket_details.xlsx).

**Prerequisites**

    Python 3.x: Ensure that Python is installed on your system. You can download it from here.
    AWS CLI: The AWS CLI must be installed and configured with the necessary credentials. You can install it from here.
    Boto3: The AWS SDK for Python (Boto3) is required. You can install it using pip:
 
pip install boto3

OpenPyXL: This library is used for working with Excel files. You can install it using pip:

pip install openpyxl

**Installation**

Clone the repository:
git clone https://github.com/C3212625/s3bkthkp.git

Navigate to the project directory:

cd <project directory)

python s3_empty_bucket.py

   ** Output:**
        The script will generate an Excel file named bucket_details.xlsx in the same directory. This file will contain:
            Bucket Name: The name of the S3 bucket.
            Creation Date: The date the bucket was created.
            Object Count: The number of objects stored in the bucket.
            Last Access Date: The last modified date of the most recently modified object within the bucket (an approximation of last access).

**Notes:-**
    The "Last Access Date" is estimated based on the last modified date of the objects within the bucket. This may not always represent the exact last access time.
    Ensure that your AWS credentials have sufficient permissions to list S3 buckets, access object metadata, and perform other necessary operations.
