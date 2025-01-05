# DECLARE Queue : ARRAY[0:99]  OF INTEGER
global Queue
global Headpointer
global Tailpointer
Headpointer = -1
Tailpointer = 0
Queue = [0]*100

def Enqueue(valuetoinsert):
    global Queue
    global Headpointer
    global Tailpointer

    if Tailpointer <100:
        Queue[Tailpointer] = valuetoinsert
        Tailpointer= Tailpointer + 1


        if Headpointer == -1:
            Headpointer=0
        return True
    else:
        return False



def DeQueue():
    global Queue
    global Headpointer
    global Tailpointer

    #  check if empty already
    if Headpointer == -1:
        return False
    dataremoved = Queue[Headpointer]
    Headpointer = Headpointer + 1

    if Headpointer == Tailpointer:
        Headpointer = -1
        Tailpointer =0

    return True

finalflag = True
for x in range(1,21):
    temp = Enqueue(x)
    if temp != True:
        finalflag = False

if finalflag == True:
    print("successfull")
else:
    print("unsuccesfull")
