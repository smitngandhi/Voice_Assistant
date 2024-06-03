import os
import pyttsx3 as p
import pyautogui
import webbrowser
import speech_recognition as sr
import time


engine = p.init()
r = sr.Recognizer()


voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


engine.setProperty('rate',150)

def speak(text):
    # engine.say("Starting")
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()


apps = {"commandprompt":"cmd" , "word":"winword", "excel":"EXCEL", "paint":"paint" ,"chrome":"chrome","vscode":"code"}


def open_app(query):
    query = query.lower()
    speak("Launching...")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open" , "")
        query = query.replace(" " , "")
        webbrowser.open(f'https://www.{query}')
    

    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f'start {apps[app]}')
def close_app(query):
    speak("Closing...")
    if "one tab" in query:
        print(f'closing one tab')
        pyautogui.hotkey("ctrl","w")
    elif "two tab" in query or "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
    elif "three tab" in query or "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
    elif "four tab" in query or "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
    elif "five tab" in query or "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
        pyautogui.hotkey("ctrl","w")
        time.sleep(2)
    else:
        keys = list(apps.keys())
        for app in keys:
            if app in query:
                os.system(f'taskkill /f /im  {apps[app]}.exe')




