import win32com.client
import os
import speech_recognition
import webbrowser
import openai
import datetime
import random
import sys

speaker = win32com.client.Dispatch("SAPI.SpVoice")

jokes = [
    'yes money can\'t buy happiness, but it is much more comfortable to cry in a new BMW than on a bike',
    'i never make the same mistake twice. i make it 5-6 times, just to be sure.',
    'I was going to tell you a joke about boxing but I forgot the punch line.',
    'What\'s an egg\'s favorite vacation spot? New Yolk City.',
    'I ate a sock yesterday. It was very time-consuming.',
    'What kind of candy do astronauts like? Mars bars',
    'What month is the shortest of the year? May, it only has three letters.',
    'My uncle named his dogs Timex and Rolex. They\'re his watch dogs.',
]

responses = {
    'what is your name': 'My name is Jarvis.',
    'what do you like to do': 'I like chatting with people and learning new things.',
    'can you help me with something': 'Of course, what do you need help with?',
    'what is the meaning of life': 'That\'s a tough question. I think it\'s different for everyone.',
}

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
    s = ("Hello I Am Jarvis AI, what can i do for you?")
    speaker.Speak(s)
    while True:
     print("listening...")
     query = takeCommand()
     sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
     for site in sites:
        if f"open {site[0]}".lower() in query.lower():
            speaker.Speak(f"Opening {site[0]} Sir...")
            webbrowser.open(site[1])
     if "play despacito" in query:
         musicpath = r"C:\Users\hp\Downloads\Despacito_320(PagalWorld).mp3"
         speaker.Speak("Playing Despacito sir...")
         os.startfile(musicpath)

     if "the time" in query:
         time = datetime.datetime.now().strftime("%H:%M")
         speaker.Speak(f"Sir The Time is {time}")

     if "open telegram".lower() in query.lower():
         telepath = r"C:\Users\hp\Desktop\Telegram.lnk"
         speaker.Speak("Opening Telegram sir...")
         os.startfile(telepath)

     if "how are you".lower() in query.lower():
         speaker.Speak("I am Fine And You")

     if "I am also fine".lower() in query.lower():
         speaker.Speak("You Should Always be Fine")

     if "I am sad".lower() in query.lower():
         speaker.speak("You Should Not be sad, if you are sad, i am also sad")

     if "You are cute".lower() in query.lower():
         speaker.Speak("Thank You")

     if "tell me a joke".lower() in query.lower():
         speaker.Speak(random.choice(jokes))

     if query.lower() in responses:
         speaker.Speak(responses[query])

     if "goodbye" in query or "offline" in query or "bye" in query:
                    speaker.Speak("Alright sir, going offline. It was nice working with you")
                    sys.exit()


     # speaker.Speak(query)
