import pywhatkit
import wikipedia
import os
import webbrowser as web
import speech_recognition
import win32com.client
import wolframalpha

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



def YoutubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term

    web.open(result)
    speaker.Speak("Here are the result")

    pywhatkit.playonyt(term)

    speaker.Speak("This May Also Help you SIr....")


# YoutubeSearch("Carryminati")    


def YoutubeDownload():
      from pytube import YouTube
      from pyautogui import click
      from pyautogui import hotkey
      import pyperclip
      from time import sleep

      sleep(2)
      click(x=596, y=55)

      hotkey('ctrl','c')
      value = pyperclip.paste()
      Link = str(value)

      def Download(link):
            
            url = YouTube(link)

            video = url.streams.first()

            video.download("C:\\Users\\hp\\Videos\\Youtube\\")

      Download(Link)
      speaker.Speak("Video Downloded Sir...")     



def wolf(query):
      api_key= "KQ73WA-Q97LL4Q33E"   

      requester = wolframalpha.Client(api_key)    
      requested = requester.query(query)

      try:
            
            answer = next(requested.results).text

            return answer
      
      except:
            
            speaker.Speak("Sorry I Don't Know The Answer.")


def calc(query):

      Term = str(query)

      Term = Term.replace("jarvis","")
      Term = Term.replace("multiply","*")
      Term = Term.replace("plus","+")
      Term = Term.replace("minus","-")
      Term = Term.replace("divide","")

      Final = str(Term)

    #   speaker.Speak("What should i calculate")

      try:
            result = wolf(Final)
            speaker.Speak(f"{result}")

      except:
            speaker.Speak("Sorry I Don't Know The Answer.")      
     
# calc("68 plus 1")            

# YoutubeSearch('tech burner')

def googlesearch(query):
      # speaker.Speak("What Should I Search")

      from pyautogui import click
      from pyautogui import hotkey
      import pyautogui
      import pyperclip
      from time import sleep
      from keyboard import press_and_release

      chrme = r"C:\Users\Public\Desktop\Google Chrome.lnk"
      os.startfile(chrme)


      sleep(2)
      click(x=596, y=55)

      pyautogui.write(query)
      press_and_release('enter')

      
# googlesearch("amitabh bachan")      


       
