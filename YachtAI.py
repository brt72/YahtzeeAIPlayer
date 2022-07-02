from Constants import CARD_SIZE
from Turn import take_turn
from PlayCard import PlayCard

def runAI():
    yachtCard = PlayCard()
    for turns in range(CARD_SIZE):
        yachtCard = take_turn(yachtCard)
    print(yachtCard)
    