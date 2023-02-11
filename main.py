from tkinter import *
from tkinter.ttk import Progressbar
import pyttsx3
from pygame import mixer
import time 






def startgame():
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
                "Which company is the world’s largest manufacturer of vaccines by number of doses produced (volume)?",
                "Which Indian hockey player holds the record for the most number of goals scored in an Olympic final? ",
                "In which state did a politician named P Subash Chandra Bose become deputy chief minister in 2019?",
                "Who commanded the ‘Hector’, the first British trading ship to land at Surat?"]

    first_option = ["Apple", "Dhokla", "Leopard", "U.P"
    , "Sindhu", "Weight", "CNG","95", "V", "Kanchenjunga","Johannes Kepler",
    "Biocon", "Gurbux Singh", "Andhra Pradesh", "Paul Canning"]

    second_option = ["Apparel", "Fafda", "Cheetah", "Gujarat", "Hindon"
    , "Distance", "Coal","85","L", "K2", "Nicolaus Copernicus", "Serum Institute", "Leslie Claudius", "West Bengal", "William Hawkins"]

    third_option = ["Apparatus", "Khaman", "Giraffe", "M.P", "Sutlej", "Time", "Diesel","100"
    , "C", "Kamet", "Hans Lippershey", "Indian Immuno", "Balbir Singh Senior", "Telangana", "Thomas Boe"]

    fourth_option = ["Application", "Dosa", "Lion", "Bihar", "Ganga"
    , "Temperature", "Petrol", "90", "X", "Nanda Devi", "Galileo Galili", "Bharat Biotech", "Keshav Dutt", "Karnataka", "James Lanraste"]

    correct_answers = ["Application", "Dosa", "Lion", "U.P", "Sindhu",
    "Time", "Coal", "100", "X", "K2", "Hans Lippershey", "Serum Institute", "Balbir Singh Senior", "Andhra Pradesh", "William Hawkins"]

    #

    def restart():
                    start_root.__init__()
                    screen_width = start_root.winfo_screenwidth()
                    screen_height = start_root.winfo_screenheight()
                    window_width = 635
                    window_height = 326
                    x = (screen_width/2) - (window_width/2)
                    y = (screen_height/2) - (window_height/2)
                    start_root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
                    start_root.resizable(0, 0)
                    start_root.title('Millionaire Game')
                    start_root.config(bg='black')
                    centerimg = PhotoImage(file='Kbc/center.png')
                    imgLabel = Label(start_root, image=centerimg, bd=0, )
                    imgLabel.pack(pady=30)
                    startbutton = Button(start_root, text='Start', font=('arial', 20, 'bold'), bg='black', fg='white',bd=0
                                                                , activebackground='black', cursor='hand2', activeforeground='white',command=startgame)
                    startbutton.pack()
                    start_root.mainloop()



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
                        win_screenroot.destroy()
                        main_root.destroy()
                        restart()



                    def on_closing():
                        win_screenroot.destroy()
                        main_root.destroy()
                        restart()

                    amountlabel.config(image=image15)
                    mixer.music.stop()
                    mixer.music.load('Kbcwon.mp3')
                    mixer.music.play()
                    win_screenroot = Toplevel()
                    win_screenroot.overrideredirect(True)
                    win_screenroot.grab_set()
                    win_screenroot.config(bg='black')
                    screen_width = win_screenroot.winfo_screenwidth()
                    screen_height = win_screenroot.winfo_screenheight()
                    window_width = 500
                    window_height = 400
                    x = (screen_width/2) - (window_width/2)
                    y = (screen_height/2) - (window_height/2)
                    win_screenroot.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
                    win_screenroot.title('Winner!!!')
                    centerimg = PhotoImage(file='Kbc/center.png')
                    imgLabel = Label(win_screenroot, image=centerimg, bd=0, )
                    imgLabel.pack(pady=30)

                    winlabel = Label(win_screenroot, text='You Won!', font=('arial', 40, 'bold'), bg='black', fg='white')
                    winlabel.pack()

                    happyimage = PhotoImage(file='Kbc/happy.png')
                    happYLabel = Label(win_screenroot, image=happyimage, bg='black')
                    happYLabel.place(x=400, y=280)

                    happYLabel1 = Label(win_screenroot, image=happyimage, bg='black')
                    happYLabel1.place(x=30, y=280)

                    playagainButton = Button(win_screenroot, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                            bd=0
                                            , activebackground='black', cursor='hand2', activeforeground='white',
                                            command=playagain)
                    playagainButton.pack()

                    closeButton = Button(win_screenroot, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                        , activebackground='black', cursor='hand2', activeforeground='white',
                                        command=on_closing)
                    closeButton.pack()

                    win_screenroot.protocol('WM_DELETE_WINDOW', on_closing)
                    win_screenroot.mainloop()
                    break

                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[i + 1])

                optionButton1.config(text=first_option[i + 1])
                optionButton2.config(text=second_option[i + 1])
                optionButton3.config(text=third_option[i + 1])
                optionButton4.config(text=fourth_option[i + 1])
                amountlabel.config(image=images[i])

                def knightmode():
                    knightmode_root.destroy()
                    mixer.music.stop()
                    mixer.music.load('KnightMusic.mp3')
                    mixer.music.play(-1)
                    phoneLifelineButton.config(state=DISABLED, image=phoneImageX)
                    lifeline50Button.config(state=DISABLED, image=image50x)
                    audiencePoleButton.config(state=DISABLED, image=audiencePolex)
                    asktheexpertLifelineButton.config(state=DISABLED,image=asktheexpertX)

                def quitgame():
                    knightmode_root.destroy()
                    main_root.destroy()
                    restart()


                if questionArea.get(1.0, 'end-1c') == questions[1]:


                    knightmode_root = Toplevel()
                    knightmode_root.overrideredirect(True)
                    knightmode_root.grab_set()
                    knightmode_root.config(bg='black')
                    screen_width = knightmode_root.winfo_screenwidth()
                    screen_height = knightmode_root.winfo_screenheight()
                    window_width = 650
                    window_height = 600
                    x = (screen_width/2) - (window_width/2)
                    y = (screen_height/2) - (window_height/2)
                    knightmode_root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
                    rootlabel = Label(knightmode_root, text='KNIGHT MODE', font=('arial', 30, 'bold'), bg='black', fg='white')
                    rootlabel.pack(pady=10)
                    centerimg = PhotoImage(file='Kbc/center.png')
                    imgLabel = Label(knightmode_root, image=centerimg, bd=0, )
                    imgLabel.pack(pady=30)
                    rootlabel1 = Label(knightmode_root, text='The Next 3 Questions will not have any lifeline!', font=('arial', 15, 'bold'), bg='black', fg='white')
                    rootlabel1.pack(pady=15)
                    rootlabel2 = Label(knightmode_root, text='Press Proceed to Enter Knight Mode!', font=('arial', 11, 'bold'), bg='black', fg='white')
                    rootlabel2.pack()
                    rootlabel3 = Label(knightmode_root, text='Press Quit to End the game here and collect your prize!', font=('arial', 11, 'bold'), bg='black', fg='white')
                    rootlabel3.pack(pady=5)
                    rootlabel3 = Label(knightmode_root, text='Proceed at your risk.. It will result in the loss of the prize attained earlier!', font=('arial', 8, 'bold'), bg='black', fg='white')
                    rootlabel3.pack(pady=5)

                

                    

                    proceedbutton = Button(knightmode_root, text='Proceed', font=('arial', 20, 'bold'), bg='black', fg='white',
                                            bd=0
                                            , activebackground='black', cursor='hand2', activeforeground='white',
                                            command=knightmode)
                    proceedbutton.pack()
                    quitButton = Button(knightmode_root, text='Quit', font=('arial', 20, 'bold'), bg='black', fg='white',
                                            bd=0
                                            , activebackground='black', cursor='hand2', activeforeground='white',
                                            command=quitgame)
                    quitButton.pack(pady=5)
                    knightmode_root.mainloop()

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
                    lose_screenroot.destroy()
                    main_root.destroy()
                    restart()


                def on_closing():
                    lose_screenroot.destroy()
                    main_root.destroy()
                    restart()
                    

                mixer.music.stop()
                mixer.music.load('Wronganswer.mp3')
                mixer.music.play()
                lose_screenroot = Toplevel()
                lose_screenroot.overrideredirect(True)
                lose_screenroot.grab_set()
                lose_screenroot.config(bg='black')
                screen_width = lose_screenroot.winfo_screenwidth()
                screen_height = lose_screenroot.winfo_screenheight()
                window_width = 600
                window_height = 500
                x = (screen_width/2) - (window_width/2)
                y = (screen_height/2) - (window_height/2)
                lose_screenroot.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
                lose_screenroot.title('Wrong!')
                img = PhotoImage(file='Kbc/center.png')
                imgLabel = Label(lose_screenroot, image=img, bd=0)
                imgLabel.pack(pady=30)
                loselabel = Label(lose_screenroot, text='Wrong Answer!!', font=('arial', 40, 'bold'), bg='black', fg='white')
                loselabel.pack(pady=3)
                loselabel1 = Label(lose_screenroot, text='Ask The Stall Respresentative for your prize!', font=('arial', 9, 'bold'), bg='black', fg='white')
                loselabel1.pack()
                sadimage = PhotoImage(file='Kbc/sad.png')
                sadlabel = Label(lose_screenroot, image=sadimage, bg='black')
                sadlabel.place(x=510, y=300)
                sadlabel1 = Label(lose_screenroot, image=sadimage, bg='black')
                sadlabel1.place(x=20, y=300)

                tryagainButton = Button(lose_screenroot, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                        , activebackground='black', cursor='hand2', activeforeground='white',
                                        command=tryagain)
                tryagainButton.pack()

                closeButton = Button(lose_screenroot, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=on_closing)
                closeButton.pack()

                lose_screenroot.protocol('WM_DELETE_WINDOW', on_closing)

                lose_screenroot.mainloop()

                break



    def lifeline50():

        def lifeline50_initiate():
            lifeline50Button.config(image=image50x)
            lifeline50Button.config(state=DISABLED)
            ll50_screenroot.destroy()

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



        
        ll50_screenroot = Toplevel()
        ll50_screenroot.overrideredirect(True)
        ll50_screenroot.grab_set()
        ll50_screenroot.config(bg='black')
        ll50_screenroot.after(2000,lifeline50_initiate)
        screen_width = ll50_screenroot.winfo_screenwidth()
        screen_height = ll50_screenroot.winfo_screenheight()
        window_width = 100
        window_height = 50
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)
        ll50_screenroot.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        ll50_screenroot.title('Lifeline')
        ll50label = Label(ll50_screenroot, text='initiating.', font=('arial', 12), bg='black', fg='white')
        ll50label.pack(pady=3)
        time.sleep(1)
        ll50label.config(text='Done!')


    def phoneLifeLine():


        def okaypress():
            phonelifeline_root.destroy()
            phoneLifelineButton.config(image=phoneImageX, state=DISABLED)

        
        phonelifeline_root = Toplevel()
        phonelifeline_root.overrideredirect(True)
        phonelifeline_root.grab_set()
        phonelifeline_root.config(bg='black')
        screen_width = phonelifeline_root.winfo_screenwidth()
        screen_height = phonelifeline_root.winfo_screenheight()
        window_width = 300
        window_height = 250
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)
        phonelifeline_root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        phonelifeline_root.resizable()
        phonelifeline_root.title('Ask Your Friend !')
        callingimage = PhotoImage(file='Kbc/phoneAFriend.png')
        callinglabel = Label(phonelifeline_root, image=callingimage, bg='black')
        callinglabel.pack(pady=10)
        phonelabel = Label(phonelifeline_root, text='Ask Your Friend!', font=('arial', 20, 'bold'), bg='black', fg='white')
        phonelabel.pack(pady= 5)
        phonelabel1 = Label(phonelifeline_root, text='Ask your Friend or Family Member to Help you Answer the Question', font=('arial', 6, 'bold'), bg='black', fg='white')
        phonelabel1.pack(pady= 10 )
        okbutton = Button(phonelifeline_root, text='OK', font=('arial', 20, 'bold'), bg='black', fg='white', bd=0
                                    , activebackground='black', cursor='hand2', activeforeground='white',
                                    command=okaypress)
        okbutton.pack(pady=5)
        phonelifeline_root.mainloop()
        


    def audiencePoleLifeline():

        def audiencepoleLifeline_initiate():
            ll_screenroot.destroy()
            audiencePoleButton.config(image=audiencePolex)
            audiencePoleButton.config(state=DISABLED)

            progressbarA.place(x=600, y=190)
            progressbarLabelA.place(x=600, y=320)

            progressbarB.place(x=640, y=190)
            progressbarLabelB.place(x=640, y=320)

            progressbarC.place(x=680, y=190)
            progressbarLabelC.place(x=680, y=320)

            progressbarD.place(x=720, y=190)
            progressbarLabelD.place(x=720, y=320)

            if questionArea.get(1.0, 'end-1c') == questions[0]: #Question 1 Poll
                progressbarA.config(value=30)

                progressbarB.config(value=60)

                progressbarC.config(value=40)

                progressbarD.config(value=90)

            if questionArea.get(1.0, 'end-1c') == questions[1]: #Question 2 Poll
                progressbarA.config(value=30)

                progressbarB.config(value=50)

                progressbarC.config(value=40)

                progressbarD.config(value=80)

            if questionArea.get(1.0, 'end-1c') == questions[2]: #Question 3 Poll 
                progressbarA.config(value=70)

                progressbarB.config(value=60)

                progressbarC.config(value=50)

                progressbarD.config(value=90)

            if questionArea.get(1.0, 'end-1c') == questions[3]:
                progressbarA.config(value=90)

                progressbarB.config(value=70)

                progressbarC.config(value=30)

                progressbarD.config(value=50)

            if questionArea.get(1.0, 'end-1c') == questions[4]:
                progressbarA.config(value=80)

                progressbarB.config(value=20)

                progressbarC.config(value=40)

                progressbarD.config(value=30)

            if questionArea.get(1.0, 'end-1c') == questions[5]:
                progressbarA.config(value=40)

                progressbarB.config(value=10)

                progressbarC.config(value=80)

                progressbarD.config(value=30)

            if questionArea.get(1.0, 'end-1c') == questions[6]: #Done 
                progressbarA.config(value=30)

                progressbarB.config(value=80)

                progressbarC.config(value=20)

                progressbarD.config(value=40)

            if questionArea.get(1.0, 'end-1c') == questions[7]:
                progressbarA.config(value=10)

                progressbarB.config(value=20)

                progressbarC.config(value=70)

                progressbarD.config(value=30)

            if questionArea.get(1.0, 'end-1c') == questions[8]:
                progressbarA.config(value=20)

                progressbarB.config(value=85)

                progressbarC.config(value=70)

                progressbarD.config(value=90)

            if questionArea.get(1.0, 'end-1c') == questions[9]:
                progressbarA.config(value=30)

                progressbarB.config(value=70)

                progressbarC.config(value=50)

                progressbarD.config(value=60)

            if questionArea.get(1.0, 'end-1c') == questions[10]:
                progressbarA.config(value=40)

                progressbarB.config(value=20)

                progressbarC.config(value=70)

                progressbarD.config(value=50)

            if questionArea.get(1.0, 'end-1c') == questions[11]:
                progressbarA.config(value=30)

                progressbarB.config(value=90)

                progressbarC.config(value=70)

                progressbarD.config(value=40)

            if questionArea.get(1.0, 'end-1c') == questions[12]:
                progressbarA.config(value=20)

                progressbarB.config(value=60)

                progressbarC.config(value=100)

                progressbarD.config(value=10)

            if questionArea.get(1.0, 'end-1c') == questions[13]:
                progressbarA.config(value=100)

                progressbarB.config(value=35)

                progressbarC.config(value=40)

                progressbarD.config(value=80)

            if questionArea.get(1.0, 'end-1c') == questions[14]:
                progressbarA.config(value=60)

                progressbarB.config(value=115)

                progressbarC.config(value=90)

                progressbarD.config(value=80)


