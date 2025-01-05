# ABSTRACT DATATYPE:
# an abstract datatype is a collection of data and set of operations on that data
# stack # queue #linked list  #binary tree

# STACKs

# a list containing several items operating on the last in first out
# principle (LIFO)
# items can be added to the stack (PUSH) AND removed from the stack (POP)
# the first item added to the stack is the last item removed from the stack

# PUSH

Names =  [" "] * 5
stackpointer = 0

def Push(value):
    global Names
    global stackpointer

    if stackpointer > 4: # check if array is full
        print("Stack Full")
    else:
        Names[stackpointer] = value
        stackpointer = stackpointer + 1


# POP

def Pop():
    global Names
    global stackpointer

    if stackpointer == 0: # check if array is empty
        print("Stack Empty")
    else:
        stackpointer = stackpointer - 1
        print(Names[stackpointer])


#Push("burair")
#Push("ali")
#Push("Alishba")
#Push("zainab")
#Push("Adil")

#Pop()
#Push("Meerub")
#Pop()
#Pop()
#Pop()
#Pop()
#Pop()
#Pop()

#print(Names)

# if stackpointer starts from -1
names = [''] * 5
stackpointer = -1

def push(value):
    global names
    global stackpointer
    if stackpointer == 4:
        print("Full")
    else:
        stackpointer = stackpointer + 1
        names[stackpointer] = value

def pop():
    global names
    global stackpointer
    if stackpointer == -1:
        print("Stack empty")
    else:
        names[stackpointer] = ""
        stackpointer = stackpointer -1


#push("burair")
#push("ali")
#push("Alishba")
#push("zainab")
#push("Adil")
#push("heelow")
#pop()
#pop()
#pop()
#pop()
#pop()
#pop()
#pop()
#print(names)


# PAST PAPER QUESTION

# DECLARE StackData : ARRAY[0:9] OF INTEGER
# DECLARE StackPointer : INTEGER
global StackData
global StackPointer
StackData = [0] * 10
StackPointer = 0

def PrintArray():
    global StackPointer
    global StackData
    for x in range(10):
        print(StackData[x])
    print("stack pointer is :",StackPointer)

def Push(value):
    global StackPointer
    global StackData
    if StackPointer > 9:
        return False
    else:
        StackData[StackPointer] = value
        StackPointer = StackPointer + 1
        return True


#for x in range(11):
 #   num = int(input("enter value to add to stack :"))
  #  temp = Push(num)
   # if temp == True:
    #   print("the value was successfully added to the stack")
    #else:
     #   print("the stack is full ,value not added")
#PrintArray()

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        StackPointer = StackPointer -1
        temp = StackData[StackPointer]
        return temp


# QUEUE

# a list containing several items operating on the first in first out
# principle ( FIFO).
# The first item added is the first item removed from the queue
# in queue the data is added from the rear end by using the ENDPOINTER
# and removed from the front by using the STARTPOINTER
# TAIL POINTER = ADD
# HEAD POINTER = REMOVE


# LINEAR ENQUEUE

# First condition will check if the queue is empty by comparing it with the max
# index value. the item will be inserted by using the tail pointer.
# after inserting the item we will check if the head pointer from where the item
# is removed is still pointing -1 then we have to point to the first value which was
# added


# DECLARE Names : ARRAY[0:9] OF STRING
Names = [""] * 10
HeadPointer = -1
TailPointer = 0

def Enqueue(name):
    global Names
    global HeadPointer
    global TailPointer

    if TailPointer <10:
        Names[TailPointer] = name
        TailPointer = TailPointer + 1

        if HeadPointer == -1:
            HeadPointer = 0
    else:
        print("Queue is Full")


# LINEAR DEQUEUE

# there are 2 ways that queue is considered to be empty
# 1) if Head pointer is pointing towards -1 this will only happen when
#    there was no value enqueued in the queue

# 2) if the head pointer is equal to the tail pointer which means that all the
#    values which were enqueued in queue are now removed

