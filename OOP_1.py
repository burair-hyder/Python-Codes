
# attributes are usually private
# methods are usually public
class Player():
    # PRIVATE name  : STRING
    # PRIVATE  age : INTEGER

    #This is a constructor with 2 attributes  ( constructor is also kind of a setter)
    def __init__(self,nameP, ageP): # self (khud) replaces the name of object
        self.__name = nameP  # __ tells that it is a private attribute
        self.__age = ageP


    #This is a method GETTER
    def GetName(self):   # accesses private attribute name
        return self.__name


    def getAge(self):
        return self.__age

    # THIS IS A SETTER  ( to change a private attribute)

    def SetName(self,nameNew):
        self.__name = nameNew

    def Setage(self,ageNew):
        self.__age = ageNew


P1 = Player("Ghost",21) # P1 is object 
P2 = Player("Ninja",19)
P3 = Player("burair",18)

temp = P2.GetName()  # accessing methods
#print(temp)    # we can access private by using methods

#print(P3.getAge())
#print(P3.GetName())

#print(P3.GetName())

P3.SetName("hyder")
#print(P3.GetName())

#print(P3.getAge())


# SETTER : Method which set a value of attribute
# GETTER : Method which accesses a private attribute


# PRACTICE QUESTION

class Picture():

    # PRIVATE Description : STRING
    # PRIVATE Width : INTEGER
    # PRIVATE Height : INTEGER
    # PRIVATE FrameColour : STRING


    # This is constructor initalizing 4 private attributes

    def __init__(self,DescriptionP, WidthP, HeightP, FrameColourP):

        self.__Description = DescriptionP
        self.__Width = int(WidthP)
        self.__Height = int(HeightP)
        self.__FrameColour = FrameColourP

    # GETTERS
    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    # SETTER
    def SetDescription(self, newdesc):
        self.__Description = newdesc


mypicture = Picture("portait",30,40,"black")

mypicture.SetDescription("Landscape")
temp = mypicture.GetDescription()
#print(temp)


# QUESTION PAST PAPER


