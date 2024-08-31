# PYTHON BASIC

````
print("Papers Dock is Papa")
number = 56
print(number)
#Print("enter name ") this is incorrect as p must be small
# DECLARE Name : STRING (it is necessary to comment the declartion
Name = "burair"
print(Name)
#1num= 56  invalid
#n*ame= hellow invalid
# name , Name, NAME are 3 diff variables
#only char allowed in a varaible name is _ underscrore
first_name ="burair" # valid name
_name = "burair" #valid varaible name

num= 5.46
print(type(num))
print(num)
numint = int(num)
print(type(numint))
print(numint)
numstring=str(num)
print(numstring)
print(type(numstring))



numstring  = "56"
ans = int(numstring)+4
print(ans)

numstring  = "56"
ans = float(numstring)+ int("4")
print(ans)
# DECLARE Num1: INTEGER
# DECLARE Answer: REAL/FLOAT
Num1 = 50
Answer = (Num1)*(40.45)
print("this is the answer:",int(Answer))


num1=35
num2= 34
num3 = 36.5
avg = (num1+num2+num3)/3
integeravg= int(avg)
print(integeravg)
x=1
for x in range(0,6):
    print(x)

# string concatention
# string ; any text in speech marks ""
# concatenation ; link together,makes a single string
# " taha " & " ali"= " taha" + " ali"

Firstname = "Burair"
Lastname = "Hyder"

Fullname = Firstname + " " + Lastname + " " + "computer science"
print(Fullname) # produces "burair hyder"
#print(Firstname,Lastname) # produces "burair" "hyder"


#practice question

String1 = "burair"
String2 = "hyder"

Combined_String = String1 + String2
print(Combined_String)

# input from the user

# number =input("Enter number")  "enter number" is a prompt
# note : in python  input fucntion always returns string value
# so if its a number then you are suppose to change it into integer or float

#number = float(input("enter a number "))

Number = input("kindly enter a number:")
print(Number)
print(type(Number)) #returns str

number = float(input("enter a number:"))
print(number)
print(type(number)) #returns float



# DECLARE number1,number2,total:REAL/FLOAT
number1= float(input("enter number 1: "))
number2 = float(input("enter number 2 : "))
total = number1 + number2
print("the total of 2 numbers is :", total )
print("the total of 2 numbers is :"+ str(total))


print((float(input("enter num:")))+(float(input("enter num 2:"))))


# SELECTION STATEMENTs
   # logical conditions
       # equal : A==b (comparsion)
       # not equal : a!=b
       # less than : a<b
       # greater than: a>b
       #greater than equal to :>=
# syntax of if
  # if(condition): "brackets are not neccessary"
       #print("xyz")
  # indentation is neccessaray


num1=5
num2=10
if (num2>num1):
    print("parhlo Allah ke bando!!")


guess_number = float(input("guess a number:"))
if (guess_number == 20):  # we can compare int and float
    print("Sahi he!!... lekin ye uska number nahi he jo khush ho rahe ho")

#ELSE is the key word that is executedd if the first condition is false


guess_number = float(input("guess the number:"))
if guess_number == 20:
    print("sahi hai")
else:
    print("ap say nah ho pae ga")


#ELIF  the elif keyword is pythons way of saying "else if" " if the pervious conditions were not true ,then try this condition

guess_number = float(input("guess the number:"))
if guess_number == 20:
    print("sahi hai")
elif guess_number == 21: # if we have used if then it would also have checked this condition if first one was true
    print("kareeb ho larke")
elif guess_number == 19:
    print("Ye bhe kareeb haai ")
else:
    print("sach mein ap say nah hoe pae ga")

#BOOLEAN OPERATROS
  # and : both the conditions should be true
  # or : any one condition should be true


age = float(input("tell me your age :"))
gender = input("tell me your gender, and we only have 2 genders:")

if (age) >= 18 and (gender == "male" or gender=="female"):
    print("you have the access to the ride")
else:
    print("GHAR jao beta")

 # input 3 numbers and print the largest number  (practice question)

num1 = float(input("enter number 1:"))
num2 = float(input("enter number 2:"))
num3 = float(input("enter number 3:"))

if num1 > num2 and num1 > num3:
    print("the greatest number was:",num1)
elif num2 > num3 and num2 > num1:
    print("the greatest  number was:",num2)
else:
    print("the greatest number was:",num3)

