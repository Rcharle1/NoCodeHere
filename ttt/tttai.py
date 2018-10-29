###
#tttai.py
#Raheem Charles 9/18
#This is a tic tac toe ai game
#The tic object comes from cwoebker at https://cwoebker.com/posts/tic-tac-toe
### 

from tkinter import *
import random

class TGui:
    def __init__(self, master):
        self.master=master
        master.title("Tic Tac Toe")
        self.x=True
        self.o=False
        self.game=True
        self.xwin=False
        self.owin=False
        self.none=False
        self.tie=False
        self.ai=Tic()
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
        
        self.button1.config(width ="7",height="1")
        self.button2.config(width ="7",height="1")
        self.button3.config(width ="7",height="1")
        self.button4.config(width ="7",height="1")
        self.button5.config(width ="7",height="1")
        self.button6.config(width ="7",height="1")
        self.button7.config(width ="7",height="1")
        self.button8.config(width ="7",height="1")
        self.button9.config(width ="7",height="1")
       
        self.button1.grid(row = 1, column = 0)
        self.button2.grid(row = 1, column = 1)
        self.button3.grid(row = 1, column = 2)
        self.button4.grid(row = 2, column = 0)
        self.button5.grid(row = 2, column = 1)
        self.button6.grid(row = 2, column = 2)
        self.button7.grid(row = 3, column = 0)
        self.button8.grid(row = 3, column = 1)
        self.button9.grid(row = 3, column = 2)
        
        self.board=["","","","","","","","",""]
    


    def click(self,num):
        if num==0:
            self.click1()
        if num==1:
            self.click2()
        if num==2:
            self.click3()

        if num==3:
            self.click4()
        if num==4:
            self.click5()
        if num==5:
            self.click6()
        if num==6:
            self.click7()
        if num==7:
            self.click8()
        if num==8:
            self.click9()
    def click1(self):
        if self.x== True and self.board[0] =="" and self.game ==True:
            self.button1.config(text="x")
            self.x=False
            self.o=True
            self.board[0]="x"
           
            self.move+=1
            self.checkwin()
            self.ai.make_move(1, "X")
                 
            computer_move = self.ai.determine("O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)

          
            
            
        elif self.o==True and self.board[0] =="" and self.game ==True:
            self.button1.config(text="o")
            self.o=False
            self.x=True
            self.board[0]="o"
           
           
            self.checkwin()

    def click2(self):
        if self.x== True and self.board[1] =="" and self.game ==True:
            self.button2.config(text="x")
            self.x=False
            self.o=True
            self.board[1]="x"
          
            
            self.move+=1
            self.checkwin()
            self.ai.make_move(2, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
        elif self.o==True and self.board[1] =="" and self.game ==True:
            self.button2.config(text="o")
            self.x=True
            self.o=False
            self.board[1]="o"
         

            self.checkwin()
    def click3(self):
        if self.x== True and self.board[2] =="" and self.game ==True:
            self.button3.config(text="x")
            self.x=False
            self.o=True
            self.board[2]="x"
          
            self.move+=1
            self.checkwin
            self.ai.make_move(3, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
      
            

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
            self.ai.make_move(1, "X")
                 
            computer_move = self.ai.determine("O")
        
            self.ai.make_move(3, "O")
            self.click(computer_move)
        

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
            self.ai.make_move(4, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
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
            self.ai.make_move(5, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
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
            self.ai.make_move(6, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
          
        elif self.o==True and self.board[6] =="" and self.game ==True:
            self.button7.config(text="o")
            self.o=False
            self.x=True
            self.board[6]="o"
            self.move+=1
            self.move+=1
            self.checkwin()
    def click8(self):
        if self.x== True and self.board[7] =="" and self.game ==True:
            self.button8.config(text="x")
            self.x=False
            self.o=True
            self.board[7]="x"
            
            self.move+=1
            self.ai.make_move(7, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)

            
        elif self.o==True and self.board[7] =="" and self.game ==True:
            self.button8.config(text="o")
            self.o=False
            self.x=True
            self.board[7]="o"
            self.move+=1
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
            self.ai.make_move(8, "X")
                 
            computer_move = self.ai.determine( "O")
        
            self.ai.make_move(computer_move, "O")
            self.click(computer_move)
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





class Tic(object):
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6])

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, squares=[]):
        if len(squares) == 0:
            self.squares = [None for i in range(9)]
        else:
            self.squares = squares



    def available_moves(self):
        """what spots are left empty?"""
        return [k for k, v in enumerate(self.squares) if v is None]

    def available_combos(self, player):
        """what combos are available?"""
        return self.available_moves() + self.get_squares(player)

    def show(self):
        for element in [self.squares[i:i + 3] for i in range(0, len(self.squares), 3)]:
            print(element)

    def complete(self):
        """is the game over?"""
        if None not in [v for v in self.squares]:
            return True
        if self.winner() != None:
            return True
        return False

    def X_won(self):
        return self.winner() == 'X'

    def O_won(self):
        return self.winner() == 'O'

    def tied(self):
        return self.complete() == True and self.winner() is None

    def winner(self):
        for player in ('X', 'O'):
            positions = self.get_squares(player)
            for combo in self.winning_combos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player
        return None

    def get_squares(self, player):
        """squares that belong to a player"""
        return [k for k, v in enumerate(self.squares) if v == player]

    def make_move(self, position, player):
        """place on square on the board"""
        self.squares[position] = player

    def alphabeta(self, player, alpha, beta):
        if self.complete():
            if self.X_won():
                return -1
            elif self.tied():
                return 0
            elif self.O_won():
                return 1
        for move in self.available_moves():
            self.make_move(move, player)
            val = self.alphabeta( self.get_enemy(player), alpha, beta)
            self.make_move(move, None)
            if player == 'O':
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta
            else:
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha
        if player == 'O':
            return alpha
        else:
            return beta


    def determine(self,player):
        a = -2
        choices = []
        if len(self.available_moves()) == 9:
            return 4
        for move in self.available_moves():
            self.make_move(move, player)
            val = self.alphabeta(self.get_enemy(player), -2, 2)
            self.make_move(move, None)
            if val > a:
                a = val
                choices = [move]
            elif val == a:
                choices.append(move)
        return random.choice(choices)


    def get_enemy(self, player):
        if player == 'X':
            return 'O'
        return 'X'



def main():
    
    tgui = Tk()
    tgui.geometry("280x150")
    my_gui = TGui(tgui)
    
    tgui.mainloop()
main()


