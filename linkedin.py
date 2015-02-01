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

root = ET.fromstring(content)

#print int(root[0].attrib["total"])
#print content


print "Python Total: " + root[0].attrib["total"]
