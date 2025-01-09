def IterativeCalculate(Number):
    # DECLARE Total : INTEGER
    # DEACLARE ToFind : INTEGER
    ToFind  = Number
    Total  = 0
    while Number != 0:
        if ToFind % Number ==0:
            Total = Total + Number

        Number = Number - 1
    return Total

print(IterativeCalculate(10))


def RecusriveValue(Number,ToFind):
    if Number == 0:
        return 0
    elif ToFind % Number == 0:
        return Number + RecusriveValue(Number-1,ToFind)
    else:
        return RecusriveValue(Number-1,ToFind)

temp = RecusriveValue(50,50)
print("the recursive value is :",temp)
