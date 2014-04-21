page = 'the contents of a weppage with some links in it maybe here is ont <a href="http://bullshit.com"</a> and some more here <a href="www.crap.com">asdf</a> and het some more links bullcrap <a href="http://python.org">link</a>'
test = "no link test"


def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote


def print_all_links(page):
	while True:
		url,endpos = get_next_target(page)
		if url: 
			print url
			page = page[endpos:]
		else:
			break

