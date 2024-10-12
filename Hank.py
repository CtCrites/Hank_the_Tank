#####################################################################
#								    
#	Author: Cameron Crites					    
#	Program Name: Hank.py				    	                    
#	Purpose: To create a virtual assistant			    
#  Created On: 1/19/23				            
#####################################################################

############################# Modules ###############################

import os
import math
import time as tipy
import random
from RockPaperScissor import RPSgame 
from ShortWiki import main as ShortWiki
import Peopleinfo as PI
import lang as CL
import speechtext as SP
######################## Base Functions #############################

def Hank():		#Prints Hank with name banner
    os.system("clear")
    os.system("echo '        N  K  THE  T  A       '")
    os.system("echo '     A     _________     N    '")
    os.system("echo '    H     /         \     K   '")
    os.system("echo '         /  -------  \        '")
    os.system("echo '        |  ~~~   ~~~  |       '")
    os.system("echo '        ^  (.)   (.)  ^       '")
    os.system("echo '       <,     | |     ,>      '")
    os.system("echo '        v\    <_>    /v       '")
    os.system("echo '          |         |         '")
    os.system("echo '          \  <===>  /         '")
    os.system("echo '           \_______/          '")
    os.system("echo '             |>.<|            '")
    os.system("echo '         AKA: MR. DANK        '")
    os.system("echo '                              '")
    return

def open():		#Prints Hank with an open mouth
    os.system("clear")
    os.system("echo '                               '")
    os.system("echo '            _________          '")
    os.system("echo '           /         \         '")
    os.system("echo '          /  -------  \        '")
    os.system("echo '         |  ~~~   ~~~  |       '")
    os.system("echo '         ^  (.)   (.)  ^       '")
    os.system("echo '        <,     | |     ,>      '")
    os.system("echo '         v\    <_>    /v       '")
    os.system("echo '           |   ___   |         '")
    os.system("echo '           \  {___}  /         '")
    os.system("echo '            \_______/          '")
    os.system("echo '              |>.<|            '")
    return

def close():		#Prints Hank with a closed mouth
    os.system("clear")
    os.system("echo '                              '")
    os.system("echo '           _________          '")
    os.system("echo '          /         \         '")
    os.system("echo '         /  -------  \        '")
    os.system("echo '        |  ~~~   ~~~  |       '")
    os.system("echo '        ^  (.)   (.)  ^       '")
    os.system("echo '       <,     | |     ,>      '")
    os.system("echo '        v\    <_>    /v       '")
    os.system("echo '          |         |         '")
    os.system("echo '          \  <===>  /         '")
    os.system("echo '           \_______/          '")
    os.system("echo '             |>.<|            '")
    return

    
def talk(str):		#Animates Hank for a given string
    l = len(str)
    syl = l / 3.5
    syl = int(math.ceil(syl))
    for i in range(syl):
        close()
        tipy.sleep(0.07)
        open()
        tipy.sleep(0.07)
        close()
        tipy.sleep(0.07)
        print(str)
    return
 
def spin():
	user_input = SP.speechtotext()
	return user_input

####################### Features of Hank    ########################

def speak(text):	#Computer outputs speech and animation from input
    out = "spd-say -r -20 -p -20 -l 'en' -y 'belinda' '{}'".format(text)
    os.system(out)
    talk(text)
    return
   
def timefind():		#Gather's time, and formats it for speech
    time = os.popen("date '+%T'")
    time = time.read()
    hour = time[0:2]
    minute = time[3:5]
    if int(hour) > 12:
        hour = int(hour) - 12
    if minute == "00":
        ftime = str(hour) + " O'Clock"
    elif int(minute) < 10:
        minute = int(minute)
        ftime = str(hour) + " oh " + str(minute)
    else:
        ftime = str(hour) + " " + str(minute)
    ftime = "Its " + ftime    
    return ftime

def typensay():		#Displays Hank and prompts him to speak the input
    Hank()
    speak("What would you like me to say")
    text = spin()
    speak(text)
    return
 
