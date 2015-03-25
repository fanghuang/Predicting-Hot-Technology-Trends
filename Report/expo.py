from jinja2 import Environment, FileSystemLoader
from jinja2 import Template

def expoGenerator(result, num):

	length = len(result)
	toplist = result[:num]
	bottomlist = result[::-1][:num]
	toplist = [(toplist[x-1],x) for x in range(1,num+1)]
	bottomlist = [(bottomlist[x],length-x) for x in range(0,num)]

	env = Environment(loader=FileSystemLoader('Template'))
	template = env.get_template('/expotmpl.html')
	html = template.render(
		variable = 'SMA Top & Bottom '+str(num)+' Technology Trends',
		total = length,
		top = toplist,
		bottom = bottomlist
		)

	print html

	file = open("Template/expo.html", "w")

	file.write(html)

	file.close()