import datetime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from datetime import date
import webbrowser



listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)
voicerate=150
engine.setProperty('rate',voicerate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            talk('listening')
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower()
            if "alexa" in command:
                command=command.replace("alexa","")
            #print(command)
            #talk(command)
            return command
    except:
        pass


def run_alex():
    command =take_command()
    try:
        if "play" in command:
            song=command.replace("play","")
            talk("playing")
            print(song)
            talk(song)
            pywhatkit.playonyt(song)
        elif 'who is' in command:
            infom=command.replace('who is','')
            talk("searching for "+infom)
            res=wikipedia.summary(infom)
            print(res)
            talk(res)
        elif 'date' in command:
            d=date.today()
            talk("to day's date is ")
            talk(d)
            print(d)
        elif 'time' in command:
            e=datetime.datetime.now()
            t="%s:%s:%s" % (e.hour, e.minute, e.second)
            talk("the time is ")
            talk(t)
            print(t)
        elif"dateandtime" in command:
            td=datetime.datetime.now()
            talk("the time and date is ")
            talk(td)
            print(td)

        elif"quit" in command:
            talk("thank you sir")
            quit()


        elif "go away" in command:
            talk("thank you sir")
            quit()
        elif "browse" in command:
            talk('opening browser')
            search_term=command.replace("browse", "")
            new = "https://www.google.com.tr/search?q={}".format(search_term)
            webbrowser.open(new)
        elif "define" in command:
            talk("searching")
            command=command.replace("define","")
            search_term = "define:"+command+""
            new = "https://www.google.com.tr/search?q={}".format(search_term)
            webbrowser.open(new)
        elif "where do i find" in command:
            talk("searching")
            command=command.replace("define","")
            search_term = "inurl:"+command+""
            new = "https://www.google.com.tr/search?q={}".format(search_term)
            webbrowser.open(new)


    except:
        pass

while True:
    run_alex()


