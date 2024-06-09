import pyttsx3
import speech_recognition
import requests
import bs4
import time
import datetime 

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
    audio = r.listen(source,0,4)
     
  try:
    print("recogniing.....")
    query = r.recognize_google(audio, language="en-in")
    print(f"you said: {query}\n")
  except Exception as e:
    print("Say that again")
    return "None"
  return query

def alarm(query):
  timehere = open("Alarmtext.txt", "a")
  timrhere.write(query)
  timehere.close()
  os.startfile("alarm.py")
  
# --------------------Main Function---------------------------
if __name__ == '__main__':
  while True:
    query = takecommand().lower()
    if "wake up" in query:
      from greatme import greetMe
      greetMe()
      while True:
        query = takecommand().lower()
        if "go to sleep" in query:
          speak("Ok Sir")
          break
        elif "hello" in query:
          speak("Hello, how ar you")
        elif "i am fine" in query:
          speak("That's great")
        elif "open" in query:
          from Dictapp import openappweb
          openappweb(query)
        elif 'close' in query:
          from Dictapp import closeappweb
          closeappweb(query)
        elif "set an alarm" in query:
          print("input time example:- 10 and 10 and 10")
          speack("set the time")
          a = input("please tell the time")
          alarm(a)
          speak("Done")
        elif "temperature" in query:
          from TempWeth import temperature
          temperature(query)
        elif "weather" in query:
          from TempWeth import weather
          weather(query)           
        elif "google" in query:
          from SearchNow import searchGoogle
          searchGoogle(query)
        elif "youtube" in query:
          from SearchNow import searchYoutube
          searchYoutube(query)
        elif "wikipedia" in query:
          from SearchNow import searchWikipedia
          searchWikipedia(query)
        elif "time" in speechtext:
          time = datetime.datetime.now().strftime("%I%M%p")
          speak(f"the time is {time}")
        elif "finally sleep" in query:
          speak("Going sleep")
          exit() 