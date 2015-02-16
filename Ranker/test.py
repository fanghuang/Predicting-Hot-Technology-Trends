import ranker
import scorers
import importers
import htmltmpl

data = importers.mongoDBImporterFangSchema("questions")
r = ranker.Ranker(data)

# print r.testScore(scorers.countTrendsTimesPercentIncrease)
print r.rank(scorers.countTrendsTimesPercentIncrease)
data = r.rank(scorers.countTrendsTimesPercentIncrease)
htmltmpl.pageGenerator(data,10)