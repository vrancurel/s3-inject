import boto3
import multiprocessing

N_THREADS=50
N_OBJS=10
BUCKET='giorgio5'

def myfunc(i):
    print(i)
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id='accessKey1',
        aws_secret_access_key='verySecretKey1',
        endpoint_url='http://127.0.0.1:8000',
    )
    counter = 0
    for counter in xrange(0,N_OBJS):
        name = '%s%s' % ('obj', i*N_OBJS + counter)
        attr = '%s%s' % ('bar', i*N_OBJS + counter)
        print(name)
        s3_client.put_object(Bucket=BUCKET,
                             StorageClass='REDUCED_REDUNDANCY',
                             Key=name,
                             Body='this is a test',
                             Metadata={ 'foo': attr, 'bar': 'qux' })

for i in range(N_THREADS):
    t = multiprocessing.Process(target=myfunc, args=(i,))
    t.start()
