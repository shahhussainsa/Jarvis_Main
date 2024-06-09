import pyttsx3
import speech_recognition
import datetime



engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def greetMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<=12:
    speak("Good Morning")
  elif hour > 12 and hour <= 18:
    speak("Good Afternoon")
  else:
    speak("Good Evening")
  
  speak("Please tell me hoe can i help you")
