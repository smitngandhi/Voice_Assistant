from driver.news import getnewstitle
from driver.news import getnewsdescription
import pyttsx3 as p
import speech_recognition as sr
from  driver import selenium_web
import time
from driver import *
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



def intro():
    #   speak("Hey I am Luna,  your personal AI assistant,  created by Smit . I'm here to add a touch of magic to your everyday life and make each moment a bit easier and more enjoyable. Here's how I can assist you: Playing Videos on YouTube: Whether it's your favorite song, a romantic movie, or a cute cat video, just let me know, and I'll play it for you on YouTube. Searching Information on Wikipedia: If you're curious about anything, I can look it up on Wikipedia and provide you with all the information you need. Searching the Web on Google: Whether you're looking for the latest trends, interesting facts, or answers to any questions, I can quickly search Google and bring you the best results. So,  what would you like me to do for you today?")
        speak("Hey")
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





def listen():
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,1.2)
            r.energy_threshold = 1000
            print("listening...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = str(text)
            text = text.lower()
            print(text)
            if  "hey" in text and "luna" in text:
                  intro()
            elif "video" in text or "youtube" in text :
                 youtube()
            elif "information" in text or "wikipedia" in text:
                 wikipedia()
            elif "search" in text or "google" in text:
                  google()
            elif "news" in text:
                  news()
            


listen()


