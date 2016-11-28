import urllib, json

def fetch_P_url(prop_str):
	a = "https://www.wikidata.org/w/api.php?action=wbsearchentities&search="
	c = "&language=en&type=property&format=json"
	word_arr = prop_str.split()
	l = len(word_arr)
	b = ""
	for i in range (0,l-1):
		b = b + word_arr[i] + "%20"
	b = b + word_arr[l-1]
	return (a+b+c)

def send_P_id (P_val):
	P_url = fetch_P_url(P_val)
	response = urllib.urlopen(P_url)
	data = json.loads(response.read())
	#print data
	return (data['search'][0]['id'])