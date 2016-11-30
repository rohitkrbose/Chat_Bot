import json, urllib, dictionary

#function to construct url
def construct_url (before, between, after):
	word_arr = between.split()
	l = len(word_arr)
	b = ""
	for i in range (0,l-1):
		b = b + word_arr[i] + "%20"
	b = b + word_arr[l-1]
	return (before+between+after)

#function to return json data
def fetch_JSON_data (url):
	response = urllib.urlopen(url)
	data = json.load(response)
	return data

#function to return P value from P ID
def get_P_val (P_id):
	url = construct_url("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=",P_id,"&props=labels&format=json")
	data = fetch_JSON_data(url)
	return data['entities'][P_id]['labels']['en']['value']

#function to return Q value from Q ID
def get_Q_val (Q_id):
	url = construct_url("https://www.wikidata.org/w/api.php?action=wbgetentities&props=labels&languages=en&ids=", Q_id, "&format=json")
	data = fetch_JSON_data (url)
	val = data['entities'][Q_id]['labels']['en']['value']
	return val

#function that returns a 2-column list of available P_values and corresponding P_ids for a given Q_id
def available_p (Q_id):
	url = construct_url ("https://www.wikidata.org/w/api.php?action=wbgetclaims&entity=",Q_id,"&format=json")
	data = fetch_JSON_data (url)
	#print data
	P_arr = []
	for key in data['claims']:
		P_arr.append(key)
	return P_arr

#search label, return index, else -1
def search_label (arr, str):
	str = str.lower()
	l = len(arr)
	for i in range (0,l):
		if (arr[i]['label'].lower() == str):
			return i
	return (-1)

#search in wikidata and return number of closest results (P ID)
def no_of_P_id (P_val):
	#processing JSON doc
	url = construct_url("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=",P_val,"&language=en&type=property&format=json")
	data = fetch_data(P_val)
	return(len(data['search']))

#function to return P_id (if existent in the P_ids under given Q)
def does_P_val_Exist (P_val, lab_P):
	l = len(lab_P)
	for i in range (0,l):
		if (P_val.lower() == lab_P[i][0].lower()):
			return lab_P[i][1]
	return ('P$#')

#get Q value corresponding to P_id
def get_2Q (Q_id, P_id):
	url = construct_url ("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=",Q_id,"&props=labels%7Cdescriptions%7Cclaims%7Csitelinks/urls&languages=en&format=json")	
	data = fetch_JSON_data(url)
	A = data['entities'][Q_id]['claims'][P_id]
	for i in range (0,len(A)):
		v = A[i]['mainsnak']['datavalue']['value']
		if 'id' in v :
			qid = A[i]['mainsnak']['datavalue']['value']['id']
			corresp_Q_val = fetching_Q_val.send_Q_val(qid)
			return(corresp_Q_val)
		else:
			return v

#return common elements of two lists
def get_match_list (lab_P, syn_list):
	match_list = []
	for i in range (0, len(syn_list)):
		for j in range (0, len(lab_P)):
			if (lab_P[j][0] == syn_list[i]):
				match_list.append([syn_list[i],lab_P[j][1]])
	return match_list

#consult the dictionary for synonyms
def consult_thesaurus (P_val, lab_P):
	syn_list = dictionary.fetch_syn (P_val)
	match_P_list = get_match_list(lab_P, syn_list)
	if (len(match_P_list) == 0):
		print ('I failed!')
	else:
		didyoumean(match_P_list)

#wikidata search
def wiki_search (P_val, lab_P, Q_id):
	url = construct_url("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=",P_val,"&language=en&type=property&format=json")
	data = fetch_JSON_data(url)
	len_search = len(data['search'])
	data_label = []
	for i in range (0, len_search):
		data_label.append(data['search'][i]['label'])
	match_P_list = get_match_list (lab_P, data_label)
	if (len(match_P_list) != 0):
		didyoumean(match_P_list)
	else:
		P_id = consult_thesaurus(P_val, lab_P)
		print get_2Q (Q_id, P_id)

def didyoumean (match_P_list):
	print(match_P_list[:,0])
	while (1):
		str = raw_input('Enter option:\n')
		k = search (match_P_list[:,0], str)
		if (k != -1):
			break
		print ('Invalid choice')
	return (match_P_list[k][1])

def get_correspQ_id (Q_id, P_val):
	lab_P = available_p (Q_id)
	P_id = does_P_val_Exist (P_val, lab_P)
	if (P_id != 'P$#'):
		print get_2Q (Q_id, P_id)
	else:
		wiki_search (P_val,lab_P, Q_id)

get_correspQ_id('Q26876', 'father')

