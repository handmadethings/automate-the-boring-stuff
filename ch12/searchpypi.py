#! python3
# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4
print('Searching...') # Display text while downloading the search results page
res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# TODO: Open a  browser tab for each result.
link_elems = soup.select('.package-snippet')
num_open = min(5, len(linkElems))
for i in range(num_open):
    url_to_open = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)