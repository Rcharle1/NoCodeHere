####
#Tic Tac Toe Ai Game
#Raheem Charles 9/18
####

from tkinter import *


class TGui:
    def __init__(self, master):
        self.master=master
        master.title("Tic Tac Toe")
        self.x=True
        self.o=False
        self.game=True
        self.move=0
        self.button1=Button(master, text="", command=self.click1)
        self.button2=Button(master, text="", command=self.click2)
        self.button3=Button(master, text="", command=self.click3)
        self.button4=Button(master, text="", command=self.click4)
        self.button5=Button(master, text="", command=self.click5)
        self.button6=Button(master, text="", command=self.click6)
        self.button7=Button(master, text="", command=self.click7)
        self.button8=Button(master, text="", command=self.click8)
        self.button9=Button(master, text="", command=self.click9)
        self.button10=Button(master, text="New Game", command=self.clear )
        self.button1.config(width ="7",height="1")
        self.button2.config(width ="7",height="1")
        self.button3.config(width ="7",height="1")
        self.button4.config(width ="7",height="1")
        self.button5.config(width ="7",height="1")
        self.button6.config(width ="7",height="1")
        self.button7.config(width ="7",height="1")
        self.button8.config(width ="7",height="1")
        self.button9.config(width ="7",height="1")
        self.button10.config(width="7",height="1")
        self.button1.grid(row = 1, column = 0)
        self.button2.grid(row = 1, column = 1)
        self.button3.grid(row = 1, column = 2)
        self.button4.grid(row = 2, column = 0)
        self.button5.grid(row = 2, column = 1)
        self.button6.grid(row = 2, column = 2)
        self.button7.grid(row = 3, column = 0)
        self.button8.grid(row = 3, column = 1)
        self.button9.grid(row = 3, column = 2)
        self.button10.grid(row=5, column=1)
        self.board=["","","","","","","","",""]
        self.ai=TicAi(self.board,1,self)

    #def createAi(self):
    #    self.ai=TicAi(self.board,0,self.gui)
    def click1(self):
        if self.x== True and self.board[0] =="" and self.game ==True:
            self.button1.config(text="x")
            self.x=False
            self.o=True
            self.board[0]="x"
            self.move+=1
            self.checkwin()

            self.ai.move()
            
            
        elif self.o==True and self.board[0] =="" and self.game ==True:
            self.button1.config(text="o")
            self.o=False
            self.x=True
            self.board[0]="o"
            self.move+=1
            self.checkwin()

    def click2(self):
        if self.x== True and self.board[1] =="" and self.game ==True:
            self.button2.config(text="x")
            self.x=False
            self.o=True
            self.board[1]="x"
            self.move+=1
            self.ai.move()
            self.checkwin()

        elif self.o==True and self.board[1] =="" and self.game ==True:
            self.button2.config(text="o")
            self.x=True
            self.o=False
            self.board[1]="o"
            self.move+=1
            self.checkwin()
    def click3(self):
        if self.x== True and self.board[2] =="" and self.game ==True:
            self.button3.config(text="x")
            self.x=False
            self.o=True
            self.board[2]="x"
            self.move+=1
            self.checkwin
            self.ai.move()

        elif self.o==True and self.board[2] =="" and self.game ==True:
            self.button3.config(text="o")
            self.o=False
            self.x=True
            self.board[2]="o"
            self.move+=1
            self.checkwin()
    def click4(self):
        if self.x== True and self.board[3] =="" and self.game ==True:
            self.button4.config(text="x")
            self.x=False
            self.o=True
            self.board[3]="x"
            self.move+=1
            self.checkwin()
            self.ai.move()
        

        elif self.o==True and self.board[3] =="" and self.game ==True:
            self.button4.config(text="o")
            self.o=False
            self.x=True
            self.board[3]="o"
            self.move+=1
            self.checkwin()
    def click5(self):
        if self.x== True and self.board[4] =="" and self.game ==True:
            

            self.button5.config(text="x")
            self.x=False
            self.o=True
            self.board[4]="x"
            self.move+=1
            self.checkwin()
            self.ai.move()
        elif self.o==True and self.board[4] =="" and self.game ==True:
            self.button5.config(text="o")
            self.o=False
            self.x=True
            self.board[4]="o"
            self.move+=1
            self.checkwin()
    def click6(self):
        if self.x== True and self.board[5] =="" and self.game ==True:
            self.button6.config(text="x")
            self.x=False
            self.o=True
            self.board[5]="x"
            self.move+=1
            self.checkwin()
            self.ai.move()
        elif self.o==True and self.board[5] =="" and self.game ==True:
            self.button6.config(text="o")
            self.o=False
            self.x=True
            self.board[5]="o"
            self.move+=1
            self.checkwin()
    def click7(self):
        if self.x== True and self.board[6] =="" and self.game ==True:
            self.button7.config(text="x")
            self.x=False
            self.o=True
            self.board[6]="x"
            self.move+=1
            self.checkwin()
            self.ai.move()
        elif self.o==True and self.board[6] =="" and self.game ==True:
            self.button7.config(text="o")
            self.o=False
            self.x=True
            self.board[6]="o"
            self.move+=1
            self.checkwin()
    def click8(self):
        if self.x== True and self.board[7] =="" and self.game ==True:
            self.button8.config(text="x")
            self.x=False
            self.o=True
            self.board[7]="x"
            self.move+=1
            self.checkwin()

            self.ai.move()
        elif self.o==True and self.board[7] =="" and self.game ==True:
            self.button8.config(text="o")
            self.o=False
            self.x=True
            self.board[7]="o"
            self.move+=1
            self.checkwin()
    def click9(self):
        if self.x== True and self.board[8] =="" and self.game ==True:
            self.button9.config(text="x")
            self.x=False
            self.o=True
            self.board[8]="x"
            self.move+=1
            self.checkwin()
            self.ai.move()
        elif self.o==True and self.board[8] =="" and self.game ==True:
            self.button9.config(text="o")
            self.o=False
            self.x=True
            self.board[8]="o"
            self.move+=1
            self.checkwin()
    def checkwin(self):
        if self.board[0] == "x" and self.board[1] == "x" and self.board[2]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[0] == "o" and self.board[1] == "o" and self.board[2]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[3] == "x" and self.board[4] == "x" and self.board[5]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[3] == "o" and self.board[4] == "o" and self.board[5]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[6] == "x" and self.board[7] == "x" and self.board[8]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[6] == "o" and self.board[7] == "o" and self.board[8]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[0] == "x" and self.board[4] == "x" and self.board[8]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[0] == "o" and self.board[4] == "o" and self.board[8]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[0] == "x" and self.board[3] == "x" and self.board[6]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[0] == "o" and self.board[3] == "o" and self.board[6]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[1] == "x" and self.board[4] == "x" and self.board[7]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[1] == "o" and self.board[4] == "o" and self.board[7]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[2] == "x" and self.board[5] == "x" and self.board[8]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[2] == "o" and self.board[5] == "o" and self.board[8]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[2] == "x" and self.board[4] == "x" and self.board[6]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[2] == "o" and self.board[4] == "o" and self.board[6]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.board[3] == "x" and self.board[5] == "x" and self.board[6]=="x":
            self.master.title("Tic Tac Toe - X Won!!")
            self.game=False
        elif self.board[3] == "o" and self.board[5] == "o" and self.board[6]=="o":
            self.master.title("Tic Tac Toe - O Won!!")
            self.game=False
        elif self.move==9:
            self.master.title("Tic Tac Toe - It's a Draw!")
            self.game=False
    def clear(self):
        self.button1.config(text="")
        self.button2.config(text="")
        self.button3.config(text="")
        self.button4.config(text="")
        self.button5.config(text="")
        self.button6.config(text="")
        self.button7.config(text="")
        self.button8.config(text="")
        self.button9.config(text="")
        self.master.title("Tic Tac Toe!!")
        self.board=["","","","","","","","",""]
        self.game=True
        self.moves=0
        self.x=True
        self.o=False




