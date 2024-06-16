import requests
import json
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def latestnews():
  api_dict = {"Business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=40ee614794564e159c76e3b1ac19049a",
            "Entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=40ee614794564e159c76e3b1ac19049a",
            "Health" :  "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=40ee614794564e159c76e3b1ac19049a",
            "Sports" : "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=40ee614794564e159c76e3b1ac19049a",
            "Techonology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=40ee614794564e159c76e3b1ac19049a",
            "Science" : "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=40ee614794564e159c76e3b1ac19049a",
  }
    
  content = None
  url = None
  speak(" which field news do you want, Sir, [Business], [Health], [Sports], [Techonology], [Science], [Entertainment] ")
  field = input("Sir, Type the field you want to here: ")
  for key, value in api_dict.items():
    if key.lower() in field.lower():
      url = value
      print(url)
      print("URl found")
      break
    else:
      # url = True
      # if url in True:
        print("url not found")
  news = requests.get(url).text
  news = json.loads(news)
  speak("Here is the first news")
  arts = news["articles"]
  for articles in arts:
    article = articles["title"]
    print(article)
    speak(article)
    news_url = articles["url"]
    print(f"For more info visit: {news_url}")
    
    a = input("[press 1 for continue] or [press 2 for exit]  \n")
    if str(a) == "1":
      pass
    elif str(a) == "2":
      break
    else:
      print("Choose Between 1 and 2")
      speak("Choose Between 1 and 2")
      speak("That's all, Thank you")
latestnews() 