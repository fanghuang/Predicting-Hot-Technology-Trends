import ranker
import scorers

r = ranker.Ranker("stackoverflow_new")

# print r.testScore(scorers.countTrendsTimesPercentIncrease)
print r.rank(scorers.countTrendsTimesPercentIncrease)