
# OOP AND DATE DATA TYPE

"""
import datetime
#          [libaray] [class]
todaydate = datetime.datetime(2024,4,29)

# datetime class has public attributes so can directly access the attributes

print(todaydate.year)
print(todaydate.day)
print(todaydate.month)

dateofbirth = datetime.datetime(2006,4,16)

age = 2024 - dateofbirth.year

print(age)

print("today is",dateofbirth.day,"April and my age is ",2024 - dateofbirth.year)


mytime = datetime.time(5,35,12)
print(mytime.hour,":",mytime.minute,"pm")
"""

# past paper question relating date data type
# 2023


import datetime
class Character():
    # PRIVATE CharacterName : STRING
    # PRIVATE DateOfBirt : DATE
    # PRIVATE Intelligence : REAL
    # PRIVATE Speed: INTEGER

    def __init__(self,CharacterNameP,DateOfbrithP,IntelligenceP,SpeedP):
        self.__CharacterName = CharacterNameP
        self.__DateOfBirth = DateOfbrithP
        self.__Intelligence = IntelligenceP
        self._Speed = SpeedP

    def SetIntelligence(self,newintelligence):
        self.__Intelligence = newintelligence

    def GetIntelligence(self):
        return self.__Intelligence

    def GetName(self):
        return self.__CharacterName

    def Learn(self):
        self.__Intelligence = self.__Intelligence + (0.1 * self.__Intelligence)


    def ReturnAge(self):
        age = 2023 - self.__DateOfBirth.year
        return age


FirstCharacter = Character("Royal",datetime.datetime(2019,1,1),70,30)
FirstCharacter.Learn()
print(FirstCharacter.GetName(),"is",FirstCharacter.ReturnAge(),"years old and his intelligence is:",FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    # PRIVATE Element : STRING

    def __init__(self,element,charactername,dateofbirth,intelligence,speed):
        super().__init__(charactername,dateofbirth,intelligence,speed)
        self.__Element = element

    def Learn(self):
        intelligence = super().GetIntelligence()

        if self.__Element == "fire" or self.__Element == "water":
            intelligence = intelligence + (0.2 * intelligence)
            super().SetIntelligence(intelligence)

        elif self.__Element == "earth":
            intelligence = intelligence + (0.3 * intelligence)
            super().SetIntelligence(intelligence)

        else:
            super().Learn()

FirstMagic = MagicCharacter("fire","light",datetime.datetime(2018,3,3),75.0,22)
FirstMagic.Learn()
print(FirstMagic.GetName(),"is",FirstMagic.ReturnAge(),"years old and his intelligence is:",FirstMagic.GetIntelligence())




