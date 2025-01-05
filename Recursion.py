# what is meant by recursion
# when a function/procedure calls itself


def recursion(x):
    y = x * 2
    print(y)
    recursion(y)

#recursion(4)

# this is recursive function in pythong that takes an argument
# x, doubles it , and then calls itself with the result as the new argument.
# the function will keep calling itself recursively, doubling the argument each time
# and printing out the result, untill it encounters and error due to reaching
# Python's maximum recursion depth



# the base case and the general case are two important concepts in recursion
# that are used to control the flow of a recursive function

# the base case is the condition that determines when the recursion should stop.
# it is the condition that prevents the function from calling itself again and again
# and allows function to return a value. In other words, the base case is the stopping point for the
# recursion. it is the case where is problem i simple enough that the function does not need to
# call itself anymore

# the general case, on the other hand , it the opposite  of the base case. it is the
# the condition that  determines when the recursion should continue. in the general case,
# function is not yet at the stopping point and needs to call itself again with a smaller
# or simpler version of the problem . this continues untill the base case is reached


def recursion(x):
    y = x * 2
    print(y)
    if y < 10000: # GENERAL CASE ,runs if this is true
        recursion(y)

#recursion(4)

# the base case is when y >= 10000
# the general case is when  y < 10000



# what is meant by Recursive Algorithm?
# any algorithm that have a base case ,work towards a base case,
# have a general case and calls itself



# CONCEPT OF WINDING AND UNWINDING

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

temp = factorial(5)
print(temp)


# winding : is done in general case in which the function calls are getting
#           pushed in the stack , no calculation is done in this phase

# Unwinding : when the base case is reached all the data stored in stack
#             gets popped out from the top of the stack

# first winds then unwinds


# explain what a compiler has to do to implement recursion?

# when the recursive call is made all value are put on the stack which is known
# as winding when the base case is met the algorithm unwinds. the last set of values
# are taken off the stack in reverse order



#   QUESTION
# converted pesudcode to python

def Unknown(X,Y):
    if X < Y:
        print(X+Y)
        return (Unknown(X+1,Y)*2)
    elif X == Y:
        return 1
    else:
        print(X+Y)
        return (Unknown(X-1,Y) // 2)


def iterativeUnknown(X,Y):
    total = 1

    while X !=Y:
        if X > Y:
            print(X+Y)
            X= X + 1
            total = total *2
        else:
            print(X+Y)
            X= X -1
            total = total // 2

    return total

