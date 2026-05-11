'''This is a quiz on the movie "hunt for the wilderpeople" made by Eric Huang'''

import time
import os
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

#This part sets up the questions and adds the consistant and temp varables, to 
# change the questions change the dict, using question:answer.
huntforthewilderpeopleQandA = { "What does Ricky call the bush?" : "jungle", 
                                "What type of poem does Ricky love to write?" : "haiku", 
                                "What is the name of the girl who dies in juvey?" : "amber", 
                                "One part of the chase sequence in the movie is very similar to an advertisement with Barry Crump in it. What brand of ute was the advertisement promoting?" : "toyota", 
                                "Who plays the role of Ricky Baker?" : "julian", 
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
QUIZNAME = "Hunt for the wilder people"
#change this to change the word limit
WORDLIMIT = 15

#This part loops through the questions getting the user input and comparing it 
# to the answers to see if its correct then giving "user friendly" output while 
# keeping score and testing for expected bounderys
print(f"welcome to this quiz on {QUIZNAME}!")
while numofquesdone < TOTALQANDA:
    for question, answer in huntforthewilderpeopleQandA.items():
        print(question + " (one word answers)")
        usrinp = input()

        #these are for testing bounderys
        wordcheck = len(usrinp)
        numbercheck = usrinp.isnumeric()
        has_special = not usrinp.isalnum()
        

        #this while loop checks for bounderys then gives the usr the chance to
        #try again if its correct it goes through a accuracy test
        while wordcheck > WORDLIMIT or numbercheck == True or usrinp == "" or usrinp.startswith('-') or has_special == True:
            print("Invalid input! Please try again.")
            time.sleep(1)
            os.system('cls')
            print(question + " (one word answers)")
            usrinp = input()
            wordcheck = len(usrinp)
            numbercheck = usrinp.isnumeric()
            has_special = not usrinp.isalnum()

        usrinp = usrinp.lower()
        #fuzz.ratio works by comparing the usrinp and answer and gives a 
        # accuracy score, if its over 78 its correct.
        score = fuzz.ratio(usrinp, answer)
        if score > 78:
            print("good job its correct!")
            score = score + POINTS
            numofquesdone = numofquesdone + 1
        else:
            print(score)
            print(f"That is incorrect, the answer was {answer}")
            numofquesdone = numofquesdone + 1

        time.sleep(2)
        os.system('cls')

#this part of the code gives more "user friendly" output depending on how well 
# they did before giving the score
if score < 4:
    print("Did you even watch the movie?")
elif score < 8:
    print("Good job you did great")
else:
    print("GET A JOB")

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
# This cat will get me an excellent