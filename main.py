from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer


kbcTune = 'kbc.mp3'
mixer.init()
mixer.music.load(kbcTune)
mixer.music.play(-1)



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

questions = ["The term ‘app’, in the context of a mobile app, is a shortened version of which word ?",
             "Which of the following is not a Gujarati snack?",
             "Which of these animals does not have spots on their bodies in their adulthood?",
             "Industrial Toxicology- Research Centre, is situated in which of the following states?",
             "From which of these rivers did our country get its name ‘ India’?",
             "The purpose of the hourglass is to measure which of these?",
             "In India, which of the following is not a common fuel used to run cars?",
             "At what temperature, in celsius, does water boil at sea level?",
             "Which of these Roman numerals will have the lowest value?",
             "Which of these mountain peaks has the greatest height above sea level?",
             "Who actually invented the telescope in 1608?",
             "HWhich company is the world’s largest manufacturer of vaccines by number of doses produced (volume)?",
             "Which Indian hockey player holds the record for the most number of goals scored in an Olympic final? ",
             "In which state did a politician named P Subash Chandra Bose become deputy chief minister in 2019?",
             "Who commanded the ‘Hector’, the first British trading ship to land at Surat?"]

first_option = ["Apple", "Dhokla", "Leopard", "U.P"
, "Sindhu", "Weight", "CNG","95", "V", "Kanchenjunga","Johannes Kepler",
 "Biocon", "Gurbux Singh", "Andhra Pradesh", "Paul Canning"]

second_option = ["Apparel", "Fafda", "Cheetah", "Gujarat", "Hindon"
, "Distance", "Coal","85","L", "K2", "Nicolaus Copernicus", "Serum Institute", "Leslie Claudius", "West Bengal", "William Hawkins"]

third_option = ["Apparatus", "Khaman", "Giraffe", "M.P", "Sutlej", "Time", "Diesel","100"
, "C", "Kamet", "Hans Lippershey", "Indian Immunologists", "Balbir Singh Senior", "Telangana", "Thomas Boe"]

fourth_option = ["Application", "Dosa", "Lion", "Bihar", "Ganga"
, "Temperature", "Petrol", "90", "X", "Nanda Devi", "Galileo Galili", "Bharat Biotech", "Keshav Dutt", "Karnataka", "James Lanraste"]

correct_answers = ["Application", "Dosa", "Lion", "Vinegar and Baking Soda", "Sindhu",
 "Time", "Coal", "100", "X", "K2", "Hans Lippershey", "Serum Institute", "Balbir Singh Senior", "Andhra Pradesh", "William Hawkins"]


