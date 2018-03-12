from tkinter import *
import random

class RPSGame(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Rock, Paper, Scissors")
        self.grid()
        self._welcome = Label(self, text ="Welcome to the Rock, Paper, Scissors Game!", fg = "purple")
        self._welcome.grid(row = 0, column = 1 )
        self._welcome = Label(self, text ="Player")
        self._welcome.grid(row = 1, column = 0 )
        self._welcome = Label(self, text ="Computer")
        self._welcome.grid(row = 1, column = 6 )
        self._playerImg = PhotoImage(file = 'question.png')
        self._compImg = PhotoImage(file = 'question.png')
        self._choiceImgLabP = Label(self, image = self._playerImg)
        self._choiceImgLabP.grid(row = 2, column = 0, rowspan = 3)
        self._choiceImgLabC = Label(self, image = self._compImg)
        self._choiceImgLabC.grid(row = 2, column = 6, rowspan = 3)
        self._textLabelP = Label(self, text = "")
        self._textLabelP.grid(row = 5, column = 0, columnspan = 1)
        self._textLabelC = Label(self, text = "")
        self._textLabelC.grid(row = 5, column = 5, columnspan = 2)
        self._winnerLabel = Label(self, text = "")
        self._winnerLabel.grid(row = 6, column = 1 )

        #buttons
        self._rockButton = Button(self, text = "Rock", command = self._choiceRock )
        self._rockButton.grid(row = 2, column = 1)
        self._paperButton = Button(self, text = "Paper", command = self._choicePaper)
        self._paperButton.grid(row = 3, column = 1)
        self._scissorsButton = Button(self, text = "Scissors", command = self._choiceScissors)
        self._scissorsButton.grid(row = 4, column = 1)

    def _computerGuess(self):
        # gets random choice from computer img 
        self._computerImgFile = random.choice(['rock.png', 'paper.png', 'scissors.png'])
        self._compImg = PhotoImage(file = self._computerImgFile )
        self._choiceImgLabC["image"] = self._compImg
        if self._computerImgFile == 'rock.png':
            self._textLabelC["text"] = "Rock"
        elif self._computerImgFile == 'paper.png':
            self._textLabelC["text"] = "Paper"
        else : 
            self._textLabelC["text"] = "Scissors"
        
        # Changes the image and plays the game on click 
    def _choiceRock(self):
        self._computerGuess()
        self._playerImg = PhotoImage(file = 'rock.png')
        self._choiceImgLabP["image"] = self._playerImg
        self._textLabelP["text"] = "Rock"
        if self._computerImgFile == 'paper.png': 
            self._winnerLabel["text"] = "YOU LOOSE!"
            self._winnerLabel["fg"] = "red"
        elif self._computerImgFile == 'scissors.png':
            self._winnerLabel["text"] = "YOU WIN!"
            self._winnerLabel["fg"] = "green"
        else: 
            self._winnerLabel["text"] = "ITS A TIE!"
            self._winnerLabel["fg"] = "blue"

    def _choicePaper(self):
        self._computerGuess()
        self._playerImg = PhotoImage(file = 'paper.png')
        self._choiceImgLabP["image"] = self._playerImg
        self._textLabelP["text"] = "Paper"
        if self._computerImgFile == 'scissors.png': 
            self._winnerLabel["text"] = "YOU LOOSE!"
            self._winnerLabel["fg"] = "red"
        elif self._computerImgFile == 'rock.png':
            self._winnerLabel["text"] = "YOU WIN!"
            self._winnerLabel["fg"] = "green"
        else: 
            self._winnerLabel["text"] = "ITS A TIE!"
            self._winnerLabel["fg"] = "blue"

    def _choiceScissors(self):
        self._computerGuess()
        self._playerImg = PhotoImage(file = 'scissors.png')
        self._choiceImgLabP["image"] = self._playerImg
        self._textLabelP["text"] = "Scissors"
        if self._computerImgFile == 'paper.png': 
            self._winnerLabel["text"] = "YOU WIN!"
            self._winnerLabel["fg"] = "green"
        elif self._computerImgFile == 'rock.png':
            self._winnerLabel["text"] = "YOU LOOSE!"
            self._winnerLabel["fg"] = "red"
        else: 
            self._winnerLabel["text"] = "ITS A TIE!"
            self._winnerLabel["fg"] = "blue"

def main():
    RPSGame().mainloop()

main()