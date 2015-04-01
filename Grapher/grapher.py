import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def movingaverage(values, window):
	weights = np.repeat(1.0, window)/window
	smas = np.convolve(values, weights, 'valid')
	return smas

class Grapher:

	def __init__(self):
		pass

	def generateSMAImages(self, data):
		# print data.keys()
		for tech in data:

			# print tech
			totals = [x[1] for x in data[tech]]
			x = range(1,len(totals)+1)

			sma2 = movingaverage(totals, 2)
			sma3 = movingaverage(totals, 3)
			sma5 = movingaverage(totals, 5)

			fig = plt.figure()
			plt.plot(x, totals, 'c.', markersize=12)
			plt.plot(x[len(x)-len(sma2):], sma2, 'r-', markersize=12)
			plt.plot(x[len(x)-len(sma3):], sma3, 'b-', markersize=12)
			plt.plot(x[len(x)-len(sma5):], sma5, 'g-', markersize=12)

			plt.legend((tech, 'SMA2', 'SMA3', 'SMA5'), loc=2)
			plt.title(tech+' Simple Moving Average')
			plt.savefig('/vagrant/generated_report/imgs/'+tech.replace('.',''))
			plt.close()