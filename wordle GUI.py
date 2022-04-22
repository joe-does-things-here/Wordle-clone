"""
Written by: Joe B
last edit: 22/04/2022

A wordle clone using tkinter for graphics!
"""
import tkinter as tk
from tkinter import ttk
import random
import csv 
from os.path import exists
import os 
import sys 
root = tk.Tk() #creates a new window for all tkinter widgets to go inside
root.title("Wordle Clone") #titles it

game = ttk.Frame(root)
utils = ttk.Frame(root)
userInput = tk.StringVar()
row = 0
words = []
Word = ""
#############################
def createCSV():
    try:
        def writeFile(): #defines a function that can be run to ask the user if they are happy to write the newly created list to a CSV file
            proceed = input("Continue? Y/n ") #asks the user if they're happy to proceed  and prompts them to respond with either "Y" or "n"
            if proceed == "Y" or proceed == "y": #if the user is happy to proceed
                alpha = input("Do you wish to sort the list alphabetically? Y/n ") #asks the user if they want to sort the file alphabetically
                if alpha == "Y" or alpha == "y": #if they do
                        words.sort() #sorts the list alphabetically 
                else: #if they don't want to sort alphabetically
                    pass #the code passes onto the next line
                ##############################
                with open('words.csv', 'w', encoding='UTF8') as f: #creates a file called "words.csv" in write mode with the correct text encoding so nothing breaks
                    writer = csv.writer(f) #creates a CSV writer
                    writer.writerow(words) #writes every word into a CSV file
                print("\n"+"CSV file created successfully" +"\n" + "do not close this program, it will close itself automatically") #tells the user the code worked, goes onto a new line and tells the user not to close the program
                print("\n"+"\n")
                time.sleep(2) #waits two second
                os.system('cls') #clears the console
                sys.exit
            elif proceed == "n": #if the user doesn't want to create the file
                print("exiting program")
                time.sleep(2)
                sys.exit
            else: #if the user answers something that isnt "Y" or "n"
                print ("Please respond with ""Y"" if happy to proceed or ""n"" if you are not") #prompts the user to answer again
                writeFile() #runs the function again
        ##############################
        with open('sgb-words.txt') as f: #opens the text file ready to be used inside the program
            myList = [line.rstrip('\n') for line in f] #goes through every item in the text file, adding it to the "myList" array and removing the carridge returns
            print("text file length: " +str(len(myList))) #prints off the length of the list
            for item in myList: 
                words.append(item) #adds the word at index i to the "words" list created earleir
        print("words list length: " + str(len(words))) #prints off the length of the newly created "words" list so the uesr can double check
        writeFile() #runs the function created earlier in the program
    except:
        print("missing file ""sgb-words.txt"" please re-download the missing file from wherever you sourced this code")
#############################
def getWord():
    global Word
    file_exists = exists("words.csv") #double checks that the list of words actually exists
    if file_exists == True: #if it does
        with open("words.csv", mode="r") as csv_file: #the file is opened
            reader = csv.reader(csv_file) 
            for item in reader: #and for every item in the file
                words.extend(item) #the code adds it into an array for the code to use
    else:
        createCSV()
        getWord()
    Word = random.choice(words)
