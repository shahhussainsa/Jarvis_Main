import pyttsx3
import speech_recognition
import requests
from pynput.keyboard import Key, Controller
from time import sleep
import bs4
from bs4 import BeautifulSoup 
import time
import datetime 
import pyautogui
import pynput
import webbrowser
import wikipedia
import os
import random
from plyer import notification
from pygame import mixer
import speedtest


for i in range(3):
  a = input("enter password ")
  pass_file = open("C:/Users/Hussain/Desktop/pythonprgm/jarvis/password.txt", "r")
  password = pass_file.read()
  if (a==password):
    print("WelCome to Jarvis")
    break
  elif (i==2 and a != password):
    exit()
  elif (a!=password):
    print("Try Again")

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

def alarm(query):
  timehere = open("Alarmtext.txt", "a")
  timehere.write(query)
  timehere.close()
  import alarm
  alarm_path = "alarm.py"
    # Verify the file path and existence
  if os.path.isfile(alarm_path):
      try:
          os.startfile(alarm_path)
      except FileNotFoundError:
          print(f"Error: '{alarm_path}' not found. Please check the file path.")
  else:
        print(f"Error: '{alarm_path}' does not exist in the current directory.")

  # os.startfile("alarm.py")
  # try:
  #       os.startfile("alarm.py")
  # except FileNotFoundError:
  #       print("Error: 'alarm.py' not found. Please check the file path.")
  
# --------------------Main Function---------------------------
if __name__ == '__main__':
  while True:
    query = takecommand().lower()
    if "hey jarvis" in query:
      from greetme import greetMe
      print(greetMe())
      while True:
          query = takecommand().lower()
          if "go to sleep" in query:
            speak("Ok Sir")
            break
          elif "hello" in query:
            speak("Hello, how are you")
          elif "i am fine" in query:
            speak("That's great")
          elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
          elif 'close' in query:
            from Dictapp import closeappweb
            closeappweb(query)
          #######password change
          elif "change password" in query:
            speak("What's your new password")
            new_pw = input("Enter new password\n")
            new_password = open("password.txt", "w")
            new_password.write(new_pw)
            new_password.close()
            speak("Your password is changed")
            speak(f"Your new password is {new_pw}") #######password
            
          
          elif "schedule my day" in query:
            tasks = []
            speak("Do you want to clear old task YES or NO")
            quer = takeCommand().lower()
            if "yes" in query:
              file = open("tasks.txt","w")
              file.write(f"")
              file.close()
              no_tasks = int(input("enter the number of tasks :- "))
              i =0
              for i in range(no_tasks):
                tasks.append(input("Enter the task"))
                file = open("taskes.txt","a")
                file.write(f"{i} : {tasks[i]}\n")
                file.close()
            elif "no" in query:
              i =0
              no_tasks = int(input("enter the number of tasks :- "))
              for i in range(no_tasks):
                tasks.append(input("Enter the task"))
                file = open("taskes.txt","a")
                file.write(f"{i} : {tasks[i]}\n")
                file.close()
          elif "show my schedule" in query:
            file = open("tasks.txt","r")
            content = file.read()
            file.close()
            mixer.init()
            mixer.music.load("notification.mp3")
            mixer.music.play()
                             
            notification.notify(
              title = "My Schedule :- ",
              message = content,
              timeout = 15
            )
          elif "open" in query:
            query = query.replace("open","")
            query = query.replace("jarvis", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(0.2)
            pyautogui.press("enter")
          
          elif "internet speed" in query:
            wifi = speedtest.Speedtest()
            upload_net = wifi.upload()/1048576  ## megabyte = 1024 * 1024 bytes
            download_net = wifi.download()/1048576
            print(f"Upload speed : {upload_net}")
            print(f"Download speed : {download_net}")
            speak(f"your upload speed is {upload_net}")
            speak(f"your Download speed is {download_net}")
                
                           
              
            
          elif "set an alarm" in query:
            print("input time example:- 10 and 10 and 10")
            speak("set the time")
            a = input("please tell the time")
            alarm(a)
            speak("Done")
          elif "temperature" in query:
            search = "temperature in tumkur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")  # Corrected parser name
            temp = data.find("div", class_="BNeawe").text
            print(temp)
            speak(f"Current {search} is {temp}")
          elif "weather" in query:
              search = "weather in tumkur"
              url = f"https://www.google.com/search?q={search}"
              r = requests.get(url)
              data = BeautifulSoup(r.text, "html.parser")  # Corrected parser name
              temp = data.find("div", class_="BNeawe").text
              print(temp)
              speak(f"Current {search} is {temp}")
          elif "my github" in query:
            web = "https://github.com/SHAHHUSSAINSA"
            speak("Opening your github account")
            webbrowser.open(web)
          elif "my linkedin" in query:
            web = "https://linkedin.com/in/shahhussain22"
            speak("Opening your Linkedin account")
            webbrowser.open(web)
          elif "volume up" in query:
            from Keyboard1 import volume_up
            speak("turning volume up")
            volume_up()
          elif "volume down" in query:
            from Keyboard1 import volume_down
            speak("turning volume down")
            volume_down()
          elif "remember " in query:
            rememberMessage = query.replace("remember","")
            rememberMessage = query.replace("jarvis", "")
            speak("You told to" + rememberMessage)
            remember = open("Remember.txt", "w")
            remember.write(rememberMessage)
            remember.close()
          elif "what do you remember" in query:
            remember = open("Remember.txt", "r")
            speak("you told me to " + remember.read())
          elif "pause" in query:
            pyautogui.press("k")
            speak("Video Paused")
          elif "play" in query:
            pyautogui.press("k")
            speak("Video Played")
          elif "video forward" in query:
            pyautogui.press("l")
            speak("Video forwarded")
          elif "video back" in query:
            pyautogui.press("j")
            speak("Video backed")
          elif "full screen" in query:
            pyautogui.press("f")
            speak("Turned Full Screen")
          elif "music please" in query:
            speak("playing you favourite songd")
            a = (1,2)
            b = random.choice(a)
            if b==1:
              webbrowser.open("https://www.youtube.com/watch?v=hoNb6HuNmU0")            
            elif b==2:
              webbrowser.open("https://www.youtube.com/watch?v=GjSOKZ4juzs")
          
          elif "calculate" in query:
            from Calculate import wolframalpha
            from Calculate import calc
            query = query.replace("Calculate", "")
            query = query.replace("jarvis", "")
            calc(query)
            
            
          elif "news" in query:
            from dailynews import latestnews
            latestnews()
            
          elif "shutdown system" in query:
            speak("Are you sure to shutdown")
            shutdown = input("Do you wish to shutdown thwe computer")
            if shutdown == "yes":
              os.system("shutdown /s /t 1") 
            elif shutdown == "no":
              break       
              
          
          # elif "music" in query:km
          #   add = "jarvis/"
          #   listsong = os.listdir(add)
          #   os.startfile(os.path.join(add, listsong[0]))
          # elif 
          elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
          elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
          elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
          elif "time" in query:
            current_time = datetime.datetime.now().strftime("%I%M%p")
            speak(f"the time is {current_time}")
          elif "stop" in query:
            speak("Going sleep")
            exit()