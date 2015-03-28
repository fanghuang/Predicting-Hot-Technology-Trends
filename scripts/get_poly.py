import numpy as np
import math

from datetime import date, timedelta
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

db_name = "stackoverflow_new"

server = couchdb.Server()

db = server[db_name]

java = []

data = {}

for doc in db:
	doc_obj = db[doc]
	for tech in doc_obj['items']:
		name = tech['name']
		if name not in data:
			data[name] = []
		data[name].append( (doc_obj['date'], tech['count']))

regressions = {}
R_squared = {}
count = 0
numPlots = 10
degree = 6
for tech in data:
	d = data[tech]
	d.sort()
	y = np.array([x[1] for x in d])
	x = np.array(range(len(y)))
	
	p, r_sq = getPolyfit(x,y,degree)
	regressions[tech] = p
	R_squared[tech] = r_sq
	# print R_squared[tech]

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
plt.savefig('figure.png')

r_sum = sum([R_squared[x] if not math.isnan(R_squared[x]) else 0 for x in R_squared])
num_none_zero = sum([1 if not math.isnan(R_squared[x]) else 0 for x in R_squared])
print '--%d Degree Polyfit--' % degree
print 'There are %d non-zero regressions, and %d total regressions' % (num_none_zero, len(R_squared))
print 'Sum R^2: %f  Avg: %f' % (r_sum, r_sum/float(num_none_zero))

## Calculate First Derivatives on Last Day
last_day = len(y)-1
first_deriv = []
for tech in regressions:
	p = regressions[tech]
	deriv = p.deriv()
	first_deriv.append( (deriv(last_day), tech))

first_deriv.sort(reverse=True)
print 'Top 10 Techs by first Deriv:'
for d, tech in first_deriv[:10]:
	print '%s: %f' % (tech, d) 