def select(event):
    mixer.music.set_volume(1)
    b = event.widget
    value = b['text']

    callButton.config(image='')
    progressbarA.place_forget()
    progressbarLabelA.place_forget()

    progressbarB.place_forget()
    progressbarLabelB.place_forget()

    progressbarC.place_forget()
    progressbarLabelC.place_forget()

    progressbarD.place_forget()
    progressbarLabelD.place_forget()


    #Correct Answers!
    for i in range(15):
        if value == correct_answers[i]:
            if value == second_option[14]:
                def playagain():
                    phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                    lifeline50Button.config(state=NORMAL, image=image50)
                    audiencePoleButton.config(state=NORMAL, image=audiencePole)
                    asktheexpertLifelineButton.config(state=NORMAL,image=asktheexpert)
                    amountlabel.config(image=amountimage)
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])
                    optionButton1.config(text=first_option[0])
                    optionButton2.config(text=second_option[0])
                    optionButton3.config(text=third_option[0])
                    optionButton4.config(text=fourth_option[0])
                    root2.destroy()
                    mixer.music.load('kbc.mp3')
                    mixer.music.play(-1)



                def on_closing():
                    root2.destroy()
                    root.destroy()

                amountlabel.config(image=image15)
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.grab_set()
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 1 million Pounds')
                centerimg = PhotoImage(file='Kbc/center.png')
                imgLabel = Label(root2, image=centerimg, bd=0, )
                imgLabel.pack(pady=30)

                winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winlabel.pack()

                happyimage = PhotoImage(file='Kbc/happy.png')
                happYLabel = Label(root2, image=happyimage, bg='black')
                happYLabel.place(x=400, y=280)

                happYLabel1 = Label(root2, image=happyimage, bg='black')
                happYLabel1.place(x=30, y=280)

                playagainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=playagain)
                playagainButton.pack()

                closeButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                     , activebackground='black', cursor='hand2', activeforeground='white',
                                     command=on_closing)
                closeButton.pack()

                root2.protocol('WM_DELETE_WINDOW', on_closing)
                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionButton1.config(text=first_option[i + 1])
            optionButton2.config(text=second_option[i + 1])
            optionButton3.config(text=third_option[i + 1])
            optionButton4.config(text=fourth_option[i + 1])
            amountlabel.config(image=images[i])

            def knightmode():
                root3.destroy()
                mixer.music.stop()
                mixer.music.load('KnightMusic.mp3')
                mixer.music.play(-1)
                phoneLifelineButton.config(state=DISABLED, image=phoneImageX)
                lifeline50Button.config(state=DISABLED, image=image50x)
                audiencePoleButton.config(state=DISABLED, image=audiencePolex)
                asktheexpertLifelineButton.config(state=DISABLED,image=asktheexpertX)

            def quitgame():
                root3.destroy()
                root.destroy()


            if questionArea.get(1.0, 'end-1c') == questions[12]:


                root3 = Toplevel()
                root3.overrideredirect(True)
                root3.grab_set()
                root3.config(bg='black')
                root3.geometry('450x320+140+30')
                rootlabel = Label(root3, text='KNIGHT MODE', font=('arial', 30, 'bold'), bg='black', fg='white')
                rootlabel.pack(pady=10)
                rootlabel1 = Label(root3, text='The Next 3 Questions will not have any lifeline!', font=('arial', 15, 'bold'), bg='black', fg='white')
                rootlabel1.pack(pady=15)
                rootlabel2 = Label(root3, text='Press Proceed to Enter Knight Mode!', font=('arial', 11, 'bold'), bg='black', fg='white')
                rootlabel2.pack()
                rootlabel3 = Label(root3, text='Press Quit to End the game here and collect your prize!', font=('arial', 11, 'bold'), bg='black', fg='white')
                rootlabel3.pack(pady=5)
            

                

                proceedbutton = Button(root3, text='Proceed', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=knightmode)
                proceedbutton.pack()
                quitButton = Button(root3, text='Quit', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         bd=0
                                         , activebackground='black', cursor='hand2', activeforeground='white',
                                         command=quitgame)
                quitButton.pack(pady=5)

            if questionArea.get(1.0, 'end-1c') == questions[13]:
                phoneLifelineButton.config(state=DISABLED, image=phoneImageX)
                lifeline50Button.config(state=DISABLED, image=image50x)
                audiencePoleButton.config(state=DISABLED, image=audiencePolex)
                asktheexpertLifelineButton.config(state=DISABLED,image=asktheexpertX)

            if questionArea.get(1.0, 'end-1c') == questions[14]:
                phoneLifelineButton.config(state=DISABLED, image=phoneImageX)
                lifeline50Button.config(state=DISABLED, image=image50x)
                audiencePoleButton.config(state=DISABLED, image=audiencePolex)
                asktheexpertLifelineButton.config(state=DISABLED,image=asktheexpertX)



#Wrong Answers! 
        if value not in correct_answers:
            def tryagain():
                mixer.music.load('kbc.mp3')
                mixer.music.play(-1)
                phoneLifelineButton.config(state=NORMAL, image=phoneImage)
                lifeline50Button.config(state=NORMAL, image=image50)
                audiencePoleButton.config(state=NORMAL, image=audiencePole)
                asktheexpertLifelineButton.config(state=NORMAL,image=asktheexpert)

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])
                optionButton1.config(text=first_option[0])
                optionButton2.config(text=second_option[0])
                optionButton3.config(text=third_option[0])
                optionButton4.config(text=fourth_option[0])
                amountlabel.config(image=amountimage)
                root1.destroy()

            def on_closing():
                root1.destroy()
                root.destroy()
                

            mixer.music.stop()
            mixer.music.load('Wronganswer.mp3')
            mixer.music.play()
            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.grab_set()
            root1.config(bg='black')
            root1.geometry('600x500+140+30')
            root1.title('Wrong!')
            img = PhotoImage(file='Kbc/center.png')
            imgLabel = Label(root1, image=img, bd=0)
            imgLabel.pack(pady=30)
            loselabel = Label(root1, text='Wrong Answer!!', font=('arial', 40, 'bold'), bg='black', fg='white')
            loselabel.pack(pady=3)
            loselabel1 = Label(root1, text='Ask The Stall Respresentative for your prize!', font=('arial', 9, 'bold'), bg='black', fg='white')
            loselabel1.pack()
            sadimage = PhotoImage(file='Kbc/sad.png')
            sadlabel = Label(root1, image=sadimage, bg='black')
            sadlabel.place(x=480, y=280)
            sadlabel1 = Label(root1, image=sadimage, bg='black')
            sadlabel1.place(x=30, y=280)

            tryagainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=tryagain)
            tryagainButton.pack()

            closeButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=on_closing)
            closeButton.pack()

            root1.protocol('WM_DELETE_WINDOW', on_closing)

            root1.mainloop()

            break