class TreasureChest():

    # PRIVATE question : STRING
    # PRIVATE answer : INTEGER
    # PRIVATE points : INTEGER

    def __init__(self, questionp, answerp , pointsp ):

        self.__question = questionp
        self.__answer = int(answerp)
        self.__points = int(pointsp)

    def getQuestion(self):
        return self.__question


    def checkAnswer(self,userAnswer):
        if self.__answer == userAnswer:
            return True
        else:
            return False


    def getPoints(self,attempts):

        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points//2)
        elif attempts == 3 or attempts == 4:
            return  int(self.__points//4)
        else:
            return 0



# PRACTICE QUESTION

class Balloon():    # part A
    # PRIVATE Health : INTEGER
    # PRIVATE Colour : STRING
    # PRIVATE DefenceItem : STRING

    def __init__(self, DefenceItemP , ColourP):

        self.__DefenceItem = DefenceItemP
        self.__Colour = ColourP
        self.__Health = 100


    def GetDefenceItem(self): # part B
        return self.__DefenceItem


    def ChangeHealth(self,numberp): # part C
        self.__Health = self.__Health + int(numberp)

    def CheckHealth(self): # part D
        if self.__Health <= 0:
            return True
        else:
            return False


# part E
#userdefence = input("Enter defence item :")
#colour = input("Enter the colour ")
#Balloon1 = Balloon(userdefence, colour)


# part F
def Defend(Balloonobject):
    userstrength = int(input("enter the strength of oppoenet "))
    Balloonobject.ChangeHealth(-userstrength)
    print("your defence is ",Balloonobject.GetDefenceItem())
    if Balloonobject.CheckHealth() == True :
        print("YOU died defence failed ")
    else:
        print("defence succeeded" )
    return Balloonobject


# part G

#Balloon1 = Defend(Balloon1)


# practice question

class Lesson():

    # PRIVATE LessonType : STRING
    # PRIVATE Instructor : STRING

    def __init__(self,LessonTypeP,InstructorP):
        self.__LessonType = LessonTypeP
        self.__Instructor = InstructorP


    def GetLessonType(self):
        return self.__LessonType

    def GetInstructor(self):
        return self.__Instructor

    def SetLessonType(self, newlesson):
        self.__LessonType = newlesson

    def SetInstructor(self, newInstructor):
        self.__Instructor = newInstructor


    def GetFee(self, skill_levelp):

        if skill_levelp == "B":
            return 45

        elif skill_levelp == "I":
            return 50
        elif skill_levelp == "A":
            return 55
        else:
            return -1


# DECLARE LessonArray : ARRAY [0:8] OF Lesson

LessonArray = [" "]*9
LessonArray[2] = Lesson('Improve Your Serve', "David")
LessonArray[2].SetInstructor("burair")
temp = LessonArray[2].GetInstructor()
print(temp)


# INHERITANCE

# what is meant by inheritance ?
# the derived class can use the properties from the parent class without redecalring them
# the derived class can use the methods from the parent class without redeclaring them
# can extend the properties from the parent class
# can extend the methods from the parent class

class PartTimeEmployee():
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER
    # PRIVATE HourlyRate : INTEGER

    def __init__(self, Namep,Agep , hourlyrateP):

        self.__Name = Namep
        self.__Age = Agep
        self.__HourlyRate = hourlyrateP

    def GetName(self):
        return self.__Name

    def DailyWage(self,hoursworked):
        temp = hoursworked * self.__HourlyRate
        return temp


class FullTimeEmployee():
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER
    # PRIVATE MonthlyRate : INTEGER

    def __init__(self, Namep,Agep , MonthlyrateP):

        self.__Name = Namep
        self.__Age = Agep
        self.__MonthlyRate = MonthlyrateP

    def GetName(self):
        return self.__Name

    def YearlySalary(self):
        temp = self.__MonthlyRate * 12
        return temp



#  IN THESE 2 ABOVE CLASSES THERE ARE THINGS WHICH ARRE BEING
#  REPEATED IN BOTH.. FOR EXAMPLE ATTRIBUTES LIKE : NAME,AGE
#  AND METHOD LIKE "GETNAME" is BEING REPEATED

# for this case we use Inheritance . we would make a PARENT CLASS{employee}
# which will include all properties(attributes, methods) whicha are
# common in both classes
# then 2  child classess will be made which will include the
# different properties { part time and full time}
# these 2 classess will inherit from the parent class{employee}
# the child class wil be able  to use the methods and attrbitues of
# parent class , since it is inheirting from it

class Employee():
    # PRIVATE Name : STRING
    # PRIVATE Age : INTEGER

    def __init__(self, NameP , AgeP):
        self.__Name = NameP
        self.__Age = AgeP

    def GetName(self):
        return self.__Name



class  PartTime(Employee):  # we have to mention the parent class
                            # it tells that  PartTime will inherit from Employee

    # PRIVATE HourlyRate

    def __init__(self,NameP , AgeP , HourlyRateP):
        self.__HourlyRate = HourlyRateP
        super().__init__(NameP, AgeP)

    def DailyWage(self, HoursWorked):
        temp = HoursWorked * self.__HourlyRate
        return temp


class FullTime(Employee):

    # PRIVATE MonthlyRate : INTEGER

    def __init__(self,NameP , AgeP , MonthlyRateP):
        self.__MonthlyRate = MonthlyRateP
        super().__init__(NameP, AgeP)

    def YearlySalary(self):
        temp = self.__MonthlyRate * 12
        return temp


worker = PartTime("bhatti", 50 , 20)
permanantworkder = FullTime("sheikh",40 ,3000)
print(permanantworkder.GetName())
print(permanantworkder.YearlySalary())
print(worker.GetName())



#  QUESTION :

class Member():

    # PRIVATE MemberName : STRING
    # PRIVATE MemberID : STRING
    # PRIVATE SubscriptionPaid : BOOLEAN

    def __init__(self):
        self.__MemberName = ""
        self.__MemberID = ""
        self.__SubscriptionPaid = False


    def SetMemberName(self,MemberNameP):
        self.__MemberName = MemberNameP

    def SetMemberID(self,MemberIDP):
        self.__MemberID = MemberIDP

    def SubscriptionPaid(self, subscriptionPaidP):
        self.__SubscriptionPaid = subscriptionPaidP



class JuniorMember(Member):
    # PRIVATE DateOfBirth : STRING

    def __init__(self):
        self.__DateOfBirth = ""
        super().__init__()

    def SetDateOfBirth(self,Dateofbirth):
        self.__DateOfBirth = Dateofbirth

    def SetMemberName(self,MemberNameP):
        super().SetMemberName(MemberNameP)


    def SetMemberID(self,MemberIDP):
        super().SetMemberID(MemberIDP)


    def SubscriptionPaid(self, subscriptionPaidP):
        super().SubscriptionPaid(subscriptionPaidP)


NewMember = JuniorMember()
NewMember.SetMemberName("Ahmed")
NewMember.SetMemberID("12347")
NewMember.SubscriptionPaid(True)
NewMember.SetDateOfBirth("12/11/2001")

# concept of OVERRIDE
# same name of method but different outcomes
# the child class takes a method from parent and uses it differently


class Vehicle():
    def drive(self):
        print("Driving the vehicle")

class car(Vehicle):
    def drive(self):
        super().drive()  # call the drive of Vehicle (class)
        print("Driving the car")

class Bike(Vehicle):
    def drive(self):
        print("Driving the Bike ")


my_car = car()
my_car.drive()  # runs both drive of vehicle and drive of car



my_bike = Bike()
my_bike.drive()

# concept of OVERRIDE

class shapes():

    def Area(self,base , height ):
        print("The Area of Shape with Base", base , "width:",height)


class Sqaure(shapes):

    def Area(self,base , height ):
        super().Area(base,height)
        area = base * height
        print(area)

class Triangle(shapes):

    def Area(self,base , height ):
        super().Area(base,height)
        area = 0.5 * base * height
        print(area)


my_square = Sqaure()
my_square.Area(10,20)

my_triangle = Triangle()
my_triangle.Area(10,20)

# PAST PAPER QUESTION
# MJ23/42 q3
# QUESTION 3
# q3 part A i

class Employee():

    # PRIVATE HourlyPay : REAL
    # PRIVATE EmployeeNumber : STRING
    # PRIVATE JobTitle : STRING
    # PRIVATE PayYear2022 : ARRAY[0:51] OF REAL

    def __init__(self, HourlyPayP , EmployeeNumberP ,  JobTitleP):
        self.__HourlyPay = HourlyPayP
        self.__EmployeeNumber = EmployeeNumberP
        self.__JobTitle = JobTitleP
        self.__PayYear2022 = [0.0] * 52


# part A ii

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber


# part A iii

    def SetPay(self,weeknumberP , numberofhoursP):
        weekpay = self.__HourlyPay * numberofhoursP
        self.__PayYear2022[weeknumberP-1] = weekpay


# part A iv


    def GetTotalPay(self):
        Totalpay = 0
        for index in range(52):
            Totalpay = Totalpay + self.__PayYear2022[index]

        return Totalpay




# part B i

class Manager(Employee):

    # PRIVATE BonusValue : REAL

    def __init__(self,BonusValueP,HourlyPayP,EomployeenumberP,JobtitleP):
        self.__BonusValue = BonusValueP
        super().__init__(HourlyPayP,EomployeenumberP,JobtitleP)


# part B ii

    def SetPay(self,weeknumberP , numberofhoursP):
        numberofhoursp = numberofhoursP + ((numberofhoursP* self.__BonusValue)/100)
        super().SetPay(weeknumberP, numberofhoursp)




# CONTAINMENT:
# Containment is a fundamental concept in oop that refers to the ability
# to include one object inside another object

# practice question


class foodItem():

    # PRIVATE name : STRING
    # PRIVATE code : STRING
    # PRIVATE cost : REAL

    def __init__(self,nameP , codeP, costP):
        self.__name = nameP
        self.__code = codeP
        self.__cost = costP


    def getCode(self):
        return self.__code

    def getCost(self):
        return self.__cost

    def getName(self):
        return self.__name



class vendingMachine():
    # PRIVATE item : ARRAY [0:3] OF fooditems
    # PRIVATE moneyIn : REAL

    def __init__(self,item1, item2, item3, item4):
        self.__items = []
        self.__items.append(item1)
        self.__items.append(item2)
        self.__items.append(item3)
        self.__items.append(item4)
        self.__moneyIn = 0.0


    def checkValid(self,codeP):
        for x in range(4):
            if self.__items[x].getCode() == codeP:
                if self.__items[x].getCost() <= self.__moneyIn:
                    return x
                else:
                    return -2
        return -1


chocolate = foodItem("feastables","1234",56.0)
sweets = foodItem("GajarHalwa","1345",32.5)
sandwich = foodItem("Club","1112",31.2)
apple = foodItem("Red","1349",10.0)

machineOne= vendingMachine(chocolate,sweets,sandwich,apple)
