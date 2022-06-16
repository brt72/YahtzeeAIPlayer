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
        this.tok = value

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
        if score >= 63:
            score += 35 
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
        if this.getOnes() == -1:
            availableHands.append(Hand.Ones)
        if this.getTwos() == -1:
            availableHands.append(Hand.Twos)
        if this.getThrees() == -1:
            availableHands.append(Hand.Threes)
        if this.getFours() == -1:
            availableHands.append(Hand.Fours)
        if this.getFives() == -1:
            availableHands.append(Hand.Fives)
        if this.getSixes() == -1:
            availableHands.append(Hand.Sixes)
        if this.getToK() == -1:
            availableHands.append(Hand.ToK)
        if this.getFoK() == -1:
            availableHands.append(Hand.FoK)
        if this.getFullHouse() == -1:
            availableHands.append(Hand.FH)
        if this.getSmallStraight() == -1:
            availableHands.append(Hand.SS)
        if this.getLargeStraight() == -1:
            availableHands.append(Hand.LS)
        if this.getYacht() == -1:
            availableHands.append(Hand.Yacht)
        if this.getChance() == -1:
            availableHands.append(Hand.Yacht)      
        return availableHands


# Creates and returns a list of N random integers between 1 and 6 in numerical order
def roll(dice_amount):
    roll_results = []
    for die in range(dice_amount):
        roll_results.append(random.randint(1,6))
    roll_results.sort()
    return roll_results

def check_max_freq(dice_list):
    max_freq = 0
    for num in range(6):
        freq = dice_list.count(num+1)
        if freq > max_freq:
            max_freq = freq
            max_num = num+1
    return (max_num, max_freq)

# Checks how many points could be scored if "Ones" is selected
def check_ones(dice_list):
    num_freq = dice_list.count(1)
    return 1*num_freq

# Checks how many points could be scored if "Twos" is selected
def check_twos(dice_list):
    num_freq = dice_list.count(2)
    return 2*num_freq

# Checks how many points could be scored if "Threes" is selected
def check_threes(dice_list):
    num_freq = dice_list.count(3)
    return 3*num_freq

# Checks how many points could be scored if "Fours" is selected
def check_fours(dice_list):
    num_freq = dice_list.count(4)
    return 4*num_freq

# Checks how many points could be scored if "Fives" is selected
def check_fives(dice_list):
    num_freq = dice_list.count(5)
    return 5*num_freq

# Checks how many points could be scored if "Sixes" is selected
def check_sixes(dice_list):
    num_freq = dice_list.count(6)
    return 6*num_freq

# Checks how many points could be scored if "Three of a Kind" is selected
def check_three_kind(dice_list):
    total_dice = 0
    if total_dice <= 2:
        for number in range(6):
            freq = dice_list.count( number+1)
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
            freq = dice_list.count( number+1)
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
            freq = dice_list.count( number+1)
            if freq == 3:
                tok_num = number+1
            total_dice += freq
    if(tok_num != 0):
        for number in range(6):
            freq = dice_list.count( number+1)
            if freq == 2:
                return 25
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
    freq = dice_list.count( dice_list[0])
    if freq == 5:
        return 50
    return 0

# Checks how many points could be scored if "Chance" is selected
def check_chance(dice_list):
    return(sum(dice_list))

# Probability Functions

# Ones, Twos, Threes, Fours, Fives, Sixes Probability (aim for 3)
def prob_num(dice_list, num):
    freq = dice_list.count( num)
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

def prob_fok(dice_list):
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

def get_fh_state(dice_list):
    if check_full_house(dice_list) != 0:
        return 101
    # Two Pair
    elif dice_list[0] == dice_list[1] and (dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4]) or dice_list[1] == dice_list[2] and dice_list[3] == dice_list[4]:
        return 102
    # 3-1-1
    elif dice_list[0] == dice_list[2] or dice_list[1] == dice_list[3] or dice_list[2] == dice_list[4]:
        return 103
    # One Pair
    elif dice_list[0] == dice_list[1] or dice_list[1] == dice_list[2] or dice_list[2] == dice_list[3] or dice_list[3] == dice_list[4]:
        return 104
    # Five Unique Values
    return 105


