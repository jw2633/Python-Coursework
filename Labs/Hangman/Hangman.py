from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.playerNum = StringVar()
        self.playerNum.set(None)
        self.rb1 = Radiobutton(self,text="1 Player", variable = self.playerNum, value = "one")
        self.rb1.grid(row = 0, column = 0, sticky = W)
        self.rb2 = Radiobutton(self,text="2 Players", variable = self.playerNum, value = "two")
        self.rb2.grid(row = 0, column = 1, sticky = W)
        self.easy = BooleanVar()
        self.hard = BooleanVar()
        self.chk_easy = Checkbutton(self, text = "easy", variable = self.easy)
        self.chk_easy.grid(row = 1, column = 0, sticky = W)
        self.chk_hard = Checkbutton(self, text = "hard", variable = self.hard)
        self.chk_hard.grid(row = 1, column = 1, sticky = W)
        self.startBttn = Button(self, text = "Let's Play")
        self.startBttn.grid(row = 1, column = 2, sticky = W)

    def game_starts(self):
        """Chooses word from easy, hard,
    for combined files, places elements for game play"""
        try:
            if self.end:
                self.end.grid_remove()
                self.blanks.grid_remove()
        except:
            pass
        self.word_select()
        self.Lbl1 = Label(self,text = "Guess this word: ").grid(row = 2, column = 0, sticky = W)
        self.blanks = "-"*len(self.word)
        self.blanksLb1 = Label(self, text = self.blanks)
        self.blanksLb1.grid(row = 2, column = 1, sticky = W)
        self.Lbl2 = Label(self, text = "Letters left to guess: ").grid(row = 3, column = 0, sticky = W)
        self.alpha = 'abcdefghijklmnopqrstuvwxyz'
        self.alphaLbl = Label(self, text = self.alpha)
        self.alphaLbl.grid(row = 3, column = 1, sticky = W)
        self.text = Entry(self, width = 3)
        self.text.grid(row = 4, column = 1, sticky = W)
        self.hangPic = PhotoImage(file = "hangman-images/hangman-0.gif")
        self.pic=Label(self, image = self.hangPic)
        self.pic.grid(row = 5, column = 1, sticky = W)
        Label(self, text = "Guesses left: ").grid(row = 6, column = 0, sticky = W)
        self.guessCt = Label(self, text = "10")
        self.guessCt.grid(row = 6, column = 1, sticky = W)
        self.text.bind('<KeyPress>',self.word_guess)
        self.text.focus_set()

    def word_guess(self, event):
        guess = event.keysym
        if guess.lower() in self.alpha:
            self.alpha = self.alpha.replace(guess.lower()," ")
            self.alphaLbl["text"] = self.alpha
            newBlanks = ""
            for letter in self.word:
                if guess.lower() == letter:
                    newBlanks+=letter
                elif letter in self.alpha:
                    newBlanks+="-"
                else:
                    newBlanks+=letter
            if newBlanks == self.blanks:
                self.guessCt['text'] = str(int(self.guessCt['text'])-1)
                self.hangPic['file'] = self.hangPic['file'][:-5]+str(10-int(self.guessCt['text']))+".gif"
                self.pic['image'] = self.hangPic
            self.blanks = newBlanks
            self.blanksLbl['text'] = self.blanks
        self.text.delete(0,END)

        if self.guessCt['text'] == '0':
            self.end = Label(self,text = "YOU LOSE")
            self.end.grid(row = 7,column = 1)
            self.text.grid_remove()
        elif "-" not in self.blanks:
            self.end = Label(self,text = "YOU WIN")
            self.end.grid(row = 7,column = 1)
            self.text.grid_remove()

    def word_select(self):
        wordList = []
        if self.easy.get():
            easyFile=open("easy_words.txt",'r')
            wordList.extend(easyFile.readlines())
            easyFile.close()
        if self.hard.get():
            hardFile = open("hard_words.txt",'r')
            wordList.extend(hardFile.readlines())
            hardFile.close()
        self.word = (random.choice(wordList).strip())
        print(self.word)

# main
root = Tk()
root.title("Hangman")
root.geometry("400x350")

app = Application(root)
root.mainloop()
        
