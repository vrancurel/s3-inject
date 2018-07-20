import boto3
import multiprocessing

def myfunc(i):
    session = boto3.session.Session()
    s3_client = session.client(
        service_name='s3',
        aws_access_key_id='5IN5X1TYPEV8SUIWYPL8',
        aws_secret_access_key='A+wW333pHOtIetpGg+OzPOyHtDWteSWGoioKiS=M',
        endpoint_url='http://zenko.local',
    )
    print(s3_client.list_buckets())
    counter = 0
    for counter in xrange(0,5000000):
        name = '%s%s' % ('obj', (counter + i) % 100)
        print(name)
        obj = s3_client.get_object(Bucket='testb11',
                                   Key=name)

for i in range(64):
    t = multiprocessing.Process(target=myfunc, args=(i,))
    t.start()
