import pyttsx3
import time

class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)
        # Prime the engine with a short silent phrase
        print("Priming the engine...")
        self.engine.say(" ")  # A space to prime the engine
        self.engine.runAndWait()
        print("Engine primed.")

    def speak(self, text):
        print(f"Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        print("Finished speaking.")

# Create a single instance of the TTS class
tts = TTS()

# Use the speak method to say different texts
tts.speak("Hello how are you?")
tts.speak("This, is a test of the text-to-speech engine.")
