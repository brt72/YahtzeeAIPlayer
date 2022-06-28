import Constants
from CheckHand import *

# Ones, Twos, Threes, Fours, Fives, Sixes Probability (aim for 3)
def prob_num(dice_list, num):
    freq = dice_list.count(num)
    if(freq == Constants.ZERO_FREQ):
        probability = Constants.PROB_RESULT_N
    elif(freq == Constants.ONE_FREQ):
        probability = Constants.PROB_RESULT_G
    elif(freq == Constants.TWO_FREQ):
        probability = Constants.PROB_RESULT_B
    else:
        probability = Constants.MAX_PROB_RESULT
    return (num*freq, probability)

def prob_tok(dice_list):
    max_freq = check_max_freq(dice_list)
    points = 0
    if(max_freq[Constants.FREQ_INDEX] == Constants.ONE_FREQ):
        probability = Constants.PROB_RESULT_G
    elif(max_freq[Constants.FREQ_INDEX] == Constants.TWO_FREQ):
        probability = Constants.PROB_RESULT_B
    else:
        probability = Constants.MAX_PROB_RESULT
        points = sum(dice_list)
    return(points, probability)

def prob_fok(dice_list):
    max_freq = check_max_freq(dice_list)
    points = Constants.POINTS_ZERO
    if(max_freq[Constants.FREQ_INDEX] == Constants.ONE_FREQ):
        probability = Constants.PROB_RESULT_Q
    elif(max_freq[Constants.FREQ_INDEX] == Constants.TWO_FREQ):
        probability = Constants.PROB_RESULT_K
    elif(max_freq[Constants.FREQ_INDEX] == Constants.THREE_FREQ):
        probability = Constants.PROB_RESULT_D
    else:
        probability = Constants.MAX_PROB_RESULT
        points = sum(dice_list)
    return(points, probability)

def get_fh_state(dice_list):
    if check_full_house(dice_list) != Constants.POINTS_ZERO:
        return Constants.FH_STATE_FULL_HOUSE
    # Two Pair
    elif dice_list[Constants.DIE_INDEX_ZERO] == dice_list[Constants.DIE_INDEX_ONE] and (dice_list[Constants.DIE_INDEX_TWO] == dice_list[3] or dice_list[Constants.DIE_INDEX_THREE] == dice_list[4]) or dice_list[Constants.DIE_INDEX_ONE] == dice_list[Constants.DIE_INDEX_TWO] and dice_list[Constants.DIE_INDEX_THREE] == dice_list[Constants.DIE_INDEX_FOUR]:
        return Constants.FH_STATE_TWO_PAIR
    # 3-1-1
    elif dice_list[Constants.DIE_INDEX_ZERO] == dice_list[Constants.DIE_INDEX_TWO] or dice_list[Constants.DIE_INDEX_ONE] == dice_list[3] or dice_list[Constants.DIE_INDEX_TWO] == dice_list[4]:
        return Constants.FH_STATE_THREE_OF_KIND
    # One Pair
    elif dice_list[Constants.DIE_INDEX_ZERO] == dice_list[Constants.DIE_INDEX_ONE] or dice_list[Constants.DIE_INDEX_ONE] == dice_list[Constants.DIE_INDEX_TWO] or dice_list[Constants.DIE_INDEX_TWO] == dice_list[Constants.DIE_INDEX_THREE] or dice_list[Constants.DIE_INDEX_THREE] == dice_list[Constants.DIE_INDEX_FOUR]:
        return Constants.FH_STATE_ONE_PAIR
    # Five Unique Values
    return Constants.FH_STATE_FIVE_VALUES


def prob_fh(dice_list):
    points = Constants.POINTS_ZERO
    state = get_fh_state(dice_list)
    # Full House
    if state == Constants.FH_STATE_FULL_HOUSE:
        points = Constants.POINTS_FULL_HOUSE
        probability = Constants.MAX_PROB_RESULT
    # Two Pair
    elif state == Constants.FH_STATE_TWO_PAIR:
        probability = Constants.PROB_RESULT_C
    # 3-1-1
    elif state == Constants.FH_STATE_THREE_OF_KIND:
        probability = Constants.PROB_RESULT_E
    # One Pair
    elif state == Constants.FH_STATE_ONE_PAIR:
        probability = Constants.PROB_RESULT_I
    # Five Unique Values
    else:
        probability = Constants.PROB_RESULT_M
    return(points, probability)

def get_ss_count(dice_list):
    all_freq = [dice_list.count(Constants.DIE_VALUE_ONE), dice_list.count(Constants.DIE_VALUE_TWO), dice_list.count(Constants.DIE_VALUE_THREE), dice_list.count(Constants.DIE_VALUE_FOUR), dice_list.count(Constants.DIE_VALUE_FIVE), dice_list.count(Constants.DIE_VALUE_SIX)]
    first = [0,0,0,0] # 1, 2, 3, 4
    middle = [0,0,0,0] # 2, 3, 4, 5
    last = [0,0,0,0] # 3, 4, 5, 6
    if all_freq[Constants.DIE_VALUE_ONE-1] > 0:
        first[Constants.DIE_VALUE_ONE-1]+=1
    if all_freq[Constants.DIE_VALUE_TWO-1] > 0:
        first[Constants.DIE_VALUE_TWO-1]+=1
        middle[Constants.DIE_VALUE_TWO-2]+=1 
    if all_freq[Constants.DIE_VALUE_THREE-1] > 0:
        first[Constants.DIE_VALUE_THREE-1]+=1
        middle[Constants.DIE_VALUE_THREE-2]+=1  
        last[Constants.DIE_VALUE_THREE-3]+=1    
    if all_freq[Constants.DIE_VALUE_FOUR-1] > 0:
        first[Constants.DIE_VALUE_FOUR-1]+=1
        middle[Constants.DIE_VALUE_FOUR-2]+=1  
        last[Constants.DIE_VALUE_FOUR-3]+=1  
    if all_freq[Constants.DIE_VALUE_FIVE-1] > 0:
        middle[Constants.DIE_VALUE_FIVE-2]+=1  
        last[Constants.DIE_VALUE_FIVE-3]+=1 
    if all_freq[Constants.DIE_VALUE_SIX-1] > 0:
        last[Constants.DIE_VALUE_SIX-3]+=1

    return (first, middle, last)

