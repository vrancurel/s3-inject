import boto3

session = boto3.session.Session()

s3_client = session.client(
    service_name='s3',
    aws_access_key_id='IMD03TW256TY1R7HQTPY',
    aws_secret_access_key='pVVCtoAht=UHK7OCqoi=BlUN2UWbsXFPOTxNNw/p',
    endpoint_url='http://10.233.65.204:8001',
)

print(s3_client.list_buckets())

counter = 0
for counter in range(0,2000):
    name = '%s%s' % ('obj', counter)
    attr = '%s%s' % ('bar', counter)
    print(name)
    s3_client.put_object(Bucket='foob3',
                         StorageClass='REDUCED_REDUNDANCY',
                         Key=name,
                         Body='this is a test',
                         Metadata={ 'foo': attr, 'bar': 'qux' })
