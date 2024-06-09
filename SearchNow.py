import pyttsx3
import speech_recognition
import pywhatkit
import webbrowser
import wikipedia

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
    

query = takecommand().lowe()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  

def searchGoogle(query):
  if "google" in query:
    import wikipedia as googleScrap
    query = query.replace("jarvis", "")
    query = query.replace("google search")
    query = query.replace("google","")
    speak("This is found on google")
    
    try:
      pywhatkit.search(query)
      result = googleScrap.summary(query,1)
      speak(result)    
    except:
      speak("No output found")
      
def searchYoutube(query):
  if "youtube" in query:
    speak("this is what i found")
    query = query.replace("jarvis", "")
    query = query.replace("youtube search")
    query = query.replace("youtube","")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    pywhatkit.playonyt(query)
    speak("Done, Hussain")


def searchWikipedia(query):
  if "wikipedia" in query:
    speak("this is what i found")
    query = query.replace("jarvis", "")
    query = query.replace("wikipedia search")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 1)
    speak("According to wikipedia")
    print(results)
    speak(results)
    
    
  
    