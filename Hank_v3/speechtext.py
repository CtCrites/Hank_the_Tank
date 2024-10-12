import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np


def speechtotext():
	fs = 44100  # Sample rate
	seconds = 3.5  # Duration of recording
	
	myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2, dtype=np.int16)
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
		 print("I didn't understand what you said.")
	except sr.RequestError as e:
		 print("Error: {0}".format(e))
	return transcript
