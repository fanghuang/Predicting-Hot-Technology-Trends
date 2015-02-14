# Sample scorer that always returns 0
def sampleScorer( data,  t): #t is the tech to be scored
	return 0;

#Simply uses the last data point for the tech as the score
def lastDataPoint(data, t):
	data = data[t]

	last = data[-1]

	return last[1]


# Counts the number of data points in a row this tech has gone up or down
def countTrends(data, t):
	# We only care about this techs data. And we care about the data in revervse date order
	data = data[t][::-1]

	if (data[0][1] - data[1][1]) > 0:
		direction = 1
	else:
		direction = -1

	count = 0
	while (data[count][1] - data[count+1][1]) * direction > 0:
		count+=1

	return count*direction


# Counts the number of data points in a row this tech has gone up or down.
# Then multiplies this by the percent the tech has gone up 
def countTrendsTimesPercentIncrease(data, t):
	# We only care about this techs data. And we care about the data in revervse date order
	data = data[t][::-1]

	if (data[0][1] - data[1][1]) > 0:
		direction = 1
	else:
		direction = -1

	count = 0
	while (data[count][1] - data[count+1][1]) * direction > 0:
		count+=1

	if data[count][1] == 0:
		increase_percent = 0
	else:
		increase_percent = float(data[0][1])/data[count][1]

	print data[0][1], data[count][1], increase_percent
	return count*direction*increase_percent