""" Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_inx: int = 0
low_card: int = int(cards[0])
#look at each number in the string
while card_inx < 4:
    #check if currect card is less than low card
    current_card: int = int(cards[card_inx])
    if (current_card < low_card):
        #update the low card
        low_card = current_card
    card_inx = card_inx + 1
print(low_card)