#############################
def scanWord(userWord):    
    global Word,row,textIn
    for i in range(5):
        if userWord == Word: #if the user guesses the word correctly
            if row == 0:
                X0Y0.config(bg="#00ff00")
                X1Y0.config(bg="#00ff00")
                X2Y0.config(bg="#00ff00")
                X3Y0.config(bg="#00ff00")
                X4Y0.config(bg="#00ff00")
            elif row == 1:
                X0Y1.config(bg="#00ff00")
                X1Y1.config(bg="#00ff00")
                X2Y1.config(bg="#00ff00")
                X3Y1.config(bg="#00ff00")
                X4Y1.config(bg="#00ff00")
            elif row == 2:
                X0Y2.config(bg="#00ff00")
                X1Y2.config(bg="#00ff00")
                X2Y2.config(bg="#00ff00")
                X3Y2.config(bg="#00ff00")
                X4Y2.config(bg="#00ff00")
            elif row == 3:
                X0Y3.config(bg="#00ff00")
                X1Y3.config(bg="#00ff00")
                X2Y3.config(bg="#00ff00")
                X3Y3.config(bg="#00ff00")
                X4Y3.config(bg="#00ff00")
            elif row == 4:
                X0Y4.config(bg="#00ff00")
                X1Y4.config(bg="#00ff00")
                X2Y4.config(bg="#00ff00")
                X3Y4.config(bg="#00ff00")
                X4Y4.config(bg="#00ff00")
            elif row == 5:
                X0Y5.config(bg="#00ff00")
                X1Y5.config(bg="#00ff00")
                X2Y5.config(bg="#00ff00")
                X3Y5.config(bg="#00ff00")
                X4Y5.config(bg="#00ff00")
            textIn = ttk.Label(utils, width=5) #replaces textIn with a label so the user can't input anything
            textIn.grid(row=6, column=1,columnspan=3) #places it on the grid
        elif Word[i] == userWord[i]: #if the letter is in the correct place
            if row == 0 and i == 0:
                X0Y0.config(bg="#00ff00")
            elif row == 0 and i == 1:
                X1Y0.config(bg="##00ff00")
            elif row == 0 and i == 2:
                X2Y0.config(bg="##00ff00")
            elif row == 0 and i == 3:
                X3Y0.config(bg="##00ff00")
            elif row == 0 and i == 4:
                X4Y0.config(bg="##00ff00")
            elif row == 1 and i == 0:
                X0Y1.config(bg="#00ff00")
            elif row == 1 and i == 1:
                X1Y1.config(bg="#00ff00")
            elif row == 1 and i == 2:
                X2Y1.config(bg="#00ff00")
            elif row == 1 and i == 3:
                X3Y1.config(bg="#00ff00")
            elif row == 1 and i == 4:
                X4Y1.config(bg="#00ff00")
            elif row == 2 and i == 0:
                X0Y2.config(bg="#00ff00")
            elif row == 2 and i == 1:
                X1Y2.config(bg="#00ff00")
            elif row == 2 and i == 2:
                X2Y2.config(bg="#00ff00")
            elif row == 2 and i == 3:
                X3Y2.config(bg="#00ff00")
            elif row == 2 and i == 4:
                X4Y2.config(bg="#00ff00")
            elif row == 3 and i == 0:
                X0Y3.config(bg="#00ff00")
            elif row == 3 and i == 1:
                X1Y3.config(bg="#00ff00")
            elif row == 3 and i == 2:
                X2Y3.config(bg="#00ff00")
            elif row == 3 and i == 3:
                X3Y3.config(bg="#00ff00")
            elif row == 3 and i == 4:
                X4Y4.config(bg="#00ff00")
            elif row == 4 and i == 0:
                X0Y4.config(bg="00ff00")
            elif row == 4 and i == 1:
                X1Y4.config(bg="#00ff00")
            elif row == 4 and i == 2:
                X2Y4.config(bg="#00ff00")
            elif row == 4 and i == 3:
                X3Y4.config(bg="#00ff00")
            elif row == 4 and i == 4:
                X4Y4.config(bg="#00ff00")
            elif row == 5 and i == 0:
                X0Y5.config(bg="#00ff00")
            elif row == 5 and i == 1:
                X1Y5.config(bg="#00ff00")
            elif row == 5 and i == 2:
                X2Y5.config(bg="#00ff00")
            elif row == 5 and i == 3:
                X3Y5.config(bg="#00ff00")
            elif row == 5 and i == 4:
                X4Y5.config(bg="#00ff00")
        elif userWord[i] in Word: #if the letter is in the final word
            if row == 0 and i == 0:
                X0Y0.config(bg="#FFA500")
            elif row == 0 and i == 1:
                X1Y0.config(bg="#FFA500")
            elif row == 0 and i == 2:
                X2Y0.config(bg="#FFA500")
            elif row == 0 and i == 3:
                X3Y0.config(bg="#FFA500")
            elif row == 0 and i == 4:
                X4Y0.config(bg="#FFA500")
            elif row == 1 and i == 0:
                X0Y1.config(bg="FFA500")
            elif row == 1 and i == 1:
                X1Y1.config(bg="#FFA500")
            elif row == 1 and i == 2:
                X2Y1.config(bg="#FFA500")
            elif row == 1 and i == 3:
                X3Y1.config(bg="#FFA500")
            elif row == 1 and i == 4:
                X4Y1.config(bg="#FFA500")
            elif row == 2 and i == 0:
                X0Y2.config(bg="FFA500")
            elif row == 2 and i == 1:
                X1Y2.config(bg="#FFA500")
            elif row == 2 and i == 2:
                X2Y2.config(bg="#FFA500")
            elif row == 2 and i == 3:
                X3Y2.config(bg="#FFA500")
            elif row == 2 and i == 4:
                X4Y2.config(bg="#FFA500")
            elif row == 3 and i == 0:
                X0Y3.config(bg="FFA500")
            elif row == 3 and i == 1:
                X1Y3.config(bg="#FFA500")
            elif row == 3 and i == 2:
                X2Y3.config(bg="#FFA500")
            elif row == 3 and i == 3:
                X3Y3.config(bg="#FFA500")
            elif row == 3 and i == 4:
                X4Y3.config(bg="#FFA500")
            elif row == 4 and i == 0:
                X0Y4.config(bg="FFA500")
            elif row == 4 and i == 1:
                X1Y4.config(bg="#FFA500")
            elif row == 4 and i == 2:
                X2Y4.config(bg="#FFA500")
            elif row == 4 and i == 3:
                X3Y4.config(bg="#FFA500")
            elif row == 4 and i == 4:
                X4Y4.config(bg="#FFA500")
            elif row == 5 and i == 0:
                X0Y4.config(bg="FFA500")
            elif row == 5 and i == 1:
                X1Y5.config(bg="#FFA500")
            elif row == 5 and i == 2:
                X2Y5.config(bg="#FFA500")
            elif row == 5 and i == 3:
                X3Y5.config(bg="#FFA500")
            elif row == 5 and i == 4:
                X4Y5.config(bg="#FFA500")
        else: #if the letter isn't in the final word
            pass
        root.update()
