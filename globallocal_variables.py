
#
# global
# local
# by value  : actual value is not changed and you pass only the copy
# by reference/global : actual value is changed and the address is passed

number = 0  # Scope : Global

def check():
    global number  # now  passes by reference
    number = 3

check()
#print(number)  # prints 3


# Global Scope : Any value/variable which exists outside functions
# Local Scope : Any value/variable which exists inside fucntions


# local variable
number = 0

def new():
    test = 3  # Local Variable Which only exists inside function and print outside function
    print(test)
new()

# global variable

number = 0 #  this is global scope means outside function
def new():
    number = 4 # LOCAL inside fucntion only
    print("this is inside function value:",number)

new()

print("this is number outside function Global scope: ",number)


# passing as global

number = 0

def new():
    global number
    number = 4  # changes the value is original address,Now it is GLOBAL
    print("this is inside function value local scope :",number)

new()
print("this is outside function value global scope :",number)



# array

# for arrays there is no issue for global or local
# but for exam we have to write global just for examiner
# even without global this would work fine

array1 = [3,5,2]

def new():
    global array1
    array1[0] = 6
new()
print(array1)
