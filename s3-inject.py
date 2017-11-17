import boto3

session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id='accessKey1',
    aws_secret_access_key='verySecretKey1',
    endpoint_url='http://127.0.0.1',
)

print(s3_client.list_buckets())

counter = 0
for counter in range(0,2000):
    name = '%s%s' % ('obj', counter)
    print(name)
    s3_client.put_object(Bucket='foob3',
                         StorageClass='REDUCED_REDUNDANCY',
                         Key=name,
                         Body='this is a test',
                         Metadata={ 'foo': 'bar' })