def Dequeue():
    global HeadPointer
    global TailPointer
    global Names

    if HeadPointer == -1:
        print("Queue is Empty")
    else:
        item = Names[HeadPointer]
        HeadPointer = HeadPointer + 1
        print(item)

    if HeadPointer == TailPointer:
        TailPointer = 0
        HeadPointer = -1


Enqueue("burair")
Enqueue("Ali")
Enqueue("Dania")
Enqueue("Bano")
Enqueue("Alishba")
Enqueue("Zainab")
Enqueue("shabana")
Enqueue("fazeela")
Enqueue("Masooma")
#Enqueue("Ramzan")
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Dequeue()
#Enqueue("Taimoor")
#Enqueue("Ramzan")
#Enqueue("Zainab")
#print(Names)


# LINEAR VS CIRCULAR QUEUE

# the condition for a linear queue being full is that tail pointer should
# point towards upperbound or the max index


# CIRCULAR QUEUE :

# DECLARE QueueArray : ARRAY[0:9] OF STRING
global headpointer
global tailpointer
global Numberofitems
headpointer = 0
tailpointer = 0
Numberofitems = 0
QueueArray = [""]* 10


# can not pass parameter as byref so have declared them as global
def  Enqueue(DataToAdd):
    global QueueArray
    global headpointer
    global tailpointer
    global Numberofitems

    if Numberofitems >=10:
        return False

    QueueArray[tailpointer] = DataToAdd

    if tailpointer >=9:
        tailpointer = 0
    else:
        tailpointer = tailpointer + 1


    Numberofitems = Numberofitems + 1
    return True




def Dequeue():
    global headpointer
    global tailpointer
    global Numberofitems
    global QueueArray

    if Numberofitems == 0:
        return False
    else:
        value = QueueArray[headpointer]
        headpointer = headpointer + 1

        if headpointer >9:
            headpointer =0

        Numberofitems = Numberofitems -1
        return value


Enqueue("A")
Enqueue("B")
Enqueue("C")
Enqueue("D")
Enqueue("E")
Enqueue("F")
Enqueue("G")
Enqueue("H")
Enqueue("I")
Enqueue("J")

print(Dequeue())
print(Dequeue())
print(Dequeue())

Enqueue("Ali")
Enqueue("bano")
Enqueue("syed")


print(Enqueue("check"))

print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())
print(Dequeue())

print("tail pointer:",tailpointer)

print("head pointer :", headpointer)
print("Number of items :",Numberofitems)
print(QueueArray)



# LINKED LIST

# ADD
# SEARCH
# DELETE

# what is node
# it contains DATA and pointer
# pointer contains location of the next pointer
# node is a class/ record

class node():
    def __init__(self,dataP,PointerP):
        self.Data = dataP
        self.Pointer = PointerP\


linkedlist = [node("20",3),node("",-1),node("",-1 ),node("15",4) ,node("30",-1) ]
# linked list is created in array of record data type

newnode = node("45",-1)


point = linkedlist[4].Pointer
temp = linkedlist[4 ].Data
print(point)
print(temp)


# INCREMENT IN POINTER
# startpointer = 2
# currentpointer = startpointer
# currentpointer = linkedlist[currentpointer].nextnode


# ORDERED LINKED LIST AND UNORDERED LINKED LIST

#  A linked list is data structure used to store a collection of items
#  where each item is



# ADDING NODE IN A LINKED LIST

# STEP 1 : CHECKING IF THE LIST IS FULL OR NOT
# STEP 2 : IS INCREMENTING EMPTY LIST POINTER
# STEP 3 : CREATE A NEW NODE AND STORE IN THE FREELIST POSITION
# STEP 4 : SEARCH FOR LAST NODE LOCATION
# STEP 5 : LASTNODE.NEXTNODE = FREELIST



# CODE FOR ADDING NODE


class node():
    # PUBLIC Data : INTEGER
    # PUBLIC nextNode: INTEGER

    def __init__(self,Datap,nextNodeP):
        self.Data = Datap
        self.nextnode = nextNodeP



# DECLARE Linkedlist : ARRAY [0:9] OF node
Linkedlist = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startpointer = 0
emptylist  = 5


