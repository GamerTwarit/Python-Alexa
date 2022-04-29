import pyautogui
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime

import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("How can i help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("please repeat ")
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if 'micro' in query:
            query.replace('micro','')

        # Logic for executing tasks based on query
########################## wikipedia searches ################################################################
        if 'search' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'wiki' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wiki', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


#######################relatd to web#################################################################################
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'play' in query:
            song = query.replace('play', '')
            pywhatkit.playonyt(song)
            speak(" there can be,,, addss")
        elif 'thanks' in query:
            speak("i am always there to help you")
            print(":)")


        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open url' in query:
            speak("please type the url")
            url = input("type the url to open: ")
            webbrowser.open(url)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
###############################basic commands################################################################

        elif 'are you active' in query:
            speak("yes im still active")
        elif 'are you still active' in query:
            speak("yes im still active")
        elif 'are you there' in query:
            speak("yes im still active")
        elif 'are you still there' in query:
            speak('yes im still active')

        elif 'hello' in query:
            speak("hi?")
        elif 'hi' in query:
            speak("hello?")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            IstrTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f", the time is {strTime} in a 24 hour clock timings")
            speak("OR")
            speak(f", the time is {IstrTime} in a 12 hour clock timings")
            hour = int(datetime.datetime.now().hour)
            if hour >= 0 and hour < 12:
                speak("So its Morning")

            elif hour >= 12 and hour < 17:
                speak("So its afternoon")

            else:
                speak("So its evening")
        elif 'thanks' in query:
            speak('your welcome')
        elif 'fine' in query:
            speak("..........k")
        elif 'nice' in query:
            speak("thanks")
        elif 'volume up' in query:
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            pyautogui.press('volumeup')
            speak("volume increased by 10")
        elif 'volume down' in query:
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            pyautogui.press('volumedown')
            speak("volume decreased by 10")
        elif 'mute' in query:
            speak('muting..... you wont be able to hear me to hear me again you will have to say volume up')
            pyautogui.press('volumemute')
        elif 'who are you' in query:
            speak("im your virtual assistant AND my name is micro")
        elif "what's your name" in query:
            speak('my name is micro ')
        elif 'pause' in query:
            speak("okay you can resume me by typing resume")
            input("type here 'resume' to resume: ")
            speak("resuming.....")
            print("resuming....")
        elif 'ok' in query:
            print("??????????????????????????????????????????????????????????")