class TicAi:
    def __init__(self,board,lvl,gui):
        self.board=board
        self.lvl=lvl 
        self.gui=gui
       

    def move(self):
        if self.lvl == 1:
            while self.gui.o and self.gui.game:
                #The first moves check to see if the ai can win
                if self.board[0] == "o" and self.board[2]=="o" and self.board[1]=="":

                    self.gui.click2()
                elif self.board[0] == "o" and self.board[1] == "o" and self.board[2]=="":
                    self.gui.click3()

                elif self.board[1] == "o" and self.board[2] =="o" and self.board[0]=="":
                    self.gui.click1()
                elif self.board[0] == "o" and self.board[8]=="o" and self.board[4]=="":
                    self.gui.click5()
                elif self.board[0] == "o" and self.board[4] == "o" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[4] == "o" and self.board[8] == "o" and self.board[0]=="":
                    self.gui.click1()
                elif self.board[2] =="o" and self.board[8] =="o" and self.board[4]=="":
                    self.gui.click5()
                elif self.board[4] == "o" and self.board[8]=="o" and self.board[2] =="":
                    self.gui.click3()
                elif self.board[2] == "o" and self.board[4]=="o" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[3] == "o" and self.board[5]=="o" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[3] == "o" and self.board [4] == "o" and self.board[2] =="":
                    self.gui.click6()
                elif self.board[3] == "o" and self.board[2] == "o" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[2] == "o" and self.board[4] == "o" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[4] == "o" and self.board[5] =="o" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[6] == "o" and self.board[8]=="o" and self.board[7] =="":
                    self.gui.click8()
                elif self.board[7] == "o" and self.board [8] == "o" and self.board[6] =="":
                    self.gui.click7()
                elif self.board[6] == "o" and self.board[7] =="o" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[0] == "o" and self.board[6]=="o" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[0] == "o" and self.board[3] == "o" and self.board[6] =="":
                    self.gui.click7()
                elif self.board[3] == "o" and self.board[6] =="o" and self.board[0] =="":
                    self.gui.click1()
                elif self.board[1] == "o" and self.board[7]=="o" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[1] == "o" and self.board [4] == "o" and self.board[2] =="":
                    self.gui.click8()
                elif self.board[4] == "o" and self.board[7] =="o" and self.board[1] =="":

                    self.gui.click2()
                elif self.board[2] == "o" and self.board[8]=="o" and self.board[5] =="":
                    self.gui.click6()
                elif self.board[2] == "o" and self.board [6] == "o" and self.board[8] =="":
                    
                    self.gui.click9()
                elif self.board[6] == "o" and self.board[8] =="o" and self.board[2] =="":

                    self.gui.click3()
                elif self.board[6] == "o" and self.board[4] =="o" and self.board[2] =="":
                        self.gui.click3()
                elif self.board[2] == "o" and self.board[4] =="o" and self.board[6] =="":
                        self.gui.click7()
                elif self.board[2] == "o" and self.board[6] =="o" and self.board[4] =="":
                        self.gui.click5()

                #These moves block the player from winning
                if self.board[0] == "x" and self.board[2]=="x" and self.board[1]=="":
    
                    self.gui.click2()
                elif self.board[0] == "x" and self.board[1] == "x" and self.board[2]=="":
                    self.gui.click3()

                elif self.board[1] == "x" and self.board[2] =="x" and self.board[0]=="":
                    self.gui.click1()
                elif self.board[0] == "x" and self.board[8]=="x" and self.board[4]=="":
                    self.gui.click5()
                elif self.board[0] == "x" and self.board[4] == "x" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[4] == "x" and self.board[8] == "x" and self.board[0]=="":
                    self.gui.click1()
                elif self.board[2] =="x" and self.board[8] =="x" and self.board[4]=="":
                    self.gui.click5()
                elif self.board[4] == "x" and self.board[8]=="x" and self.board[2] =="":
                    self.gui.click3()
                elif self.board[2] == "x" and self.board[4]=="x" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[3] == "x" and self.board[5]=="x" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[3] == "x" and self.board[4] == "x" and self.board[2] =="":
                    self.gui.click6()
                elif self.board[3] == "x" and self.board[2] == "x" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[2] == "x" and self.board[4] == "x" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[4] == "x" and self.board[5] =="x" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[6] == "x" and self.board[8]=="x" and self.board[7] =="":
                    self.gui.click8()
                elif self.board[7] == "x" and self.board [8] == "x" and self.board[6] =="":
                    self.gui.click7()
                elif self.board[6] == "x" and self.board[7] =="x" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[0] == "x" and self.board[6]=="x" and self.board[3] =="":
                    self.gui.click4()
                elif self.board[0] == "x" and self.board[3] == "x" and self.board[6] =="":
                    self.gui.click7()
                elif self.board[3] == "x" and self.board[6] =="x" and self.board[0] =="":
                    self.gui.click1()
                elif self.board[1] == "x" and self.board[7]=="x" and self.board[4] =="":
                    self.gui.click5()
                elif self.board[1] == "x" and self.board[4] == "x" and self.board[2] =="":
                    self.gui.click8()
                elif self.board[4] == "x" and self.board[7] =="x" and self.board[1] =="":
                    self.gui.click2()
                elif self.board[2] == "x" and self.board[8]=="x" and self.board[5] =="":
                    self.gui.click6()
                elif self.board[2] == "x" and self.board[6] == "x" and self.board[8] =="":
                    self.gui.click9()
                elif self.board[6] == "x" and self.board[8] =="x" and self.board[2] =="":
                    self.gui.click3()
                elif self.board[6] == "x" and self.board[4] =="x" and self.board[2] =="":
                    self.gui.click3()
                elif self.board[2] == "x" and self.board[4] =="x" and self.board[6] =="":
                        self.gui.click7()
                elif self.board[2] == "x" and self.board[6] =="x" and self.board[4] =="":
                        self.gui.click5()
                ## This move puts an o in the center
                elif self.board[4]=="":
                    self.gui.click5()
                ## These moves puts an o in the opposite corner of the users
                elif self.board[0]=="x" and self.board[8] == "":
                    self.gui.click9()
                elif self.board[8]=="x" and self.board[0] == "":
                        self.gui.click1()
                elif self.board[2]=="x" and self.board[6] =="":
                        self.gui.click7()
                elif self.board[6]=="x" and self.board[2] == "":
                    self.gui.click5()
                ##These moves put an o in an empty corner
                elif self.board[0]=="":
                    self.gui.click1()
                elif self.board[2]=="":
                    self.gui.click3()
                elif self.board[6]=="":
                    self.gui.click7()
                elif self.board[8]=="":
                    self.gui.click9()
                ### These moves put an o in an empty middle square
                elif self.board[1]=="":
                    self.gui.click2()
                elif self.board[3]=="":
                    self.gui.click4()
                elif self.board[5]=="":
                    self.gui.click6()
                elif self.board[7]=="":
                    self.gui.click8()
        


def main():
    
    tgui = Tk()
    tgui.geometry("280x150")
    my_gui = TGui(tgui)
    tgui.mainloop()

main()

        



