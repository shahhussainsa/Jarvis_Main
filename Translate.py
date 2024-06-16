from time import sleep
from googletrans import Translator
from playsound import playsound
import time
from gtts import gTTS
import pyttsx3
import speech_recognition
import googletrans
import os


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def takecommand():
  r = speech_recognition.Recognizer()
  with speech_recognition.Microphone() as source:
    print("Listening....")
    r.pause_threshold = 1   # listen of pause
    r.energy_threshold = 300   # voice recognizer  how loud to speak
    audio = r.listen(source,0,5)
     
  try:
    print("recogniing.....")
    query = r.recognize_google(audio, language="en-in")
    print(f"you said: {query}\n")
  except Exception as e:
    print("Say that again")
    return "None"
  return query

def translategl(query):
  speak("Sure, Sir")
  print(googletrans.LANGUAGES)
  translator = Translator()
  speak("What language you want to translate to, Sir")
  b = input("Languages: ")
  text_translator = translator.translate(query, src = "auto", dest = b,)
  text = text_translator.text
  try:
    speakgl = gTTS(text = text, lang=b, slow = False)
    speakgl.save("voice.mp3")
    playsound("voice.mp3")
    time.sleep(5)
    os.remove("voice.mp3")
  except:
    print("Unable to Translate Voice")