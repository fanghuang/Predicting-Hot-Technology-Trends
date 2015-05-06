from Importer import importer


from Ranker import ranker
from Ranker import scorers

from Report import htmltmpl
from Report import expo
from Report import email

from Grapher import grapher

from premailer import transform

#Import the data from the stackoverflow_monthly db
dataImporter = importer.Importer()
data = dataImporter.getDataFromDB("stackoverflow_monthly_2000")

# Create the Ranker object and rank the techs
r = ranker.Ranker(data)
ranked = r.rank(scorers.countTrendsTimesPercentIncrease)

# Generate the expo report
(html, images) = email.generateEmail(ranked, 5)
html = transform(html)

# Create a graph for each technology
g = grapher.Grapher()
g.generateSMAImages(data, images)


# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage

# Define these once; use them twice!
strFrom = 'PredictingHotTechTrends@gmail.com'
strTo = 'coreyja@gmail.com, alexancj@rose-hulman.edu'

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Weekly Hot Technology Report'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('Email client doesn\'t support HTML email. Please view this email in an HTML client.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText(html, 'html')
msgAlternative.attach(msgText)

for image in images:
    # This example assumes the image is in the current director
    fp = open('/vagrant/generated_report/imgs/%s.png' % image, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<%s>' % image)
    msgRoot.attach(msgImage)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP_SSL()
smtp.connect('smtp.gmail.com', 465)
smtp.login('PredictingHotTechTrends', 'Tq3ZvHHFSnUqCTRaEHcKY3Ma')
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()


# print html
