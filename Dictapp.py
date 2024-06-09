import os
import pyautogui
import webbrowser
import pyttsx3
import time

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
dictapp = {"commamdprompt": "cmd", "paint": "paint", "word":"word","vscode":"vscode","excel":"excel","chrome":"chrome"}

def openappweb(query):
    speak("Launching.") 
    if ".com" in query or ".co.in" in query or ".org" in query:
      query = query.replace("jarvis", "")
      query = query.replace("open","")
      query = query.replace("launch","")
      query = query.replace(" ","")
      webbrowser.open(f"https://www.{query}")
    else:
      keys = list(dictapp.keys())
      for app in keys:
        if app in query:
          os.system(f"start {dictapp[app]}")
          
def closeappweb(query):
  speak("Closing")
  if "one tab" in query or "1 tab" in query:
    pyautogui.hotkey("ctrl", "w")
  elif "2 tab" in query:
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    speak("All tabs closed")
  elif "3 tab" in query:
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    speak("All tabs closed")
  elif "4 tab" in query:
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    speak("All tabs closed")
  elif "5 tab" in query:
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    sleep(0.5)
    pyautogui.hotkey("ctrl","w")
    speak("All tabs closed")
  
  else:
    keys = list(dictapp.keys())
    for app in keys:
      if app in query:
        os.system(f"taskkill /f /im {dictapp[app]}.exe")