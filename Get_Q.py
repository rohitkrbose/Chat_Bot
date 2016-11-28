import pywikibot

def send_Q_id (Q_val):
	site = pywikibot.Site("en", "wikipedia")
	page = pywikibot.Page(site, Q_val)
	item = pywikibot.ItemPage.fromPage(page)
	k = str(item)
	k = k[11:]
	k = k[:-2]
	return k