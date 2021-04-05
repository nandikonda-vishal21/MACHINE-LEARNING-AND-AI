import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def jarvisvoice(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    print("hour",hour)
    if hour>=0 and hour<12:
       jarvisvoice("good morning")
    elif hour>=12 and hour<18:
        jarvisvoice("good afternoon")
    else :
        jarvisvoice("good evening")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("user said:" +query)
    except Exception as e :
        print(e)
        print("sorry...say that again please")
        return "None"
    return query

jarvisvoice("hello")
wish()
jarvisvoice("welcome to voice assistant")

while True:
    query = takecommand().lower()
    if "what is" in query or "who is" in query:
    jarvisvoice("searching in wikipedia...pls wait")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    print(results)
    jarvisvoice("according to wikipedia...")
    jarvisvoice(results)
elif "open google" in query:
    webbrowser.open("google.com")
elif "open gmail" in query:
    webbrowser.open("gmail.com")
elif "open youtube" in query:
    webbrowser.open("youtube.com")
    
        
        
