import random
from Hand import HandTypes
from Probability import *
from Constants import *


# Creates and returns a list of N random integers between 1 and 6 in numerical order
def roll(dice_amount):
    rollResults = []
    for die in range(dice_amount):
        rollResults.append(random.randint(MIN_DIE_VALUE, MAX_DIE_VALUE))
    rollResults.sort()
    return rollResults
    
def takeTurn(card):
    turnsLeft = TOTAL_TURNS
    markCard = True
    handType = HandTypes.Nothing
    availableHands = card.availableHands()
    while turnsLeft > 0 and markCard:
        potentialHands = []

        # Roll Dice
        newDice = roll(MAX_DICE-len(heldDice))
        totalDice = heldDice + newDice
        totalDice.sort() 
        heldDice = []
        
        # Determine Strategy
        probDict = {
            HandTypes.Ones:probNum(totalDice, DIE_VALUE_ONE),
            HandTypes.Twos:probNum(totalDice, DIE_VALUE_TWO),
            HandTypes.Threes:probNum(totalDice, DIE_VALUE_THREE),
            HandTypes.Fours:probNum(totalDice, DIE_VALUE_FOUR),
            HandTypes.Fives:probNum(totalDice, DIE_VALUE_FIVE),
            HandTypes.Sixes:probNum(totalDice, DIE_VALUE_SIX),
            HandTypes.ToK:probTok(totalDice),
            HandTypes.FoK:probFok(totalDice),
            HandTypes.FH:probFH(totalDice),
            HandTypes.SS:probSS(totalDice),
            HandTypes.LS:probLS(totalDice),
            HandTypes.Yacht:probYacht(totalDice)
        }

        # Check if any hand has been met
        for hand in availableHands:
            if probDict[hand][PROB_INDEX] == MAX_PROB_RESULT:
                potentialHands.append(hand)
        
        # If So, find the highest scoring hand
        if potentialHands != []:
            maxHand = availableHands[0]
            maxPoints = probDict[maxHand][POINT_INDEX]
            for hand in availableHands:
                if probDict[hand][POINT_INDEX] > maxPoints:
                    maxPoints = probDict[hand][POINT_INDEX]
                    maxHand = hand
            handType = maxHand
            if handType == HandTypes.Yacht:
                markCard = False
                card.setYacht(checkYacht(totalDice))
            elif handType == HandTypes.LS:
                markCard = False
                card.setLargeStraight(checkLargeStraight(totalDice))
            elif handType == HandTypes.FH:
                markCard = False
                card.setFullHouse(checkFullHouse(totalDice))
            elif handType == HandTypes.SS:
                if turnsLeft == LAST_TURN or HandTypes.LS not in availableHands:
                    markCard = False
                    card.setSmallStraight(checkSmallStraight(totalDice))
                else:
                    if totalDice[DIE_INDEX_ZERO] == MIN_DIE_VALUE:
                        heldDice = [DIE_VALUE_ONE, DIE_VALUE_TWO, DIE_VALUE_THREE, DIE_VALUE_FOUR]
                    elif totalDice[DIE_INDEX_FOUR] == MAX_DIE_VALUE:
                        heldDice = [DIE_VALUE_THREE, DIE_VALUE_FOUR, DIE_VALUE_FIVE, DIE_VALUE_SIX]
                    else:
                        heldDice = [DIE_VALUE_TWO, DIE_VALUE_THREE, DIE_VALUE_FOUR, DIE_VALUE_FIVE]
            elif handType == HandTypes.FoK:
                fokNum = totalDice[DIE_INDEX_TWO]
                if fokNum == DIE_VALUE_ONE:
                    fokHand = HandTypes.Ones
                elif fokNum == DIE_VALUE_TWO:
                    fokHand = HandTypes.Twos
                elif fokNum == DIE_VALUE_THREE:
                    fokHand = HandTypes.Threes
                elif fokNum == DIE_VALUE_FOUR:
                    fokHand = HandTypes.Fours
                elif fokNum == DIE_VALUE_FIVE:
                    fokHand = HandTypes.Fives
                else:
                    fokHand = HandTypes.Sixes
                if turnsLeft == LAST_TURN:
                    if maxPoints <= POINTS_HALF_MAX and fokHand in availableHands:
                        if fokHand == HandTypes.Ones:
                            card.setOnes(checkOnes(totalDice))
                        elif fokHand == HandTypes.Twos:
                            card.setTwos(checkTwos(totalDice))
                        elif fokHand == HandTypes.Threes:
                            card.setThrees(checkThrees(totalDice))
                        elif fokHand == HandTypes.Fours:
                            card.setFours(checkFours(totalDice))
                        elif fokHand == HandTypes.Fives:
                            card.setFives(checkFives(totalDice))
                        else:
                            card.setSixes(checkSixes(totalDice))
                    else:
                        card.setFoK(checkFourKind(totalDice))
                else:
                    heldDice = [fokNum, fokNum, fokNum, fokNum]
            elif handType == HandTypes.ToK:
                tokNum = totalDice[DIE_INDEX_TWO]
                if tokNum == DIE_VALUE_ONE:
                    tokHand = HandTypes.Ones
                elif tokNum == DIE_VALUE_TWO:
                    tokHand = HandTypes.Twos
                elif tokNum == DIE_VALUE_THREE:
                    tokHand = HandTypes.Threes
                elif tokNum == DIE_VALUE_FOUR:
                    tokHand = HandTypes.Fours
                elif tokNum == DIE_VALUE_FIVE:
                    tokHand = HandTypes.Fives
                else:
                    tokHand = HandTypes.Sixes
                if turnsLeft == LAST_TURN:
                    if maxPoints <= POINTS_HALF_MAX and tokHand in availableHands:
                        if tokHand == HandTypes.Ones:
                            card.setOnes(checkOnes(totalDice))
                        elif tokHand == HandTypes.Twos:
                            card.setTwos(checkTwos(totalDice))
                        elif tokHand == HandTypes.Threes:
                            card.setThrees(checkThrees(totalDice))
                        elif tokHand == HandTypes.Fours:
                            card.setFours(checkFours(totalDice))
                        elif tokHand == HandTypes.Fives:
                            card.setFives(checkFives(totalDice))
                        else:
                            card.setSixes(checkSixes(totalDice))
                    else:
                        card.setToK(checkThreeKind(totalDice))
                else:
                    heldDice = [tokNum, tokNum, tokNum]
            elif handType == HandTypes.Sixes:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setSixes(checkSixes(totalDice))
                    markCard = False
                else:
                    firstIndex = totalDice.index(DIE_VALUE_SIX)
                    heldDice = totalDice[firstIndex:DIE_INDEX_FOUR+1]
            elif handType == HandTypes.Fives:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setFives(checkFives(totalDice))
                    markCard = False
                else:
                    firstIndex = totalDice.index(DIE_VALUE_FIVE)
                    freq = totalDice.count(DIE_VALUE_FIVE)
                    heldDice = totalDice[firstIndex:firstIndex+freq]
            elif handType == HandTypes.Fours:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setFours(checkFours(totalDice))
                    markCard = False
                else:
                    firstIndex = totalDice.index(DIE_VALUE_FOUR)
                    freq = totalDice.count(DIE_VALUE_FOUR)
                    heldDice = totalDice[firstIndex:firstIndex+freq]
            elif handType == HandTypes.Threes:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setThrees(checkThrees(totalDice))
                    markCard = False
                else:
                    firstIndex = totalDice.index(DIE_VALUE_THREE)
                    freq = totalDice.count(DIE_VALUE_THREE)
                    heldDice = totalDice[firstIndex:firstIndex+freq]
            elif handType == HandTypes.Twos:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setTwos(checkTwos(totalDice))
                    markCard = False
                else:
                    firstIndex = totalDice.index(DIE_VALUE_TWO)
                    freq = totalDice.count(DIE_VALUE_TWO)
                    heldDice = totalDice[firstIndex:firstIndex+freq]
            elif handType == HandTypes.Ones:
                if turnsLeft == LAST_TURN or totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_FOUR]:
                    card.setOnes(checkOnes(totalDice))
                    markCard = False
                else:
                    freq = totalDice.count(DIE_VALUE_ONE)
                    heldDice = totalDice[DIE_INDEX_ZERO:freq]


        # If not, and a Strategy has not been decided, find the highest probability hand
        else:
            maxHand = availableHands[0]
            maxProb = probDict[maxHand][PROB_INDEX]
            for hand in availableHands:
                if probDict[hand][PROB_INDEX] > maxProb:
                    maxProb = probDict[hand][PROB_INDEX]
                    maxHand = hand
            handType = maxHand
            if handType == HandTypes.Yacht:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setYacht(checkYacht(totalDice))
                else:
                    maxNum = checkMaxFreq(totalDice)
                    for die in range(maxNum[FREQ_INDEX]):
                        heldDice.append(maxNum[NUM_INDEX])
            elif handType == HandTypes.LS:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setLargeStraight(checkLargeStraight(totalDice))
                else:
                    (first, last) = getLSCount(totalDice)
                    if sum(first) > sum(last):
                        if first[DIE_VALUE_ONE-1] == 1:
                            heldDice.append(DIE_VALUE_ONE)
                        if first[DIE_VALUE_TWO-1] == 1:
                            heldDice.append(DIE_VALUE_TWO)
                        if first[DIE_VALUE_THREE-1] == 1:
                            heldDice.append(DIE_VALUE_THREE)
                        if first[DIE_VALUE_FOUR-1] == 1:
                            heldDice.append(DIE_VALUE_FOUR)
                        if first[DIE_VALUE_FIVE-1] == 1:
                            heldDice.append(DIE_VALUE_FIVE)
                    else:
                        if last[DIE_VALUE_TWO-2] == 1:
                            heldDice.append(DIE_VALUE_TWO)
                        if last[DIE_VALUE_THREE-2] == 1:
                            heldDice.append(DIE_VALUE_THREE)
                        if last[DIE_VALUE_FOUR-2] == 1:
                            heldDice.append(DIE_VALUE_FOUR)
                        if last[DIE_VALUE_FIVE-2] == 1:
                            heldDice.append(DIE_VALUE_FIVE)
                        if last[DIE_VALUE_SIX-2] == 1:
                            heldDice.append(DIE_VALUE_SIX)
            elif handType == HandTypes.SS:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setSmallStraight(checkSmallStraight(totalDice))
                else:
                    (first, middle, last) = getSSCount(totalDice)
                    if sum(first) >= sum(last) and sum(first) >= sum(middle):
                        if first[DIE_VALUE_ONE-1] == 1:
                            heldDice.append(DIE_VALUE_ONE)
                        if first[DIE_VALUE_TWO-1] == 1:
                            heldDice.append(DIE_VALUE_TWO)
                        if first[DIE_VALUE_THREE-1] == 1:
                            heldDice.append(DIE_VALUE_THREE)
                        if first[DIE_VALUE_FOUR-1] == 1:
                            heldDice.append(DIE_VALUE_FOUR)
                    elif sum(middle) >= sum(last) and sum(middle) >= sum(first):
                        if middle[DIE_VALUE_TWO-2] == 1:
                            heldDice.append(DIE_VALUE_TWO)
                        if middle[DIE_VALUE_THREE-2] == 1:
                            heldDice.append(DIE_VALUE_THREE)
                        if middle[DIE_VALUE_FOUR-2] == 1:
                            heldDice.append(DIE_VALUE_FOUR)
                        if middle[DIE_VALUE_FIVE-2] == 1:
                            heldDice.append(DIE_VALUE_FIVE)
                    else:
                        if last[DIE_VALUE_THREE-3] == 1:
                            heldDice.append(DIE_VALUE_THREE)
                        if last[DIE_VALUE_FOUR-3] == 1:
                            heldDice.append(DIE_VALUE_FOUR)
                        if last[DIE_VALUE_FIVE-3] == 1:
                            heldDice.append(DIE_VALUE_FIVE)
                        if last[DIE_VALUE_SIX-3] == 1:
                            heldDice.append(DIE_VALUE_SIX)
            elif handType == HandTypes.FH:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setFullHouse(checkFullHouse(totalDice))
                else:
                    state = getFHState(totalDice)
                    if state == FH_STATE_TWO_PAIR:
                        if totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_ONE]:
                            if totalDice[DIE_INDEX_TWO] == totalDice[DIE_INDEX_THREE]:
                                heldDice = totalDice[DIE_INDEX_ZERO:DIE_INDEX_THREE+1]
                            else:
                                heldDice = totalDice[DIE_INDEX_ZERO:DIE_INDEX_ONE+1] + totalDice[DIE_INDEX_THREE:DIE_INDEX_FOUR+1]
                        else:
                            heldDice = totalDice[DIE_INDEX_ONE:DIE_INDEX_FOUR+1]
                    elif state == FH_STATE_THREE_OF_KIND:
                        if totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_TWO]:
                            heldDice == totalDice[DIE_INDEX_ZERO:DIE_INDEX_TWO+1]
                        elif totalDice[DIE_INDEX_ONE] == totalDice[DIE_INDEX_THREE]:
                            heldDice == totalDice[DIE_INDEX_ONE:DIE_INDEX_THREE+1]
                        else:
                            heldDice == totalDice[DIE_INDEX_TWO:DIE_INDEX_FOUR+1]
                    elif state == FH_STATE_ONE_PAIR:
                        if totalDice[DIE_INDEX_ZERO] == totalDice[DIE_INDEX_ONE]:
                            heldDice = totalDice[DIE_INDEX_ZERO:DIE_INDEX_ONE+1]
                        elif totalDice[DIE_INDEX_ONE] == totalDice[DIE_INDEX_TWO]:
                            heldDice = totalDice[DIE_INDEX_ONE:DIE_INDEX_TWO+1]
                        elif totalDice[DIE_INDEX_TWO] == totalDice[DIE_INDEX_THREE]:
                            heldDice = totalDice[DIE_INDEX_TWO:DIE_INDEX_THREE+1]
                        elif totalDice[DIE_INDEX_THREE] == totalDice[DIE_INDEX_FOUR]:
                            heldDice = totalDice[DIE_INDEX_THREE:DIE_INDEX_FOUR+1]
                    # If 5 unique values, hold no dice
            elif handType == HandTypes.FoK:
                maxFreq = checkMaxFreq(totalDice)
                maxNum = maxFreq[NUM_INDEX]
                if turnsLeft == LAST_TURN:
                    if maxNum == DIE_VALUE_ONE and HandTypes.Ones in availableHands:
                        card.setOnes(checkOnes(totalDice))
                    elif maxNum == DIE_VALUE_TWO and HandTypes.Twos in availableHands:
                        card.setTwos(checkTwos(totalDice))
                    elif maxNum == DIE_VALUE_THREE and HandTypes.Threes in availableHands:
                        card.setThrees(checkThrees(totalDice))
                    elif maxNum == DIE_VALUE_FOUR and HandTypes.Fours in availableHands:
                        card.setFours(checkFours(totalDice))
                    elif maxNum == DIE_VALUE_FIVE and HandTypes.Fives in availableHands:
                        card.setFives(checkFives(totalDice))
                    elif maxNum == DIE_VALUE_SIX and HandTypes.Sixes in availableHands:
                        card.setSixes(checkSixes(totalDice))
                    elif card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setFoK(checkFourKind(totalDice))
                else:
                    for die in range(DIE_INDEX_ZERO, maxFreq[FREQ_INDEX]):
                        heldDice.append(maxNum)
            elif handType == HandTypes.ToK:
                maxFreq = checkMaxFreq(totalDice)
                maxNum = maxFreq[NUM_INDEX]
                if turnsLeft == LAST_TURN:
                    if maxNum == DIE_VALUE_ONE and HandTypes.Ones in availableHands:
                        card.setOnes(checkOnes(totalDice))
                    elif maxNum == DIE_VALUE_TWO and HandTypes.Twos in availableHands:
                        card.setTwos(checkTwos(totalDice))
                    elif maxNum == DIE_VALUE_THREE and HandTypes.Threes in availableHands:
                        card.setThrees(checkThrees(totalDice))
                    elif maxNum == DIE_VALUE_FOUR and HandTypes.Fours in availableHands:
                        card.setFours(checkFours(totalDice))
                    elif maxNum == DIE_VALUE_FIVE and HandTypes.Fives in availableHands:
                        card.setFives(checkFives(totalDice))
                    elif maxNum == DIE_VALUE_SIX and HandTypes.Sixes in availableHands:
                        card.setSixes(checkSixes(totalDice))
                    elif card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setToK(checkThreeKind(totalDice))
                else:
                    for die in range(DIE_INDEX_ZERO, maxFreq[FREQ_INDEX]):
                        heldDice.append(maxNum)
            elif handType == HandTypes.Sixes:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setSixes(checkSixes(totalDice))
                else:
                    freq = totalDice.count(DIE_VALUE_SIX)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_SIX)
            elif handType == HandTypes.Fives:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setFives(checkFives(totalDice))
                else:
                    freq = totalDice.count(DIE_VALUE_FIVE)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_FIVE)
            elif handType == HandTypes.Fours:
                if turnsLeft == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(checkChance(totalDice))
                    else:
                        card.setFours(checkFours(totalDice))
                else:
                    freq = totalDice.count(DIE_VALUE_FOUR)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_FOUR)
            elif handType == HandTypes.Threes:
                if turnsLeft == LAST_TURN:
                    card.setThrees(checkThrees(totalDice))      
                else:
                    freq = totalDice.count(DIE_VALUE_THREE)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_THREE)
            elif handType == HandTypes.Twos:
                if turnsLeft == LAST_TURN:
                    card.setTwos(checkTwos(totalDice))      
                else:
                    freq = totalDice.count(DIE_VALUE_TWO)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_TWO)
            elif handType == HandTypes.Ones:
                if turnsLeft == LAST_TURN:
                    card.setOnes(checkOnes(totalDice))      
                else:
                    freq = totalDice.count(DIE_VALUE_ONE)
                    for die in range(freq):
                        heldDice.append(DIE_VALUE_ONE)
            else:
                if turnsLeft == LAST_TURN:
                    card.setChance(checkChance(totalDice))
                else:
                    for die in totalDice:
                        if die > DIE_VALUE_FOUR:
                            heldDice.append(die)

        turnsLeft-=1
    return card