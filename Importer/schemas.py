import utils
import couchdb



def importerCoreySchema(db):
	# Get the data from Mongo and transform it
	data = {}

	for doc in db:
		doc_obj = db[doc]
		for tech in doc_obj['items']:
			name = tech['name']

			if name not in data:
				data[name] = []

			total = tech['count']
			date_str = doc_obj['date']

			date = utils.stringToDate(date_str)

			data[name].append( (date, tech['count']))


	# Sort the data list for each technology because Mongo is unsorted
	for t in data:
		data[t].sort()

	return data


def importerFangSchema(db):
	# Get the data from Mongo and transform it
	data = {}

	for doc in db:
		doc_obj = db[doc]
		for tech in doc_obj['items']:
			name = tech['name']['name']

			if name not in data:
				data[name] = []

			total = tech['total']
			date_str = doc_obj['fromdate']

			date = utils.stringToDate(date_str)

			data[name].append( (date, total))


	# Sort the data list for each technology because Mongo is unsorted
	for t in data:
		data[t].sort()
	
	return data