def lifeline50():
    lifeline50Button.config(image=image50x)
    lifeline50Button.config(state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionButton3.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionButton3.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionButton1.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionButton2.config(text='')
        optionButton1.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionButton1.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionButton2.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionButton3.config(text='')
        optionButton4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionButton4.config(text='')
        optionButton2.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionButton2.config(text='')
        optionButton3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionButton1.config(text='')
        optionButton4.config(text='')


def phoneLifeLine():


    def okaypress():
        root4.destroy()
        phoneLifelineButton.config(image=phoneImageX, state=DISABLED)

    
    root4 = Toplevel()
    root4.overrideredirect(True)
    root4.grab_set()
    root4.config(bg='black')
    root4.resizable()
    root4.title('Ask Your Friend !')
    phonelabel = Label(root4, text='Ask Your Friend!', font=('arial', 20, 'bold'), bg='black', fg='white')
    phonelabel.pack(pady= 5)
    phonelabel1 = Label(root4, text='Ask your Friend or Family Member to Help you Answer the Question', font=('arial', 9, 'bold'), bg='black', fg='white')
    phonelabel1.pack(pady= 10 )
    okbutton = Button(root4, text='OK', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                 , activebackground='black', cursor='hand2', activeforeground='white',
                                 command=okaypress)
    okbutton.pack(pady=5)
    


def audiencePoleLifeline():
    audiencePoleButton.config(image=audiencePolex)
    audiencePoleButton.config(state=DISABLED)

    progressbarA.place(x=580, y=190)
    progressbarLabelA.place(x=580, y=320)

    progressbarB.place(x=620, y=190)
    progressbarLabelB.place(x=620, y=320)

    progressbarC.place(x=660, y=190)
    progressbarLabelC.place(x=660, y=320)

    progressbarD.place(x=700, y=190)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)

        progressbarB.config(value=60)

        progressbarC.config(value=40)

        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=80)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)

        progressbarB.config(value=70)

        progressbarC.config(value=90)

        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=80)

        progressbarB.config(value=10)

        progressbarC.config(value=40)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=20)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=10)

        progressbarB.config(value=70)

        progressbarC.config(value=50)

        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=90)

        progressbarB.config(value=80)

        progressbarC.config(value=70)

        progressbarD.config(value=20)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=30)

        progressbarB.config(value=50)

        progressbarC.config(value=70)

        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=40)

        progressbarB.config(value=20)

        progressbarC.config(value=50)

        progressbarD.config(value=70)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)

        progressbarB.config(value=80)

        progressbarC.config(value=90)

        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=20)

        progressbarB.config(value=60)

        progressbarC.config(value=50)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=60)

        progressbarB.config(value=35)

        progressbarC.config(value=40)

        progressbarD.config(value=80)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=60)

        progressbarB.config(value=65)

        progressbarC.config(value=90)

        progressbarD.config(value=80)


def asktheexpertlifeline():
    mixer.music.stop()
    mixer.music.load('calling.mp3')
    mixer.music.play()
    engine.say(f'The Expert is Waiting , Pls press the Call Icon to Listen to the Expert')
    engine.runAndWait()
    asktheexpertLifelineButton.config(image=asktheexpertX)
    asktheexpertLifelineButton.config(state=DISABLED) 
    callButton.config(image=callimage)
    
    



def phoneclick():
    callButton.config(image='')
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The Answer is {correct_answers[i]}')
            engine.runAndWait()


root = Tk()
root.geometry('1270x652+0+0')
root.resizable(0, 0)
root.title('Millionaire Game')
root.config(bg='black')

leftFrame = Frame(root, bg='black', padx=90)
leftFrame.grid(row=0, column=0)

rightFrame = Frame(root, bg='black', padx=50, pady=25)
rightFrame.grid(row=0, column=1)

topFrame = Frame(leftFrame, bg='black', pady=15)
topFrame.grid(row=0, column=0)

middleFrame = Frame(leftFrame, bg='black', pady=15)
middleFrame.grid(row=1, column=0)

bottomFrame = Frame(leftFrame, bg='black')
bottomFrame.grid(row=2, column=0)

centreImage = PhotoImage(file='Kbc/center.png')
logoLabel = Label(middleFrame, image=centreImage, bd=0, width=300, height=200, bg='black')
logoLabel.grid(row=0, column=0)

