"""
%% Version V1
%  Authors - Mario De Los Santos, Santiago Rossi
%  Date - January 13th, 2023
%  Description:
%       Class create to send the recompile images to google cloud storage. 
%
%% Input Parameters
%
% - Object: Python Dictionary with: {
    'ServicekeyPath': 'From Google Cloub Service',
    'BucketName' : '',
    'BucketLocation' : '',
    'FilePath' : 'To read and download data'
    }
%%
"""
import os 
import pathlib
import mimetypes
from google.cloud import storage 


class GoogleCloud:
    def __init__(self, Object):
        self.GClient = Object
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.GClient['ServicekeyPath']
        self.storage_client = storage.Client()

    def GoogleCloud_CreateBucket(self):
        #Data extraction
        self.Bucket_name = self.GClient['BucketName']
        self.Bucket_location = self.GClient['BucketLocation']
        
        Verification = self.GoogleCloud_listbuckets()
        if not self.Bucket_name in Verification:
            #Bucket creation
            Bucket = self.storage_client.bucket(self.Bucket_name)
            Bucket.location = self.Bucket_location
            Bucket = self.storage_client.create_bucket(Bucket)
            print('Created')
        else:
            Bucket = self.storage_client.get_bucket(self.Bucket_name)
            print('Called')


    def GoogleCloud_listbuckets(self):
        Buckets = self.storage_client.list_buckets()
        return [bucket.name for bucket in Buckets]


    def GoogleCloud_Uploadfile(self, blob_name, file_path): 
        try:
            Bucket = self.storage_client.get_bucket(self.Bucket_name);
            Blob = Bucket.blob(blob_name)
            Blob.upload_from_filename(self.GClient['FilePath'] + file_path)

        except Exception as error:
            print(error)
            return 

    def GoogleCloud_download(self, blob_name, download_path):
        try:
            Bucket = self.storage_client.get_bucket(self.Bucket_name)
            Blob = Bucket.blob(blob_name)
            with open(os.path.join(os.getcwd(), download_path), 'wb') as f:
                self.storage_client.download_blob_to_file(Blob, f)
            return True
        except Exception as error:
            print(error)
            return False

    def GoogleCloud_delete(self, blob_name):
        try:
            Bucket = self.storage_client.get_bucket(self.Bucket_name)
            Blob = Bucket.blob(blob_name)
            Blob.delete()
            return True
        except Exception as error:
            print(error)
            return False






