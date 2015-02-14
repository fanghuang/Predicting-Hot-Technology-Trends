import requests
import couchdb
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import tech

def stringToDate(str):
	date_parts = [int(x) for x in str.split('-')]
	return date(year=date_parts[0], month=date_parts[1], day=date_parts[2])

def getNumQuestionsWithTagInDayBeforeGiven(tag, curr_date, return_quota = False):
	base_url = 'https://api.stackexchange.com'

	question_url = base_url + "/2.2/questions"

	today = curr_date
	tomorrow = today - timedelta(days=1)

	d1 = int(((tomorrow) - epoch).total_seconds())
	d2 = int(((today) - epoch).total_seconds())

	payload = {
		'filter': '!GeF-5sUcKKJEl', #This filter returns the total and quota_remaining
		'fromdate': d1,
		'todate': d2,
		'site': 'stackoverflow',
		'tagged': tag,
		'key':'XGgeLjmonD8zytJD18S3ug(('
	}

	r = requests.get(question_url, params=payload)
	r = r.json()

	total = r['total'] if 'total' in r else 0;
	
	if return_quota:
		return total, r['quota_remaining']
	return total

db_name = "stackoverflow_new"

server = couchdb.Server()

db = server[db_name]

finished_dates = sorted([db[doc]['date'] for doc in db])

epoch = date(1970,1,1)
start_date = stringToDate(finished_dates[0])
end_date = stringToDate(finished_dates[-1])

numDays = (end_date - start_date).days

techs, quota = tech.listTechnologies(return_quota=True)

for i in range(numDays):
	curr = start_date + relativedelta(days=i)
	if str(curr) not in finished_dates:
		#This date is missing. Add it

		if quota < len(techs)+10: #10 is simply a buffer so we don't use all the API calls
			# If there isn't enough requests availible dont run
			break

		print "Date: %s  Quota: %s" % (str(curr), quota)

		doc = {
			'date': curr.isoformat(),
			'items': []
		}

		for n in techs:
			count, quota = getNumQuestionsWithTagInDayBeforeGiven(n, curr, return_quota=True)
			doc['items'].append({
				'name': n,
				'count': count
			});

		db.save(doc)