age= float(input("etner the age:"))
gender = input("enter your gender?:")

if age >18 or gender == "male":
    print("access dediya")
else:
    print("ghar jao")

# NESTED IF
 # IF WITHIN IF
a= 10
b=8
c=3
if a>b:
    if a>c:
        print(a,"is the largest")


# practice question
# input email and passsword...print login successfull only if both are correct

email = input("enter your email please:")
password = input("enter your password:")

if (email) == "123@papersdock.com" and  (password) == "12ab":
    print("login successfull")
else:
    print("login denied")

# LOOPS
  # TYPES OF LOOPS:
     # COUNT CONTROLLED LOOP
     # CONDITIONAL LOOP

# COUNT CONTROLLED LOOP
 # FOR LOOP
   #it will automatically increment a variable and will run for fix amount of times

 #syntax for for loop
   #  for x in range(10): "untill 10 not including 10 (0-9)
            #print(X)

for x in range(10):
    print(x)  # 0 till 9

for x in range(1,11):
    print(x)  # 1-10

for x in range (2,11):
    print(x)


for x in range(10):
    name = input("enter your name: ")
    temp = "Good Morning" + " "+ name
    print(temp)


# SUM TECHNIQUE
   # sum=0
   # for x in range(10):
     # number = float(input("enter number"))
     # sum = sum + number
   #print(sum)

sum=0
for x in range(10):
    number = float(input("ENTER NUMBER:"))
    sum = sum + number
print(sum)

# practice question. ask 5 numbers from the user and print the sum of those numbers

Sum = 0
for x in range(5):
    number = float(input("enter number:"))
    Sum = Sum + number
print("the sum is "+ " "+ str(Sum))


# LARGEST NUMBER TECHNIQUE

  # large = 0
  # for x in range(10):
  #      number = float(input("enter numbber:")
  #      if number > larage:
  #         large= number
  # print(large)

large = 0
for x in range(5):
    number= float(input("enter the number:"))
    if number > large:
        large = number
print(large)

# COUNTING TECHNIQUE
    # count = 0
    # for x in range(5):
    #   count = count + 1
    #print(count)

count = 0
for x in range(5):
    count = count + 1
print(count)
print(x)

# practice question .ask for 5 numbers .and count
countneg=0
countpos = 0
for x in range(5):
     number= float(input("enter number"))
     if  number > 0:
         countpos = countpos +1
     elif number < 0:
         countneg= countneg +1
print("the  total postive numbers were ", countpos)
print("the  total negative numbers were ",countneg)


# CONDITIONAL LOOPS
  # WHILE..DO..ENDWHILE -- loop will run untill the condition is true
  # REPEAT..UNTILL (not in python though)

# SYNTAX
#while condition:
#  print("hello")

 # prints hello 10 times
x= 0
while x<10:
    print("hello")
    print(x)
    x= x+1

# practice question .ask 5 numbers and print sum

Sum=0
x=0 # loop variable

while x < 5:
    number = float(input("Enter Number:"))
    Sum = Sum + number
    x = x + 1

print(Sum)

# ARRAYS
# we do not have arrays in python..we have lists in python which can items of diff data types
# first index is lower bound
# last index is upper bound
# in python the index starts from zero (0).we can not alter this
# names[0]= "taha"
# arrays stores multiple values of same data type


# how to create array
# index    0       1       2      3       4       5     = length is 6
Names = ["taha","ahmed","pappu","bano","banto","pappan"]

# how to access individual  elements

print(Names[2])  # prints pappu
print(Names[4])  # prints banto
print(Names[5])  # prints pappan

# how to find the length of an array ( how many elements are there

Length = len(Names)
print(Length)   # ans is 6 as 6 elements are present


# how to print all the elements of the array one by one
# x is intially zero in for loops as it starts from 0 by defualt is not specified
for x in range(6):

    print(Names[x])

# for loop using length function

for y in range(len(Names)):
    print(Names[y])


# PRACTICE QUESTION
# find the index position of bano


Name = ["taha","ahmed","pappu","bano","banto","pappan"]
for x in range(len(Name)):
    if Name[x] == "bano":
        print(x)



name = ["taha","ahmed","pappu","bano","banto","pappan"]

for x in range(len(name)):
    if name[x] == "pappan":
        print(x)


# PRACTICE QUESTION
# count how many numbers in this array are postive and how many are negative

