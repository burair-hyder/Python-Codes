# what is meant by Exception ?
# it is an unplanned event and a situation causing a crash
# for example : wrong name of file entered to open.


# what are the situations an exception handling routine? would be required ?
# DIVISION BY ZERO
# RUNTIME ERROR
# FILE DOES NOT EXIST
# INVALID ARRAY INDEX
# INVALID INPUT

# Describe the benefits of using exception handling in a program ?
# the program will not crash
# results does not cause further errors
# Appropriate error message
# exception handling conditions are indentified
# improve readability


# syntax of Exception Handling

#try:
#    code which might
#    contain exception
#except:
#    print("customised error")


try:
    file = open("high.txt","r")
    temp = file.read()
    print(temp)
except:
    print("file does not exist")

# if try does not execute due to error then it executes except
try:
    file = open("HighScore.txt","r")
    temp = file.read()
    print(temp)
except:
    print("file does not exist")
num = 2
print(num)


#
try:
    num = int(input("enter a number: ")) # error : string is input/ value error
    print(num)
except:
    print("wrong input kindly write an integer value as asked")


#
try:
    num = 5/0
    print(num)
except:
    print("cant divide by zero")


#
try:
    file = open("progress.txt", "r")
    gamedata = file
    file.close()
except:
    print("the file does not exist")


#
try:
    file = open("HighScore.txt", "r")
    gamedata = file.read()
    print(gamedata)
    file.close()

except:
    print("the file doest not exist")

#
try:
    num = 5/0
    print(num)
except:
    print("cant divide by zero")

print("check")

# SPECIFIC EXCEPTION

# VALUE ERROR ( DATA TYPE ERRORS)
# ZERO DIVISION ERROR
# IO ERROR  (FILE ERRORS)



try:
    file = open("High.txt", "r")
    gamedata = file.read()
    print(gamedata)
    file.close()

except IOError:
    print("the file doest not exist")


#

try:
    file = open("HighScore.txt", "r")
    gamedata = file.read()
    print(gamedata)
    file.close()

    #num = 5/0  # this is zero divsion error how ever we have specified IOERROR
    #print(num) # for except..so excpet does take place on this error
                # it will show error for this part of code

except IOError:
    print("the file doest not exist")


######
try:
    try:
        file = open("High.txt", "r")
        gamedata = file.read()
        print(gamedata)
        file.close()
    except IOError:
        print("file does not exist")


    num = 5/0
    print(num)

except ZeroDivisionError:
    print("cant divide 5 by zero")


###

try:
    num = int(input("enter the number:"))
    print(num)
except ValueError: # related to value error
    print("kindly write Integer value")




