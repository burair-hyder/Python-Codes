# question No 2 part a


# DECLARE arrayData : ARRAY [0:9] of INTEGER
arrayData = []
arrayData.append(10)
arrayData.append(5)
arrayData.append(6)
arrayData.append(7)
arrayData.append(1)
arrayData.append(12)
arrayData.append(13)
arrayData.append(15)
arrayData.append(21)
arrayData.append(8)


# question NO 2 part b


def LinearSearch(valuesearch):
    global  arrayData
    for x in range(10):
        if arrayData[x] == valuesearch:
            return True
    return False

number = int(input("enter a number to search"))
temp = LinearSearch(number)
if temp == True:
    print("the value was found ")
else:
    print("the value was not found")

def bubblesort(thearray):
    # DECALRE temp : INTEGER
    temp = 0
    for x in range(0,10):
        for y in range(0,9):
            if int(thearray[y]) < int(thearray[y + 1]):
                temp = thearray[y]
                thearray[y] = thearray[y+1]
                thearray[y+1] = temp


bubblesort(arrayData)
print(arrayData)
