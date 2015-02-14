import requests

def listTechnologies(return_quota = False):

	base_url = 'https://api.stackexchange.com'
	tag_url = base_url + "/2.2/tags"

	techs = []
	quota = -1

	for i in [x+1 for x in range(5)]:
		payload = {
			'order': 'desc', #Return the quantity of matching items, not the actual items
			'sort': 'popular',
			'site': 'stackoverflow',
			'page': i,
			'pagesize': 100,
			'key':'XGgeLjmonD8zytJD18S3ug(('
		}

		r = requests.get(tag_url, params=payload)
		r = r.json()
		
		techs += [str(x['name']) for x in r['items']]
		quota = r['quota_remaining']
	

	if return_quota:
		return techs, quota

	return techs