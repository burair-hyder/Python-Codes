# BUILT IN FUNCTIONS

 # Random Function
 # for this function you have to import a library with the name random
 # by following statement
import random


x = random.randint(1,100) # 1 and 100 are inclusive
print(x)



for x in range(10):
    x = random.randint(1, 100)  # 1 and 100 are inclusive
    print(x)



name  = "PapersDock"

length = len(name)
print(length)

name  = "PapersDock"
temp = name.upper()
print(temp)

temp2 = name.lower()
print(temp2)

reply = input("yes or no")
if reply.lower()  == "yes":
    print("working")
else:
    print("not working ")


name  = "PapersDock"
temp = name[2:5] # extracts  from  2 to 4
print(temp) 
