class Character():
    # PRIVATE Name : STRING
    # PRIVATE XPosition : INTEGER
    # PRIVATE YPosition : INTEGER

    def  __init__(self,Namep,Xpositionp,Ypositionp):
        self.__Name  = Namep
        self.__XPosition = Xpositionp
        self.__YPosition = Ypositionp


    def GetXPosition(self):
        return self.__XPosition

    def GetYPosition(self):
        return self.__YPosition


    def SetXPosition(self,Xchange):
        temp = self.__XPosition + Xchange
        if temp > 10000:
            self.__XPosition = 10000
        elif temp <0:
            self.__XPosition = 0
        else:
            self.__XPosition = temp

    def SetYPosition(self, Ychange):
        temp = self.__YPosition + Ychange
        if temp > 10000:
            self.__YPosition = 10000
        elif temp < 0:
            self.__YPosition = 0
        else:
            self.__YPosition = temp


    def Move(self,direction):
        if direction == "up":
            self.__YPosition = self.__YPosition + 10
        elif direction == "down":
            self.__YPosition = self.__YPosition - 10
        elif direction == "left":
            self.__XPosition = self.__XPosition - 10
        elif direction  ==  "right":
            self.__XPosition = self.__XPosition + 10



Jack  = Character("Jack",50,50)

class BikeCharacter(Character):
    # PRIVATE Name : STRING
    # PRIVATE XPosition : INTEGER
    # PRIVATE YPosition : INTEGER

    def __init__(self,name,xposition,yposition):
        super().__init__(name,xposition,yposition)


    def Move(self,direction):
        yposition = 0
        xposition = 0
        if direction == "up":

            yposition =  20
        elif direction == "down":
            yposition  =  -20
        elif direction == "left":
            xposition = -20
        elif direction  ==  "right":
            xposition =  20

        super().SetXPosition(xposition)
        super().SetYPosition(yposition)





Karla = BikeCharacter("Karla",100,50)


charactermove = input("please enter the name of character to be moved:")
directionmove = input("input direction to move.left right down up:")

if charactermove.lower() == "karla":
    Karla.Move(directionmove)
    xmovement = Karla.GetXPosition()
    ymovement = Karla.GetYPosition()
    print("Karla's new position is X =" + " " +str(xmovement) + " " + "Y="+" "+ str(ymovement))
elif charactermove.lower() == "jack":
    Jack.Move(directionmove)
    xmovement = Jack.GetXPosition()
    ymovement = Jack.GetYPosition()
    print("Jack's new position is X =" + " " + str(xmovement) + " " + "Y=" + " " + str(ymovement))
