import speech_recognition
import win32com.client
import datetime
import os
from pyautogui import click
from keyboard import write
from keyboard import press
from keyboard import press_and_release

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def takeCommand():
            r = speech_recognition.Recognizer()
            with speech_recognition.Microphone() as source:
                r.pause_threshold = 0.6
                audio = r.listen(source)
                try:
                     query = r.recognize_google(audio, language="en-in")
                     print(f"User Said {query}")
                     return query
                except Exception as e:
                     return "Some Error Occurred, Sorry From Jarvis"

def chromeauto(command):
    query = str(command)
    if 'new tab' in query:
          press_and_release('ctrl + t')

    elif 'close tab' in query:
          press_and_release('ctrl + w')

    elif 'new window' in query:
          press_and_release('ctrl + n')

    elif 'switch tab' in query:
          speaker.Speak("To Which Tab") 
          tab = takeCommand()
        #   Tab = int(tab)

          if '1' in tab or 'one' in tab:
                press_and_release('ctrl + 1')

          elif '2' in tab or 'two' in tab:
                press_and_release('ctrl + 2')

          elif '3' in tab or 'three' in tab:
                press_and_release('ctrl + 3')   

          elif '4' in tab or 'four' in tab:
                press_and_release('ctrl + 4')  
          
# chromeauto(command)

def notepad():
    speaker.Speak("Sir Tell Me What Should I Write.")
    print("listening...")

    writes = takeCommand()

    time = datetime.datetime.now().strftime("%H:%M")


    filename = str(time).replace(":","-") + "-note.txt" 

    with open(filename,"w") as file:
          file.write(writes)


    path_1 = "E:\\Jarvis AI\\" + str(filename)

    path_2 = "E:\\Jarvis AI\\DataBase\\NotePad\\" + str(filename)

    os.rename(path_1,path_2)

    os.startfile(path_2)     

# notepad()

def closenote():
      os.system("TASKKILL /F /im Notepad.exe")

# closenote()      