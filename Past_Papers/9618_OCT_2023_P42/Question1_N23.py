# DECLARE StackVowel : ARRAY [0:99] OF STRING
# DECLARE StackConsonant : ARRAY [0:99] OF STRING
global StackVowel
global StackConsonant
StackVowel = [""]*100
StackConsonant = [""]*100

global VowelTop
global ConsonantTop
VowelTop = 0
ConsonantTop = 0


def PushData(letter):
    global StackVowel
    global StackConsonant
    global VowelTop
    global ConsonantTop

    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        if VowelTop >= 100:
            print("the stack vowel is full")
        else:
            StackVowel[VowelTop] = letter
            VowelTop = VowelTop + 1

    else:
        if ConsonantTop >= 100:
            print("the stack consonant is full")
        else:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop = ConsonantTop + 1




def ReadData():
    try:
        file= open("StackData.txt","r")
        for x in range(100):
            check = file.readline().strip()
            PushData(check)

        file.close()
    except IOError:
        print("file not found")

def PopVowel():
    global StackVowel
    global VowelTop

    if VowelTop <= 0:
        return "No Data"




    VowelTop = VowelTop - 1
    returnitem = StackVowel[VowelTop]
    return returnitem


def PopConsonant():
    global StackConsonant
    global ConsonantTop

    if ConsonantTop <= 0:
        return "No Data"



    ConsonantTop = ConsonantTop - 1
    returnitem = StackConsonant[ConsonantTop]
    return returnitem


ReadData()
temp = ""
x= 0
while x < 5:
    inputchoice = input("Enter your Choice: vowel or consonant:")
    if inputchoice.lower() == "vowel":
        char  = PopVowel()
        if char != "No Data":
            temp = temp + char
            x= x+1
        else:
            print("the stack is empty")
    elif inputchoice.lower() == "consonant":
        char = PopConsonant()
        if char != "No Data":
            temp = temp + char
            x = x + 1
        else:
            print("stack is empty")
    else:
        print("enter a valid choice ")

print(temp)
