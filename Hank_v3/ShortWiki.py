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

def ShortWiki(query):
	import wikipedia
	import math
	
	query = str(query)
	
	wiki = wikipedia.summary(query, auto_suggest=False)
	s1 = wiki.index(".")
	
	wiki = wiki[0:s1]

	return wiki

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
	
	
def l2s(list):
	string = ""
	for i in list:
		string = string + " " + str(i)
	return string	
	
def format(string):
	words = string.split()
	half = math.ceil(len(words)/2)
	word1 = words[0:half]
	word2 = words[half::]
	wiki1 = l2s(word1)
	wiki2 = l2s(word2)
	return wiki1, wiki2
	

	
	
def main(query):
	wiki = ShortWiki(query)
	wiki = rempar(wiki)
	if wiki == rempar(wiki):
		pass
	else:
		wiki = rempar(wiki)
	wiki1, wiki2 = format(wiki)
	return wiki1, wiki2
	

