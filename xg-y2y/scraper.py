# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

years = ["0708", "0809", "0910", "1011", "1112", "1213", "1314", "1415", "1516"]

for year in years:
	url = "html/" + year + ".html"
	html = urllib.urlopen(url).read()

	soup = BeautifulSoup(html)

	# Retrieve all of the anchor tags
	tables = soup('table')
	text_file = open(year + ".txt", "w")
	text_file.write(str(tables[2]))
	text_file.close()
