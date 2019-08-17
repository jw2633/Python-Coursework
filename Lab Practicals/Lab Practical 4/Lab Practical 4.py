from tkinter import *
import random

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.canvas = Canvas(self, height=310, width=500)
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=3, sticky = N)
        
        self.title = Label(self, text="Roman Numeral Canvas")
        self.title.grid(row=0, column=0, columnspan = 4)

        self.num_lbl = Label(self, text="Number:")
        self.num_lbl.grid(row = 1, column = 2)

        self.number = Entry(self, width=20)
        self.number.grid(row = 1, column = 3)

        #self.numbers = BooleanVar()
        #self.numbers(False)
        #self.chkbttn = checkbutton(self,text="Numbers",variable = self.numbers)
        #self.chkbttn.grid(row=1,column=4)

        self.color_lbl = Label(self, text="Line Width:")
        self.color_lbl.grid(row = 2, column = 2)

        self.linWid = StringVar()
        self.linWid.set("1")
        self.rb1 = Radiobutton(self,text='1',variable = self.linWid,value='1')
        self.rb1.grid(row=2,column=3)
        self.rb3 = Radiobutton(self,text='3',variable = self.linWid,value='3')
        self.rb3.grid(row=2,column=4)
        self.rb5 = Radiobutton(self,text='5',variable = self.linWid,value='5')
        self.rb5.grid(row=2,column=5)

        self.length_lbl = Label(self, text="Line Color:")
        self.length_lbl.grid(row = 3, column = 2)

        self.clr = StringVar()
        self.clr.set("Black")
        self.rbblk = Radiobutton(self,text='Black',variable = self.clr,value='Black')
        self.rbblk.grid(row=3,column=3)
        self.rbrd = Radiobutton(self,text='Red',variable = self.clr,value='Red')
        self.rbrd.grid(row=3,column=4)
        self.rbblu = Radiobutton(self,text='Blue',variable = self.clr,value='Blue')
        self.rbblu.grid(row=3,column=5)

        self.roman = PhotoImage(file='roman.gif')
        self.romanBttn = Button(self,image = self.roman)
        self.romanBttn.grid(row = 4, rowspan = 3, column = 3, sticky = W )

        self.random = PhotoImage(file='random.gif')
        self.randomBttn = Button(self,image=self.random)
        self.randomBttn.grid(row=4 , rowspan=3 , column=4 , sticky = W)

        self.x, self.y = 20, 20



    def draw_M(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x+5, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x+14, self.y, self.x+19, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x+3, self.y, self.x+9, self.y+10, width=linWid, fill=color)
        self.canvas.create_line(self.x+9, self.y+9, self.x+16, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x+3, self.y, self.x+3, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+17, self.y, self.x+17, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+5, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+15, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.x += 20 + 10

    def draw_D(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y, self.x+10, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+10, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+10, self.y, self.x+20, self.y+10, width=linWid, fill=color)
        self.canvas.create_line(self.x+19, self.y + 40, self.x+20, self.y+30, width=linWid, fill=color)
        self.canvas.create_line(self.x+20, self.y + 10, self.x+20, self.y+30, width=linWid, fill=color)
        self.x += 20 + 10

    def draw_C(self, linWid, color):
        self.canvas.create_line(self.x, self.y+10, self.x, self.y+30, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+10, self.x+10, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+30, self.x+10, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+10, self.y, self.x+20, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x+10, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.x += 20 + 10

    
    def draw_L(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x+5, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x+3, self.y, self.x+3, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.x += 20 + 10

    def draw_X(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+5, self.y, self.x+15, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+15, self.y, self.x+5, self.y+40, width=linWid, fill=color)
        self.x += 20 + 10

    def draw_V(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+5, self.y, self.x+10, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+10, self.y+40, self.x+15, self.y, width=linWid, fill=color)
        self.x += 20 + 10

    def draw_I(self, linWid, color):
        self.canvas.create_line(self.x, self.y, self.x+20, self.y, width=linWid, fill=color)
        self.canvas.create_line(self.x, self.y+40, self.x+20, self.y+40, width=linWid, fill=color)
        self.canvas.create_line(self.x+10, self.y, self.x+10, self.y+40, width=linWid, fill=color)
        self.x += 20 + 10


    
    for letter in self.number:
        M = draw_M
        D = draw_D
        C = draw_C
        L = draw_L
        X = draw_X
        V = draw_V
        I = draw_I

    return letter



    
        
# main
root = Tk()
root.title("Roman Numerals")
root.geometry("900x350")

app = Application(root)
root.mainloop()
