'''This is a quiz on the movie "hunt for the wilderpeople" made by Eric Huang'''

import time
import os

#This part sets up the questions and adds the consistant and temp varables, to 
# change the questions change the dict, using question:answer.
huntforthewilderpeopleQandA = {"What is the directors name?" : "taika waititi", 
                                "What type of poem does Ricky love to write?" : "haiku", 
                                "What is the name of the girl who dies in juvey?" : "amber", 
                                "One part of the chase sequence in the movie is very similar to an advertisement with Barry Crump in it. What brand of ute was the advertisement promoting?" : "toyota", 
                                "What was the name of the man that Uncle Hec and Ricky hide out at?" : "psycho sam", 
                                "What is the name of the girl who finds Ricky" : "kahu", 
                                "What is the name of the bad egg protagonist?" : "ricky", 
                                "What is the name of Ricky’s dog?" : "tupac", 
                                "What kind of chocolate bar is advertised?" : "flake", 
                                "What is the name of the social welfare officer?" : "paula"
                                }
numofquesdone = 0
usrinp = ""
score = 0
POINTS = 1
TOTALQANDA = len(huntforthewilderpeopleQandA)
#change this to change the word limit
WORDLIMIT = 20
QUIZNAME = "Hunt for the wilder people"

#This part loops through the questions getting the user input and comparing it 
# to the answers to see if its correct then giving "user friendly" output while 
# keeping score and testing for expected bounderys
print(f"welcome to this quiz on {QUIZNAME}!")
while numofquesdone < TOTALQANDA:
    for question, answer in huntforthewilderpeopleQandA.items():
        print(question)
        usrinp = input()

        #these are for testing bounderys
        wordcheck = len(usrinp)
        numbercheck = usrinp.isnumeric()

        #this while loop checks for bounderys then gives the usr the change to
        #try again
        while wordcheck > WORDLIMIT or numbercheck == True or usrinp == "" or usrinp.startswith('-'):
            print("Invalid input! Please try again.")
            time.sleep(1)
            os.system('cls')
            print(question)
            usrinp = input()
            wordcheck = len(usrinp)
            numbercheck = usrinp.isnumeric()

        usrinp = usrinp.lower()
        if usrinp == answer:
            print("good job its correct!")
            score = score + POINTS
            numofquesdone = numofquesdone + 1
        else:
            print(f"That is incorrect, the answer was {answer}")
            numofquesdone = numofquesdone + 1

        time.sleep(2)
        os.system('cls')

#this part of the code gives more "user friendly" output before giving the score
print("Congratulations you finished the quiz!")
print(f"The score you got was {score} out of {TOTALQANDA}!")
input("press enter to exit")

#⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣠⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀
#⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
#⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
#⠀⠀⠀⠘⣿⣿⣿⣿⠟⠁⠀⠀⠀⠹⣿⣿⣿⣿⣿⠟⠁⠀⠀⠹⣿⣿⡿⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⢼⣿⠀⢿⣿⣿⣿⣿⠀⣾⣷⠀⠀⢿⣿⣷⠀⠀⠀⠀⠀
#⠀⠀⠀⢠⣿⣿⣿⣷⡀⠀⠀⠈⠋⢀⣿⣿⣿⣿⣿⡀⠙⠋⠀⢀⣾⣿⣿⠀⠀⠀⠀⠀
#⢀⣀⣀⣀⣿⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣾⣿⣷⣦⣤⣴⣿⣿⣿⣿⣤⠤⢤⣤⡄
#⠈⠉⠉⢉⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣀⣀⣀⡀⠀
#⠐⠚⠋⠉⢀⣬⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣥⣀⡀⠈⠀⠈⠛
#⠀⠀⠴⠚⠉⠀⠀⠀⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠋⠁⠀⠀⠀⠉⠛⠢⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⢀⣤⣤⣄⢀⣶⠏⢷⡄
#⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⢽⠀⠀⠀⠹⠀⠀⠀⣿
#⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠈⣆⠀⠀⠀⠀⠀⣸⠁
#⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠑⣄⠀⠀⡾⠀⠀
#⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠹⡜⠀⠀⠀
#⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
#⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