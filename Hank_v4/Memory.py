#############################################################################
# Program Title: Memory
# Creation Date: 1/8/24
# Description: This program will interact with Hank's memory bank
#
##### Definitions
#name: Refers to the name of the user currently speaaking with Hank
#Topic: Refers to category of information Hank is remembering
#Item: Refers to the specifics of the category
#Example: Name= Fred, Topic= Major, Item= Business
##### Functions
def meetnew(name):			#Creates new person section in Hank's memory bank
	with open("memory-bank.txt", "r") as file:
		total_memory = file.readlines()
		file.close()
		
	with open("memory-bank.txt", "w") as file:
		total_memory.append("-{}\n".format(name))
		for line in total_memory:
			file.write(line)
		file.close()
	return

def recall(name):				#Recalls information related to a given name
	with open("memory-bank.txt", "r") as file:
		total_memory = file.readlines()
		file.close()
	save = 0
	user_memory = []
	other_users = []
	for line in total_memory:
		if "-" in line and name.lower() in line.lower():
			save = 1
		elif "-" in line and name.lower() not in line.lower():
			save = 0
		else:
			pass
		if save == 1:
			user_memory.append(line)
		elif save == 0:
			other_users.append(line)
	return user_memory, other_users
	
def deformat(user_name):	#Formats user information into 2 lists
	user_memory, other_users = recall(user_name)
	topics = []
	items = []
	for chunk in user_memory[1::]:
		lischunk = chunk.split(": ")
		topics.append(lischunk[0])
		items.append(lischunk[1])
	return topics, items
	
def remember(name, topic, item):	#Commits new information to memory
	user_memory, other_users = recall(name)
	user_memory.append("{}: {}\n".format(topic, item))
	with open("memory-bank.txt", "w") as file:
		for line in other_users:
			file.write(line)
		for line in user_memory:
			file.write(line)
		file.close()
	return
	
def forget(name, topic):			#Removes existing information from Hank's memory
	user_memory, other_users = recall(name)
	user_memory_new = []
	for item in user_memory:
		if topic.lower() not in item.lower():
			user_memory_new.append(item)
	with open("memory-bank.txt", "w") as file:
		for line in other_users:
			file.write(line)
		for line in user_memory_new:
			file.write(line)
		file.close()
	return

#Last Updated: 1/9/23
