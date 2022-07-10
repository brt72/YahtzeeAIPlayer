from Constants import *
from CheckHand import *

# Ones, Twos, Threes, Fours, Fives, Sixes Probability (aim for 3)
def probNum(diceList, num):
    freq = diceList.count(num)
    if(freq == ZERO_FREQ):
        probability = PROB_RESULT_N
    elif(freq == ONE_FREQ):
        probability = PROB_RESULT_G
    elif(freq == TWO_FREQ):
        probability = PROB_RESULT_B
    else:
        probability = MAX_PROB_RESULT
    return (num*freq, probability)

def probTok(diceList):
    maxFreq = checkMaxFreq(diceList)
    points = 0
    if(maxFreq[FREQ_INDEX] == ONE_FREQ):
        probability = PROB_RESULT_G
    elif(maxFreq[FREQ_INDEX] == TWO_FREQ):
        probability = PROB_RESULT_B
    else:
        probability = MAX_PROB_RESULT
        points = sum(diceList)
    return(points, probability)

def probFok(diceList):
    maxFreq = checkMaxFreq(diceList)
    points = POINTS_ZERO
    if(maxFreq[FREQ_INDEX] == ONE_FREQ):
        probability = PROB_RESULT_Q
    elif(maxFreq[FREQ_INDEX] == TWO_FREQ):
        probability = PROB_RESULT_K
    elif(maxFreq[FREQ_INDEX] == THREE_FREQ):
        probability = PROB_RESULT_D
    else:
        probability = MAX_PROB_RESULT
        points = sum(diceList)
    return(points, probability)

def getFHState(diceList):
    if checkFullHouse(diceList) != POINTS_ZERO:
        return FH_STATE_FULL_HOUSE
    # Two Pair
    elif diceList[DIE_INDEX_ZERO] == diceList[DIE_INDEX_ONE] and (diceList[DIE_INDEX_TWO] == diceList[3] or diceList[DIE_INDEX_THREE] == diceList[4]) or diceList[DIE_INDEX_ONE] == diceList[DIE_INDEX_TWO] and diceList[DIE_INDEX_THREE] == diceList[DIE_INDEX_FOUR]:
        return FH_STATE_TWO_PAIR
    # 3-1-1
    elif diceList[DIE_INDEX_ZERO] == diceList[DIE_INDEX_TWO] or diceList[DIE_INDEX_ONE] == diceList[3] or diceList[DIE_INDEX_TWO] == diceList[4]:
        return FH_STATE_THREE_OF_KIND
    # One Pair
    elif diceList[DIE_INDEX_ZERO] == diceList[DIE_INDEX_ONE] or diceList[DIE_INDEX_ONE] == diceList[DIE_INDEX_TWO] or diceList[DIE_INDEX_TWO] == diceList[DIE_INDEX_THREE] or diceList[DIE_INDEX_THREE] == diceList[DIE_INDEX_FOUR]:
        return FH_STATE_ONE_PAIR
    # Five Unique Values
    return FH_STATE_FIVE_VALUES


def probFH(diceList):
    points = POINTS_ZERO
    state = getFHState(diceList)
    # Full House
    if state == FH_STATE_FULL_HOUSE:
        points = POINTS_FULL_HOUSE
        probability = MAX_PROB_RESULT
    # Two Pair
    elif state == FH_STATE_TWO_PAIR:
        probability = PROB_RESULT_C
    # 3-1-1
    elif state == FH_STATE_THREE_OF_KIND:
        probability = PROB_RESULT_E
    # One Pair
    elif state == FH_STATE_ONE_PAIR:
        probability = PROB_RESULT_I
    # Five Unique Values
    else:
        probability = PROB_RESULT_M
    return(points, probability)

def getSSCount(diceList):
    allFreq = [diceList.count(DIE_VALUE_ONE), diceList.count(DIE_VALUE_TWO), diceList.count(DIE_VALUE_THREE), diceList.count(DIE_VALUE_FOUR), diceList.count(DIE_VALUE_FIVE), diceList.count(DIE_VALUE_SIX)]
    first = [0,0,0,0] # 1, 2, 3, 4
    middle = [0,0,0,0] # 2, 3, 4, 5
    last = [0,0,0,0] # 3, 4, 5, 6
    if allFreq[DIE_VALUE_ONE-1] > 0:
        first[DIE_VALUE_ONE-1]+=1
    if allFreq[DIE_VALUE_TWO-1] > 0:
        first[DIE_VALUE_TWO-1]+=1
        middle[DIE_VALUE_TWO-2]+=1 
    if allFreq[DIE_VALUE_THREE-1] > 0:
        first[DIE_VALUE_THREE-1]+=1
        middle[DIE_VALUE_THREE-2]+=1  
        last[DIE_VALUE_THREE-3]+=1    
    if allFreq[DIE_VALUE_FOUR-1] > 0:
        first[DIE_VALUE_FOUR-1]+=1
        middle[DIE_VALUE_FOUR-2]+=1  
        last[DIE_VALUE_FOUR-3]+=1  
    if allFreq[DIE_VALUE_FIVE-1] > 0:
        middle[DIE_VALUE_FIVE-2]+=1  
        last[DIE_VALUE_FIVE-3]+=1 
    if allFreq[DIE_VALUE_SIX-1] > 0:
        last[DIE_VALUE_SIX-3]+=1

    return (first, middle, last)

