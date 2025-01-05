# STACK AND FILES
# june 2023

# DECLARE Animal : ARRAY[0:19] of STRING
# DECLARE Colour : ARRAY [0:9] OF STRING
global Animal
global AnimalTopPointer
global ColourTopPointer
global Colour
Colour = [""]* 10
Animal = [""]* 20
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    global Animal

    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer +1
        return True


def PopAnimal():
    global Animal
    global AnimalTopPointer
    ReturnData = 0
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer = AnimalTopPointer -1
        ReturnData = Animal[AnimalTopPointer]
        return ReturnData


def ReadData():
    global Animal
    global AnimalTopPointer
    try:
        file = open("AnimalData.txt","r")
        for line in file:
            animalname = line.strip()
            PushAnimal(animalname)
        file.close()
    except IOError:
        print("file does not exist")

    try:
        file = open("ColourData.txt", "r")
        for line in file:
            colour = line.strip()
            PushColour(colour)
        file.close()
    except IOError:
        print("file does not exist")


def PushColour(value):
    global ColourTopPointer
    global Colour

    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = value
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    global Colour
    global ColourTopPointer
    ReturnData = 0
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer = ColourTopPointer -1
        ReturnData = Colour[ColourTopPointer]
        return ReturnData


def OutputItem():

    colourpop =PopColour()
    animapop = PopAnimal()


    if colourpop == "":
        PushAnimal(animapop)
        print("No Colour")

    elif animapop == "":
        PopColour(colourpop)
        print("No Animal")

    else:
        print(colourpop + " " + animapop)


ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()
