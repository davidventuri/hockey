import pandas as pd
import re

pron2013 = pd.read_csv('2013 pronman.csv')

for line, value in pron2013.iterrows():
	print str(line)
	name = re.search(r'\d\.\s\w+\s\w+', str(value))
	print name.group()