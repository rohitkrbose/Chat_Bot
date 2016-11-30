import urllib, json

def construct_url (search_str):
	a = 'http://words.bighugelabs.com/api/2/58bb85d31dbc5dff46991743a156aacc/'
	c = '/json'
	word_arr = search_str.split()
	l = len(word_arr)
	b = ""
	for i in range (0,l-1):
		b = b + word_arr[i] + "%20"
	b = b + word_arr[l-1]
	return (a+b+c)


def fetch_syn (word):
	url = construct_url(word)
	response = urllib.urlopen(url)
	syn_list = []
	data = json.loads(response.read())
	for key in data:
		if ('syn' in data[key]):
			for synonym in data[key]['syn'] :
				syn_list.append(synonym)
		else: 
			print('No Syn')
	return syn_list