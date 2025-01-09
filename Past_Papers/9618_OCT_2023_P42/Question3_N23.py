
import datetime

class Character():
    # PRIVATE CharacterName : STRING
    # PRIVATE DateOfBirth : DATE
    # PRIVATE Intelligence : REAL
    # PRIVATE Speed : INTEGER

    def __init__(self,CharacterNamep,DateOfBirthp,Intelligencep,speedp):
        self.__CharacterName = CharacterNamep
        self.__DateOfBirth = DateOfBirthp
        self.__Intelligence = Intelligencep
        self.__Speed = speedp


    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName


    def SetIntelligence(self,newIntelligence):
        self.__Intelligence = newIntelligence


    def Learn(self):

        self.__Intelligence = self.__Intelligence + (0.1*self.__Intelligence)

    def ReturnAge(self):
        yearborn = self.__DateOfBirth.year
        age = 2023 - yearborn
        return age



datebirth = datetime.datetime(2019,1,1)

FirstCharacter = Character("Royal",datebirth,70,30)

FirstCharacter.Learn()
print("the name is :",FirstCharacter.GetName())
print("the age is :",FirstCharacter.ReturnAge())
print("the intelligencec is:",FirstCharacter.GetIntelligence())



class MagicCharacter(Character):
    # PRIVATE Element : STRING

    def __init__(self,Elementp,CharacterNamep,DateOFbrithp,Intelligencep,speedp):
        super().__init__(CharacterNamep,DateOFbrithp,Intelligencep,speedp)
        self.__Element = Elementp


    def Learn(self):
        
        if self.__Element == "fire" or self.__Element == "water":
            int = super().GetIntelligence()
            int = int + (int* 0.2)
            super().SetIntelligence(int)

        elif self.__Element == "earth":
            int = super().GetIntelligence()
            int = int + (int * 0.3)
            super().SetIntelligence(int)
        else:
            super().Learn()



DOB = datetime.datetime(2018,3,3)
FirstMagic = MagicCharacter("fire","Light",DOB,75,22)

FirstMagic.Learn()
print("the name is :",FirstMagic.GetName())
print("the age is :",FirstMagic.ReturnAge())
print("the intelligencec is:",FirstMagic.GetIntelligence())

