import numpy as np
import math

from datetime import datetime, timedelta
import couchdb

import matplotlib as mpl
mpl.use('Agg')
# mpl.rcParams['axes.color_cycle'] = ['r', 'r', 'g', 'g', 'b', 'b']
import matplotlib.pyplot as plt

def getPolyfit(x,y, degree=3):
	z = np.polyfit(x,y, degree)
    	p = np.poly1d(z)

    	yhat = p(x)
    	ybar = np.sum(y)/len(y)
    	ssreg = np.sum((yhat-ybar)**2)
    	sstot = np.sum((y - ybar)**2)

	return (p, ssreg/sstot)

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


db_name = "stackoverflow_new"

server = couchdb.Server()

db = server[db_name]

# Preprocess the data. Put it in a easier format to use
data = {}
for doc in db:
	doc_obj = db[doc]
	for tech in doc_obj['items']:
		name = tech['name']
		if name not in data:
			data[name] = []
		date = datetime.strptime(doc_obj['date'], "%Y-%m-%d")
		data[name].append( (date, tech['count']))

numPlots = 10
#degree = 3
num_to_avg=3
for degree in [x+1 for x in range(10)]:
	regressions = {}
	R_squared = {}
	sum_diff = {}
	count = 0
	plt.figure()
	for tech in data:
		d = data[tech]
		d.sort()
		
		first_day = d[0][0]	

		y = np.array([x[1] for x in d])
		x = np.array([(x[0]-first_day).days for x in d])

		
		y_sma = moving_average(y, num_to_avg)
		x_sma = x[1:-1]

		p, r_sq = getPolyfit(x_sma,y_sma,degree)
		regressions[tech] = p
		R_squared[tech] = r_sq		
		
		yhat = p(x)
		sum_diff[tech] = np.sum((yhat - y)**2)

		if count < numPlots and sum(p.coeffs) > 0:
			xp = np.linspace(0, 60,61)
			_ = plt.plot(xp, p(xp), '-', label=tech)
			# _ = plt.plot(xp, y, '.', label=tech)
			count += 1

	# print data.keys()[:5]
	# plt.legend(data.keys()[:numPlots])

	#print z
	#print data
	#print len(y)
	plt.ylim(-50,150)
	plt.savefig('figure-%d.png'%degree)

	r_sum = sum([R_squared[x] if not math.isnan(R_squared[x]) else 0 for x in R_squared])
	num_none_zero = sum([1 if not math.isnan(R_squared[x]) else 0 for x in R_squared])
	sum_sq_diffs = sum([sum_diff[x] if not math.isnan(sum_diff[x]) else 0 for x in sum_diff])
	
	print '--%d Degree Polyfit--' % degree
	print 'There are %d non-zero regressions, and %d total regressions' % (num_none_zero, len(R_squared))
	print 'Sum R^2: %f  Avg: %f' % (r_sum, r_sum/float(num_none_zero))
	print 'Sum of squared diffs between Polyfit and orig data: %f' % sum_sq_diffs

	## Calculate First Derivatives on Last Day
	#last_day = len(y)-1
	#first_deriv = []
	#for tech in regressions:
	#	p = regressions[tech]
	#	deriv = p.deriv()
	#	first_deriv.append( (deriv(last_day), tech))

	#first_deriv.sort(reverse=True)
	#print 'Top 10 Techs by first Deriv:'
	#for d, tech in first_deriv[:10]:
	#	print '%s: %f' % (tech, d) 
	#print ''