def prob_fh(dice_list):
    points = 0
    state = get_fh_state(dice_list)
    # Full House
    if state == 101:
        points = 25
        probability = 1
    # Two Pair
    elif state == 102:
        probability = 1/3
    # 3-1-1
    elif state == 103:
        probability = 1/6
    # One Pair
    elif state == 104:
        probability = (1/6)*(1/6) + (5/6)*((1/6)*(1/6)+(1/6)*(1/3))
    # Five Unique Values
    else:
        probability = (6 + 10*6*5)/(6^5)
    return(points, probability)

def get_ss_count(dice_list):
    all_freq = [dice_list.count(1), dice_list.count(2), dice_list.count(3), dice_list.count(4), dice_list.count(5), dice_list.count(6)]
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

    return (first, middle, last)

def prob_ss(dice_list):
    points = 0
    ssCount = get_ss_count(dice_list)
    first = ssCount[0]
    middle = ssCount[1]
    last = ssCount[2]

    if sum(first) == 4 or sum(middle) == 4 or sum(last) == 4:
        probability = 1
        points = 30
    elif (first == [0,1,1,1] and middle == [1,1,1,0]) or (middle == [0,1,1,1] and last == [1,1,1,0]):
        probability = (1/3) + (2/3)*(1/3)
    elif sum(first) == 3 or sum(middle) == 3 or sum(last) == 3:
        probability = (1/6) + (5/6)*(1/6)
    elif sum(first) == 2 or sum(middle) == 2 or sum(last) == 2:
        probability = (1/3)*((1/6)+(5/6)*(1/6)) + (2/3)*(1/3)*(1/6)
    else:
        probability = (1/2)*((1/3)*((1/6)+(5/6)*(1/6))+(2/3)*(1/3)*(1/6))+(1/2)*(1/2)*(1/3)*(1/6)
    return(points, probability)

def get_ls_count(dice_list):
    all_freq = [dice_list.count(1), dice_list.count(2), dice_list.count(3), dice_list.count(4), dice_list.count(5), dice_list.count(6)]
    first = [0,0,0,0,0] # 1, 2, 3, 4, 5
    last = [0,0,0,0,0] # 2, 3, 4, 5, 6
    if all_freq[0] > 0:
        first[0]+=1
    if all_freq[1] > 0:
        first[1]+=1
        last[0]+=1
    if all_freq[2] > 0:
        first[2]+=1
        last[1]+=1    
    if all_freq[3] > 0:
        first[3]+=1
        last[2]+=1
    if all_freq[4] > 0:
        first[4]
        last[3]+=1
    if all_freq[5] > 0:
        last[4]+=1

    return (first, last)

# Large Straight
def prob_ls(dice_list):
    points = 0
    lsCount = get_ls_count(dice_list)
    first = lsCount[0]
    last = lsCount[1]

    if sum(first) == 5 or sum(last) == 5:
        probability = 1
        points = 40
    elif first == [0,1,1,1,1] and last == [1,1,1,1,0]:
        probability = 1/3
    elif sum(first) == 4 or sum(last) == 4:
        probability = 1/6
    elif (first == [0,0,1,1,1] and last == [0,1,1,1,0]) or (first == [0,1,1,1,0] and last == [1,1,1,0,0]):
        probability = (1/3)*(1/3)
    elif sum(first) == 3 or sum(last) == 3:
        probability = (1/3)*(1/6)
    elif sum(first) == 2 or sum(last) == 2:
        probability = (1/2)*(1/3)*(1/6)
    else:
        probability = (2/3)*(1/2)*(1/3)*(1/6)
    return(points, probability)


def prob_yacht(dice_list):
    points = 0
    max_freq = check_max_freq(dice_list)
    if max_freq[1] == 5:
        points = 50
    probability = 1/(6^(5-max_freq[1]))
    return (points, probability)

    