Numbers = [54,-2,-4,43,12,-8,14,-7]
#DECLARE countpos,countneg : INTEGER
countpos = 0
countneg = 0

for x in range(len(Numbers)):
    if Numbers[x] >0:
        countpos= countpos+1

    elif Numbers[x]<0:
        countneg = countneg +1

print("there are ",countpos,"positive numbers")
print("there are ",countneg,"negative  numbers")


# ADDING AN ITEM IN THE LIST(ARRAY)
# APPEND only add in the last one by one
name = ["taha","ahmed","pappu","bano","banto","pappan"]
print(name)

name.append("babay baji")
name.append("mumtaz beghum")
name.append("allah bachae")
name.append("dua")
print(name)


# PRACTICE QUESTION

Names = ["Taha", 'Ahmed', "Pappu", "Bano", "Banto", "Pappan"]

checkname = input("enter the name you want to add")
found  = False

for x in range(len(Names)):
    if Names[x] == checkname:
        found= True
if found==False:
    Names.append(checkname)
    print(Names)
else:
    print("already present")

# using while loop
Names = ["Taha", 'Ahmed', "Pappu", "Bano", "Banto", "Pappan"]
checkname = input("enter your name")
found = False
x=0
while found == False and x<len(Names):
    if Names[x] == checkname:
        found=True
    x=x+1

if found == False:
    Names.append(checkname)
    print(Names)
else:
    print("already there")

# PRACTICE QUESTION

Numbers = [10,32,24,56,75,86]
num2 = []  # empty array
length = len(Numbers)
i=1
# reverse the order of the array

for x in range(len(Numbers)):
    num2.append(Numbers[length-i])
    i=i+1
print(num2)

# second method
# index    0 1  2  3  4  5
Numbers = [10,32,24,56,75,86] # new[0] = Numbeers[5]

new = [0,0,0,0,0,0]

opposite_index = 5

for x in range(len(Numbers)):  # 0 -5
    new[x] = Numbers[opposite_index]

    opposite_index = opposite_index-1

print(new)
print(Numbers)



# practice question
# ask numbers from the user until zero is entered
# print avg
Flag = True
total = 0
count = 0
avg = 0
while  Flag == True:
    num = float(input("enter a number:"))
    if num == 0:
        Flag = False
    else:
        total = total + num
        count = count +1
avg = (total)/count
print("the avg is"+" "+str(avg))

# PRACTICE QUESTION
# Question: Create a while loop that asks the user for a number and adds it to a total
# sum. Exit the loop when the user enters 'done'.

Sum =0
Flag = False

while Flag==False:
    strnum =input("Enter the number :")
    if strnum=="done":
        Flag=True
    else:
        Sum = Sum + float(strnum)

print("the total is: ",Sum)

# PRACTICE QUESTION
#Question: Use a for loop to find the smallest number in an array.
smallest_num = 9999
numbers = [5, 1, 3, 2, 4]

for x in range(len(numbers)):
    if numbers[x]<smallest_num:
        smallest_num=numbers[x]

print("the smallest number in the array was:",smallest_num)

# PRACTICE QUESTION
#Question: Find the largest number in an array without using built-in functions.
numbers = [5, 1, 3, 2, 4,]

largest_num =-999
for x in range(len(numbers)):
    if numbers[x]>largest_num:
        largest_num = numbers[x]

print("the largest number of the array is ",largest_num)

# PRACTICE QUESTION

#Question: Implement a linear search algorithm that finds the smallest and largest
#number in a list.

numbers = [5, 1, 3, 2, 4,]

smallest_num = 9999
largest_num =-999

for x in range(len(numbers)):
    if numbers[x]>largest_num:
        largest_num = numbers[x]
    if numbers[x]<smallest_num:
        smallest_num=numbers[x]

print(largest_num)
print(smallest_num)

# PRACTICE QUESTION
#Question: Implement a linear search algorithm that finds how many numbers are greater
#           than 3 in a list and replace all the numbers which are less than 3 by 10

numbers = [5, 1, 3, 2, 4]

count = 0

for x in range(len(numbers)):
    if numbers[x]>3:
        count = count + 1
    elif numbers[x]<3:
        numbers[x] = 10
print(numbers)
print("there are",count,"number which are greater than 3")

# PRACTICE QUESTION
number = [-1,3,4,5,-4,-8,-4,6]
# count how many numbers are positive and how many numbers are negative and replace negative numbers with 11

