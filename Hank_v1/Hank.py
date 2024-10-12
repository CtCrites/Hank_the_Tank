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

####################### Features of Hank    ########################

def speak(text):	#Computer outputs speech and animation from input
    out = "spd-say -r -20 -p -20 -l 'ru-LV' -y 'whisper' '{}'".format(text)
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
    text = input("What would you like Hank to say?: ")
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
    print("Hello")
    w = os.popen("weather --quiet 19530")
    long = w.read()
    long = long.split()
    temp = long[1]
    sky = long[-1]
    weath = long[-4]
    tempout = "It is currently, " + temp + " degrees"
    skyout = "The sky, is currently " + sky
    weathout = "With " + weath + " weather."
    speak(tempout)
    tipy.sleep(1.5)
    speak(skyout)
    tipy.sleep(1.5)
    speak(weathout)
    return

def wiki():			#Hank speaks the 1st sentence of a wikipedia search
	Hank()
	query = input("What would you like Hank to tell you about?: ")
	wiki1, wiki2 = ShortWiki(query)
	speak(wiki1)
	tipy.sleep(0.25)
	os.system("clear")
	speak(wiki2)
	return
	
wiki()
