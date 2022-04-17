"""
Written by: Joe Buckley
last edit: 17/04/2022

A program that takes every word in a .txt file and saves it to a .csv with the option to sort alphabetically
"""

import csv #imports a library for handling CSV files
import time #imports a library that lets the code wait between actions
import sys #imports the system library so the program can automatically close itself later
from os.path import exists #used to check if necessary files exist

words = [] #creates empty list that will be filled with 5 letter words later
def execute():
    file_exists = exists("sgb-words.txt") #double checks that the list of words actually exists
    if file_exists == True:
        def writeFile(): #defines a function that can be run to ask the user if they are happy to write the newly created list to a CSV file
            proceed = input("Continue? Y/n ") #asks the user if they're happy to proceed  and prompts them to respond with either "Y" or "n"
            if proceed == "Y" or proceed == "y": #if the user is happy to proceed
                alpha = input("Do you wish to sort the list alphabetically? Y/n ") #asks the user if they want to sort the file alphabetically
                if alpha == "Y" or alpha == "y": #if they do
                        words.sort() #sorts the list alphabetically 
                else: #if they don't want to sort alphabetically
                    pass #the code passes onto the next line

                with open('words.csv', 'w', encoding='UTF8') as f: #creates a file called "words.csv" in write mode with the correct text encoding so nothing breaks or messes up
                    writer = csv.writer(f) #creates a CSV writer
                    writer.writerow(words) #writes every word into a CSV file
                print("\n"+"CSV file created successfully" +"\n" + "do not close this program, it will close itself automatically") #tells the user the code worked, goes onto a new line and tells the user not to close the program
                print("\n"+"\n")
                time.sleep(2) #waits two second
                sys.exit
            elif proceed == "n": #if the user doesn't want to create the file
                print("exiting program")
                time.sleep(2)
                sys.exit
            else: #if the user answers something that isnt "Y" or "n"
                print ("Please respond with ""Y"" if happy to proceed or ""n"" if you are not") #prompts the user to answer again
                writeFile() #runs the function again


        with open('sgb-words.txt') as f: #opens the text file ready to be used inside the program
            myList = [line.rstrip('\n') for line in f] #goes through every item in the text file, adding it to the "myList" array and removing the carridge returns
            print("text file length: " +str(len(myList))) #prints off the length of the list
            for item in myList: 
                words.append(item) #adds the word at index i to the "words" list created earleir
        print("words list length: " + str(len(words))) #prints off the length of the newly created "words" list so the uesr can double check

        writeFile() #runs the function created earlier in the program
    else:
        print("missing file ""sgb-words.txt"" please re-download the missing file from wherever you sourced this code")
execute()