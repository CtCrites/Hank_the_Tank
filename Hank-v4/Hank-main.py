#############################################################################
# Program Title: Hank-main
# Creation Date: 1/9/2023
# Description: This program will serve as the main for the Hank assistant
#
##### Installed Packages
import os
from gtts import gTTS
import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

##### Self Created
import Memory as mem
import ShortWiki as SW
import InfoGet as IG
##### Functions

def writelog(speaker, message):
	timestamp = IG.timestamp()
	logline = str(timestamp) + "  " + str(speaker) + ": '" + str(message) + "'\n"
	with open("logs.txt", "a") as file:
		file.write(logline)
		file.close()
	return

def speak(text):
	writelog("Hank", text)
	tts = gTTS(text=text, lang='en')
	filename = "Hank_to_user.wav"
	tts.save(filename)
	os.system("mpg123 -q " + filename)
	return
	
def speechtotext(seconds):				#Listens through microphone and gives string
	fs = 44100  # Sample rate

	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)	#Records speech using given parameters
	sd.wait()  # Wait until recording is finished
	write('user_to_Hank.wav', fs, myrecording.astype(np.int16))  # Save as WAV file 


	# Create a recognizer
	recognizer = sr.Recognizer()

	# Load the wav file
	with sr.AudioFile("user_to_Hank.wav") as source:
		 audio = recognizer.record(source)

	# Recognize the speech
	try:
		 # Decode the audio into a string
		 transcript = recognizer.recognize_google(audio)
		 #print(transcript)
	except sr.UnknownValueError:
		 transcript = "I didn't understand what you said."
	except sr.RequestError as e:
		 print("Error: {0}".format(e))
	return transcript
	
def standby():
	recognize = 0
	while recognize == 0:
		print("Listening...")
		check = speechtotext(3)
		if "hank" in check.lower():
			writelog("User", check)
			recognize = 1
		else:
			pass
	return

def hank_response(user_input):
	if "my" in user_input.lower():
		speak("Who are you?")
		user_name = speechtotext(3)
		writelog(user_name, user_name)
		user_info, others_info = mem.recall(user_name)
		if user_name.lower() in user_info[0].lower():
			query_index = user_input.index("my") + 3
			query = user_input[query_index::]
			topics, items = mem.deformat(user_name)
			none = 0
			for thing in topics:
				if query.lower() in thing.lower():
					none = none + 1
					query_item = items[topics.index(thing)]
					break
			if none == 0:
				speak("I do not know that, {}".format(user_name))
				speak("What is your {}?".format(query))
				new_query_item = speechtotext(4)
				writelog(user_name, new_query_item)
				mem.remember(user_name, query, new_query_item)
				speak("Okay, I will remember that for next time")
			else:
				speak("{}, your {} is {}".format(user_name, query, query_item))
		else:
			speak("I do not know you")
			speak("Should I remember you?")
			user_input = speechtotext(3)
			writelog(user_name, user_input)
			if "yes" in user_input.lower():
				mem.meetnew(user_name)
				speak("Okay, {}, I got it".format(user_name))
				pass
			else:
				pass
				
	elif "tell me about" in user_input.lower():
		query_index = user_input.index("about") + 6
		query = user_input[query_index::]
		wiki = SW.ShortWiki(query)
		speak(wiki)
	
	elif "when" in user_input.lower():
		if "prayer times" in user_input:
			speak("Where are you located?")
			place = speechtotext(3)
			prayers = IG.prayer_times(place)
			for time in prayers:
				speak(time)
		else:
			speak("Where are you located?")
			place = speechtotext(3)
			prayers = IG.prayer_times(place)
			for time in prayers:
				this = time.split()
				if this[0].lower() in user_input.lower():
					speak(time)
			
	elif "what" in user_input.lower() and "time" in user_input.lower():
		time = IG.currenttime()
		speak("It is currently, {}".format(time))
		
	elif "today" in user_input.lower() and "date" in user_input.lower():
		date = IG.currentdate()
		speak("Today is {}".format(date))
		
	elif "what" in user_input.lower() and "weather" in user_input.lower():
		speak("Where would you like to know the weather?")
		query = speechtotext(4)
		writelog("User", query)
		weather = IG.weather(query)
		speak(weather)
	return
			
def Main():
	standby()
	speak("What's up?")
	user_input = speechtotext(5)
	writelog("User", user_input)
	hank_response(user_input)
	Main()
	return

#####
Main()

#Last Updated: 1/23/2024


