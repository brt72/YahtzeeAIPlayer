import re
from Constants import *

def checkMaxFreq(diceList):
    maxFreq = 0
    for num in range(MAX_DIE_VALUE):
        freq = diceList.count(num+1)
        if freq > maxFreq:
            maxFreq = freq
            maxNum = num+1
    return (maxNum, maxFreq)

# Checks how many points could be scored if "Ones" is selected
def checkOnes(diceList):
    diceList = diceList.count(DIE_VALUE_ONE)
    return DIE_VALUE_ONE*diceList

# Checks how many points could be scored if "Twos" is selected
def checkTwos(diceList):
    diceList = diceList.count(DIE_VALUE_TWO)
    return DIE_VALUE_TWO*diceList

# Checks how many points could be scored if "Threes" is selected
def checkThrees(diceList):
    diceList = diceList.count(DIE_VALUE_THREE)
    return DIE_VALUE_THREE*diceList

# Checks how many points could be scored if "Fours" is selected
def checkFours(diceList):
    diceList = diceList.count(DIE_VALUE_FOUR)
    return DIE_VALUE_FOUR*diceList

# Checks how many points could be scored if "Fives" is selected
def checkFives(diceList):
    diceList = diceList.count(DIE_VALUE_FIVE)
    return DIE_VALUE_FIVE*diceList

# Checks how many points could be scored if "Sixes" is selected
def checkSixes(diceList):
    diceList = diceList.count(DIE_VALUE_SIX)
    return DIE_VALUE_SIX*diceList

# Checks how many points could be scored if "Three of a Kind" is selected
def checkThreeKind(diceList):
    diceFreq = 0
    if diceFreq <= 2:
        for number in range(MAX_DIE_VALUE):
            freq = diceList.count(number+1)
            if freq >= THREE_FREQ:
                return sum(diceList)
            else:
                diceFreq += freq
    return POINTS_ZERO

# Checks how many points could be scored if "Four of a Kind" is selected
def checkFourKind(diceList):
    diceFreq = 0
    if diceFreq <= 1:
        for number in range(MAX_DIE_VALUE):
            freq = diceList.count( number+1)
            if freq >= FOUR_FREQ:
                return sum(diceList)
            else:
                diceFreq += freq
    return POINT_INDEX

# Checks how many points could be scored if "Full House" is selected
def checkFullHouse(diceList):
    if(diceList[DIE_INDEX_ZERO] == diceList[DIE_INDEX_ONE] and diceList[DIE_INDEX_TWO] == diceList[DIE_INDEX_FOUR]):
        return POINTS_FULL_HOUSE
    if(diceList[DIE_INDEX_ZERO] == diceList[DIE_INDEX_TWO] and diceList[DIE_INDEX_THREE] == diceList[DIE_INDEX_FOUR]):
        return POINTS_FULL_HOUSE
    return POINTS_ZERO

# Checks how many points could be scored if "Small Straight" is selected
def checkSmallStraight(diceList):
    if(diceList[DIE_INDEX_ZERO]+1 == diceList[DIE_INDEX_ONE] and diceList[DIE_INDEX_ONE]+1 == diceList[DIE_INDEX_TWO] and diceList[DIE_INDEX_TWO]+1 == diceList[DIE_INDEX_THREE]):
        return POINTS_SMALL_STRAIGHT
    if(diceList[DIE_INDEX_ONE]+1 == diceList[DIE_INDEX_TWO] and diceList[DIE_INDEX_TWO]+1 == diceList[DIE_INDEX_THREE] and diceList[DIE_INDEX_THREE]+1 == diceList[DIE_INDEX_FOUR]):
        return POINTS_SMALL_STRAIGHT
    return POINTS_ZERO

# Checks how many points could be scored if "Large Straight" is selected
def checkLargeStraight(diceList):
    if(diceList[DIE_INDEX_ZERO]+1 == diceList[DIE_INDEX_ONE] and diceList[DIE_INDEX_ONE]+1 == diceList[DIE_INDEX_TWO] and diceList[DIE_INDEX_TWO]+1 == diceList[DIE_INDEX_THREE] and diceList[DIE_INDEX_THREE]+1 == diceList[DIE_INDEX_FOUR]):
        return POINTS_LARGE_STRAIGHT
    return POINTS_ZERO

# Checks how many points could be scored if "Yacht" is selected
def checkYacht(diceList):
    freq = diceList.count(diceList[DIE_INDEX_ZERO])
    if freq == MAX_DICE:
        return POINTS_YACHT
    return POINTS_ZERO

# Checks how many points could be scored if "Chance" is selected
def checkChance(diceList):
    return(sum(diceList))