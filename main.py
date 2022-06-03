from functools import total_ordering
from hashlib import new
import random
from enum import Enum

class Hand(Enum):
    Nothing = 0
    Ones = 1
    Twos = 2
    Threes = 3
    Fours = 4
    Fives = 5
    Sixes = 6
    ToK = 7
    FoK = 8
    FH = 9
    SS = 10
    LS = 11
    Yacht = 12
    Chance = 13

class PlayCard():
    ones = -1
    twos = -1
    threes = -1
    fours = -1
    fives = -1
    sixes = -1
    tok = -1
    fok = -1
    fh = -1
    ss = -1
    ls = -1
    yacht = -1
    chance = -1

    def getOnes(this):
        return this.ones
    
    def setOnes(this, value):
        this.ones = value

    def getTwos(this):
        return this.twos
    
    def setTwos(this, value):
        this.twos = value

    def getThrees(this):
        return this.threes
    
    def setThrees(this, value):
        this.threes = value

    def getFours(this):
        return this.fours
    
    def setFours(this, value):
        this.fours = value

    def getFives(this):
        return this.fives
    
    def setFives(this, value):
        this.fives = value

    def getSixes(this):
        return this.sixes
    
    def setSixes(this, value):
        this.Sixes = value

    def getToK(this):
        return this.tok
    
    def setToK(this, value):
        this.ones = value

    def getFoK(this):
        return this.fok
    
    def setFoK(this, value):
        this.fok = value

    def getFullHouse(this):
        return this.fh
    
    def setFullHouse(this, value):
        this.fh = value

    def getSmallStraight(this):
        return this.ss
    
    def setSmallStraight(this, value):
        this.ss = value

    def getLargeStraight(this):
        return this.ls
    
    def setLargeStraight(this, value):
        this.ls = value

    def getYacht(this):
        return this.yacht
    
    def setYacht(this, value):
        this.yacht = value

    def getChance(this):
        return this.chance
    
    def setChance(this, value):
        this.chance = value

    def totalScore(this):
        score = 0
        if this.getOnes() == -1:
            score += 0
        else:
            score += this.getOnes()
        if this.getTwos() == -1:
            score += 0
        else:
            score += this.getTwos()
        if this.getThrees() == -1:
            score += 0
        else:
            score += this.getThrees()
        if this.getFours() == -1:
            score += 0
        else:
            score += this.getFours()
        if this.getFives() == -1:
            score += 0
        else:
            score += this.getFives()
        if this.getSixes() == -1:
            score += 0
        else:
            score += this.getSixes()  
        if this.getToK() == -1:
            score += 0
        else:
            score += this.getToK()
        if this.getFoK() == -1:
            score += 0
        else:
            score += this.getFoK()
        if this.getFullHouse() == -1:
            score += 0
        else:
            score += this.getFullHouse()
        if this.getSmallStraight() == -1:
            score += 0
        else:
            score += this.getSmallStraight()
        if this.getLargeStraight() == -1:
            score += 0
        else:
            score += this.getLargeStraight()
        if this.getYacht() == -1:
            score += 0
        else:
            score += this.getYacht()
        if this.getChance() == -1:
            score += 0
        else:
            score += this.getChance()       
        return score

    def availableHands(this):
        availableHands = []
        if this.getOnes() != -1:
            availableHands.append(Hand.Ones)
        if this.getTwos() != -1:
            availableHands.append(Hand.Twos)
        if this.getThrees() != -1:
            availableHands.append(Hand.Threes)
        if this.getFours() != -1:
            availableHands.append(Hand.Fours)
        if this.getFives() != -1:
            availableHands.append(Hand.Fives)
        if this.getSixes() != -1:
            availableHands.append(Hand.Sixes)
        if this.getToK() != -1:
            availableHands.append(Hand.ToK)
        if this.getFoK() != -1:
            availableHands.append(Hand.FoK)
        if this.getFullHouse() != -1:
            availableHands.append(Hand.FH)
        if this.getSmallStraight() != -1:
            availableHands.append(Hand.SS)
        if this.getLargeStraight() != -1:
            availableHands.append(Hand.LS)
        if this.getYacht() != -1:
            availableHands.append(Hand.Yacht)
        if this.getChance() != -1:
            availableHands.append(Hand.Yacht)      
        return availableHands


# Creates and returns a list of N random integers between 1 and 6 in numerical order
def roll(dice_amount):
    roll_results = []
    for die in range(dice_amount):
        roll_results.append(random.randint(1,6))
    roll_results.sort()
    return roll_results

# Checks how often a selected number appears in a list of 5 integers and returns the frequency
def check_num_freq(dice_list, number):
    freq = 0
    for die in dice_list:
        if die == number:
            freq += 1
    return freq

def check_max_freq(dice_list):
    max_freq = 0
    for num in range(6):
        freq = check_num_freq(dice_list,num+1)
        if(freq > max_freq):
            max_freq = freq
            max_num = num+1
    return (max_num, max_freq)

