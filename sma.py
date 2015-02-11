import couchdb
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def movingaverage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas


server = couchdb.Server('http://localhost:9000')
#server = couchdb.Server()
tagdb = server['tags']
tags = tagdb['a2fa8c775de9bc7d97ea22c5a9135649']['items']

db = server['questions']

x = range(1,61)

counter = 0
for tagname in tags:
	counter+=1
	tmplist = []
	for i in db:
		for j in db[i]['items']:
			if j['name']['name'] == tagname['name']:
				tmplist.append(j['total'])

	print tagname['name'], len(tmplist[::-1])
	sma2 = movingaverage(tmplist[::-1], 2)
	sma3 = movingaverage(tmplist[::-1], 3)
	sma5 = movingaverage(tmplist[::-1], 5)

	fig = plt.figure()
	plt.plot(x, tmplist[::-1], 'c.', markersize=12)
	plt.plot(x[len(x)-len(sma2):], sma2, 'r-', markersize=12)
	plt.plot(x[len(x)-len(sma3):], sma3, 'b-', markersize=12)
	plt.plot(x[len(x)-len(sma5):], sma5, 'g-', markersize=12)

	plt.legend((tagname['name'], 'SMA2', 'SMA3', 'SMA5'), loc='lower right')
	plt.title('Simple Moving Average')
	plt.savefig(str(counter))