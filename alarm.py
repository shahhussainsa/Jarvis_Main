from playsound import playsound
import os
import datetime
import bs4
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
extractedtime = open("Alarmtext.txt","rt")
time = extractedtime.read()
Time = str(time)
extractedtime.close()

deletetime = open("Alarmtext.txt", "r+")
deletetime.truncate(0) #delete time
deletetime.close()

def ring(time):
  timeset = str(time)
  timenow = timeset.replace("jarvis", "")
  timenow = timeset.replace("Set an alarm", "")
  timenow = timeset.replace(" and ", ":")
  Alarmtime = str(timenow)
  print(Alarmtime)
  while True:
    currenttime = datetime.datetime.now().strftime("%H:%M:%S")
    if currenttime == Alarmtime:
      speak("Alarm Ringing")
      # playsound("captain.mp3")
      os.system("jarvis\captain.mp3")
    elif currenttime + "00:00:30" == Alarmtime:
      exit()
ring(time)      