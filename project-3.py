
import speech_recognition as sr
import pywhatkit
import pyttsx3
import os

speaker = pyttsx3.init()
mic = sr.Recognizer()

speaker.say("Welcome")
speaker.runAndWait()

while True:
    with sr.Microphone() as source:
        print("Start Speaking...")
        mic.adjust_for_ambient_noise(source)
        
        try:
            voice = mic.listen(source)
            text = mic.recognize_google(voice)
            text = text.lower()
            print("You Said:", text)

        except sr.UnknownValueError:
            print("Could not understand audio")
            continue

        except sr.RequestError:
            print("No internet connection")
            continue


        if "open notepad" in text:
            print("Opening Notepad...")
            os.system("start notepad")

        elif "open chrome" in text:
            print("Opening Chrome...")
            os.system("start chrome")

        elif "open brave" in text:
            print("Opening Brave...")
            os.system("start brave")

        elif "send message" in text:
            print("Sending Message")
            pywhatkit.sendwhatmsg_instantly("+919262806552" , "Aur kya haal chaal h aapke")

        elif "open youtube" in text:
            print("Opening Youtube...")
            pywhatkit.playonyt({text})

        elif "shut yourself" in text:
            print("Closing.....")
            break

        else:
            print("Command not recognized")