countpos = 0
countneg = 0

for x in range(len(number)):
    if number[x] > 0:
        countpos = countpos + 1
    elif number[x]<0:
        countneg = countneg + 1
        number[x] = 11

print("there are  ",countpos,"positive numbers")
print("there were ",countneg,"negative number")
print("the new array is:",number)

# PRACTICE QUESTION
names = ["Bano", "Zulaikha", "Shabnam", "Zainab", "Dua", "Shagufta"]
# find the index posistion of Shagufta and then replace it with "zainab kay papa"



for x in range(len(names)):
    if names[x] == "Shagufta":
        names[x] = "zainab kay papa"
        print(x)
print(names)

# create a function that takes array as argument and cube and sum all the elements of the array

num = []
def cube(array):  # array passed as argument
    # DECLARE SUM : INTEGER
    sum =0
    for x in range(len(num)):    # access each element ..
        sum = sum + (num[x])**3  #cube it and add it to sum
    return sum
def main():
    index = int(input("enter how many number are to be added:"))
    for x in range(index):   # to take input
        number = float(input("enter a number; "))
        num.append(number)   #adds the input to array
main()

print(cube(num))
print(num)


# 2D ARRAYS

# how many positive numbers and how many negative numbers are there and convert all the negative to 100

number = [[6, -1, 4, 2, -1], [-3, -1, -7, -9, 10], [4, 1, 2, 11, 2], [-1, -2, -4, 19, 1], [3, 6, 7, 8, 9]]
countpos = 0
countneg = 0
for row in range(len(number)):
    for col in range(5):  # for col in range(len(number[0])): # len of first array which tells how many columns are there
        # num[0] means first row ---[6, -1, 4, 2, -1]
        if number[row][col] >0:
            countpos = countpos + 1
        elif number[row][col] < 0:
            countneg = countneg +1
            number[row][col] = 100
print("positive numbers  are ",countpos)
print("negative numbers are", countneg)

for x in range(len(number)):
    print(number[x])


print(len(number)) # prints number of rows present
print(len(number[0])) # prints numer of columns present


# input 500 numbers and store it in the 1D array
number = [0] * 20  # intializes an array with 20 elements with value zer0  #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(number)

# input 40 number and store it in a 1D array

num = [0]*40
for x in range(40):
    value = float(input("enter value;"))
    num[x] = value

print(num)

# input 10 names and store it in 1D array
name = [" "]*10
for x in range(len(name)):
    naam = input("Enter the  name:")
    name[x] = naam
print(name)


# second method

name = []

for x in range(10):
    temp = input("enter name ")
    name.append(temp)
print(name)

# 2D ARRAY INITSIALIZATION

# 4 rows and 6 col

number = [[0]*6 for i in range(4)]

for rows in range(len(number)):
    print(number[rows])
    [0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0]
    [0, 0, 0, 0, 0, 0]


# name 10 rows  and 4 colums
name = [[" "]*4 for i in range(10)]  # pehley columns pher rows

for rows in range(len(name)):
    print(name[rows])



# FUNCTIONS

# What are functions ?
#  we name some steps(instructions)
# any value passed in function is called parameter'
# f(x)  where x is a parameter

# a functions is bascially a block of code which only runs when it is called

def f(x): # FUNCTIONS f ( X ; INTEGER)
   temp = x + 4
   print(temp)

f(2) # calling function
f(8)

def name():
    print("Hello")

name() # calling function
name()

def greeting(name):
    combine = "Good Morning"+" "+name
    print(combine)

greeting("Burair")
greeting("Taha")
greeting("Bano")

def avg(Sum,count):
    average = Sum/count
    print(average)

avg(54,2)

# multiply(x,y,z) print the product

def multiply(x,y,z):
    product = x * y * z
    print(product)

multiply(5,4,6)

# diff between print and return

def number(x):
    ans = x + 4
    print(ans)
number(5)
# we cant multiply the number(x) to something


def number(y):
    ans = y + 4
    return ans
temp = number(4)
print(temp*2)


def average(sum,count):
    avg = sum/count
    return  avg  # value of avg is returned
temp = average(54,2) # value of avg is stored in temp
print(temp)



# create a function to display the table of the number which is passed as parameter

def table(x):
    for i in range(11):
        ans = i * x
        text =str(x) + " " + "x" + " " + str(i) + " " "=" + " " + str(ans)
        print(text)


