from driver.news import getnewstitle
from driver.news import getnewsdescription
import pyttsx3 as p
import speech_recognition as sr
from  driver import selenium_web
import time

from driver import *
import randfacts
import datetime
from  driver.apps import open_app
from  driver.apps import close_app

engine = p.init()
r = sr.Recognizer()
#used to find speed rate of voice the higher the faster

# rate = engine.getProperty('rate')
# engine.setProperty('rate',180)
# print(rate)

# used to change the voice of assistant

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)
# print(voices[0].id)



engine.setProperty('rate',150)

def speak(text):
    # engine.say("Starting")
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()

engine.say("Starting in 3,  2  ,  1 ")
speak("Good Morning User, For activating me Say the magical phrase: Hey Luna")

time = datetime.datetime.now().strftime("%H:%M")
def intro():
        speak("Hello! I'm Luna, your personal AI assistant.")
        assist = selenium_web.Info()
        temperature = assist.get_temperature(f'Temperature in Ahmedabad')
        speak(f'Current Temperature in Ahmedabad is {temperature} and the time is {time}')
        speak('Furthermore, I can help you find information on Wikipedia, search the web on Google, play videos on YouTube, read out the latest news, provide you temperature of any region across the globe. So what can i do for you today?"')
        listen()

def youtube():
        speak("Sir which video do you want to see")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,.5)
            r.energy_threshold = 1000
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            speak(f"Getting {text} on youtube")
            assist = selenium_web.Info()
            assist.open_youtube(text)

def wikipedia():
    speak("Sir could you please give me a specific topic to search about")
    with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.5)
            r.energy_threshold = 1000
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            speak(f"Searching {text} on Wikipedia")
            assist = selenium_web.Info()
            assist.get_info_wikipedia(text)

def chatgpt():
      speak("Sir could you please give me a specific topic to search about")
      with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.5)
            r.energy_threshold = 1000
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            speak(f"Searching {text} on Wikipedia")
            assist = selenium_web.Info()
            assist.get_chatgpt(text)

def google():
      speak("Sir could you please give me a specific topic to search about")
      with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.5)
            r.energy_threshold = 1000
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            speak(f"Searching {text} on Google")
            assist = selenium_web.Info()
            assist.get_google(text)

def news():
      arr_news_title = getnewstitle()
      arr_news_description = getnewsdescription()
      speak("Sir here are the top 5  news of the day")
      for i in range(5):
            speak(arr_news_title[i])
            print("Title: " + arr_news_title[i])
            print("Description: " + arr_news_description[i])

def facts():
      x = randfacts.getFact()
      speak("Did you know that " + x)
      print(x)

def temperature():
      speak("Sir you want to know the temperature of which city")

      with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.5)
            r.energy_threshold = 1000
            print("listening..")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f'Getting temperature of {text}')
            assist = selenium_web.Info()
            temperature = assist.get_temperature(f'temperature in {text}')
            print(temperature)
            speak(f"Temperature of {text} is {temperature}")


def launch_app():
      speak("Sir which app do you wanna open")
      with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,0.5)
            r.energy_threshold = 1000
            print("listening..")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(f'Opening {text}')
            open_app(f'{text}')
            with sr.Microphone() as source:
                  r.adjust_for_ambient_noise(source,1.2)
                  r.energy_threshold = 1000
                  speak("Next")
                  print("listening...")
                  audio = r.listen(source)
                  text = r.recognize_google(audio)
                  text = text.lower()
                  close_app(text)
            listen()



def listen():
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,1.2)
            r.energy_threshold = 1000
            speak("Next")
            print("listening...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()
            print(text)
            if  "hey" in text or "luna"  in text or "heyluna" in text:
                  intro()
            elif "video" in text or "youtube" in text :
                 youtube()
            elif "information" in text or "wikipedia" in text:
                 wikipedia()
            elif "search" in text or "google" in text:
                  google()
            elif "news" in text:
                  news()
            elif "fact" in text or "facts" in text or "fax" in text:
                  facts()
            elif "temperature" in text:
                  temperature()
            elif "go" in text and "to" in text  and "sleep" in text:
                  speak("Goodbye sir. You can call me anytime")
                  exit() 
            elif "open application" in text:
                  launch_app()
            else:
                  speak("Could you please repeat the magical phrase:  hey luna")
                  listen()

listen()
