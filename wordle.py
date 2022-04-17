"""
Written by: Joe Buckley
last edit: 17/04/2022

todo: make sure csv file and word-sifter files exist to play the game 
A console version of the popular web game "wordle"
"""
import random #imports the random library so the program can randomly pick a word
import csv #imports a library for handling the previously created CSV file
from os.path import exists #used to check if necessary files exist
import word_sifter
#############################
words = []
Word = ""
guess = ["-","-","-","-","-"]
#############################
def scanInput(input,Word): #creates a function that takes the users input and checks it against the random word
    for i in range(5):
        if input == Word: #if the user guesses the word correctly
            return True
        elif input[i] == Word[i]: #scans through the users input letter by letter to see if matches the word
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
            trys = trys-1 
        print("Sorry, you lost this round!")
#############################
def run():
    file_exists = exists("words.csv") #double checks that the list of words actually exists
    if file_exists == True: #if it does
        with open("words.csv", mode="r") as csv_file: #the file is opened
            reader = csv.reader(csv_file) 
            for item in reader: #and for every item in the file
                words.extend(item) #the code adds it into an array for the code to use
    else: #if the file doesn't exist
        print("missing file detected, entering setup mode:")
        file_exists = exists("word-sifter.py") #it checks that the code for creating the file exists
        if file_exists == True: #if it does
            word_sifter.execute() #it runs the code to create the missing CSV file
            run()
        else:
            print("Missing critical files, please delete current files and attempt re-downloading all files")
    #############################
    Word = random.choice(words) #picks the random word for the round
    print(Word)
    #############################
    game(6) #makes sure the game starts with 6 trys
    print("###########################")
run()