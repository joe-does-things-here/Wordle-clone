"""
Written by: Joe Buckley
last edit: 14/04/2022

Todo: scan user input letter by letter to see if it matches or fits (carry on with what I'm doing now), add graphics

My version of the popular web game "wordle"
"""

import random
import csv
#############################
words = []
guess = ["-","-","-","-","-"]
#############################
def scanInput(input,Word): #creates a function that takes the users input and the chosen word as parameters
    guesses = 0
    letters = 0 #this is used to count how many correct letters the user found
    break_flag = False
    for i in range(5):
        guesses = 1 #this is used to count how many itterations the loop has gone through, starting with 1 going to six
        if input == Word:
            return
        elif input[i] == Word[i]:
            guess[i] = input[i]
            letters = letters+1
            if letters == 5:
                print(guess)
                break_flag = True
                return
        elif input[i] in Word:
            print("Letter: "+input[i]+" is in the word")
        elif guesses == 6:
            return
        elif break_flag == True:
            return
        else:
            pass
        guesses = guesses+1
        print(guess)
#############################
with open("C:\\Users\\joe5b\\Documents\\CODE\\python\\wordle clone\\words.csv", mode="r") as csv_file:
    reader = csv.reader(csv_file) 
    for item in reader:
        words.extend(item) #adds it into an array for the code to use
#############################
Word = random.choice(words) #picks the random word for the round
print(Word)
#############################
for i in range(6): #gives the user 6 guesses
    user = input("Input your guess: ")
    scanInput(user,Word) #runs the scanInput function and passes the usesr's input as a parameter
print("###########################")