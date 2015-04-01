import couchdb
import oauth2 as oauth
import xml.etree.ElementTree as ET
from datetime import datetime

today = datetime.today()
#url = "http://api.linkedin.com/v1/companies/1337"
#url = "https://api.linkedin.com/v1/job-search?company-name=Facebook"
#url = 'https://api.linkedin.com/v1/job-search?&keywords=python&facet=date-posted,'+yesterday.strftime('%Y%m%d')
#url = "https://api.linkedin.com/v1/job-search?job-title=Software+Engineer"
#url = "https://api.linkedin.com/v1/companies/162479"
baseurl = 'https://api.linkedin.com/v1/job-search?&keywords='

consumer = oauth.Consumer(
     key="77hjmrg7xoj582",
     secret="xHDKhWWs4mCLawNH")
     
token = oauth.Token(
     key="ae84e3e4-d29a-4492-b925-6b4836b7ceb6", 
     secret="d275a5a2-2494-4807-9540-02e653e46cbe")

server = couchdb.Server('http://localhost:9000')
tagdb = server['tags']
tags = tagdb['a2fa8c775de9bc7d97ea22c5a9135649']['items']
#db = server.create('linkedin')
db = server['linkedin']

client = oauth.Client(consumer, token)

lists = []
tmp = 0
for tagname in tags:
	url = baseurl + tagname['name']
	resp, content = client.request(url)
	root = ET.fromstring(content)
	total = root[0].attrib["total"]
	lists.append({
				'name':tagname['name'],
				'total':total
				})
	print tagname['name'], total
	#easily hit hrottle limit
	if tmp == 10:
		break
	tmp += 1
	

doc = {
        'processdate': today.isoformat(),
		'items': lists
}

db.save(doc)