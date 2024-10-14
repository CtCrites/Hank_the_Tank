#######################################################################
#
#   Author:           Cameron Crites 
#   Creation Date:    Feb 21, 2023 
#   Filename:         ShortWiki 
#
#   Purpose:        
#      This program will return a string containing the first
#      sentence from a desired Wikipedia page.
#
#######################################################################
import math
import wikipedia

def rempar(string):
	try:
		p1 = string.index("(")
	except ValueError:
		fstring = string
		pass
	else:
		string2 = string[p1::]
		try:
			p2 = string2.index(")") + 1
		except ValueError:
			pass
		else:
			string3 = string2[p2::]
			fstring = string[0:p1] + string3
	try:
		b1 = fstring.index("[")
	except ValueError:
		pass
	else:
		fstring2 = fstring[b1::]
		try:
			b2 = fstring2.index("]") + 1
		except ValueError:
			pass
		else:
			fstring3 = fstring2[b2::]
			fstring = fstring[0:b1] + fstring3
			
	return fstring
	
def ShortWiki(query):
	query = str(query)
	wiki = wikipedia.summary(query, sentences=2, auto_suggest=False)
	clear = False
	while clear == False:
		if wiki == rempar(wiki):
			clear = True
		else:
			wiki = rempar(wiki)
	return wiki
	
