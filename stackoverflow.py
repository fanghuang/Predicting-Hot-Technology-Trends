import requests
import tech
from datetime import date, timedelta
import couchdb


def getNumQuestionsWithTagInLastDay(tag):
	base_url = 'https://api.stackexchange.com'

	question_url = base_url + "/2.2/questions"

	today = date.today()
	yesterday = today - timedelta(days=1)

	payload = {
		'filter': 'total', #Return the quantity of matching items, not the actual items
		'fromdate': yesterday,
		'todate': today,
		'site': 'stackoverflow',
		'tagged': tag
	}

	r = requests.get(question_url, params=payload)

	return r.json()['total']

db_name = "stackoverflow"

server = couchdb.Server()
if db_name not in server:
	server.create(db_name)
db = server[db_name]

today = date.today()
yesterday = today - timedelta(days=1)

doc = {
	'date': yesterday.isoformat()
}

for n in tech.listTechnologies():
	doc[n] = getNumQuestionsWithTagInLastDay(n)

db.save(doc)