def addNode(currentpointer):
    global Linkedlist
    global emptylist
    data = input("Enter the data to Add:")
    # CHECK IF THE LINKED LIST IF FULL OR NOT

    if emptylist <0 or emptylist > 9: # empty is null .null is anything outside range
        return False
    else:
        # INCREMENT EMPTYLIST POINTER AFTER STORING IT IN A TEMPORARY VARIABLE KNOWN AS freelist
        freelist = emptylist
        emptylist = Linkedlist[emptylist].nextnode

        # CREATE A NEW NODE
        newnode = node(data,-1)

        # store it where the freelist is pointing

        Linkedlist[freelist] = newnode

        # NOW YOU HAVE TO FIND THE LAST NODE INDEX

        previouspointer = 0
        while currentpointer != -1:
            previouspointer = currentpointer
            currentpointer = Linkedlist[currentpointer].nextnode

        Linkedlist[previouspointer].nextnode = freelist
        return True

addNode(startpointer)
for  x in range(len(Linkedlist)):
    print(Linkedlist[x].Data,Linkedlist[x].nextnode)
print("Empty list:", emptylist)


# LINKED LIST DELETION

# CASE 1 :
# if node is in middle

# STEP 1 :  SEARCH FOR THE DATA / LOCATION OF NODE
# STEP 2 : current pointer  = start pointer (index of data)
# STEP 3 : previous pointer = current pointer
# STEP 4 : current pointer = linkedlist[current pointer ].next node
# STEP 5 : linkedlist [previous pointer].next_node = linkedlist [current pointer].next_node

# CASE 2:
# if node is in start

# STEP 1 : IF current pointer  == start pointer  (ensures it is first node)
# STEP 2 : start pointer = linkedlist[current pointer].next_node

#     how to set removed node
# we have to add it to the empty list

# STEP 1 : EMPTY THE DATA IN NODE
#          Linkedlist[current pointer].Data == 0 / ""
# STEP 2 : CONNECT THE NODE TO THE FIRST NODE OF EMPTY LIST
#          linkedlist[current pointer].next_node = Empty list
# STEP 3 : CHANGE THE VALUE OF EMPTY LIST TO POINT TOWARDS THE NEW FIRST NODE ADDED
#           Empty list  = current pointer



# CODE FOR DELETION OF NODE :

def deleteNode():
    global Linkedlist
    global emptylist
    global startpointer

    currentpointer = startpointer

    DataToremove = input("Enter the Data that you want to remove:")

    # SEARCH THE INDEX OF THE ELEMENT YOU WANT TO REMOVE
    previouspointer = 0
    while currentpointer != -1 and Linkedlist[currentpointer].Data != DataToremove:
        previouspointer = currentpointer
        currentpointer = Linkedlist[currentpointer].nextnode


    # FIRST CONDITION check if it exsists or not by currentpointer
    if currentpointer == -1:
        return False
    else:
        # IN ELSE WE WILL HAVE TWO CASES  1) start node to be removed or any other
        if startpointer == currentpointer:
            startpointer = Linkedlist[currentpointer].nextnode # incrementing start pointer

        else:
            Linkedlist[previouspointer].nextnode  = Linkedlist[currentpointer].nextnode


        Linkedlist[currentpointer].Data = 0
        Linkedlist[currentpointer].nextnode = emptylist
        emptylist = currentpointer
        return True




def DeleteNode(currentpointer):
    global Linkedlist
    global startpointer
    global emptylist
    data = input("enter data to delete")

    while currentpointer!= -1 and Linkedlist[currentpointer].Data != data:
        previouspointer = currentpointer
        currentpointer = Linkedlist[currentpointer].nextnode

    if currentpointer == -1:
        return "data not present "
    else:
        if currentpointer == startpointer:
            startpointer = Linkedlist[startpointer].nextnode
        else:
            Linkedlist[previouspointer].nextnode = Linkedlist[currentpointer].nextnode

    Linkedlist[currentpointer].Data = 0
    Linkedlist[currentpointer].nextnode = emptylist
    emptylist = currentpointer

