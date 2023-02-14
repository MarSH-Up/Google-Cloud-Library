#Example
from src.GoogleCloud import GoogleCloud

#Testing class 

#Credentials Objects
GoogleCloudObject = {
    'ServicekeyPath': 'ServiceKey_GoogleCloud.json',
    'BucketName' : '',
    'BucketLocation' : 'US',
    'FilePath' : ''
    }

#Creating the Class Object
TestingGoogleClass = GoogleCloud(GoogleCloudObject)

#Creating the Bucket
TestingGoogleClass.GoogleCloud_CreateBucket()

#Upload
TestingGoogleClass.GoogleCloud_Uploadfile('Testing_Library', 'SirMeliodas.jpeg')

#Download
TestingGoogleClass.GoogleCloud_download('Testing_Library', 'SirMeliodas_cloud.jpeg')

#Delete File
Status = TestingGoogleClass.GoogleCloud_delete('Testing_Library')
print(Status)