'''This is a quiz on the movie "hunt for the wilderpeople" made by Eric Huang'''

huntforthewilderpeopleQandA = {"What is the directors name?" : "Taika Waititi", "What type of poem does Ricky love to write?" : "Haiku", "What is the name of Ricky's foster father?" : "Uncle Hec", "One part of the chase sequence in the movie is very similar to an advertisement with Barry Crump in it. What brand of ute was the advertisement promoting?" : "Toyota", "What was the name of the man that Uncle Hec and Ricky hide out at?" : "Psycho Sam", "What is the name of the girl who finds Ricky" : "Kahu", "Who argue over who is more like the terminator?" : "Paula and Ricky", "What are names of the dogs?" : "Zag And Tupac", "What kind of chocolate bar is advertised?" : "Flake", "What is the name of the social welfare officer?" : "Paula"}
numofquestion = 0
usrinp = ""
score = 0

while numofquestion < 10:
    for question in huntforthewilderpeopleQandA.keys():
        print(question)
        for name in huntforthewilderpeopleQandA.items():
            usrinp = input()
            usrinp = usrinp.lower()
            usrinp = usrinp.title()
            print(usrinp)
            print(name)
            print(question)
            if usrinp in name:
                print("good job its correct!")
                score = score + 1
                numofquestion = numofquestion + 1
                break
            else:
                print("idiot")
                numofquestion = numofquestion + 1
                break
        