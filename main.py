import speech_recognition as sr
A = 1
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import time as Time_module
import  pyautogui as PG
listener= sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def talk (text):
    engine.say(text)
    engine.runAndWait()



def take_command():
    try:
         with sr.Microphone() as source:
             print("listening...")
             voice = listener.listen(source)
             command = listener.recognize_google(voice)
             command=command.lower()
             if  'alexa' in command:
                 command=command.replace('alexa','')
                 print(command)
    except:
        pass
    return command

def run_alexa():
    while True:
        command = take_command()
        print(command)

        if 'play song' in command:
            song = command.replace('play', '')
            talk('..playing song there can be ads.. sorry about that ' + song)
            pywhatkit.playonyt(song)

        elif 'i am bored' in command:
            talk("i am sorry that you are bored ...but why dont play a game")
            talk("in google there are many free online games..no download.. like 1 v 1 lol, justfall. Etsectra")
        elif "thank you" in command:
            talk("welcome, ... i am always here to help you")
        elif 'give me an introduction ' in command:
            talk("sure,.......,")
            talk("this module is not alexa but similar to it")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            talk("the time is" + time)

        elif 'start auto click' in command:
            talk(" left click yes starting in 3, 2, 1")
            B = 3
            while B == 3:
                PG.click(button='left')
        elif 'shutdown' in command:
            os.system("shutdown /s /t 1")
        elif 'log off' in command:
            os.system("shutdown -l")
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'who ' in command:
            person = command.replace('who', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'open microsoft teams ' in command:
            talk("sure,,... redirecting you to microsoft teams folder,... there you can open it,...")
            dir = 'D:\\MS Teams'

            os.startfile(dir)
            os.system(dir)

            import subprocess
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif 'why' in command:
            person = command.replace('why', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'why' in command:
            person = command.replace('why', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'open epic games' in command:
            talk("sure,,... redirecting you to epic games folder,... there you can open it,...")
            dir = 'D:\\Epic Games'

            os.startfile(dir)
            os.system(dir)

            import subprocess
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif 'open google' in command:
            talk("sure redirecting you to chrome's folder,... there you can open it")
            dir = 'D:\\Google'

            os.startfile(dir)
            os.system(dir)

            import subprocess
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif 'when' in command:
            person = command.replace('when', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'what' in command:
            person = command.replace('what', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'when' in command:
            person = command.replace('when', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)

        elif 'you are the best' in command:
            talk("thank you,,,...... i am always here to help you")
        elif 'thanks' in command:
            talk("thank you,,,...... i am always here to help you")
        elif 'tell a joke' in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())

        elif 'show me a joke' in command:
            talk(pyjokes.get_joke())
        elif 'game' in command:
            talk("sure....which Game, like escape horror or open among us ")
        elif 'escape horror' in command:
            talk(
                "sure..., redirecting to the game folder,...now here you need to double click the game and extract it, after that game will automaticcaly start")
            dir = 'D:\\Escape horror'

            os.startfile(dir)
            os.system(dir)

            import subprocess
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif 'open among us' in command:
            talk("sure,... redirecting you to among us folder,.... there you can open the game")
            dir = 'D:\\Amonus'

            os.startfile(dir)
            os.system(dir)

            import subprocess
            subprocess.Popen([dir])
            subprocess.call(dir)
        elif 'open zoom' in command:
            talk("opening")
            PG.press('winleft')
            PG.typewrite('zoom')
            PG.press('enter')
        elif 'open teams' in command:
            talk("opening")
            PG.press('winleft')
            Time_module.sleep(2)
            PG.typewrite('microsoft teams')
            Time_module.sleep(1)
            PG.press('enter')
        elif 'open spotify' in command:
            talk("opening")
            PG.press('winleft')
            Time_module.sleep(2)
            PG.typewrite('spotify')
            Time_module.sleep(1)
            PG.press('enter')
        else:
            talk('Please tell the command again')

run_alexa()