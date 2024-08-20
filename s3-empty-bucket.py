import boto3
import openpyxl
from datetime import datetime

def list_empty_buckets():
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Create an Excel workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Bucket Details'
    ws.append(['Bucket Name', 'Creation Date', 'Object Count', 'Last Access Date'])
    
    # List all S3 buckets
    response = s3.list_buckets()
    buckets = response.get('Buckets', [])
    
    print(f"Total Buckets Found: {len(buckets)}")
    
    for bucket in buckets:
        bucket_name = bucket['Name']
        creation_date = bucket['CreationDate'].replace(tzinfo=None)  # Remove timezone info
        
        print(f"Checking Bucket: {bucket_name}")
        
        # Initialize object count and last access date
        object_count = 0
        last_access_date = None
        
        # Check the object count in the bucket
        objects = s3.list_objects_v2(Bucket=bucket_name)
        object_count = objects.get('KeyCount', 0)
        
        if object_count > 0:
            # Get the last modified date of the most recent object
            last_access_date = max(obj['LastModified'] for obj in objects.get('Contents', [])).replace(tzinfo=None)
            print(f"Bucket: {bucket_name}, Object Count: {object_count}, Last Access Date: {last_access_date}")
        else:
            print(f"Bucket: {bucket_name} is empty.")
        
        # Append the bucket information to the worksheet
        ws.append([bucket_name, creation_date, object_count, last_access_date])
    
    # Save the workbook to a local file
    output_file = 'bucket_details.xlsx'
    wb.save(output_file)
    
    print(f"Excel file created: {output_file}")

if __name__ == "__main__":
    list_empty_buckets()