# PRINTING ALL THE VALUES OF THE LINKED LIST
def outputNode(currentpointer):
    # can not take them as byref parameters so have taken as global
    global Linkedlist
     # taking global is taking parameter
    while currentpointer != -1:
        print(str(Linkedlist[currentpointer].Data))
        currentpointer = Linkedlist[currentpointer].nextnode

outputNode(startpointer)


# SEARCHING IN A LINKED LIST

# for searching a particular element or value you are suppose to use the
# concept of increment in a linked list and compare the value of each
# element in the linked list with the value you are searching and return
# the current pointer as it will be used to increment


def FindItem(currentpointer,SearchValue):
    global Linkedlist
    while currentpointer != -1 :
        if Linkedlist[currentpointer].Data == SearchValue:
            return currentpointer
        else:
            currentpointer = Linkedlist[currentpointer].nextnode


    return currentpointer


test = FindItem(startpointer,56)
print(test)



# INSERTING IN AN ORDERED LINKED LIST


# inserting in an ordered linked list is to some extent similar to the insertion in an unordered linked
# list .But in this you first have to find the correct position and then insert the node

# take input .....(data = 9)
# check if there is space in linked list using value of empty list
# free list = empty list
# increment empty list
# make new node
# newnode= node(9,-1)
# store this new node at free list index in linked list
# linkedlist[freelist] = newnode
# find the correct location to insert the value 6 as linked list is ordered
# while currentpointer != -1 and 9 > linkedlist[currentpointer].Data:
#       previouspointer = currentpointer
#       currentpointer = linkedlist.[currentpointer].nextnode

# linkedlist[freelist].nextnode = linkedlist[previouspointer].nextnode   # or use  = current pointer
# linkedlist[previouspointer].nextnode = freelist

# what if value is added at the start ( first node)

# if currentpointer = startpointer
# linkedlist[freelist].nextnode = startpointer
# startpointer = freelist



# CODE FOR INSERTION OF NODE IN AN ORDERED LINKED LIST


def OrderedInsertion(currentpointer):
    global Linkedlist
    global startpointer
    global emptylist

    datatoinsert = int(input("Enter the value to insert:"))

    # CHECK DO YOU HAVE SPACE OR NOT

    if emptylist <0 or emptylist >9:
        return False
    else:
        freelist = emptylist
        emptylist = Linkedlist[emptylist].nextnode

        # CREATE A NEW NODE

        NEWnode = node(datatoinsert,-1)
        # STORE IT BY USING FREELIST
        Linkedlist[freelist].Data = NEWnode

        # NOW FIND THE CORRECT POSTION TO INSERT THE NODE
        previouspoitner = 0
        while currentpointer != -1 and datatoinsert > Linkedlist[currentpointer].Data:
            previouspointer = currentpointer
            currentpointer = Linkedlist[currentpointer].nextnode

        # check condition whether it is stored in start or in between
        if currentpointer == startpointer:
            Linkedlist[freelist].nextnode = startpointer
            startpointer = freelist
        else:
            Linkedlist[freelist].nextnode = Linkedlist[previouspoitner].nextnode
            Linkedlist[previouspointer].nextnode = freelist

        return True






def OrederedLinkedlistAddNode(currentpointer)
    global Linkedlist
    global emptylist
    global startpointer

    data = input("enter value to add")

    if emptylist<0 and emptylist >9:
        return False
    else:
        frelist = emptylist
        emptylist = Linkedlist[emptylist].nextnode
        newnode = node(data,-1)
        Linkedlist[frelist] = newnode

        previouspointer = 0
        while currentpointer != -1 and Linkedlist[currentpointer].Data < data:
            previouspointer = currentpointer
            currentpointer = Linkedlist[currentpointer].nextnode

        if currentpointer == startpointer:
            Linkedlist[frelist].nextnode = startpointer
            startpointer = frelist
        else:
            Linkedlist[frelist].nextnode = Linkedlist[previouspointer].nextnode
            Linkedlist[previouspointer].nextnode = frelist

