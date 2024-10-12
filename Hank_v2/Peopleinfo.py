import nltk
import nltk.corpus
from nltk.corpus import wordnet

def lineindex(name):					#Locate the line that starts given person
	with open("people.txt", "r") as file:
		i = 0
		for line in file:
			i = i + 1
			if line[0] != "-":
				pass
			elif line[0] == "-":
				line = line[1:-1]
				if line == name or line == name.lower():
					index = i
				else:
					pass
	file.close()	
	return index

def infoget(index):					#Obtain personal info from file
	endline = index + 9
	info = ""
	with open("people.txt", "r") as file:
		i = 0 
		for line in file:
			i = i + 1
			if i < index:
				pass
			elif i >= index and i <= endline:
				info = info + line
	file.close()
	return info
				
def informat(info):				#Format categories and info into lists
	toks = info.split()
	about = []
	category = ['Name:']
	for item in toks:
		if ":" in item:
			category.append(item)
		else:
			about.append(item)
	return category, about

def synonyms(word):					#Find synonyms for input
	synonyms = []

	for syn in wordnet.synsets(word):
   	 for i in syn.lemmas():
   	     synonyms.append(i.name())
	return synonyms

def thesaur(cat, category):		#Compare synonyms to categories
	for item in category:
		syn = synonyms(item[0:-1])
		if cat in item:
			cat = item[0:-1]
			pass
		elif cat not in item:
			if cat in syn:
				cat = item[0:-1]
			elif cat.lower() not in syn:
				pass
	return cat
	
def inout(name, cat, category, about):	#Output info
	for item in category:
		if cat in item:
			print("{}, your {} is {}". format(name, cat, about[category.index(item)]))
		else:
			pass
	return

def infoassign(category, about):			#Assigns new info to list
	cat = input("What would you like Hank to know about you? Your, ")
	inn = input("What is your {}? ".format(cat))
	category.append(cat)
	about.append(inn)
	return category, about

def READINFO(name):						#Gathers info based on name and category			
	num = lineindex(name)			#Outputs read info
	info = infoget(num)
	category, about = informat(info)
	cat = input("What would you like Hank to tell you? Your, ")
	cat = thesaur(cat, category)
	inout(name, cat, category, about)
	return

def writnav(category, about, index):	#Writes info to file
	file = open("people.txt", "a+")
	i = 1
	category = category[1::]
	for item in category:
		file.write(item)
		file.write(": ")
		file.write(about[i])
		file.write("\n")
		i = i + 1
	file.flush()
	file.close()
	return

def WRITEINFO():						#Prompts for which person info's for
	name = input("Name: ")			#Writes new info to file
	num = lineindex(name)
	info = infoget(num)
	category, about = informat(info)
	category, about = infoassign(category, about)
	writnav(category, about, num)
	return

def filegather(name):
	namecomp = [name, name.lower()]
	with open("people.txt", "r") as file:
		lines = file.readlines()
		d = 0
		for item in lines:
			if "-" in item and item[1:-1] in namecomp:
				index1 = lines.index(item)
				d = d + 1
			elif "-" in item and item[1:-1] not in namecomp:
				if d == 1:
					index2 = lines.index(item)
					d = d + 1
				else:
					pass
			else:
				pass
		file.close()
	with open("people.txt", "r") as file:
		lines2 = file.readlines()
		info = []
		rest = []
		for item in lines2:
			if lines2.index(item) >= index1 and lines2.index(item) < index2:
				info.append(item)
			else:
				rest.append(item)
	return info, rest

def infoedit(info):
	cat = input("What would you like Hank to know? Your, ")
	about = input("{}, what is your {}? ".format(name, cat))
	line = "{}: {}\n".format(cat, about)
	info.append(line)
	print(info)
	return info

def writnew(info, rest):
	with open("people.txt", "w") as file:
		for item in info:
			file.write(item)
		for item in rest:
			file.write(item)
		file.close()
	return




