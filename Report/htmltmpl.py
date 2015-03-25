from jinja2 import Template

def pageGenerator(result, num):

	toplist = result[:num]
	bottomlist = result[::-1][:num]
	print toplist
	print bottomlist
	tmpl = Template(u'''\
	<!DOCTYPE html>
	<html>
		<head>
		<title>{{ variable|escape }}</title>
		</head>
		<body>
			<h1>Top {{ number|escape }}</h1>
			{%- for item in top %}
			<img src="/pic/{{ item[0].replace('.','') }}.png"></img>
			{%- endfor %}

			<h1>Bottom {{ number|escape }}</h1>
			{%- for item in bottom %}
			<img src="/pic/{{ item[0].replace('.','') }}.png"></img>
			{%- endfor %}
		</body>
	</html>
	''')

	html = tmpl.render(
		variable = 'SMA Top & Bottom '+str(num)+' Technology Trends',
		number = num,
		top = toplist,
		bottom = bottomlist
	)
	print html
	file = open("Template/index.html", "w")

	file.write(html)

	file.close()
