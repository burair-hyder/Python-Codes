# mj 2021 p41

# question 1
# part a

class node():
    # PUBLIC data : INTEGER
    # PUBLIC nextNode : INTEGERQue

    def __init__(self,datap,nextnodep):
        self.data = datap
        self.nextNode = nextnodep


# question 1 part b
# DECLARE Linkedlist : ARRAY [0:9] Of node

Linkedlist = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]

startPointer = 0
emptyList  = 5

# question part c i
def outputNodes():
    global Linkedlist
    global startPointer
    currentpointer = startPointer

    while currentpointer != -1:
        print(Linkedlist[currentpointer].data)
        currentpointer = Linkedlist[currentpointer].nextNode




# question d i
def addNode(currentpointer):
    global Linkedlist
    global emptyList

    inputvalue = input("enter a data value")

    nextnode = node(inputvalue,-1)

    if  emptyList > 9 and emptyList < 0:
        return False

    freelist = emptyList
    emptyList = Linkedlist[emptyList].nextNode

    Linkedlist[freelist]= nextnode

    previouspointer = 0
    while currentpointer != -1 :
        previouspointer = currentpointer
        currentpointer = Linkedlist[currentpointer].nextNode

    Linkedlist[previouspointer].nextNode = freelist

    return True



outputNodes()
# question d ii
temp = addNode(startPointer)
if temp == True:
    print("node was succesfully added")
else:
    print("node was not added")


outputNodes()
