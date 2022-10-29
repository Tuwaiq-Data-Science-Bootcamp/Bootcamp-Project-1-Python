import random
from tkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk

attempt_counter=0
correct_guesses=0
Stopping_Condition=0
root = Tk()


ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
w = 1280 # width for the Tk root
h = 720 # height for the Tk root

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title('HANG MAN')
root.config(bg = '#25e6f4')
root.resizable(False, False)
root.overrideredirect(True)


def ElementIsAllowed(value,Allowed_List):
    for character in value:
        flag=False
        for k in Allowed_List:
                if(character.lower()==k.lower()):
                        flag=True   
        if(flag==False): 
                return False
    return True

def hangman_setup(stage,canvas):
        tk_img = ImageTk.PhotoImage(file = "H" + str(stage) + ".png")
        canvas.image=tk_img  
        canvas.create_image(225, 225, image=tk_img) 
        
        
        
def compare_numbers(letter,input,k):
        return letter.lower()==input[k].lower()
        

def returntostart(game_window, top):
        top.destroy()
        game_window.destroy()


        
def LetterChecking(letter,button_letter,input, game_window,canvas):
        button_letter["state"]=DISABLED
        match_found=False
        for k in range(0,len(input)):
                if(compare_numbers(letter,input,k)):
                        global correct_guesses
                        if(letter.lower()=="i"):
                                added_letter=Label(game_window,text=letter,bg = "#FFFFFF",font=("arial",40))
                                added_letter.place(x=k*40+40+10,y=480)
                                correct_guesses+=1
                                match_found=True
                        else:
                                added_letter=Label(game_window,text=letter,bg = "#FFFFFF",font=("arial",40))
                                added_letter.place(x=k*40+40,y=480)                       
                                correct_guesses+=1
                                match_found=True  
                        
                        
        if(match_found==False):
                global attempt_counter
                attempt_counter+=1
                hangman_setup(attempt_counter,canvas)
        if(attempt_counter==6):
                top= Toplevel(game_window)
                
                top.grab_set()
                ws = root.winfo_screenwidth() # width of the screen
                hs = root.winfo_screenheight() # height of the screen
                w = 250 # width for the Tk root
                h = 250 # height for the Tk root

                # calculate x and y coordinates for the Tk root window
                x = (ws/2) - (w/2)
                y = (hs/2) - (h/2)
                
                top.geometry('%dx%d+%d+%d' % (w, h, x, y))
                top.title("...")
                top.resizable(False, False)
                top.overrideredirect(True)
                
                Label(top, text= "You failed...", font=("arial",15),).place(x=70,y=0)
                Label(top, text= "The word was: "  , font=("arial",12)).place(x=0,y=40)
                Label(top, text= input, font=("arial",12)).place(x=0,y=80)
                Label(top, text= "What you like to play again or exit?", font=("arial",12)).place(x=0,y=120)
                
                exit_button = Button(top, text="Exit", command=root.destroy)
                exit_button.place(x=218,y=220)
                return_button = Button(top, text="Play Again", command=lambda: returntostart(game_window,top) )
                return_button.place(x=150,y=220)
                top.grab_release()
                
        if(correct_guesses==Stopping_Condition):
                top= Toplevel(game_window)
                

                if(attempt_counter>=4):
                        hangman_setup(7,canvas)
                        
                top.grab_set()
                ws = root.winfo_screenwidth() # width of the screen
                hs = root.winfo_screenheight() # height of the screen
                w = 250 # width for the Tk root
                h = 250 # height for the Tk root

                # calculate x and y coordinates for the Tk root window
                x = (ws/2) - (w/2)
                y = (hs/2) - (h/2)
                
                top.geometry('%dx%d+%d+%d' % (w, h, x, y))
                top.title("...")
                top.resizable(False, False)
                top.overrideredirect(True)
                
                Label(top, text= "Congratulations!", font=("arial",15),).place(x=50,y=0)
                Label(top, text= "You guessed correctly "  , font=("arial",12)).place(x=0,y=40)
                Label(top, text= "What you like to play again or exit?", font=("arial",12)).place(x=0,y=80)
                
                exit_button = Button(top, text="Exit", command=root.destroy)
                exit_button.place(x=218,y=220)
                return_button = Button(top, text="Play Again", command=lambda: returntostart(game_window,top) )
                return_button.place(x=150,y=220)
                top.grab_release()
                   
                        
                
  
        
        
       
        
       
