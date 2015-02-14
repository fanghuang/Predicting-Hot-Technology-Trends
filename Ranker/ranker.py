import couchdb
import utils

class Ranker:

	def __init__(self, db_name):
		self.db_name = db_name;

		# Get the data from Mongo and transform it
		server = couchdb.Server()
		db = server[db_name]
		data = {}

		for doc in db:
			doc_obj = db[doc]
			for tech in doc_obj['items']:
				name = tech['name']

				if name not in data:
					data[name] = []

				# Tests for different formats different dbs used
				if 'count' in tech:
					total = tech['count']
					date_str = doc_obj['date']
				elif 'total' in tech:
					total = tech['total']
					date_str = doc_obj['fromdate']
				else:
					print "ERROR: Neither count or total was found in data"
					exit()

				date = utils.stringToDate(date_str)

				data[name].append( (date, tech['count']))


		# Sort the data list for each technology because Mongo is unsorted
		for t in data:
			data[t].sort()

		self.data = data

	def score(self, scoreFunc):
		scores = [(t,scoreFunc(self.data, t)) for t in self.data.keys()]

		return scores

	# Get the scores then sort the list with the highest scores first
	def rank(self, scoreFunc):
		scores = self.score(scoreFunc)

		# Flip the order of the tuple, then sort the list
		scores = sorted( [(x[1],x[0]) for x in scores], reverse=True )

		# Re-flip the tuples and return the list
		return [(x[1],x[0]) for x in scores]

	#DEBUG CODE - Run the tech through the score func
	def testScore(self, scoreFunc, tech=None):
		if tech is None:
			tech = self.data.keys()[0]

		return scoreFunc(self.data, tech)