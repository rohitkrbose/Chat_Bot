import urllib, json

def fetch_Q_url (Q_id):
	a = "https://www.wikidata.org/w/api.php?action=wbgetentities&props=labels&languages=en&ids="
	c = "&format=json"
	return (a+Q_id+c)

def send_Q_val (Q_id):
	Q_url = fetch_Q_url(Q_id)
	response = urllib.urlopen(Q_url)
	data = json.loads(response.read())
	val = data['entities'][Q_id]['labels']['en']['value']
	return val


