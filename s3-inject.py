import boto3
import multiprocessing

def myfunc(i):
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id='SJC6KQDGRRLSQ9QJ0ODZ',
        aws_secret_access_key='5EmgJJ4y2vJBKV3pS8t/l45kmaRkb4cdlBOE9NhC',
        endpoint_url='http://10.233.99.137:8001',
    )
    counter = 0
    for counter in xrange(0,1000000000):
        name = '%s%s' % ('obj', counter + i)
        attr = '%s%s' % ('bar', counter + i)
        print(name)
        s3_client.put_object(Bucket='foob8',
                             StorageClass='REDUCED_REDUNDANCY',
                             Key=name,
                             Body='this is a test',
                             Metadata={ 'foo': attr, 'bar': 'qux' })

for i in range(3):
    t = multiprocessing.Process(target=myfunc, args=(i,))
    t.start()
