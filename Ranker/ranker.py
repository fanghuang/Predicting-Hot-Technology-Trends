import couchdb
import utils

class Ranker:

	def __init__(self, data):
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