#Root Initiation!!!
        ll_screenroot = Toplevel()
        ll_screenroot.overrideredirect(True)
        ll_screenroot.grab_set()
        ll_screenroot.config(bg='black')
        ll_screenroot.after(2000,audiencepoleLifeline_initiate)
        screen_width = ll_screenroot.winfo_screenwidth()
        screen_height = ll_screenroot.winfo_screenheight()
        window_width = 100
        window_height = 50
        x = (screen_width/2) - (window_width/2)
        y = (screen_height/2) - (window_height/2)
        ll_screenroot.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        ll_screenroot.title('Lifeline')
        ll50label = Label(ll_screenroot, text='initiating.', font=('arial', 12), bg='black', fg='white')
        ll50label.pack(pady=3)
        time.sleep(1)
        ll50label.config(text='Done!')


        

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



    start_root.destroy()

    main_root = Tk()
    screen_width = main_root.winfo_screenwidth()
    screen_height = main_root.winfo_screenheight()
    window_width = 1270
    window_height = 652
    x = (screen_width/2) - (window_width/2)
    y = (screen_height/2) - (window_height/2)
    main_root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
    main_root.resizable(0, 0)
    main_root.title('Millionaire Game')
    main_root.config(bg='black')

    leftFrame = Frame(main_root, bg='black', padx=90)
    leftFrame.grid(row=0, column=0)

    rightFrame = Frame(main_root, bg='black', padx=50, pady=25)
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
    callButton = Button(main_root, bg='black', bd=0, activebackground='black', cursor='hand2', command=phoneclick)
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

    optionButton1 = Button(bottomFrame,wraplength=140, text=first_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                                cursor='hand2',bd=0,activebackground='black',activeforeground='white')
    optionButton1.place(x=100,y=105)

    labelB = Label(bottomFrame, font=('arial', 16, 'bold'), text='B:', bg='black', fg='white')
    labelB.place(x=330,y=110)

    optionButton2 = Button(bottomFrame,wraplength=140, text=second_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                                cursor='hand2',bd=0,activebackground='black',activeforeground='white')
    optionButton2.place(x=370,y=105)

    labelC = Label(bottomFrame, font=('arial', 16, 'bold'), text='C:', bg='black', fg='white')
    labelC.place(x=60,y=190)

    optionButton3 = Button(bottomFrame,wraplength=140,text=third_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                                cursor='hand2',bd=0,activebackground='black',activeforeground='white')
    optionButton3.place(x=100,y=185)

    labelD = Label(bottomFrame, font=('arial', 16, 'bold'), text='D:', bg='black', fg='white')
    labelD.place(x=330,y=190)

    optionButton4 = Button(bottomFrame,wraplength=140, text=fourth_option[0], font=('arial', 16, 'bold'),height=1, bg='black', fg='white',
                                cursor='hand2',bd=0,activebackground='black',activeforeground='white')
    optionButton4.place(x=370,y=185)

    progressbarA = Progressbar(main_root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelA = Label(main_root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarB = Progressbar(main_root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelB = Label(main_root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarC = Progressbar(main_root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelC = Label(main_root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')

    progressbarD = Progressbar(main_root, orient=VERTICAL, mode='determinate', length=120)

    progressbarLabelD = Label(main_root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

    optionButton1.bind('<Button-1>', select)
    optionButton2.bind('<Button-1>', select)
    optionButton3.bind('<Button-1>', select)
    optionButton4.bind('<Button-1>', select)

    main_root.mainloop()

    


start_root = Tk()
start_root.resizable(0, 0)
start_root.title('Millionaire Game')
screen_width = start_root.winfo_screenwidth()
screen_height = start_root.winfo_screenheight()
window_width = 635
window_height = 326
x = (screen_width/2) - (window_width/2)
y = (screen_height/2) - (window_height/2)
start_root.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
start_root.config(bg='black')
centerimg = PhotoImage(file='Kbc/center.png')
imgLabel = Label(start_root, image=centerimg, bd=0, )
imgLabel.pack(pady=30)
startbutton = Button(start_root, text='Start', font=('arial', 20, 'bold'), bg='black', fg='white',bd=0
                                            , activebackground='black', cursor='hand2', activeforeground='white',command=startgame)
startbutton.pack()
start_root.mainloop()