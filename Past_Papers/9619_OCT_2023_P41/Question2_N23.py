# DECLARE Queue : ARRAY [1:50] OF STRING
global Queue
global HeadPointer
global TailPointer
Queue = [""]* 50
HeadPointer =-1
TailPointer = 0



def Enqueue(valueinput):
    global TailPointer
    global Queue
    global HeadPointer

    if TailPointer ==50:
        print("the Queue is already full")
    else:
        Queue[TailPointer] = valueinput
        TailPointer = TailPointer + 1
        if HeadPointer ==-1:
            HeadPointer = 0




def DeQueue():
    global HeadPointer
    global Queue
    global TailPointer

    if HeadPointer == -1 :
        print("the Queue is empty")
        return "Empty"
    else:
        returnvalue=  Queue[HeadPointer]
        HeadPointer = HeadPointer + 1

        if HeadPointer == TailPointer:
            HeadPointer= -1
            TailPointer = 0
        return returnvalue

def ReadData():

    try:
        file = open("QueueData.txt","r")
        for line in file:
            temp = line.strip()
            Enqueue(temp)
        file.close()
    except IOError:
        print("file was not found ")


class RecordData():
    # PUBLIC ID: string
    # PUBLIC Total : INTEGER

    def __init__(self,IDP,TOTalP):
        self.ID = IDP
        self.Total = TOTalP


# DECLARE Records : ARRAY [1:50]  OF RecordData
global Records
global NumberRecords
NumberRecords = 0
Records = []

for x in range(50):
    Records.append(RecordData("",0))

def TotalData():
    global NumberRecords
    global Records

    # DECLARE DataAccessed : STRING
    # DECLARE Flag : BOOLEAN
    DataAccessed = DeQueue()
    Flag = False
    if NumberRecords == 0 :
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords = NumberRecords + 1
    else:
        for x in range(0,NumberRecords):
            if Records[x].ID  == DataAccessed:
                Records[x].Total = Records[x].Total + 1
                Flag = True

    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total =  1
        NumberRecords = NumberRecords + 1




def OutputRecords():
    global Records
    global NumberRecords

    for x in range(NumberRecords):
        IDtemp  = Records[x].ID
        totaltemp = Records[x].Total
        print("ID"+" "+ str(IDtemp)+ " " + "Total" + " " + str(totaltemp))


ReadData()
while HeadPointer != -1:
    TotalData()
OutputRecords()
