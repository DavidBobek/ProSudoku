from hashlib import new
from tkinter import *

from sudoku import Sudoku
from random import *
import time 
from tkinter import messagebox
'''
To do:
    https://pypi.org/project/py-sudoku/

    pip install py-sudoku
'''


root = Tk()
root.geometry("800x800")

puzzle = Sudoku(3).difficulty(0.5)
Unsolved_board = puzzle.board
solvedtitle = puzzle.solve()
solvedboard = solvedtitle.board
entries = []

#first board 

for y in range(9):
    newrow = []
    for x in range(9):
        name = StringVar(root,value=Unsolved_board[y][x])

        myEntry  = Entry(root,width = 8,textvariable =name,justify= "center",font=("Arial", 20, "bold"))
        if myEntry.get() == str(Unsolved_board[y][x]):
            myEntry.config(bg="green",state='readonly',font=("Arial", 20, "bold"),justify= "center")
        myEntry.place(x=100 + x *70, y = 100 + 70* y, width=80, height=80)
        newrow.append(myEntry)
    entries.append(newrow)    

#this function is launched every time the program detects a change
def check(t):

    for y in range(9):
        for x in range(9):
            iteratingvalue = entries[y][x].get()
            resultiteratingvalue = solvedboard[y][x]
           
            try:
                iteratingvalue = int(iteratingvalue)
                if str(iteratingvalue) == str(resultiteratingvalue):
                    entries[y][x].configure(bg="green")
                else:
                    entries[y][x].configure(bg="red")
            except:
                pass

#function is trigerred with a load button that loads a number set from a different file, however the numbers must be written specifically(9 rows ,9 columns)
def loading():
    global seconds
    global minutes
    seconds = 0
    minutes = 0
    timing()
    global solvedboard
    global entries
    Unsolved_board = []
    solvedboard = []
    entries = []
    with open("anothersudoku.txt") as foreignLayout:
        for x in range(9):
            matrixLine = []
            line =foreignLayout.readline()
            for x in line:
                try:
                    matrixLine.append(int(x))
                except:
                    pass
            Unsolved_board.append(matrixLine)
    

    Loaded = Sudoku(3,board=Unsolved_board)
    Unsolved_board = Loaded.board
    solvedLoaded = Sudoku(3,board=Unsolved_board).solve()
    solvedboard = solvedLoaded.board

   
    for y in range(9):
        newrow = []
        for x in range(9):
            name = StringVar(root,value=Unsolved_board[y][x])

            myEntry  = Entry(root,width = 8,textvariable =name,font=("Arial", 20, "bold"), justify='center')
            if myEntry.get() == str(Unsolved_board[y][x]):
                myEntry.config(bg="green",state='readonly',font=("Arial", 20, "bold"), justify='center')
                
            myEntry.place(x=100 + x *70, y = 100 + 70* y, width=80, height=80)
            newrow.append(myEntry)
        entries.append(newrow)
    


# this function displays every number into the entry widgets 
def showsolution():
    for y in range(9):
        for x in range(9):
            name = StringVar(root,value=solvedboard[y][x])

            myEntry  = Entry(root,width = 8,textvariable =name,font=("Arial", 20, "bold"), justify='center')
            if myEntry.get() == str(solvedboard[y][x]):
                myEntry.config(bg="green",state='readonly',font=("Arial", 20, "bold"), justify='center')
            myEntry.place(x=100 + x *70, y = 100 + 70* y, width=80, height=80)
    

#function cleans deletes all of the inputs that user has inputted
def clean():

    global Unsolved_board
    global entries
  
    for y in range(9):
        for x in range(9):
            iteratingvalue = entries[y][x].get()
            resultiteratingvalue = Unsolved_board[y][x]
          
            try:
                iteratingvalue = int(iteratingvalue)
                if str(iteratingvalue) == str(resultiteratingvalue):
                    pass
                else:
                    entries[y][x].configure({'background': 'white'})
                    entries[y][x].delete (0, last = 100)
            except:
                pass

   
    




#makes a completely new sudoku with a difficulty set by the scale
def generateNew():
    
    MsgBx = messagebox.askquestion("askquestion", "Are you sure?")
    if MsgBx == "no":
        return
    else:
        pass
    global solvedboard
    global entries
    global Unsolved_board
    solvedboard = []
    entries = []
    global seconds
    global minutes
    seconds = 0
    minutes = 0
    
    x  = randint(0,150)
    custom_difficulty = custom_difficulty_Scale.get()/100
    newpuzzle = Sudoku(3,seed = (x)).difficulty(custom_difficulty)
    Unsolved_board = newpuzzle.board
    solvedNewPuzzle = newpuzzle.solve()
    solvedboard = solvedNewPuzzle.board

  

    for y in range(9):
        newrow = []
        for x in range(9):
            name = StringVar(root,value=Unsolved_board[y][x])

            myEntry  = Entry(root,width = 8,textvariable =name,font=("Arial", 20, "bold"), justify='center')
            if myEntry.get() == str(Unsolved_board[y][x]):
                myEntry.config(bg="green",state='readonly',font=("Arial", 20, "bold"), justify='center')
            myEntry.place(x=100 + x *70, y = 100 + 70* y, width=80, height=80)
            newrow.append(myEntry)
        entries.append(newrow)    

#provides user a hint (i have not managed to completely get the grasp of this function)   

def getHint():
    global Unsolved_board
    currentvalues = []
    global solvedboard
    global entries
    for row in Unsolved_board:
        for column in row:
            cell = entries[row][column]
            if cell["state"] != "readonly":
                currentvalues.append(entries[row][column].get())
    
    currentvalues[randint(0,len(currentvalues)-1)]
    entries[row][column].insert(index = 0,string =str(solvedboard[row][column]))
    entries[row][column].config({'background': 'white'})

seconds = 0
minutes = 0
stop = 0

#function timing keeps the user informed on how much time has he/she spent on the current sudoku
#function is launched every second with .after(1000,timing)
def timing ():

    global seconds
    global minutes
    
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 5:
        print("over")
    if stop ==0:
        timelabel = Label(root,text = f"{minutes}:{seconds}")
        timelabel.after(1000,timing)

        timelabel.grid(row=1,column=11)
timing ()

#gui stuff

MyButtons = Frame(root, width=600, height=200, bd=0)
MyButtons.grid(row=1, column=0)
load= Button(MyButtons,command=loading,text="LOAD")
load.grid(row =0, column =1)
showsol = Button(MyButtons,command = showsolution,text = "SHOW SOLUTION")
showsol.grid(row =0, column =2)
cleaning = Button(MyButtons,command = clean,text = "CLEAN INPUT")
cleaning.grid(row= 0,column=3)
genNew = Button(MyButtons,command = generateNew,text = "Generate New")
genNew.grid(row= 0,column=4)
hintButton = Button(MyButtons,command = getHint,text = "Get Hint!")
hintButton.grid(row= 0,column = 5)
DifficultyText = Label(MyButtons, text= "Difficulty of Sudoku!")
DifficultyText.grid(row=0,column=8)
custom_difficulty_Scale = Scale(MyButtons, from_=1, to=99, orient=HORIZONTAL)
custom_difficulty_Scale.grid(row= 0,column=9)
TimeDesc = Label(MyButtons, text= "Time")
TimeDesc.grid(row=0,column=10)
custom_difficulty_Scale.set(50)

root.bind("<KeyPress>",check)
root.mainloop()
        
