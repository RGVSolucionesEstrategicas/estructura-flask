# python/services/s3_service.py

import os
import uuid
import boto3
from python.models.rds_models import Files, db


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name=os.getenv("AWS_REGION"),
        )
        self.bucket_name = os.getenv("AWS_S3_BUCKET_NAME")

    def upload_file(self, file):
        """Sube un archivo a S3 con un nombre UUID y lo guarda en la base de datos."""
        try:
            file_uuid = str(uuid.uuid4())
            filename = file.filename
            filepath = f"{file_uuid}_{filename}"

            # Subir a S3
            self.s3_client.upload_fileobj(file, self.bucket_name, filepath)

            # Crear la URL del archivo
            file_url = f"https://{self.bucket_name}.s3.{os.getenv('AWS_REGION')}.amazonaws.com/{filepath}"

            # Guardar en la base de datos
            new_file = Files(filename=filename, filepath=file_url)
            db.session.add(new_file)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Error al subir el archivo: {e}")
