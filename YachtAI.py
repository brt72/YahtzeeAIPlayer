from Constants import CARD_SIZE
from Turn import takeTurn
from PlayCard import PlayCard

def runAI():
    yachtCard = PlayCard()
    for turns in range(CARD_SIZE):
        yachtCard = takeTurn(yachtCard)
    print(yachtCard)
    