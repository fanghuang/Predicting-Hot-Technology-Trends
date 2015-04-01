import requests, json

page = 1
pagesize = 100
has_more = True
total = 0

url = 'https://api.stackexchange.com/2.2/search?fromdate=1417392000&todate=1419984000&order=desc&sort=activity&tagged=apache-spark&site=stackoverflow&filter=!9YdnSQVoS'

lists = []
while (has_more) :

        payload = {
                'page':page,
                'pagesize':pagesize,
                'key':'XGgeLjmonD8zytJD18S3ug(('
                        }
        r = requests.get(url, params=payload)
        r = r.json()
        
        for i in r["items"]:
            total +=i['view_count']

        lists = lists + r["items"]
        has_more = r['has_more']

        page += 1
        
print page
print total