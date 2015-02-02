import requests, json
import couchdb
from datetime import date
from dateutil.relativedelta import relativedelta

url = 'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&filter=!9YdnSQVoS'

firstdate = date(2011, 7, 1)
epoch = date(1970,1,1)

server = couchdb.Server()
#db = server.create('questions')
tagdb = server['tags']
tags = tagdb['a2fa8c775de9bc7d97ea22c5a9135649']['items']

db = server['questions']
#tags = ['javascript','java','c','python','swift']

for i in range(18):
#for i in range(1):
	t1 = firstdate - relativedelta(months=i+1)
	t2 = firstdate - relativedelta(months=i)
	d1 = int(((t1) - epoch).total_seconds())
	d2 = int(((t2) - epoch).total_seconds())
	time_series = [d1, d2]
	lists = []
	print t1, t2

	for tagname in tags:		
		#tagname = i['name']
		payload = {
			'fromdate':d1, 
			'todate':d2, 
			'tagged':tagname['name'],
			'key':'XGgeLjmonD8zytJD18S3ug(('
				}
		r = requests.get(url, params=payload)
		r = r.json()
		#print r
		total = r['total']
		print 'quota_remaining:', r['quota_remaining']
		#print tagname
		lists.append({
				'name':tagname,
				'total':total
			})
		#print lists

	doc = {
			'fromdate': t1.isoformat(),
			'todate': t2.isoformat(),
			'items': lists
	}

	db.save(doc)

	