def take_turn(card):
    turns_left = 3
    mark_card = True
    held_dice = []
    hand_type = Hand.Nothing
    available_hands = card.availableHands()
    while turns_left > 0 and mark_card:
        potential_hands = []

        # Roll Dice
        new_dice = roll(5-len(held_dice))
        total_dice = held_dice + new_dice
        total_dice.sort() 
        print(total_dice)       
        held_dice = []
        
        # Determine Strategy
        prob_dict = {
            Hand.Ones:prob_num(total_dice, 1),
            Hand.Twos:prob_num(total_dice, 2),
            Hand.Threes:prob_num(total_dice, 3),
            Hand.Fours:prob_num(total_dice, 4),
            Hand.Fives:prob_num(total_dice, 5),
            Hand.Sixes:prob_num(total_dice, 6),
            Hand.ToK:prob_tok(total_dice),
            Hand.FoK:prob_fok(total_dice),
            Hand.FH:prob_fh(total_dice),
            Hand.SS:prob_ss(total_dice),
            Hand.LS:prob_ls(total_dice),
            Hand.Yacht:prob_yacht(total_dice)
        }

        # Check if any hand has been met
        for hand in available_hands:
            if prob_dict[hand][1] == 1:
                potential_hands.append(hand)
        
        # If So, find the highest scoring hand
        if potential_hands != []:
            max_points = prob_dict[available_hands[0]][0]
            max_hand = available_hands[0]
            for hand in available_hands:
                if prob_dict[hand][0] > max_points:
                    max_points = prob_dict[hand][0]
                    max_hand = hand
            hand_type = max_hand
            if hand_type == Hand.Yacht:
                mark_card = False
                card.setYacht(check_yacht(total_dice))
            elif hand_type == Hand.LS:
                mark_card = False
                card.setLargeStraight(check_large_straight(total_dice))
            elif hand_type == Hand.FH:
                mark_card = False
                card.setFullHouse(check_full_house(total_dice))
            elif hand_type == Hand.SS:
                if turns_left == 1 or Hand.LS not in available_hands:
                    mark_card = False
                    card.setSmallStraight(check_small_straight(total_dice))
                else:
                    if total_dice[0] == 1:
                        held_dice = [1,2,3,4]
                    elif total_dice[4] == 6:
                        held_dice = [3,4,5,6]
                    else:
                        held_dice = [2,3,4,5]
            elif hand_type == Hand.FoK:
                fok_num = total_dice[2]
                print(fok_num)
                if fok_num == 1:
                    fok_hand = Hand.Ones
                elif fok_num == 2:
                    fok_hand = Hand.Twos
                elif fok_num == 3:
                    fok_hand = Hand.Threes
                elif fok_num == 4:
                    fok_hand = Hand.Fours
                elif fok_num == 5:
                    fok_hand = Hand.Fives
                else:
                    fok_hand = Hand.Sixes
                if turns_left == 1:
                    if max_prob[0] <= 15 and fok_hand in available_hands:
                        if fok_hand == Hand.Ones:
                            card.setOnes(check_ones(total_dice))
                        elif fok_hand == Hand.Twos:
                            card.setTwos(check_twos(total_dice))
                        elif fok_hand == Hand.Threes:
                            card.setThrees(check_threes(total_dice))
                        elif fok_hand == Hand.Fours:
                            card.setFours(check_fours(total_dice))
                        elif fok_hand == Hand.Fives:
                            card.setFives(check_fives(total_dice))
                        else:
                            card.setSixes(check_sixes(total_dice))
                    else:
                        card.setFoK(check_four_kind(total_dice))
                else:
                    held_dice = [fok_num, fok_num, fok_num, fok_num]
            elif hand_type == Hand.ToK:
                tok_num = total_dice[2]
                print(tok_num)
                if tok_num == 1:
                    tok_hand = Hand.Ones
                elif tok_num == 2:
                    tok_hand = Hand.Twos
                elif tok_num == 3:
                    tok_hand = Hand.Threes
                elif tok_num == 4:
                    tok_hand = Hand.Fours
                elif tok_num == 5:
                    tok_hand = Hand.Fives
                else:
                    tok_hand = Hand.Sixes
                if turns_left == 1:
                    if max_points <= 15 and tok_hand in available_hands:
                        if tok_hand == Hand.Ones:
                            card.setOnes(check_ones(total_dice))
                        elif tok_hand == Hand.Twos:
                            card.setTwos(check_twos(total_dice))
                        elif tok_hand == Hand.Threes:
                            card.setThrees(check_threes(total_dice))
                        elif tok_hand == Hand.Fours:
                            card.setFours(check_fours(total_dice))
                        elif tok_hand == Hand.Fives:
                            card.setFives(check_fives(total_dice))
                        else:
                            card.setSixes(check_sixes(total_dice))
                    else:
                        card.setToK(check_three_kind(total_dice))
                else:
                    held_dice = [tok_num, tok_num, tok_num]
            elif hand_type == Hand.Sixes:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setSixes(check_sixes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(6)
                    held_dice = total_dice[first_index:5]
            elif hand_type == Hand.Fives:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setFives(check_fives(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(5)
                    freq = total_dice.count(5)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Fours:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setFours(check_fours(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(4)
                    freq = total_dice.count(4)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Threes:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setThrees(check_threes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(3)
                    freq = total_dice.count(3)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Twos:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setTwos(check_twos(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(2)
                    freq = total_dice.count(2)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Ones:
                if turns_left == 1 or total_dice[0] == total_dice[4]:
                    card.setOnes(check_ones(total_dice))
                    mark_card = False
                else:
                    freq = total_dice.count(1)
                    held_dice = total_dice[0:freq]


        # If not, and a Strategy has not been decided, find the highest probability hand
        else:
            max_hand = available_hands[0]
            max_prob = prob_dict[max_hand][1]
            for hand in available_hands:
                if prob_dict[hand][1] > max_prob:
                    max_prob = prob_dict[hand][1]
                    max_hand = hand
            hand_type = max_hand
            if hand_type == Hand.Yacht:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setYacht(check_yacht(total_dice))
                else:
                    max_num = check_max_freq(total_dice)
                    for die in range(max_num[1]):
                        held_dice.append(max_num[0])
            elif hand_type == Hand.LS:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setLargeStraight(check_large_straight(total_dice))
                else:
                    lsCount = get_ls_count(total_dice)
                    first = lsCount[0]
                    last = lsCount[1]
                    if sum(first) > sum(last):
                        if first[0] == 1:
                            held_dice.append(1)
                        if first[1] == 1:
                            held_dice.append(2)
                        if first[2] == 1:
                            held_dice.append(3)
                        if first[3] == 1:
                            held_dice.append(4)
                        if first[4] == 1:
                            held_dice.append(5)
                    else:
                        if last[0] == 1:
                            held_dice.append(2)
                        if last[1] == 1:
                            held_dice.append(3)
                        if last[2] == 1:
                            held_dice.append(4)
                        if last[3] == 1:
                            held_dice.append(5)
                        if last[4] == 1:
                            held_dice.append(6)
            elif hand_type == Hand.SS:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSmallStraight(check_small_straight(total_dice))
                else:
                    ssCount = get_ss_count(total_dice)
                    first = ssCount[0]
                    middle = ssCount[1]
                    last = ssCount[2]
                    if sum(first) >= sum(last) and sum(first) >= sum(middle):
                        if first[0] == 1:
                            held_dice.append(1)
                        if first[1] == 1:
                            held_dice.append(2)
                        if first[2] == 1:
                            held_dice.append(3)
                        if first[3] == 1:
                            held_dice.append(4)
                    elif sum(middle) >= sum(last) and sum(middle) >= sum(first):
                        if middle[0] == 1:
                            held_dice.append(2)
                        if middle[1] == 1:
                            held_dice.append(3)
                        if middle[2] == 1:
                            held_dice.append(4)
                        if middle[3] == 1:
                            held_dice.append(5)
                    else:
                        if last[0] == 1:
                            held_dice.append(3)
                        if last[1] == 1:
                            held_dice.append(4)
                        if last[2] == 1:
                            held_dice.append(5)
                        if last[3] == 1:
                            held_dice.append(6)
            elif hand_type == Hand.FH:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFullHouse(check_full_house(total_dice))
                else:
                    state = get_fh_state(total_dice)
                    if state == 102:
                        if total_dice[0] == total_dice[1]:
                            if total_dice[2] == total_dice[3]:
                                held_dice = total_dice[0:4]
                            else:
                                held_dice = total_dice[0:2] + total_dice[3:5]
                        else:
                            held_dice = total_dice[1:5]
                    elif state == 103:
                        if total_dice[0] == total_dice[2] or total_dice[1] == total_dice[3]:
                            held_dice == total_dice[0:4]
                        else:
                            held_dice == total_dice[1:5]
                    elif state == 104:
                        if total_dice[0] == total_dice[1]:
                            held_dice = total_dice[0:2]
                        elif total_dice[1] == total_dice[2]:
                            held_dice = total_dice[1:3]
                        elif total_dice[2] == total_dice[3]:
                            held_dice = total_dice[2:4]
                        elif total_dice[3] == total_dice[4]:
                            held_dice = total_dice[3:5]
                    # If 5 unique values, hold no dice
            elif hand_type == Hand.FoK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[0]
                if turns_left == 1:
                    if max_num == 1 and Hand.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == 2 and Hand.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == 3 and Hand.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == 4 and Hand.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == 5 and Hand.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == 6 and Hand.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFoK(check_four_kind(total_dice))
                else:
                    for die in range(0,max_freq[1]):
                        held_dice.append(max_num)
            elif hand_type == Hand.ToK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[0]
                if turns_left == 1:
                    if max_num == 1 and Hand.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == 2 and Hand.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == 3 and Hand.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == 4 and Hand.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == 5 and Hand.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == 6 and Hand.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setToK(check_three_kind(total_dice))
                else:
                    for die in range(max_freq[1]):
                        held_dice.append(max_num)
            elif hand_type == Hand.Sixes:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSixes(check_sixes(total_dice))
                else:
                    freq = total_dice.count(6)
                    for die in range(freq):
                        held_dice.append(6)
            elif hand_type == Hand.Fives:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFives(check_fives(total_dice))
                else:
                    freq = total_dice.count(5)
                    for die in range(freq):
                        held_dice.append(5)
            elif hand_type == Hand.Fours:
                if turns_left == 1:
                    if card.getChance() == -1:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFours(check_fours(total_dice))
                else:
                    freq = total_dice.count(4)
                    for die in range(freq):
                        held_dice.append(4)
            elif hand_type == Hand.Threes:
                if turns_left == 1:
                    card.setThrees(check_threes(total_dice))      
                else:
                    freq = total_dice.count(3)
                    for die in range(freq):
                        held_dice.append(3)
            elif hand_type == Hand.Twos:
                if turns_left == 1:
                    card.setTwos(check_twos(total_dice))      
                else:
                    freq = total_dice.count(2)
                    for die in range(freq):
                        held_dice.append(2)
            elif hand_type == Hand.Ones:
                if turns_left == 1:
                    card.setOnes(check_ones(total_dice))      
                else:
                    freq = total_dice.count(1)
                    for die in range(freq):
                        held_dice.append(1)
            else:
                if turns_left == 1:
                    card.setChance(check_chance(total_dice))
                else:
                    for die in total_dice:
                        if die > 4:
                            held_dice.append(die)

        turns_left-=1
        print(held_dice)
    return card

for i in range(1000):
    playcard = PlayCard()
    playcard = take_turn(playcard)
    print(playcard.getOnes())
    print(playcard.getTwos())
    print(playcard.getThrees())
    print(playcard.getFours())
    print(playcard.getFives())
    print(playcard.getSixes())
    print(playcard.getToK())
    print(playcard.getFoK())
    print(playcard.getFullHouse())
    print(playcard.getSmallStraight())
    print(playcard.getLargeStraight())
    print(playcard.getYacht())
    print(playcard.getChance())
