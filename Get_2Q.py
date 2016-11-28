import urllib, json
import fetching_P, Get_Q, fetching_Q_val

def construct_url(Q_id):
	a = "https://www.wikidata.org/w/api.php?action=wbgetentities&ids="
	c = "&props=labels%7Cdescriptions%7Cclaims%7Csitelinks/urls&languages=en&format=json"
	return (a+Q_id+c)


Q_id = Get_Q.send_Q_id('Taylor Swift')
P_id = fetching_P.send_P_id('birth name')

url = construct_url(Q_id)
response = urllib.urlopen(url)
data = json.loads(response.read())

A = data['entities'][Q_id]['claims'][P_id]
for i in range (0,len(A)):
	v = A[i]['mainsnak']['datavalue']['value']
	if 'id' in v :
		qid = A[i]['mainsnak']['datavalue']['value']['id']
		corresp_Q_val = fetching_Q_val.send_Q_val(qid)
		print(corresp_Q_val)
	else:
		print v