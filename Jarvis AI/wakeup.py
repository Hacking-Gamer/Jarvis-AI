import os
import win32com.client
import speech_recognition
import sys

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
        
while 1:
        s = ("Hello I am wake up Jarvis. ")
        speaker.Speak(s)
        while True:
         print("listening...")
         query = takeCommand()

         if "wake up".lower() in query.lower():
             speaker.Speak("waking up")
             mainpath = r'"E:\Jarvis AI\Jarvis AI.py"'
             os.startfile(mainpath)
             sys.exit()
             