# Checks how many points could be scored if "Ones" is selected
def check_ones(dice_list):
    num_freq = check_num_freq(dice_list, 1)
    return 1*num_freq

# Checks how many points could be scored if "Twos" is selected
def check_twos(dice_list):
    num_freq = check_num_freq(dice_list, 2)
    return 2*num_freq

# Checks how many points could be scored if "Threes" is selected
def check_threes(dice_list):
    num_freq = check_num_freq(dice_list, 3)
    return 3*num_freq

# Checks how many points could be scored if "Fours" is selected
def check_fours(dice_list):
    num_freq = check_num_freq(dice_list, 4)
    return 4*num_freq

# Checks how many points could be scored if "Fives" is selected
def check_fives(dice_list):
    num_freq = check_num_freq(dice_list, 5)
    return 5*num_freq

# Checks how many points could be scored if "Sixes" is selected
def check_sixes(dice_list):
    num_freq = check_num_freq(dice_list, 6)
    return 6*num_freq

# Checks how many points could be scored if "Three of a Kind" is selected
def check_three_kind(dice_list):
    total_dice = 0
    if total_dice <= 2:
        for number in range(6):
            freq = check_num_freq(dice_list, number+1)
            if freq >= 3:
                return sum(dice_list)
            else:
                total_dice += freq
    return 0

# Checks how many points could be scored if "Four of a Kind" is selected
def check_four_kind(dice_list):
    total_dice = 0
    if total_dice <= 1:
        for number in range(6):
            freq = check_num_freq(dice_list, number+1)
            if freq >= 4:
                return sum(dice_list)
            else:
                total_dice += freq
    return 0

# Checks how many points could be scored if "Full House" is selected
def check_full_house(dice_list):
    total_dice = 0
    tok_num = 0
    if total_dice <= 2:
        for number in range(6):
            freq = check_num_freq(dice_list, number+1)
            if freq == 3:
                tok_num = number+1
            total_dice += freq
    if(tok_num != 0):
        for number in range(6):
            freq = check_num_freq(dice_list, number+1)
            if freq == 2:
                return sum(dice_list)
    return 0

# Checks how many points could be scored if "Small Straight" is selected
def check_small_straight(dice_list):
    if(dice_list[-1] - dice_list[0] >= 3):
        if(dice_list[0]+1 == dice_list[1] and dice_list[1]+1 == dice_list[2] and dice_list[2]+1 == dice_list[3]):
            return 30
        if(dice_list[1]+1 == dice_list[2] and dice_list[2]+1 == dice_list[3] and dice_list[3]+1 == dice_list[4]):
            return 30
    return 0

# Checks how many points could be scored if "Large Straight" is selected
def check_large_straight(dice_list):
    if(dice_list[-1] - dice_list[0] == 4):
        if(dice_list[0]+1 == dice_list[1] and dice_list[1]+1 == dice_list[2] and dice_list[2]+1 == dice_list[3]and dice_list[3]+1 == dice_list[4]):
            return 40
    return 0

# Checks how many points could be scored if "Yacht" is selected
def check_yacht(dice_list):
    freq = check_num_freq(dice_list, dice_list[0])
    if freq == 5:
        return 50
    return 0

# Checks how many points could be scored if "Chance" is selected
def check_chance(dice_list):
    return(sum(dice_list))

# Probability Functions

# Ones, Twos, Threes, Fours, Fives, Sixes Probability (aim for 3)
def prob_num(dice_list, num):
    freq = check_num_freq(dice_list, num)
    if(freq == 0):
        probability = (1/6)*((1/6)*((1/6)+(5/6)*((1/6)+(5/6)*(1/6)))+(5/6)*((1/6)*((1/6)+(5/6)*(1/6))+(5/6)*(1/6)*(1/6))) + (5/6)*((1/6)*((1/6)*((1/6)+(5/6)*(1/6))+(5/6)*(1/6)*(1/6))+(5/6)*(1/6)*(1/6)*(1/6))
    elif(freq == 1):
        probability = (1/6)*((1/6)+(5/6)*((1/6)+(5/6)*(1/6))) + (5/6)*((1/6)*((1/6)+(5/6)*(1/6))+(5/6)*(1/6)*(1/6))
    elif(freq == 2):
        probability = (1/6) + (5/6)*((1/6)+(5/6)*(1/6))
    else:
        probability = 1
    return (num*freq, probability)

def prob_tok(dice_list):
    max_freq = check_max_freq(dice_list)
    points = 0
    if(max_freq[1] == 1):
        probability = (1/6)*((1/6)+(5/6)*((1/6)+(5/6)*(1/6))) + (5/6)*((1/6)*((1/6)+(5/6)*(1/6))+(5/6)*(1/6)*(1/6))
    elif(max_freq[1] == 2):
        probability = (1/6) + (5/6)*((1/6)+(5/6)*(1/6))
    else:
        probability = 1
        points = sum(dice_list)
    return(points, probability)