image50 = PhotoImage(file='Kbc/50-50.png')
image50x = PhotoImage(file='Kbc/50-50-X.png')

lifeline50Button = Button(topFrame, image=image50, bd=0, bg='black', cursor='hand2', activebackground='black', width=150,
                      height=60, command=lifeline50)
lifeline50Button.grid(row=0, column=0)

audiencePole = PhotoImage(file='Kbc/audiencePole.png')
audiencePolex = PhotoImage(file='Kbc/audiencePoleX.png')
audiencePoleButton = Button(topFrame, image=audiencePole, bd=0, bg='black', cursor='hand2', activebackground='black',
                            width=150, height=60, command=audiencePoleLifeline)
audiencePoleButton.grid(row=0, column=1)

phoneImage = PhotoImage(file='Kbc/FriendHelp.png')
phoneImageX = PhotoImage(file='Kbc/FriendHelpX.png')
phoneLifelineButton = Button(topFrame, image=phoneImage, bd=0, bg='black', cursor='hand2', activebackground='black', width=150,
                     height=60, command=phoneLifeLine)
phoneLifelineButton.grid(row=0, column=2)

asktheexpert = PhotoImage(file='Kbc/asktheexpert1.png')
asktheexpertX = PhotoImage(file='Kbc/asktheexpert1X.png')
asktheexpertLifelineButton = Button(topFrame, image=asktheexpert, bd=0, bg='black', cursor='hand2', activebackground='black', width=150,
                     height=60, command=asktheexpertlifeline)
asktheexpertLifelineButton.grid(row=0, column=3)


callimage = PhotoImage(file='Kbc/phone.png')
callButton = Button(root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
callButton.place(x=70, y=260)

amountimage = PhotoImage(file='Kbc/Picture0.png')
image1 = PhotoImage(file='Kbc/Picture1.png')
image2 = PhotoImage(file='Kbc/Picture2.png')
image3 = PhotoImage(file='Kbc/Picture3.png')
image4 = PhotoImage(file='Kbc/Picture4.png')
image5 = PhotoImage(file='Kbc/Picture5.png')
image6 = PhotoImage(file='Kbc/Picture6.png')
image7 = PhotoImage(file='Kbc/Picture7.png')
image8 = PhotoImage(file='Kbc/Picture8.png')
image9 = PhotoImage(file='Kbc/Picture9.png')
image10 = PhotoImage(file='Kbc/Picture10.png')
image11 = PhotoImage(file='Kbc/Picture11.png')
image12 = PhotoImage(file='Kbc/Picture12.png')
image13 = PhotoImage(file='Kbc/Picture13.png')
image14 = PhotoImage(file='Kbc/Picture14.png')
image15 = PhotoImage(file='Kbc/Picture15.png')

images = [image1, image2, image3, image4, image5, image6, image7, image8, image9, image10, image11, image12, image13
    , image14, image15]

amountlabel = Label(rightFrame, image=amountimage, bg='black', bd=0)
amountlabel.grid(row=0, column=0)

layoutimage = PhotoImage(file='Kbc/lay.png')
layoutlabel = Label(bottomFrame, image=layoutimage, bg='black', bd=0)
layoutlabel.grid(row=0, column=0)


questionArea = Text(bottomFrame, font=('arial', 16, 'bold'), bg='black', fg='white',width=36, height=2,
                        wrap='word',bd=0)
questionArea.place(x=80,y=10)

questionArea.insert(END, questions[0])




labelA = Label(bottomFrame, font=('arial', 16, 'bold'), text='A:', bg='black', fg='white')
labelA.place(x=60,y=110)

optionButton1 = Button(bottomFrame,wraplength=110, text=first_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton1.place(x=100,y=100)

labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
labelB.place(x=330,y=110)

optionButton2 = Button(bottomFrame,wraplength=110, text=second_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                              cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton2.place(x=370,y=100)

labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
labelC.place(x=60,y=190)

optionButton3 = Button(bottomFrame,wraplength=110,text=third_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton3.place(x=100,y=180)

labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
labelD.place(x=330,y=190)

optionButton4 = Button(bottomFrame,wraplength=110, text=fourth_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                             cursor='hand2',bd=0,activebackground='black',activeforeground='white')
optionButton4.place(x=370,y=180)

progressbarA = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarB = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarC = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

progressbarD = Progressbar(root, orient=VERTICAL, mode='determinate', length=120)

progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionButton1.bind('<Button-1>', select)
optionButton2.bind('<Button-1>', select)
optionButton3.bind('<Button-1>', select)
optionButton4.bind('<Button-1>', select)

root.mainloop()