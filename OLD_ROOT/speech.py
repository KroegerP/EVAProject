import pyttsx3
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #fetching different voices from the system
engine.setProperty('voice', voices[1].id) #setting voice properties
engine.setProperty('rate', 190) #sets speed of speech

def speak(text):
    time.sleep(.5)
    engine.say(text)
    engine.runAndWait()