def prob_ss(dice_list):
    points = Constants.POINTS_ZERO
    (first, middle, last) = get_ss_count(dice_list)


    if sum(first) == Constants.STRAIGHT_CORRECT_FOUR or sum(middle) == Constants.STRAIGHT_CORRECT_FOUR or sum(last) == Constants.STRAIGHT_CORRECT_FOUR:
        probability = Constants.MAX_PROB_RESULT
        points = Constants.POINTS_SMALL_STRAIGHT
    elif (first == [0,1,1,1] and middle == [1,1,1,0]) or (middle == [0,1,1,1] and last == [1,1,1,0]):
        probability = Constants.PROB_RESULT_A
    elif sum(first) == Constants.STRAIGHT_CORRECT_THREE or sum(middle) == Constants.STRAIGHT_CORRECT_THREE or sum(last) == Constants.STRAIGHT_CORRECT_THREE:
        probability = Constants.PROB_RESULT_D
    elif sum(first) == Constants.STRAIGHT_CORRECT_TWO or sum(middle) == Constants.STRAIGHT_CORRECT_TWO or sum(last) == Constants.STRAIGHT_CORRECT_TWO:
        probability = Constants.PROB_RESULT_F
    else:
        probability = Constants.PROB_RESULT_J
    return(points, probability)

def get_ls_count(dice_list):
    all_freq = [dice_list.count(Constants.DIE_VALUE_ONE), dice_list.count(Constants.DIE_VALUE_TWO), dice_list.count(Constants.DIE_VALUE_THREE), dice_list.count(Constants.DIE_VALUE_FOUR), dice_list.count(Constants.DIE_VALUE_FIVE), dice_list.count(Constants.DIE_VALUE_SIX)]
    first = [0,0,0,0,0] # 1, 2, 3, 4, 5
    last = [0,0,0,0,0] # 2, 3, 4, 5, 6
    if all_freq[Constants.DIE_VALUE_ONE-1] > 0:
        first[Constants.DIE_VALUE_ONE-1]+=1
    if all_freq[Constants.DIE_VALUE_TWO-1] > 0:
        first[Constants.DIE_VALUE_TWO-1]+=1
        last[Constants.DIE_VALUE_TWO-2]+=1
    if all_freq[Constants.DIE_VALUE_THREE-1] > 0:
        first[Constants.DIE_VALUE_THREE-1]+=1
        last[Constants.DIE_VALUE_THREE-2]+=1    
    if all_freq[Constants.DIE_VALUE_FOUR-1] > 0:
        first[Constants.DIE_VALUE_FOUR-1]+=1
        last[Constants.DIE_VALUE_FOUR-2]+=1
    if all_freq[Constants.DIE_VALUE_FIVE-1] > 0:
        first[Constants.DIE_VALUE_FIVE-1]
        last[Constants.DIE_VALUE_FIVE-2]+=1
    if all_freq[Constants.DIE_VALUE_SIX-1] > 0:
        last[Constants.DIE_VALUE_SIX-1]+=1

    return (first, last)

# Large Straight
def prob_ls(dice_list):
    points = Constants.POINTS_ZERO
    (first, last) = get_ls_count(dice_list)

    if sum(first) == Constants.STRAIGHT_CORRECT_FIVE or sum(last) == Constants.STRAIGHT_CORRECT_FIVE:
        probability = Constants.MAX_PROB_RESULT
        points = Constants.POINTS_LARGE_STRAIGHT
    elif first == [0,1,1,1,1] and last == [1,1,1,1,0]:
        probability = Constants.PROB_RESULT_C
    elif sum(first) == Constants.STRAIGHT_CORRECT_FOUR or sum(last) == Constants.STRAIGHT_CORRECT_FOUR:
        probability = Constants.PROB_RESULT_E
    elif (first == [0,0,1,1,1] and last == [0,1,1,1,0]) or (first == [0,1,1,1,0] and last == [1,1,1,0,0]):
        probability = Constants.PROB_RESULT_H
    elif sum(first) == Constants.STRAIGHT_CORRECT_THREE or sum(last) == Constants.STRAIGHT_CORRECT_THREE:
        probability = Constants.PROB_RESULT_L
    elif sum(first) == Constants.STRAIGHT_CORRECT_TWO or sum(last) == Constants.STRAIGHT_CORRECT_TWO:
        probability = Constants.PROB_RESULT_O
    else:
        probability = Constants.PROB_RESULT_P
    return(points, probability)


def prob_yacht(dice_list):
    points = Constants.POINTS_ZERO
    max_freq = check_max_freq(dice_list)
    if max_freq[Constants.FREQ_INDEX] == Constants.FIVE_FREQ:
        points = Constants.POINTS_YACHT
    probability = 1/(Constants.TOTAL_UNIQUE_DIE_VALUES**(Constants.MAX_DICE-max_freq[1]))
    return (points, probability)

