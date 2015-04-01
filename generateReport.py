from Importer import importer


from Ranker import ranker
from Ranker import scorers

from Report import htmltmpl
from Report import expo

from Grapher import grapher

#Import the data from the stackoverflow_monthly db
dataImporter = importer.Importer()
data = dataImporter.getDataFromDB("stackoverflow_monthly")

# Create a graph for each technology
g = grapher.Grapher()
g.generateSMAImages(data)

# Create the Ranker object and rank the techs
r = ranker.Ranker(data)
ranked = r.rank(scorers.countTrendsTimesPercentIncrease)

# Generate the expo report
expo.expoGenerator(ranked,10)