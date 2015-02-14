import ranker
import scorers
import importers

data = importers.mongoDBImporterFangSchema("questions")
r = ranker.Ranker(data)

# print r.testScore(scorers.countTrendsTimesPercentIncrease)
print r.rank(scorers.countTrendsTimesPercentIncrease)