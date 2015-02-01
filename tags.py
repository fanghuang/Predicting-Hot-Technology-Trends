import requests, json
import couchdb
from datetime import date, timedelta


page = 1
pagesize = 100
has_more = True
url = 'https://api.stackexchange.com/2.2/tags?order=desc&sort=popular&site=stackoverflow&filter=!bMMRSq0xzCuaKt'

server = couchdb.Server()
#db = server.create('tags')
db = server['tags']
lists = []
while (has_more) :

        payload = {
                'page':page,
                'pagesize':pagesize,
                'key':'XGgeLjmonD8zytJD18S3ug(('
                        }
        r = requests.get(url, params=payload)
        r = r.json()
        #print r
        print page

        lists = lists + r["items"]
        has_more = r['has_more']

        #if page == 20:
        if page == 5:
                has_more = False

        page += 1


today = date.today()
#yesterday = today - timedelta(days=1)

doc = {
        'date': today.isoformat(),
        'items': lists
}

db.save(doc)