# create a function for findiing the largest value in an array and then print the table of that number
number = [45,34,23,87,96,23]
def largest(array):
    largest = array[0]

    for i in range(len(array)):
        if array[i] > largest:
            largest =  array[i]

    return largest
temp = largest(number)

table(temp)


# linear search function
# pass an array as parameter and string value which you are suppose to find

Name = ["Taha", "Bano", "Zainab", "Dua"]
def search(array , find):0
    for x in range(len(array)):
        if array[x] == find:
            return x
        return -1
ans = search(Name,"Bano")
print("The Index Position of Bano is"+" "+str(ans))

#
number = [2,3,2,3,2,5,6,4,7,5,85,1,-1]

for x in range(len(number)):
    if number[x] < 0:
        while number[x] < 0:
            new = str(input("enter a postitive number to be added to the arrray please:"))
            int_new = int(new)
            number[x] = int_new
print("the new upodated array is the following:", number)
num = [6,6,2,8,-78,-98,25,14]
for x in range(len(num)):
    if num[x] < 0:
        num[x]="invalid"
print("the new updated array is the following: ")
print(num)

# DIV AND MOD
# // is used for div
# % is used for mod
ans = 11 //2
print(ans)

# input numbers from the user untill they type "done" and print even or odd for each number

flag = True
while flag == True:
    number = input("enter a number or done to stop")
    if str(number)!= "done":
        if float(number)%2 == 0:
            print("Even Number")
        else:
            print("Odd Number")
    else:
        flag = False

# create a function which will take 2 numbers as parameter and return the div of those numbers

def div(x,y):
     result = x//y
     return result

num1 = float(input("enter first number;"))
num2 = float(input("enter second number;"))

print(div(num1,num2))


def mod(x, y):
    result = x % y
    return result


num1 = float(input("enter first number;"))
num2 = float(input("enter second number;"))

print(mod(num1, num2))

full_name = input("enter your full name please:")
first_name = ""
last_name = ""

for x in range(len(full_name)):
    if full_name[x] !=" ":
        first_name = first_name + full_name[x]
    else:
        break
last_name = full_name[x+1:len(full_name)]

print(first_name)
print(last_name)


name = input("Enter the full name: ")
firstlen = 0
totallen = len(name)

for x in range(totallen):
    if name[x] != " ":
        firstlen = firstlen + 1
    else:
        break

firstname = name[0:firstlen]    # Taha Ali
lastname = name[firstlen + 1 : totallen]
print(firstname)
print(lastname)



# STRING MANIPULATION/SLICING  (used in web scrapping)
# 0  1  2  3  4  5  6  7  8  9
# P  A  P  E  R  S  D  O  C  K  (papersdock)

# name = "papersdock"
#          0        :   5+1  (to extract papers)
# name[starting chr:ending chr +1(range)]
#                   (uptill this number but not including this number)


name = ("PapersDock")

temp = name[0:6] # 0 to 5
templast = name[6:10] # 6 to 9

print(temp)
print(templast)

# note : space is also considered as a character


# practice question
name = "Burair Hyder"

firstname = name[0:6]
lastname = name[7:12]

print(firstname)
print(lastname)

# LENGTH OF A STRING
name = "papersdock"  # 10 characters
temp = len(name)
print(temp)  # prints 10

# practice question
# separate the first name and the last name after taking the full name as input

fullname = input("Kindly Enter Your Full Name:")
length = len(fullname)
firstname = ""
lastname = ""
for x in range(length):
    if fullname[x] != " ":
        firstname = firstname + fullname[x]
    else:
        break
lastname = lastname + fullname[x+1:length   ]

print(firstname)
print(lastname)

# OR
fullname = input("Kindly Enter Your Full Name:")
length = len(fullname)
firstnamecounter=0

for x in range(length):
    if fullname[x] != " ":
        firstnamecounter = firstnamecounter+1
    else:
        break
firstname = fullname[0:firstnamecounter]
lastname = fullname[firstnamecounter+1:length]

print(firstname)
print(lastname)

# OR
fullname = input("Kindly Enter Your Full Name:")
flag = False
count = 0
while flag == False:
    if fullname[count] == " ":
        flag = True
    else:
        count= count +1
firstname = fullname[0:count]
lastname = fullname[count+1:len(fullname)]
print(firstname)
print(lastname)
````