def probSS(diceList):
    points = POINTS_ZERO
    (first, middle, last) = getSSCount(diceList)


    if sum(first) == STRAIGHT_CORRECT_FOUR or sum(middle) == STRAIGHT_CORRECT_FOUR or sum(last) == STRAIGHT_CORRECT_FOUR:
        probability = MAX_PROB_RESULT
        points = POINTS_SMALL_STRAIGHT
    elif (first == [0,1,1,1] and middle == [1,1,1,0]) or (middle == [0,1,1,1] and last == [1,1,1,0]):
        probability = PROB_RESULT_A
    elif sum(first) == STRAIGHT_CORRECT_THREE or sum(middle) == STRAIGHT_CORRECT_THREE or sum(last) == STRAIGHT_CORRECT_THREE:
        probability = PROB_RESULT_D
    elif sum(first) == STRAIGHT_CORRECT_TWO or sum(middle) == STRAIGHT_CORRECT_TWO or sum(last) == STRAIGHT_CORRECT_TWO:
        probability = PROB_RESULT_F
    else:
        probability = PROB_RESULT_J
    return(points, probability)

def getLSCount(diceList):
    allFreq = [diceList.count(DIE_VALUE_ONE), diceList.count(DIE_VALUE_TWO), diceList.count(DIE_VALUE_THREE), diceList.count(DIE_VALUE_FOUR), diceList.count(DIE_VALUE_FIVE), diceList.count(DIE_VALUE_SIX)]
    first = [0,0,0,0,0] # 1, 2, 3, 4, 5
    last = [0,0,0,0,0] # 2, 3, 4, 5, 6
    if allFreq[DIE_VALUE_ONE-1] > 0:
        first[DIE_VALUE_ONE-1]+=1
    if allFreq[DIE_VALUE_TWO-1] > 0:
        first[DIE_VALUE_TWO-1]+=1
        last[DIE_VALUE_TWO-2]+=1
    if allFreq[DIE_VALUE_THREE-1] > 0:
        first[DIE_VALUE_THREE-1]+=1
        last[DIE_VALUE_THREE-2]+=1    
    if allFreq[DIE_VALUE_FOUR-1] > 0:
        first[DIE_VALUE_FOUR-1]+=1
        last[DIE_VALUE_FOUR-2]+=1
    if allFreq[DIE_VALUE_FIVE-1] > 0:
        first[DIE_VALUE_FIVE-1]
        last[DIE_VALUE_FIVE-2]+=1
    if allFreq[DIE_VALUE_SIX-1] > 0:
        last[DIE_VALUE_SIX-2]+=1

    return (first, last)

# Large Straight
def probLS(diceList):
    points = POINTS_ZERO
    (first, last) = getLSCount(diceList)

    if sum(first) == STRAIGHT_CORRECT_FIVE or sum(last) == STRAIGHT_CORRECT_FIVE:
        probability = MAX_PROB_RESULT
        points = POINTS_LARGE_STRAIGHT
    elif first == [0,1,1,1,1] and last == [1,1,1,1,0]:
        probability = PROB_RESULT_C
    elif sum(first) == STRAIGHT_CORRECT_FOUR or sum(last) == STRAIGHT_CORRECT_FOUR:
        probability = PROB_RESULT_E
    elif (first == [0,0,1,1,1] and last == [0,1,1,1,0]) or (first == [0,1,1,1,0] and last == [1,1,1,0,0]):
        probability = PROB_RESULT_H
    elif sum(first) == STRAIGHT_CORRECT_THREE or sum(last) == STRAIGHT_CORRECT_THREE:
        probability = PROB_RESULT_L
    elif sum(first) == STRAIGHT_CORRECT_TWO or sum(last) == STRAIGHT_CORRECT_TWO:
        probability = PROB_RESULT_O
    else:
        probability = PROB_RESULT_P
    return(points, probability)


def probYacht(diceList):
    points = POINTS_ZERO
    maxFreq = checkMaxFreq(diceList)
    if maxFreq[FREQ_INDEX] == FIVE_FREQ:
        points = POINTS_YACHT
    probability = 1/(TOTAL_UNIQUE_DIE_VALUES**(MAX_DICE-maxFreq[1]))
    return (points, probability)

