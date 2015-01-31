import requests, json
from datetime import datetime, timedelta

url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&filter=!9YdnSQVoS&key=XGgeLjmonD8zytJD18S3ug(('

d1 = datetime(2013, 1, 1)
d2 = datetime(2014, 12, 1)
epoch = datetime(1970,1,1)

print (d1-epoch).total_seconds()
#payload = {'tagged':'java'}
payload = {'tagged':'java','fromdate':int((d1-epoch).total_seconds()),'todate':int((d2-epoch).total_seconds())}

r = requests.get(url, params=payload)
#r = requests.get(url)
print r.url
r = r.json()
print r
print r['total'],r['quota_remaining']