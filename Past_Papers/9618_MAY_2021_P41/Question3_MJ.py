# question no3

class TreasureChest():
    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER

    def __init__(self,questionp,answerp,pointsp):
        self.__question = questionp
        self.__answer = answerp
        self.__points = pointsp

    def getQuestion(self):
        return self.__question


    def checkAnswer(self,answer):
        if answer == self.__answer:
            return True
        else:
            return False

    def getPoints(self,numberofattempts):
        if numberofattempts == 1:
            return self.__points
        elif numberofattempts == 2 :
            return int((self.__points)//2)

        elif numberofattempts ==3 or numberofattempts ==4:
            return int((self.__points) // 4)
        else:
            return 0





# question no 3 part b
global arrayTreasure
def readData():
    try:
        file = open("TreasureChestData.txt","r")
        # DECLARE arrayTreasure : ARRAY [0:4] OF TreasureChest
        global arrayTreasure
        arrayTreasure = []

        for x in range(5):
            question = file.readline().strip()
            answer = file.readline().strip()
            points = file.readline().strip()

            treasure = TreasureChest(question,answer,points)
            arrayTreasure.append(treasure)
    except IOError:
        print("file not found")


# question part c i

readData()
questionnumber = int(input("enter a question number: "))
temp = (arrayTreasure[questionnumber-1].getQuestion())
print(temp)
answer = input("enter the answer")

count = 0
flag = False
while flag == False:
    answer = int(input("enter the answer"))
    count = count+1
    temp  =(arrayTreasure[questionnumber-1].checkAnswer(answer))
    if temp == True:
        flag = True

point =arrayTreasure[questionnumber-1].getPoints(count)
print(point)

readData()
choice = int(input("Pick a treasure chest to open"))
if choice > 0 and choice < 6:
    result = False
    attempts = 0
while result == False:
     answer = int(input(arrayTreasure[choice-1].getQuestion()))
     result = arrayTreasure[choice-1].checkAnswer(answer)
     attempts = attempts + 1
     print(int(arrayTreasure[choice-1].getPoints(attempts)))