def prob_tok(dice_list):
    max_freq = check_max_freq(dice_list)
    points = 0
    if(max_freq[1] == 1):
        probability = (1/6)*((1/6)*((1/6)+(5/6)*(1/6))+(5/6)*(1/6)*(1/6)) + (5/6)*(1/6)*(1/6)*(1/6)
    elif(max_freq[1] == 2):
        probability = (1/6)*((1/6)+(5/6)*(1/6)) + (5/6)*(1/6)*(1/6)
    elif(max_freq[1] == 3):
        probability = (1/6) + (5/6)*(1/6)
    else:
        probability = 1
        points = sum(dice_list)
    return(points, probability)

def prob_fh(dice_list):
    points = 0
    # Full House
    if(check_full_house(dice_list) != 0):
        points = sum(dice_list)
        probability = 1
    # Two Pair
    elif(dice_list[0] == dice_list[1] and (dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4]) or dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]):
        probability = 1/3
    # 3-1-1
    elif(dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]):
        probability = 1/6
    # One Pair
    elif(dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2] or dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4]):
        probability = (1/6)*(1/6) + (5/6)*((1/6)*(1/6)+(1/6)*(1/3))
    # Five Unique Values
    else:
        probability = (6 + 10*6*5)/(6^5)
    return(points, probability)

# Small Straight
def prob_ss(dice_list):
    all_freq = [check_num_freq(dice_list,1), check_num_freq(dice_list,2), check_num_freq(dice_list,3), check_num_freq(dice_list,4), check_num_freq(dice_list,5), check_num_freq(dice_list,6)]
    first = [0,0,0,0] # 1, 2, 3, 4
    middle = [0,0,0,0] # 2, 3, 4, 5
    last = [0,0,0,0] # 3, 4, 5, 6
    if all_freq[0] > 0:
        first[0]+=1
    if all_freq[1] > 0:
        first[1]+=1
        middle[0]+=1 
    if all_freq[2] > 0:
        first[2]+=1
        middle[1]+=1  
        last[0]+=1    
    if all_freq[3] > 0:
        first[3]+=1
        middle[2]+=1  
        last[1]+=1  
    if all_freq[4] > 0:
        middle[3]+=1  
        last[2]+=1 
    if all_freq[5] > 0:
        last[3]+=1

    if sum(first) == 4 or sum(middle) == 4 or sum(last) == 4:
        probability = 1
    elif (first == [0,1,1,1] and middle == [1,1,1,0]) or (middle == [0,1,1,1] and last == [1,1,1,0]):
        probability = (1/3) + (2/3)*(1/3)
    elif sum(first) == 3 or sum(middle) == 3 or sum(last) == 3:
        probability = (1/6) + (5/6)*(1/6)
    elif sum(first) == 2 or sum(middle) == 2 or sum(last) == 2:
        probability = (1/3)*((1/6)+(5/6)*(1/6)) + (2/3)*(1/3)*(1/6)
    else:
        probability = (1/2)*((1/3)*((1/6)+(5/6)*(1/6))+(2/3)*(1/3)*(1/6))+(1/2)*(1/2)*(1/3)*(1/6)

# Large Straight

def prob_yacht(dice_list):
    max_freq = check_max_freq(dice_list)
    return (1/(6^(5-max_freq)))
    
def take_turn(card):
    turns_left = 3
    mark_card = True
    held_dice = []
    hand_type = Hand.Nothing
    while(turns_left > 0 and mark_card):
        # Roll Dice
        new_dice = roll(5-len(held_dice))
        total_dice = held_dice + new_dice
        total_dice.sort()        
        held_dice = []
        all_scores = PlayCard()
        all_scores.setOnes(check_ones(total_dice))
        all_scores.setTwos(check_twos(total_dice))
        all_scores.setThrees(check_threes(total_dice))
        all_scores.setFours(check_fours(total_dice))
        all_scores.setFives(check_fives(total_dice))
        all_scores.setSixes(check_sixes(total_dice))
        all_scores.setToK(check_three_kind(total_dice))
        all_scores.setFoK(check_four_kind(total_dice))
        all_scores.setFullHouse(check_full_house(total_dice))
        all_scores.setSmallStraight(check_small_straight(total_dice))
        all_scores.setLargeStraight(check_large_straight(total_dice))
        all_scores.setYacht(check_yacht(total_dice))
        all_scores.setChance(check_chance(total_dice))

        # Determine Strategy
        if card.getYacht() == -1 and check_yacht(total_dice) == 50:
            card.setYacht(check_yacht(total_dice))
            mark_card = False
        elif card.getLargeStraight() == -1 and check_large_straight(total_dice) == 40:
            card.setLargeStraight(check_large_straight(total_dice))
            mark_card = False
        available_hands = card.availableHands()
        # Check Straights
        if Hand.LS in available_hands and check_small_straight(total_dice) == 30:
            if total_dice[0] + 1 == total_dice[1]:
                held_dice = total_dice[0:3]
            else:
                held_dice = total_dice[1:4]

        
        turns_left-=1

playcard = PlayCard()
take_turn(playcard)
