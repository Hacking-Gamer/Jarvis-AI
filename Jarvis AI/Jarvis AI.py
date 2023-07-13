import typing

from Jarvis_Ui import Ui_MainWindow
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget, QTextBrowser
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, Qt , QTimer , QTime , QDate, pyqtSlot
from PyQt5.uic import loadUiType
# import wakeup
import sys

class MainThread(QThread):
    
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        # Put your actual code here
        import win32com.client
        import os
        import speech_recognition
        import webbrowser
        import openai
        import datetime
        import random
        import sys
        from keyboard import write
        from keyboard import press
        from keyboard import press_and_release

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



        s = ("Hello I Am Jarvis AI, what can i do for you?")
        speaker.Speak(s)

        while 1:
          #   don't write something here
            while True:
             print("listening...")
             query = takeCommand()

             sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["gmail", "https://mail.google.com"], ["1337x", "https://1337x.to"]]
             for site in sites:
              if f"open {site[0]}".lower() in query.lower():
                speaker.Speak(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
                break
              
             if "play despacito" in query:
              musicpath = r"C:\Users\hp\Downloads\Despacito_320(PagalWorld).mp3"
              speaker.Speak("Playing Despacito sir...")
              os.startfile(musicpath)
              break

             if "the time" in query:
                  time = datetime.datetime.now().strftime("%H:%M")
                  speaker.Speak(f"Sir The Time is {time}")
                  break

             if "open telegram".lower() in query.lower():
                  telepath = r"C:\Users\hp\Desktop\Telegram.lnk"
                  speaker.Speak("Opening Telegram sir...")
                  os.startfile(telepath)
                  break

             if "how are you".lower() in query.lower():
                  speaker.Speak("I am Fine And You")
                  break

             if "I am also fine".lower() in query.lower():
                  speaker.Speak("You Should Always be Fine")
                  break

             if "I am sad".lower() in query.lower():
                  speaker.speak("You Should Not be sad, if you are sad, i am also sad")
                  break

             if "You are cute".lower() in query.lower():
                  speaker.Speak("Thank You")
                  break

             if "tell me a joke".lower() in query.lower():
                  speaker.Speak(random.choice(jokes))
                  break

             if query.lower() in responses:
                  speaker.Speak(responses[query])
                  break
             
             if "open vs code" in query.lower() or "open VS code" in query.lower():
                 speaker.Speak("opening V.S. code sir...")
                 vs = r"C:\Users\hp\Desktop\Visual Studio Code.lnk"
                 os.startfile(vs)
                 break
             
             if "open windscribe" in query.lower():
                 speaker.Speak("opening Windscribe sir...")
                 ws = r"C:\Users\Public\Desktop\Windscribe.lnk"
                 os.startfile(ws)
                 break
             
             if "open chrome" in query.lower():
                 speaker.Speak("opening Chrome sir...")
                 chrme = r"C:\Users\Public\Desktop\Google Chrome.lnk"
                 os.startfile(chrme)
                 break
             
             if "open discord" in query.lower():
                 speaker.Speak("opening Discord sir...")
                 discord = r"C:\Users\hp\Desktop\Discord   Friends.lnk"
                 os.startfile(discord)
                 break
             
             if "youtube search" in query.lower():
                 Query = query.replace("jarvis", "")
                 query = Query.replace("youtube search", "")
                 query = Query.replace("YouTube search", "")
                #  query = Query.replace("Youtube Search", "")
                #  query = Query.replace("youtube Search", "")
                #  query = Query.replace("Youtube search", "")
                 from feature import YoutubeSearch
                 YoutubeSearch(query)
                 break
             
             if "download this video" in query.lower():
                 from feature import YoutubeDownload
                 YoutubeDownload()
                 break
             
             if "write a note" in query.lower() or "take a note" in query.lower():
                 from automation import notepad
                 notepad()
                 break
             
            #  if "dismiss" in query.lower:
            #      from automation import closenote
            #      closenote()
            #      break
             
            #  if "calculate"  in query.lower():
            #      from feature import calc
            #     #  que = takeCommand()
            #      speaker.Speak("What should i calculate")
            #      calc(query)

             if 'new tab' in query:
                    press_and_release('ctrl + t')

             elif 'closed tab' in query:
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

             if "google search" in query.lower():
                 Query = query.replace("jarvis", "")
                 query = Query.replace("google search", "")
                 query = Query.replace("Google search", "")
                 from feature import googlesearch
                 googlesearch(query)
                    
          



             if "goodbye" in query or "offline" in query or "bye" in query:
                           speaker.Speak("Alright sir, going offline. It was nice working with you")
                           sys.exit()
                           break
            
            #  else:
            #      speaker.Speak("Sorry, I Don't Know What You Are Saying.")
            #      break




     # speaker.Speak(query)

        pass
    


startExe = MainThread()

# class ConsoleOutput(QTextBrowser):
#     def __init__(self, parent=None):
#         super(ConsoleOutput, self).__init__(parent)


#     def write(self, text):
#         self.insertPlainText(str(text))


#     def flush(self):
#         pass     


class Gui_Start(QMainWindow):
   
   def __init__(self):
      
      super().__init__()

      self.gui = Ui_MainWindow()
      self.gui.setupUi(self)

      self.gui.pushButton.clicked.connect(self.startTask1)
      self.gui.pushButton.clicked.connect(self.startTask2)
      self.gui.pushButton.clicked.connect(self.startTask3)
      self.gui.pushButton.clicked.connect(self.startTask4)
      self.gui.pushButton_2.clicked.connect(self.close)
     #  self.console = ConsoleOutput(self)
     #  self.setCentralWidget(self.console)

     #  sys.stdout = self.console
     #  sys.stderr = self.console

     #  write = ConsoleOutput(self)


   def startTask1(self):
      
      self.gui.label1 = QMovie("E:\Jarvis AI\jarvis gui\B.G\Iron_Template_1.gif")
      self.gui.gif_1.setMovie(self.gui.label1)
      self.gui.label1.start()

   def startTask2(self):
      
      self.gui.label2 = QMovie("E:\\Jarvis AI\\jarvis gui\\VoiceReg\\Ntuks.gif")
      self.gui.gif_2.setMovie(self.gui.label2)
      self.gui.label2.start()

   def startTask3(self):
      
      self.gui.label3 = QMovie("E:\Jarvis AI\jarvis gui\ExtraGui\Earth.gif")
      self.gui.gif_3.setMovie(self.gui.label3)
      self.gui.label3.start()

   def startTask4(self):
      
      self.gui.label4 = QMovie("E:\\Jarvis AI\\jarvis gui\\ExtraGui\\live.gif")
      self.gui.gif_4.setMovie(self.gui.label4)
      self.gui.label4.start()

      startExe.start()


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())