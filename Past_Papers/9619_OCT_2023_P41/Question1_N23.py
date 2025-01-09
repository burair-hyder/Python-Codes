def IterativeVowels(Value):
    Total = 0
    LengthString = len(Value)

    for x in range(LengthString):
        FirstCharacter = Value[0]

        if FirstCharacter == 'a' or FirstCharacter == 'e'  or FirstCharacter == 'i' or  FirstCharacter == 'o' or FirstCharacter == 'u':
            Total = Total + 1

        Value = Value[1:len(Value)]

    return Total




def RecursivVowels(value):
    LengthString = len(value)
    if LengthString == 0:
        return 0
    else:
        FirstCharacter = value[0]

        if FirstCharacter == 'a' or FirstCharacter == 'e' or FirstCharacter == 'i' or FirstCharacter == 'o' or FirstCharacter == 'u':
            value = value[1:len(value)]
            return RecursivVowels(value) + 1
        else:
            value = value[1:len(value)]
            return RecursivVowels(value)

temp = RecursivVowels("imagine")
print(temp)
