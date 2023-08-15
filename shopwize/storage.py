# Storage classs configurations:

from django.core.files.storage import default_storage
from storages.backends.s3boto3 import S3Boto3Storage

class ShopWizeS3Boto3Stoarage(S3Boto3Storage):
    def url(self, name):
        return super().url(name)