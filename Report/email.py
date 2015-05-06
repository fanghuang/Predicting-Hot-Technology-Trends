from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

def generateEmail(result, numToDisplay):
    length = len(result)
    toplist = result[:numToDisplay]
    bottomlist = result[::-1][:numToDisplay]
    toplist = [(toplist[x-1],x) for x in range(1,numToDisplay+1)]
    bottomlist = [(bottomlist[x],length-x) for x in range(0,numToDisplay)]

    env = Environment(loader=FileSystemLoader('/vagrant/Report/Template'))
    template = env.get_template('/email.html')
    html = template.render(
		total = length,
		top = toplist,
		bottom = bottomlist
		)

    images = toplist + bottomlist
    images = [x[0][0].replace('.','') for x in images]

    # print html, images

    return html, images