def joke():		#Hank tells a random joke
    pick = random.randint(1, 5)
    if pick == 1: #Knock knock ... hatch ... Bless you
        s = "Knock Knock"
        m = "Hatch"
        p = "Bless you, ha ha ha"
        speak(s)
        tipy.sleep(2)
        speak(m)
        tipy.sleep(2)
        speak(p)
    elif pick == 2: #Time flies like an arrow ... Fruit flies like a banana
        s = "Time flies like an arrow"
        m = "Fruit flies like a banana"
        p = "ha ha ha"
        speak(s)
        tipy.sleep(1)
        speak(m)
        speak(p)
    elif pick == 3: #What did one computer say to the other ... Shhh, they're on to us
        s = "What, did one computer say to the other?"
        m = "Sh, theyre on to us"
        speak(s)
        tipy.sleep(2)
        speak(m)
    elif pick == 4: #What do you call a magician without magic ... Ian
        s = "What do you call, a magician without magic?"
        m = "Ian"
        speak(s)
        tipy.sleep(2)
        speak(m)
    elif pick == 5: #I invented a new word ... Plagarism
        s = "I just, invented a new word"
        m = "plagarism"
        speak(s)
        tipy.sleep(2)
        speak(m)
    return
	
def weather():		#Hank reads the weather and sky
    w = os.popen("weather --quiet 19530")
    long = w.read()
    long = long.split()
    temp = long[1]
    sky = long[-1]
    tempout = "It is currently, " + temp + " degrees"
    skyout = "The sky, is currently " + sky
    speak(tempout)
    tipy.sleep(1.5)
    speak(skyout)
    return

def wiki():			#Hank speaks the 1st sentence of a wikipedia search
	Hank()
	speak("What can I tell you about?")
	query = spin()
	wiki1, wiki2 = ShortWiki(query)
	speak(wiki1)
	tipy.sleep(0.25)
	print("")
	speak(wiki2)
	return
	
def infout(user_name):
	info, rest = PI.filegather(user_name)
	speak("What type of thing should I know?")
	cat = spin()
	speak("{}, what is your {}?".format(user_name, cat))
	about = spin()
	line = "{}: {}\n".format(cat, about)
	info.append(line)
	PI.writnew(info, rest)
	return
	
def readinf(user_name):
	num = PI.lineindex(user_name)			#Outputs read info
	info = PI.infoget(num)
	category, about = PI.informat(info)
	speak("What can I tell you about yourself?")
	cat = spin()
	cat = PI.thesaur(cat, category)
	speak(PI.inout(user_name, cat, category, about))
	return


def Menu(user_name):
	speak("What can I do for you?")
	print("What would you like Hank to do for you?")
	print("1. Personal Info			2. Rock Paper Scissors")
	print("3. Tell the Time 		4. Tell the Weather")
	print("5. Tell a Joke			6. Make you Smarter")
	print("7. Have a conversation")
	choice = spin()
	s = "on"
	match choice:
		case "1":
			while s == "on":
				speak("Can I recall or remember something for you?")
				print("1. Recall\n 2. Remember\n 3. Meet new person\n")
				ch = spin()
				if ch == "1":
					readinf(user_name)
				elif ch == "2":
					infout(user_name)
				elif ch == "3":
					speak("Who should I add to my memory?")
					name = spin()
					PI.addpers(name)
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "2":
			while s == "on":
				RPSgame()
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "3":
			while s == "on":
				timefind()
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "4":
			while s == "on":
				weather()
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "5":
			while s == "on":
				joke()
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "6":
			while s == "on":
				wiki()
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
		case "7":
			while s == "on":
				Hank()
				CL.Convoloop(user_name)
				speak("Would you like to repeat this function? [y/n]")
				chs = input()
				if chs == "y" or chs == "Y":
					s = "on"
				elif chs == "n" or chs == "N":
					s = "off"
				else:
					pass
	return
	return

loop = "on"
Hank()
input()
speak("With whom am I speaking?")
user_name = spin()
while loop == "on":
	Menu(user_name)
	again = input("Would you like to return to the menu? [y/n]: ")
	if again == "y" or again == "Y":
		loop = "on"
	elif again == "n" or again == "N":
		loop = "off"
	else:
		print("Invalid entry.")
		again = input("Would you like to return to the menu? [y/n]: ")
		if again == "y" or again == "Y":
			loop = "on"
		elif again == "n" or again == "N":
			print("GOODBYE")
			loop = "off"
		else:
			print("Invalid entry.\n", "Goodbye")
			pass

		
	
	
	
	
	
