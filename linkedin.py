import oauth2 as oauth
import xml.etree.ElementTree as ET
from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
#url = "http://api.linkedin.com/v1/companies/1337"
#url = "https://api.linkedin.com/v1/job-search?company-name=Facebook"
url = 'https://api.linkedin.com/v1/job-search?&keywords=python&facet=date-posted,'+yesterday.strftime('%Y%m%d')
print url
#url = "https://api.linkedin.com/v1/job-search?job-title=Software+Engineer"
#url = "https://api.linkedin.com/v1/companies/162479"

consumer = oauth.Consumer(
     key="77hjmrg7xoj582",
     secret="xHDKhWWs4mCLawNH")
     
token = oauth.Token(
     key="ae84e3e4-d29a-4492-b925-6b4836b7ceb6", 
     secret="d275a5a2-2494-4807-9540-02e653e46cbe")


client = oauth.Client(consumer, token)
resp, content = client.request(url)

# root = ET.fromstring(content)

# print int(root[0].attrib["total"])
print content



# import requests
# import tech
# from datetime import date, timedelta
# import couchdb


# def getNumQuestionsWithTagInLastDay(tag):
# 	today = date.today()
# 	yesterday = today - timedelta(days=1)

# 	url = 'https://api.linkedin.com/v1/job-search?keywords='+tag+'&facet=date-posted,'+yesterday.strftime('%Y%m%d')

# 	resp, content = client.request(url)

# 	root = ET.fromstring(content)

# 	print int(root[0].attrib["total"])

	

# 	payload = {
# 		'filter': 'total', #Return the quantity of matching items, not the actual items
# 		'fromdate': yesterday,
# 		'todate': today,
# 		'site': 'stackoverflow',
# 		'tagged': tag
# 	}

# 	r = requests.get(url, params=payload)

# 	if 'total' in r.json():
# 		return r.json()['total']
# 	else:
# 		return 0

# db_name = "stackoverflow"

# server = couchdb.Server()
# if db_name not in server:
# 	server.create(db_name)
# db = server[db_name]

# today = date.today()
# yesterday = today - timedelta(days=1)

# doc = {
# 	'date': yesterday.isoformat()
# }

# for n in tech.listTechnologies():
# 	doc[n] = getNumQuestionsWithTagInLastDay(n)
# 	print "%s: %s" % (n, doc[n])

# db.save(doc)


print "Python Total: " + root[0].attrib["total"]
