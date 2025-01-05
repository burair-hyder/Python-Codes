class Card():
    # PRIVATE Number : INTEGER
    # PRIVATE Colour : STRING

    def __init__(self,Numberp,Colourp):
        self.__Number = Numberp
        self.__Colour = Colourp

    def GetNumber(self):
        return self.__Number

    def GetColour(self):
        return self.__Colour

card1red = Card(1,"red")
card2red = Card(2,"red")
card3red = Card(3,"red")
card4red = Card(4,"red")
card5red = Card(5,"red")

card1blue = Card(1,"blue")
card2blue = Card(2,"blue")
card3blue = Card(3,"blue")
card4blue = Card(4,"blue")
car5blue = Card(5,"blue")

card1yellow = Card(1,"Yellow")
card2yellow = Card(2,"Yellow")
card3yellow = Card(3,"Yellow")
card4yellow = Card(4,"Yellow")
card5yellow = Card(5,"Yellow")


class Hand():
    # PRIVATE FirstCard : INTEGER
    # PRIVATE NumberCards : INTEGER
    # PRIVATE Cards : ARRAY[0:9] OF Card

    def __init__(self,card1,card2,card3,card4,card5):
        self.__FirstCard = 0
        self.__NumberCards = 5
        self.__Cards= [""]*10
        self.__Cards[0] = card1
        self.__Cards[1] = card2
        self.__Cards[2] = card3
        self.__Cards[3] = card4
        self.__Cards[4] = card5

    def GetCard(self,indexp):
        return self.__Cards[indexp]



player1 = Hand(card1red,card2red,card3red,card4red,card1yellow)
player2 = Hand(card2yellow,card3yellow,card4yellow,card5yellow,card1blue)

def CalculateValue(hand):
    playerscore = 0
    for x in range(5):
        temp =hand.GetCard(x)
        number = temp.GetNumber()
        if temp.GetColour() == "red":
            playerscore =playerscore + 5
        elif temp.GetColour() == "blue":
            playerscore = playerscore + 10
        else:
            playerscore = playerscore + 15
        playerscore = playerscore + number
    return playerscore bnb    

score2 = (CalculateValue(player2))
score1 = (CalculateValue(player1))
if score1 > score2:
    print("player 1 wins")
elif score2 > score1:
    print("player2 wins")
else:
    print("draw")

print("score of player 1 is ", score1)
print("score of player 2 is ", score2)