def start(given_input):
        
        global Stopping_Condition
        Stopping_Condition=len(given_input)
        
        Allowed = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P,','Q','R','S','T','U','V','W','X','Y','Z',' ')
        if(ElementIsAllowed(given_input,Allowed)==False):
                
            tkinter.messagebox.showinfo("ERROR", "Don't enter numbers or symbols!")   
            return
        if(given_input==''):
                tkinter.messagebox.showinfo("ERROR", "Don't leave the box empty")  
                return
        if(len(given_input)<3 or len(given_input)>24):
                tkinter.messagebox.showinfo("ERROR","Enter a word that is at between 3 and 24 letters")
                return
        global attempt_counter
        attempt_counter=0
        
        global correct_guesses
        correct_guesses=0
        
        game_window = Toplevel(root)
        game_window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        game_window.title('HANG MAN')
        game_window.config(bg = '#FFFFFF')
        game_window.resizable(False, False)
        game_window.overrideredirect(True)
        """
        my_img=PhotoImage(file="H1.png")
        bg_label=Label(game_window,bg="#E7FFFF",image= my_img)
        bg_label.image=my_img
        bg_label.place(x =0,y =0)
        """
        canvas = Canvas(game_window, width=450, height=450,bg = '#FFFFFF')
        canvas.place(x=300,y=0)
        
              
        exit_button = Button(game_window, text="Exit", command=root.destroy)
        exit_button.place(x=0,y=0)
        
        back_button = Button(game_window, text="back", command=game_window.destroy)
        back_button.place(x=30,y=0)
        
        #Set up underscores
        underscore_pos=0
        for i in range(0,len(given_input)):
                
                if(given_input[i]== " "):
                       
                       Stopping_Condition-=1
                       underscore_pos+=40
                       continue
               
                underscore_pos+=40
                underscore=Label(game_window,text="_",bg = "#FFFFFF",font=("arial",40))
                underscore.place(x=underscore_pos,y=500)
                
        #Set up hang man image
        hangman_setup(0,canvas)
        
        #Set up letters
        Button_A = Button(game_window, text="A",command=lambda: LetterChecking("A",Button_A,given_input,game_window,canvas),font=("arial",20)); Button_A.place(x=900,y=10)
        Button_B = Button(game_window, text="B",command=lambda: LetterChecking("B",Button_B,given_input,game_window,canvas),font=("arial",20)); Button_B.place(x=960,y=10)
        Button_C = Button(game_window, text="C",command=lambda: LetterChecking("C",Button_C,given_input,game_window,canvas),font=("arial",20)); Button_C.place(x=1020,y=10)
        Button_D = Button(game_window, text="D",command=lambda: LetterChecking("D",Button_D,given_input,game_window,canvas),font=("arial",20)); Button_D.place(x=1080,y=10)
        Button_E = Button(game_window, text="E",command=lambda: LetterChecking("E",Button_E,given_input,game_window,canvas),font=("arial",20)); Button_E.place(x=1140,y=10)
        Button_F = Button(game_window, text="F",command=lambda: LetterChecking("F",Button_F,given_input,game_window,canvas),font=("arial",20)); Button_F.place(x=1200,y=10)
        
        Button_G = Button(game_window, text="G",command=lambda: LetterChecking("G",Button_G,given_input,game_window,canvas),font=("arial",20)); Button_G.place(x=900,y=70)
        Button_H = Button(game_window, text="H",command=lambda: LetterChecking("H",Button_H,given_input,game_window,canvas),font=("arial",20)); Button_H.place(x=960,y=70)
        Button_I = Button(game_window, text="I",command=lambda: LetterChecking("I",Button_I,given_input,game_window,canvas),font=("arial",20)); Button_I.place(x=1020,y=70)
        Button_J = Button(game_window, text="J",command=lambda: LetterChecking("J",Button_J,given_input,game_window,canvas),font=("arial",20)); Button_J.place(x=1080,y=70)
        Button_K = Button(game_window, text="K",command=lambda: LetterChecking("K",Button_K,given_input,game_window,canvas),font=("arial",20)); Button_K.place(x=1140,y=70)
        Button_L = Button(game_window, text="L",command=lambda: LetterChecking("L",Button_L,given_input,game_window,canvas),font=("arial",20)); Button_L.place(x=1200,y=70)
        
        Button_M = Button(game_window, text="M",command=lambda: LetterChecking("M",Button_M,given_input,game_window,canvas),font=("arial",20)); Button_M.place(x=900,y=130)
        Button_N = Button(game_window, text="N",command=lambda: LetterChecking("N",Button_N,given_input,game_window,canvas),font=("arial",20)); Button_N.place(x=960,y=130)
        Button_O = Button(game_window, text="O",command=lambda: LetterChecking("O",Button_O,given_input,game_window,canvas),font=("arial",20)); Button_O.place(x=1020,y=130)
        Button_P = Button(game_window, text="P",command=lambda: LetterChecking("P",Button_P,given_input,game_window,canvas),font=("arial",20)); Button_P.place(x=1080,y=130)
        Button_Q = Button(game_window, text="Q",command=lambda: LetterChecking("Q",Button_Q,given_input,game_window,canvas),font=("arial",20)); Button_Q.place(x=1140,y=130)
        Button_R = Button(game_window, text="R",command=lambda: LetterChecking("R",Button_R,given_input,game_window,canvas),font=("arial",20)); Button_R.place(x=1200,y=130)
        
        Button_S = Button(game_window, text="S",command=lambda: LetterChecking("S",Button_S,given_input,game_window,canvas),font=("arial",20)); Button_S.place(x=900,y=190)
        Button_T = Button(game_window, text="T",command=lambda: LetterChecking("T",Button_T,given_input,game_window,canvas),font=("arial",20)); Button_T.place(x=960,y=190)
        Button_U = Button(game_window, text="U",command=lambda: LetterChecking("U",Button_U,given_input,game_window,canvas),font=("arial",20)); Button_U.place(x=1020,y=190)
        Button_V = Button(game_window, text="V",command=lambda: LetterChecking("V",Button_V,given_input,game_window,canvas),font=("arial",20)); Button_V.place(x=1080,y=190)
        Button_W = Button(game_window, text="W",command=lambda: LetterChecking("W",Button_W,given_input,game_window,canvas),font=("arial",20)); Button_W.place(x=1140,y=190)
        Button_X = Button(game_window, text="X",command=lambda: LetterChecking("X",Button_X,given_input,game_window,canvas),font=("arial",20)); Button_X.place(x=1200,y=190)
        
        Button_Y = Button(game_window, text="Y",command=lambda: LetterChecking("Y",Button_Y,given_input,game_window,canvas),font=("arial",20)); Button_Y.place(x=900,y=250)
        Button_Z = Button(game_window, text="Z",command=lambda: LetterChecking("Z",Button_Z,given_input,game_window,canvas),font=("arial",20)); Button_Z.place(x=960,y=250)

       

        


        
        

 

welcome_text = Label(root,text = "Welcome to Hangman!",bg = "#25e6f4",font = ("Helvetica",50))
welcome_text.place(x = 300,y = 300)

enter_word = Label(root,text = "Input the string that will be guessed (Space included): ",bg = "#25e6f4",font = ("Helvetica",20))
enter_word.place(x = 200,y = 500)

entry = Entry(fg="black", bg="white", width=20, show="*")
entry.place(x=860, y=510)

begin=tkinter.Button(root, text="Begin", font = ("Helvetica",30), command= lambda: start(entry.get()))
begin.place(x=570, y=600)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.place(x=0, y=0)





     
root.mainloop()