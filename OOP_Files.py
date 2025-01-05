
class Character():
    # PRIVATE Name : STRING
    # PRIVATE XCoordinate : INTEGER
    # PRIVATE YCoordinate : INTEGER

    def __init__(self,Namep,XCoordinatep,YCoordinatep):
        self.__Name = Namep
        self.__XCoordinate = XCoordinatep
        self.__YCoordinate = YCoordinatep

    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return  self.__YCoordinate


    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange




# DECLARE CharArray: ARRAY [0:9] OF Character
CharArray = [""]* 10
try:
    File = open("Characters.txt", "r")
    for x in range(10):
        name = str(File.readline().strip())
        xcord  = int(File.readline().strip())
        ycord = int(File.readline().strip())

        CharacterObject= Character(name,xcord,ycord) # creates object
        CharArray[x] = CharacterObject
    File.close()
except IOError :
    print("file not found")

print(CharArray[0].GetName())

Flag = False
while Flag ==  False:
    name = input("enter the name to be searched in the array: ")
    for x in range(10):
        compare = CharArray[x].GetName()
        if compare.lower() == name.lower():
            indexPosition = x
            Flag = True

NewFlag = False
while NewFlag == False:
    letter = input("enter a letter W,A,S,D:")
    if letter.upper() == "A":
        CharArray[indexPosition].ChangePosition(-1,0)
        NewFlag = True
    elif letter.upper() ==  "W":
        CharArray[indexPosition].ChangePosition(0, 1)
        NewFlag = True
    elif letter.upper() == "S":
        CharArray[indexPosition].ChangePosition(0, -1)
        NewFlag = True
    elif letter.upper() == "D":
        CharArray[indexPosition].ChangePosition(1, 0)
        NewFlag = True


print(name,"has changed coordinates  to X =",CharArray[indexPosition].GetX(),"and Y =",CharArray[indexPosition].GetY())