def displayWord():
    global row
    userWord = userInput.get()
    if row == 0:
        X0Y0.insert(0.0,userWord[0])
        X1Y0.insert(0.0,userWord[1])
        X2Y0.insert(0.0,userWord[2])
        X3Y0.insert(0.0,userWord[3])
        X4Y0.insert(0.0,userWord[4])
    elif row == 1:
        X0Y1.insert(0.0,userWord[0])
        X1Y1.insert(0.0,userWord[1])
        X2Y1.insert(0.0,userWord[2])
        X3Y1.insert(0.0,userWord[3])
        X4Y1.insert(0.0,userWord[4])
    elif row == 2:
        X0Y2.insert(0.0,userWord[0])
        X1Y2.insert(0.0,userWord[1])
        X2Y2.insert(0.0,userWord[2])
        X3Y2.insert(0.0,userWord[3])
        X4Y2.insert(0.0,userWord[4])
    elif row == 3:
        X0Y3.insert(0.0,userWord[0])
        X1Y3.insert(0.0,userWord[1])
        X2Y3.insert(0.0,userWord[2])
        X3Y3.insert(0.0,userWord[3])
        X4Y3.insert(0.0,userWord[4])
    elif row == 4:
        X0Y4.insert(0.0,userWord[0])
        X1Y4.insert(0.0,userWord[1])
        X2Y4.insert(0.0,userWord[2])
        X3Y4.insert(0.0,userWord[3])
        X4Y4.insert(0.0,userWord[4])
    elif row == 5:
        X0Y5.insert(0.0,userWord[0])
        X1Y5.insert(0.0,userWord[1])
        X2Y5.insert(0.0,userWord[2])
        X3Y5.insert(0.0,userWord[3])
        X4Y5.insert(0.0,userWord[4])
    else:
        pass
    scanWord(userWord)
    row = row+1
