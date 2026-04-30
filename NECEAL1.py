'''This is a quiz on the movie "hunt for the wilderpeople" made by Eric Huang'''

import time
import os

#This part sets up the questions and adds the consistant and temp varables, to 
# change the questions change the dict, using anser:question.

huntforthewilderpeopleQandA = {"What is the directors name?" : "taika waititi", 
                                "What type of poem does Ricky love to write?" : "haiku", 
                                "What is the name of Ricky's foster father?" : "uncle hec", 
                                "One part of the chase sequence in the movie is very similar to an advertisement with Barry Crump in it. What brand of ute was the advertisement promoting?" : "toyota", 
                                "What was the name of the man that Uncle Hec and Ricky hide out at?" : "psycho sam", 
                                "What is the name of the girl who finds Ricky" : "kahu", 
                                "Who argue over who is more like the terminator?" : "paula and ricky", 
                                "What are names of the dogs?" : "zag And tupac", 
                                "What kind of chocolate bar is advertised?" : "flake", 
                                "What is the name of the social welfare officer?" : "paula"
                                }
numofquesdone = 0
usrinp = ""
score = 0
POINTS = 1
TOTALQANDA = len(huntforthewilderpeopleQandA)

#This part loops through the questions getting the user input and comparing it 
# to the answers to see if its correct then giving "user friendly" output while 
# keeping score and testing for expected bounderys
while numofquesdone < TOTALQANDA:
    for question, answer in huntforthewilderpeopleQandA.items():
        print(question)
        usrinp = input()

        #these are for testing bounderys
        wordcheck = len(usrinp)
        numbercheck = usrinp.isnumeric()

        #The first if statment checks for people who just put lots of letters 
        # and the secound if statment catches numbers
        while wordcheck > 12 or numbercheck == True:
            print("What you have entered is too long! Please try again.")
            usrinp = input()
            wordcheck = len(usrinp)
            numbercheck = usrinp.isnumeric()

        usrinp = usrinp.lower()
        if usrinp in answer:
            print("good job its correct!")
            score = score + POINTS
            numofquesdone = numofquesdone + 1
        else:
            print(f"That is incorrect, the answer was {answer}")
            numofquesdone = numofquesdone + 1

#this part of the code gives more "user friendly" output before giving the score
print("Congratulations you finished the quiz!")
print(f"The score you got was {score} points!")
input("press enter to exit")