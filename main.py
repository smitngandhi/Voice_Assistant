import pyttsx3 as p
import speech_recognition as sr
from  driver import selenium_web
engine = p.init()

#used to find speed rate of voice the higher the faster

# rate = engine.getProperty('rate')
# engine.setProperty('rate',180)
# print(rate)

# used to change the voice of assistant

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)
# print(voices[0].id)

engine.setProperty('rate',170)

def speak(text):
    engine.say(text)
    engine.runAndWait()


speak("Hello Sir I am your personal assistant, My name is Millie..For now I can only play a video on youtube or search an information on wikipedia...What do you want me to do?")

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




# speak("Hello Sir I am your Personal Assistant, My name is Alex...I can search information on Wikipedia or play a video on youtube...What do you want me to do sir")

r = sr.Recognizer()




def listen():
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,1.2)
            r.energy_threshold = 1000
            print("listening")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = str(text)
            text = text.lower()
            print(text)
            if "video" in text or "youtube" in text :
                 youtube()
            if "information" in text or "wikipedia" in text:
                 wikipedia()


listen()