#############################
X0Y0 = tk.Text(game, bg="gray", height=2, width=2) 
X0Y0.grid(row=0, column=0)
X1Y0 = tk.Text(game, bg="gray", height=2, width=2)
X1Y0.grid(row=0, column=1)
X2Y0 = tk.Text(game, bg="gray", height=2, width=2)
X2Y0.grid(row=0, column=2)
X3Y0 = tk.Text(game, bg="gray", height=2, width=2)
X3Y0.grid(row=0, column=3)
X4Y0 = tk.Text(game, bg="gray", height=2, width=2)
X4Y0.grid(row=0, column=4)

X0Y1 = tk.Text(game, bg="gray", height=2, width=2)
X0Y1.grid(row=1, column=0)
X1Y1 = tk.Text(game, bg="gray", height=2, width=2)
X1Y1.grid(row=1, column=1)
X2Y1 = tk.Text(game, bg="gray", height=2, width=2)
X2Y1.grid(row=1, column=2)
X3Y1 = tk.Text(game, bg="gray", height=2, width=2)
X3Y1.grid(row=1, column=3)
X4Y1 = tk.Text(game, bg="gray", height=2, width=2)
X4Y1.grid(row=1, column=4)

X0Y2 = tk.Text(game, bg="gray", height=2, width=2)
X0Y2.grid(row=2, column=0)
X1Y2 = tk.Text(game, bg="gray", height=2, width=2)
X1Y2.grid(row=2, column=1)
X2Y2 = tk.Text(game, bg="gray", height=2, width=2)
X2Y2.grid(row=2, column=2)
X3Y2 = tk.Text(game, bg="gray", height=2, width=2)
X3Y2.grid(row=2, column=3)
X4Y2 = tk.Text(game, bg="gray", height=2, width=2)
X4Y2.grid(row=2, column=4)

X0Y3 = tk.Text(game, bg="gray", height=2, width=2)
X0Y3.grid(row=3, column=0)
X1Y3 = tk.Text(game, bg="gray", height=2, width=2)
X1Y3.grid(row=3, column=1)
X2Y3 = tk.Text(game, bg="gray", height=2, width=2)
X2Y3.grid(row=3, column=2)
X3Y3 = tk.Text(game, bg="gray", height=2, width=2)
X3Y3.grid(row=3, column=3)
X4Y3 = tk.Text(game, bg="gray", height=2, width=2)
X4Y3.grid(row=3, column=4)

X0Y4 = tk.Text(game, bg="gray", height=2, width=2)
X0Y4.grid(row=4, column=0)
X1Y4 = tk.Text(game, bg="gray", height=2, width=2)
X1Y4.grid(row=4, column=1)
X2Y4 = tk.Text(game, bg="gray", height=2, width=2)
X2Y4.grid(row=4, column=2)
X3Y4 = tk.Text(game, bg="gray", height=2, width=2)
X3Y4.grid(row=4, column=3)
X4Y4 = tk.Text(game, bg="gray", height=2, width=2)
X4Y4.grid(row=4, column=4)

X0Y5 = tk.Text(game, bg="gray", height=2, width=2)
X0Y5.grid(row=5, column=0)
X1Y5 = tk.Text(game, bg="gray", height=2, width=2)
X1Y5.grid(row=5, column=1)
X2Y5 = tk.Text(game, bg="gray", height=2, width=2)
X2Y5.grid(row=5, column=2)
X3Y5 = tk.Text(game, bg="gray", height=2, width=2)
X3Y5.grid(row=5, column=3)
X4Y5 = tk.Text(game, bg="gray", height=2, width=2)
X4Y5.grid(row=5, column=4)

def userSubmit(): #code that runs when the user enters a guess
    user = userInput.get() #gets the users input and stores it in the variable "user"
    if len(user) != 5:
        pass
    else:
        displayWord() #displays the word on the board

prompt = tk.Label(utils,text="enter text: ")
prompt.grid(row=6, column=0)

textIn = ttk.Entry(utils, width=5, textvariable=userInput)
textIn.grid(row=6, column=1,columnspan=3)

submit = tk.Button(utils,text="submit", command=lambda: userSubmit())
submit.grid(row=6, column=4)

game.pack()
utils.pack()
getWord() #gets the word
root.mainloop() #displays the graphics