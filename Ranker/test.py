import ranker
import scorers
import importers

data = importers.mongoDBImporterCoreySchema("stackoverflow_new")
r = ranker.Ranker(data)

# print r.testScore(scorers.countTrendsTimesPercentIncrease)
print r.rank(scorers.countTrendsTimesPercentIncrease)