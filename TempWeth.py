import pyttsx3
from bs4 import BeautifulSoup 
import os
import bs4
import requests

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
  
def temperature(query):
  search = "temerature in tumkur"
  url = f"https://www.google.com/search?q={search}"
  r = requests.get(url)
  data.BeautifulSoup(r.text, "html.parse")
  temp = data.find("div", class_ = "BNeawe").text
  speak(f"Currect {search} is {temp}")
  
def weather(query):
  search = "weather in tumkur"
  url = f"https://www.google.com/search?q={search}"
  r = requests.get(url)
  data.BeautifulSoup(r.text, "html.parse")
  temp = data.find("div", class_ = "BNeawe").text
  speak(f"Currect {search} is {temp}")