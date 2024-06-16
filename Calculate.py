import wolframalpha
import pyttsx3
import speech_recognition


engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
  
def WolfRamAlpha(query):
  apikey = "LJRKWL-EH47W97JTW"
  requester = wolframalpha.Client(apikey)
  requested = requester.query(query)
  
  try:
    answer = next(requested.results).text
    return answer
  except:
    speak("The Value is not answerable")

def calc(query):
  Term = str(query)
  Term = Term.replace("Jarvis", "")
  Term = Term.replace("multiply", "*")
  Term = Term.replace("into", "*")
  Term = Term.replace("divide", "/")
  Term = Term.replace("add", "+")
  Term = Term.replace("plus", "+")
  Term = Term.replace("minus", "-")
  Term = Term.replace("modulos", "%")
  
  final = str(Term)
  
  try:
    result = WolfRamAlpha(final)
    print(f"Result : {result}")
    speak(result) 
  except:
    speak("the value is not answered")
   