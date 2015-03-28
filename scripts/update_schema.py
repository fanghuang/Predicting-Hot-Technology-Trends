from datetime import date, timedelta
import couchdb

db_name = "stackoverflow"

db_name_new = "stackoverflow_new"

server = couchdb.Server()
if db_name not in server:
	server.create(db_name)
db = server[db_name]

if db_name_new in server:
	server.delete(db_name_new)
server.create(db_name_new)
db_new = server[db_name_new]

cur_date = date(2014,11,10)


for doc in db:
	doc_new = {
		'items': [],
		'date': cur_date.isoformat() 
	}
	
	if isinstance(db[doc]['date'],basestring):
		continue

	for tech in db[doc]:
		if tech[0] == '_':
			continue
		doc_new['items'].append({
			'name': tech,
			'count': db[doc][tech]
			})
		
	cur_date = cur_date + timedelta(days=1)

	db_new.save(doc_new)

