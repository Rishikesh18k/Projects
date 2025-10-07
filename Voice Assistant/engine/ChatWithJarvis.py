import pyttsx3    # pip install pyttsx3
import eel

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatA(query):
    eel.DisplayMessage("Hi, How can I help you")
    speak("Hi, How can I help You")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatB(query):
    eel.DisplayMessage("I am Great, thank you for asking! How about you?")
    speak("I am Great, thank you for asking!  How about you?")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatC(query):
    eel.DisplayMessage("Awesome!")
    speak("Awesome!")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatD(query):
    eel.DisplayMessage("Sorry, I didn't Understand.")
    speak("Sorry, I didnot Understand")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatE(query):
    eel.DisplayMessage("I am jarvis assistan. How can I help you?")
    speak("I am jarvis assistan. How can I help you?")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatF(query):
    eel.DisplayMessage("A first I was just an idea and Now here I am")
    speak("A first I was just an idea and Now here I am")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatG(query):
    eel.DisplayMessage("I'm happy you're happy")
    speak("I'm happy you're happy")
#>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def ChatH(query):
    eel.DisplayMessage("My name is Jarvis I'm your Assistant")
    speak("My name is Jarvis I'm your Assistant")