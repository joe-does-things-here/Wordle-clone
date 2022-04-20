"""
Written by: Joe B
last edit: 20/04/2022

A console version of the popular web game "wordle"
"""
import random
import csv 
from os.path import exists
import os 
import sys 
import time
#############################
words = []
Word = ""
guess = ["-","-","-","-","-"]
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
def scanInput(input,Word): #creates a function that takes the users input and checks it against the random word
    for i in range(5):
        if input == Word: #if the user guesses the word correctly
            return True
        elif Word[i] == input[i]: #scans through the users input letter by letter to see if matches the word
            guess[i] = Word[i] #fills in the blank ready to be shown to the user
            print(guess) #shows the user the letters they've got correct
        elif input[i] in Word: #if the letter is in the final word
            print("Letter: "+input[i]+" is in the word")
        else: #if the letter isn't in the final word
            pass
#############################
def game(trys): #creates a function that lets users input a word to be checked
        for i in range(trys): #gives the user 6 guesses
            user = input("Input your guess: ")
            if len(user) != 5:
                print("You must enter a five letter word")
                game(trys) #runs the function again to let the user have another go
            win = scanInput(user,Word) #runs the scanInput function and passes the usesr's input as a parameter
            if win == True:
                print("Congratulations you got the word!!")
                break
            trys = trys-1 #takes away 1 try after the user guesses a word
        if win != True: #if "win" isn't true after 6 rounds
            print("Sorry, you lost this round!")
            print("The word was: "+Word)
#############################
def getWord():
    file_exists = exists("words.csv") #double checks that the list of words actually exists
    if file_exists == True: #if it does
        with open("words.csv", mode="r") as csv_file: #the file is opened
            reader = csv.reader(csv_file) 
            for item in reader: #and for every item in the file
                words.extend(item) #the code adds it into an array for the code to use
    else: #if the file doesn't exist
        print("missing file detected, entering setup mode:")
        createCSV()
        getWord()
#############################
def start(): #main function that runs all the other functions in order to play the game
    getWord()
    global Word
    Word = random.choice(words) #picks the random word for the round
    game(6) #makes sure the game starts with 6 trys
    print("###########################")
    again = input("Want to play again? Y/n ")
    if again == "Y" or again == "y":
        os.system('cls')
        start()
    else:
        print("ok, hope you had fun!")
start()