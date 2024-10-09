import boto3
from botocore.exceptions import NoCredentialsError


s3 = boto3.client('s3', 
                  aws_access_key_id='AKIAEXAMPLE123456',  # Ganti dengan Access Key ID Anda
                  aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCyEXAMPLEKEY')  # Ganti dengan Secret Access Key Anda


def upload_to_aws(local_file, bucket, s3_file):
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"File {local_file} berhasil diunggah ke {bucket}/{s3_file}")
        return True
    except FileNotFoundError:
        print("File tidak ditemukan")
        return False
    except NoCredentialsError:
        print("Kredensial tidak tersedia")
        return False


local_file = 'test.txt'

bucket = 'nama-bucket-anda'

s3_file = 'test.txt'


uploaded = upload_to_aws(local_file, bucket, s3_file)
