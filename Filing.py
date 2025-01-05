# FILES
# you cant use a file untill the source file and file to be used are not in same
# directory

# 3 modes of file
# reodead mode (when you want to read data from existing file)
# # write m  ( when you want to write data to a new file)
# append mode  (when you want to write data to an existing file )

# reading from a file

# step 1  : open file in read mode by using open() function
# file = open("HighScore.txt","r")  # r means read mode
# step 2 : reaading the content of the complete file by using read() function
# text = file.read()
# step 3 : close the file
#file.close()


file = open("HighScore.txt","r")
text = file.read()   # to read full file
#print(text)
file.close()

# readline() function
# in python, the readline() function is used to read a single line
# of text from a file. this function is commonly used in situtations
# where you want to read a file line by line rather than reading the entire
# file at once

file = open("HighScore.txt","r")
firstline = file.readline()
secondline = file.readline()
#print(firstline)
#print(secondline)
file.close()

# how to print last 2 lines

file = open("HighScore.txt","r")
for x in range(18):
    temp = file.readline()
secondlastline = file.readline()
lastline = file.readline()
#print(secondlastline)
#print(lastline)

file.close()

# using readline() print all lines in file
file = open("HighScore.txt","r")
for x in range(20):
    temp = file.readline()
   # print(temp)

file.close()

# question ]
# find the sum of scores of all the players

file = open("HighScore.txt","r")
totalscore = 0
for x in range(10):
    name = file.readline()
    score = file.readline()
    totalscore = totalscore + int(score)

file.close()

#print(totalscore)

#.STRIP FUNCTION
file = open("HighScore.txt","r")

#for x in range(20):
    #filedata = file.readline()
   # print(filedata)  # but it prints with  extra new line

# how to remove new line
# use .strip function to remove extra new line
# .strip removes new line character
for x in range(20):
    filedata = file.readline().strip()
    #print(filedata)
for x in range(20):
    filedata = file.readline().strip()
   # print(filedata + "\n") # reverses the effect
file.close()


#  practice question
# create an array with 10 elements in which you will store all the player
# names and scores from HighScore.txt file
# open the file HighScore.txt and store all the player name with their score in 2d array


# DECLARE Filedata : ARRAY[0:9 , 0:1] OF STRING
Filedata = [[""]*2 for x in range(10)]


file = open("HighScore.txt","r")




for x in range(10):
        name = file.readline().strip()
        score = file.readline().strip()
        Filedata[x][0]= name
        Filedata[x][1] = score

file.close()

#for x in range(10):
   # print(Filedata[x])

# part c
def OutputHighSchores():
     for x in range(10):
         name = Filedata[x][0]
         score = Filedata[x][1]
         combine = name + " " + score
         print(combine)


#OutputHighSchores()



# WRITING A NEW FILE

# STEP 1 :  open the file in write mode by using open() function
#file = open("filename ","w")
# w stands for write mode

# STEP 2 : Writing a text line by using .write("...")
#file.write("taha")

# STEP 3 : CLOSE the file
# file.close()

file = open("newfile.txt" ,"w")
file.write("Burair\n")
file.write("Taha\n")
file.write("Alishba")
file.write("burair")
file.close()


file = open("newfile.txt","r")
temp = file.read()
#print(temp)


file = open("newtext.txt","w")
name = "Taha"
secondname= "Bano"
file.write(name + "\n")
file.write(secondname + "\n")
file.close()

# PRACTICE QUESTION
# Create a new file with the name
# "EventGuest.txt" and input from the user the name of the guest they want
# to invite in the event and when they type "NO" stop taking input and
# store all the names in the file and each name should be on a new line
# so for that concatenate the "\n" with the name

flag = True

file = open("EventGuest.txt","w")
while flag == True:
    name = input("Enter the name of the guest:")
    if name != "No":
        file.write(name + "\n")
    else:
        flag = False

file.close()


# WRITING IN AN EXISTING FILE

# STEP 1 : Open the file in append mode by using open()function
#file = open("filename.txt","a")
# a stands for append mode
# step 2 :" write a text line  using .write("..")
#file.write("taha")
# step 3 : close the file
# file.close()

file = open("EventGuest.txt", "a")
file.write("Bano\n")
file.close()

# WHAT IF YOU DONT KNOW THE NUMBER OF LINES WHILE READING

#file1 = open("filename.txt","r")
#for line in file1:
#    print(line.strip())

file = open("HighScore.txt","r")

#for line in file:
#    print(line.strip())
#file.close()

#
file = open("HighScore.txt", "r")
for line in file:
    if line.strip() == "PAI":
        print("present")
file.close()

# PRACTICE QUESTION
# APPEND "Papersdock" in the file " EventGuest.txt" but first check if that
# name is in the list or not. if its in the list then print already
# invited and if not then add it to the file


file = open("EventGuest.txt", "r")
flag = False

for line in file:
    if line.strip() == "Papersdock":
        Flag = True
        print("Already invited")
file.close()
file = open("EventGuest.txt","a")
if flag == False:
    file.write("Papersdock\n")
file.close()
