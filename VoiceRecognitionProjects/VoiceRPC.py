from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import pyttsx3
import speech_recognition
import pyaudio
import threading


PlScore = 0
PcScore = 0
i = speech_recognition.Recognizer()
PL = 0
PC = 'b'
w = 0




def SpeakText(command):

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-1000)
    engine.say(command)
    engine.runAndWait()


def choice(n):
    global PL
    global PC
    global PcScore
    global PlScore
    global w

    if n == 1:
        PL = 1
        Playerlbl.configure(image=rock)

    elif n == 2:
        PL = 2
        Playerlbl.configure(image=paper)

    elif n == 3:
        PL = 3
        Playerlbl.configure(image=scissors)



    a = random.randint(1, 3)
    if a == 1:
        PC = 1
        Pclbl.configure(image=rock)
    elif a == 2:
        PC = 2
        Pclbl.configure(image=paper)
    else:
        PC = 3
        Pclbl.configure(image=scissors)



    if PL == PC:
        threading.Thread(target=SpeakText, args=("Draw",)).start()

    if PL == 1:
        if PC == 2:

            PcScore += 1
            Scorelbl.configure(text = "Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You lost",)).start()
        elif PC == 3:

            PlScore += 1
            Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You won",)).start()
    elif PL == 2:
        if PC == 1:

            PlScore += 1
            Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You won",)).start()
        elif PC == 3:

            PcScore += 1
            Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You lost",)).start()
    elif PL == 3:
        if PC == 1:

            PcScore += 1
            Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You lost",)).start()
        elif PC == 2:

            PlScore += 1
            Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
            threading.Thread(target=SpeakText, args=("You won",)).start()


    if w == 0:
        if PlScore == 3:
            Rockbtn["state"] = DISABLED
            Paperbtn["state"] = DISABLED
            Scissorsbtn["state"] = DISABLED
            threading.Thread(target=SpeakText, args=("You have won the game",)).start()
            Startbtn.configure(text = 'Start')
            Playerlbl.configure(image=RPC)
            Pclbl.configure(image=RPC)
            w = 1
            Startbtn["state"] = NORMAL

        elif PcScore == 3:
            Rockbtn["state"] = DISABLED
            Paperbtn["state"] = DISABLED
            Scissorsbtn["state"] = DISABLED
            threading.Thread(target=SpeakText, args=("You have lost the game",)).start()
            Startbtn.configure(text='Start')
            Playerlbl.configure(image=RPC)
            Pclbl.configure(image=RPC)
            w = 1
            Startbtn["state"] = NORMAL




def Start():
    global PL
    global PC
    global PcScore
    global PlScore
    global w
    PcScore = 0
    PlScore = 0
    w = 0
    Scorelbl.configure(text="Player:  " + str(PlScore) + "  Pc:  " + str(PcScore))
    threading.Thread(target=SpeakText, args=("Press Rock, Paper, or Scissors to choose",)).start()



    Rockbtn["state"] = NORMAL
    Paperbtn["state"] = NORMAL
    Scissorsbtn["state"] = NORMAL
    Startbtn["state"] = DISABLED


    print(PlScore)
    print(PcScore)









window = ThemedTk(theme = "yaru")
window.configure(themebg="yaru")
window.geometry("800x600")

rock = PhotoImage(file = "rock.png")
scissors = PhotoImage(file = "scissors.png")
paper = PhotoImage(file = "paper.png")
RPC = PhotoImage(file = "RPC.png")

Titlelbl = ttk.Label(window,text="Rock Paper Scissors Game vs Computer!",justify=CENTER,font = ("Mangal", 20,'bold'))
Titlelbl.place(x= 120,y=0)

Playerlbl = ttk.Label(window,image =RPC)
Playerlbl.place(x=125,y=230)

Pclbl = ttk.Label(window,image =RPC)
Pclbl.place(x=520,y=230)

Label1 = ttk.Label(window,text = "You:",font = ("Mangal", 15,'bold'))
Label1.place(x=143,y=180)

Label2 = ttk.Label(window,text = "Pc:",font = ("Mangal", 15,'bold'))
Label2.place(x=577,y=180)

Scorelbl = ttk.Label(window,text = "Player:  " + str(PlScore) + "  Pc:  " + str(PcScore),font = ("Mangal", 15,'bold'))
Scorelbl.place(x=315,y=70)


Startbtn = ttk.Button(window,text = "Start",command = Start)
Startbtn.place(x=350,y=420)

Rockbtn = ttk.Button(window, text = 'Rock',command = lambda:choice(1))
Rockbtn.place(x=57,y=120)
Rockbtn["state"] = DISABLED

Paperbtn = ttk.Button(window, text = 'Paper',command = lambda:choice(2))
Paperbtn.place(x=141,y=120)
Paperbtn["state"] = DISABLED

Scissorsbtn = ttk.Button(window, text = 'Scissors',command = lambda:choice(3))
Scissorsbtn.place(x=225,y=120)
Scissorsbtn["state"] = DISABLED

window.mainloop()