'''This is a quiz on the movie "hunt for the wilderpeople" made by Eric Huang'''

huntforthewilderpeopleQandA = {"What is the directors name?" : "Taika Waititi"}
numofquestion = 14
usrinp = ""
score = 0

while numofquestion != 0:
    for question in huntforthewilderpeopleQandA.keys():
        print(question)
        usrinp = input().title()
        if question in huntforthewilderpeopleQandA.items():
            print("good job its correct!")
            score = score + 1
        else:
            print("idiot")
        