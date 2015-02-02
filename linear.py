import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import couchdb

server = couchdb.Server()
db = server['questions']
java = []
for i in db:
	for j in db[i]['items']:
		if j['name']['name'] == 'java':
			java.append(j['total'])

print len(java)
n = len(java)
x = np.arange(n)
y = np.append([],java[::-1])

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression
print('Coefficients: ', lr.coef_)
fig = plt.figure()
plt.plot(x, y, 'r.', markersize=n)
plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')
plt.legend(('Data', 'Linear Fit'), loc='lower right')
plt.title('Linear regression')
plt.savefig('fig.png')