# python/services/s3_service.py

import os

import boto3
from botocore.exceptions import NoCredentialsError


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        self.bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

    def upload_file(self, file, filename):
        """Sube un archivo a S3 sin usar ACLs."""
        try:
            self.s3_client.upload_fileobj(file, self.bucket_name, filename)
            file_url = f"https://{self.bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filename}"
            return file_url
        except NoCredentialsError:
            raise Exception("Credenciales de AWS no encontradas.")
        except Exception as e:
            raise Exception(f"Error al subir el archivo: {e}")
