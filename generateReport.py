import Ranker.ranker
import Ranker.scorers
import Ranker.importers
import Report.htmltmpl
import Report.expo

data = importers.mongoDBImporterFangSchema("questions")
r = ranker.Ranker(data)

# print r.testScore(scorers.countTrendsTimesPercentIncrease)
print r.rank(scorers.countTrendsTimesPercentIncrease)
data = r.rank(scorers.countTrendsTimesPercentIncrease)
#htmltmpl.pageGenerator(data,10)
expo.expoGenerator(data,10)