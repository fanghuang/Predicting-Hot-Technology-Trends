import requests

def listTechnologies():

	base_url = 'https://api.stackexchange.com'
	tag_url = base_url + "/2.2/tags"

	techs = []

	for i in [x+1 for x in range(10)]:
		payload = {
			'order': 'desc', #Return the quantity of matching items, not the actual items
			'sort': 'popular',
			'site': 'stackoverflow',
			'page': i,
			'pagesize': 100
		}

		r = requests.get(tag_url, params=payload)
		techs += [str(x['name']) for x in r.json()['items']]
	

	return techs

