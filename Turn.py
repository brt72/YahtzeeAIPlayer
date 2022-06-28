from ast import Constant
import random, Constants, PlayCard, Hand
from Probability import *
from YahtzeeAIPlayer.Constants import DIE_INDEX_ONE, DIE_INDEX_TWO, POINT_INDEX



# Creates and returns a list of N random integers between 1 and 6 in numerical order
def roll(dice_amount):
    roll_results = []
    for die in range(dice_amount):
        roll_results.append(random.randint(Constants.MIN_DIE_VALUE, Constants.MAX_DIE_VALUE))
    roll_results.sort()
    return roll_results
    
def take_turn(card):
    turns_left = Constants.TOTAL_TURNS
    mark_card = True
    held_dice = []
    hand_type = Hand.Nothing
    available_hands = card.availableHands()
    while turns_left > 0 and mark_card:
        potential_hands = []

        # Roll Dice
        new_dice = roll(Constants.MAX_DICE-len(held_dice))
        total_dice = held_dice + new_dice
        total_dice.sort() 
        print(total_dice)       
        held_dice = []
        
        # Determine Strategy
        prob_dict = {
            Hand.Ones:prob_num(total_dice, Constants.DIE_VALUE_ONE),
            Hand.Twos:prob_num(total_dice, Constants.DIE_VALUE_TWO),
            Hand.Threes:prob_num(total_dice, Constants.DIE_VALUE_THREE),
            Hand.Fours:prob_num(total_dice, Constants.DIE_VALUE_FOUR),
            Hand.Fives:prob_num(total_dice, Constants.DIE_VALUE_FIVE),
            Hand.Sixes:prob_num(total_dice, Constants.DIE_VALUE_SIX),
            Hand.ToK:prob_tok(total_dice),
            Hand.FoK:prob_fok(total_dice),
            Hand.FH:prob_fh(total_dice),
            Hand.SS:prob_ss(total_dice),
            Hand.LS:prob_ls(total_dice),
            Hand.Yacht:prob_yacht(total_dice)
        }

        # Check if any hand has been met
        for hand in available_hands:
            if prob_dict[hand][Constants.PROB_INDEX] == Constants.MAX_PROB_RESULT:
                potential_hands.append(hand)
        
        # If So, find the highest scoring hand
        if potential_hands != []:
            max_hand = available_hands[0]
            max_points = prob_dict[max_hand][Constants.POINT_INDEX]
            for hand in available_hands:
                if prob_dict[hand][Constants.POINT_INDEX] > max_points:
                    max_points = prob_dict[hand][Constants.POINT_INDEX]
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
                if turns_left == Constants.LAST_TURN or Hand.LS not in available_hands:
                    mark_card = False
                    card.setSmallStraight(check_small_straight(total_dice))
                else:
                    if total_dice[Constants.DIE_INDEX_ZERO] == Constants.MIN_DIE_VALUE:
                        held_dice = [Constants.DIE_VALUE_ONE, Constants.DIE_VALUE_TWO, Constants.DIE_VALUE_THREE, Constants.DIE_VALUE_FOUR]
                    elif total_dice[Constants.DIE_INDEX_FOUR] == Constants.MAX_DIE_VALUE:
                        held_dice = [Constants.DIE_VALUE_THREE, Constants.DIE_VALUE_FOUR, Constants.DIE_VALUE_FIVE, Constants.DIE_VALUE_SIX]
                    else:
                        held_dice = [Constants.DIE_VALUE_TWO, Constants.DIE_VALUE_THREE, Constants.DIE_VALUE_FOUR, Constants.DIE_VALUE_FIVE]
            elif hand_type == Hand.FoK:
                fok_num = total_dice[Constants.DIE_INDEX_TWO]
                print(fok_num)
                if fok_num == Constants.DIE_VALUE_ONE:
                    fok_hand = Hand.Ones
                elif fok_num == Constants.DIE_VALUE_TWO:
                    fok_hand = Hand.Twos
                elif fok_num == Constants.DIE_VALUE_THREE:
                    fok_hand = Hand.Threes
                elif fok_num == Constants.DIE_VALUE_FOUR:
                    fok_hand = Hand.Fours
                elif fok_num == Constants.DIE_VALUE_FIVE:
                    fok_hand = Hand.Fives
                else:
                    fok_hand = Hand.Sixes
                if turns_left == Constants.LAST_TURN:
                    if max_prob[Constants.POINT_INDEX] <= Constants.POINTS_HALF_MAX and fok_hand in available_hands:
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
                tok_num = total_dice[Constants.DIE_INDEX_TWO]
                print(tok_num)
                if tok_num == Constants.DIE_VALUE_ONE:
                    tok_hand = Hand.Ones
                elif tok_num == Constants.DIE_VALUE_TWO:
                    tok_hand = Hand.Twos
                elif tok_num == Constants.DIE_VALUE_THREE:
                    tok_hand = Hand.Threes
                elif tok_num == Constants.DIE_VALUE_FOUR:
                    tok_hand = Hand.Fours
                elif tok_num == Constants.DIE_VALUE_FIVE:
                    tok_hand = Hand.Fives
                else:
                    tok_hand = Hand.Sixes
                if turns_left == Constants.LAST_TURN:
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
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setSixes(check_sixes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(Constants.DIE_VALUE_SIX)
                    held_dice = total_dice[first_index:Constants.DIE_INDEX_FOUR+1]
            elif hand_type == Hand.Fives:
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setFives(check_fives(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(Constants.DIE_VALUE_FIVE)
                    freq = total_dice.count(Constants.DIE_VALUE_FIVE)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Fours:
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setFours(check_fours(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(Constants.DIE_VALUE_FOUR)
                    freq = total_dice.count(Constants.DIE_VALUE_FOUR)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Threes:
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setThrees(check_threes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(Constants.DIE_VALUE_THREE)
                    freq = total_dice.count(Constants.DIE_VALUE_THREE)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Twos:
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setTwos(check_twos(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(Constants.DIE_VALUE_TWO)
                    freq = total_dice.count(Constants.DIE_VALUE_TWO)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == Hand.Ones:
                if turns_left == Constants.LAST_TURN or total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_FOUR]:
                    card.setOnes(check_ones(total_dice))
                    mark_card = False
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_ONE)
                    held_dice = total_dice[Constants.DIE_INDEX_ZERO:freq]


        # If not, and a Strategy has not been decided, find the highest probability hand
        else:
            max_hand = available_hands[0]
            max_prob = prob_dict[max_hand][Constants.PROB_INDEX]
            for hand in available_hands:
                if prob_dict[hand][Constants.PROB_INDEX] > max_prob:
                    max_prob = prob_dict[hand][Constants.PROB_INDEX]
                    max_hand = hand
            hand_type = max_hand
            if hand_type == Hand.Yacht:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setYacht(check_yacht(total_dice))
                else:
                    max_num = check_max_freq(total_dice)
                    for die in range(max_num[Constants.FREQ_INDEX]):
                        held_dice.append(max_num[Constants.NUM_INDEX])
            elif hand_type == Hand.LS:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setLargeStraight(check_large_straight(total_dice))
                else:
                    (first, last) = get_ls_count(total_dice)
                    if sum(first) > sum(last):
                        if first[Constants.DIE_VALUE_ONE-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_ONE)
                        if first[Constants.DIE_VALUE_TWO-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_TWO)
                        if first[Constants.DIE_VALUE_THREE-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_THREE)
                        if first[Constants.DIE_VALUE_FOUR-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_FOUR)
                        if first[Constants.DIE_VALUE_FIVE-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_FIVE)
                    else:
                        if last[Constants.DIE_VALUE_TWO-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_TWO)
                        if last[Constants.DIE_VALUE_THREE-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_THREE)
                        if last[Constants.DIE_VALUE_FOUR-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_FOUR)
                        if last[Constants.DIE_VALUE_FIVE-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_FIVE)
                        if last[Constants.DIE_VALUE_SIX-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_SIX)
            elif hand_type == Hand.SS:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSmallStraight(check_small_straight(total_dice))
                else:
                    (first, middle, last) = get_ss_count(total_dice)
                    if sum(first) >= sum(last) and sum(first) >= sum(middle):
                        if first[Constants.DIE_VALUE_ONE-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_ONE)
                        if first[Constants.DIE_VALUE_TWO-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_TWO)
                        if first[Constants.DIE_VALUE_THREE-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_THREE)
                        if first[Constants.DIE_VALUE_FOUR-1] == 1:
                            held_dice.append(Constants.DIE_VALUE_FOUR)
                    elif sum(middle) >= sum(last) and sum(middle) >= sum(first):
                        if middle[Constants.DIE_VALUE_TWO-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_TWO)
                        if middle[Constants.DIE_VALUE_THREE-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_THREE)
                        if middle[Constants.DIE_VALUE_FOUR-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_FOUR)
                        if middle[Constants.DIE_VALUE_FIVE-2] == 1:
                            held_dice.append(Constants.DIE_VALUE_FIVE)
                    else:
                        if last[Constants.DIE_VALUE_THREE-3] == 1:
                            held_dice.append(Constants.DIE_VALUE_THREE)
                        if last[Constants.DIE_VALUE_FOUR-3] == 1:
                            held_dice.append(Constants.DIE_VALUE_FOUR)
                        if last[Constants.DIE_VALUE_FIVE-3] == 1:
                            held_dice.append(Constants.DIE_VALUE_FIVE)
                        if last[Constants.DIE_VALUE_SIX-3] == 1:
                            held_dice.append(Constants.DIE_VALUE_SIX)
            elif hand_type == Hand.FH:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFullHouse(check_full_house(total_dice))
                else:
                    state = get_fh_state(total_dice)
                    if state == Constants.FH_STATE_TWO_PAIR:
                        if total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_ONE]:
                            if total_dice[Constants.DIE_INDEX_TWO] == total_dice[Constants.DIE_INDEX_THREE]:
                                held_dice = total_dice[Constants.DIE_INDEX_ZERO:Constants.DIE_INDEX_THREE+1]
                            else:
                                held_dice = total_dice[Constants.DIE_INDEX_ZERO:Constants.DIE_INDEX_ONE+1] + total_dice[Constants.DIE_INDEX_THREE:Constants.DIE_INDEX_FOUR+1]
                        else:
                            held_dice = total_dice[Constants.DIE_INDEX_ONE:Constants.DIE_INDEX_FOUR+1]
                    elif state == Constants.FH_STATE_THREE_OF_KIND:
                        if total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_TWO]:
                            held_dice == total_dice[Constants.DIE_INDEX_ZERO:Constants.DIE_INDEX_TWO+1]
                        elif total_dice[Constants.DIE_INDEX_ONE] == total_dice[Constants.DIE_INDEX_THREE]:
                            held_dice == total_dice[Constants.DIE_INDEX_ONE:Constants.DIE_INDEX_THREE+1]
                        else:
                            held_dice == total_dice[Constants.DIE_INDEX_TWO:Constants.DIE_INDEX_FOUR+1]
                    elif state == Constants.FH_STATE_ONE_PAIR:
                        if total_dice[Constants.DIE_INDEX_ZERO] == total_dice[Constants.DIE_INDEX_ONE]:
                            held_dice = total_dice[Constants.DIE_INDEX_ZERO:Constants.DIE_INDEX_ONE+1]
                        elif total_dice[Constants.DIE_INDEX_ONE] == total_dice[Constants.DIE_INDEX_TWO]:
                            held_dice = total_dice[Constants.DIE_INDEX_ONE:Constants.DIE_INDEX_TWO+1]
                        elif total_dice[Constants.DIE_INDEX_TWO] == total_dice[Constants.DIE_INDEX_THREE]:
                            held_dice = total_dice[Constants.DIE_INDEX_TWO:Constants.DIE_INDEX_THREE+1]
                        elif total_dice[Constants.DIE_INDEX_THREE] == total_dice[Constants.DIE_INDEX_FOUR]:
                            held_dice = total_dice[Constants.DIE_INDEX_THREE:Constants.DIE_INDEX_FOUR+1]
                    # If 5 unique values, hold no dice
            elif hand_type == Hand.FoK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[Constants.NUM_INDEX]
                if turns_left == Constants.LAST_TURN:
                    if max_num == Constants.DIE_VALUE_ONE and Hand.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == Constants.DIE_VALUE_TWO and Hand.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == Constants.DIE_VALUE_THREE and Hand.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == Constants.DIE_VALUE_FOUR and Hand.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == Constants.DIE_VALUE_FIVE and Hand.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == Constants.DIE_VALUE_SIX and Hand.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFoK(check_four_kind(total_dice))
                else:
                    for die in range(Constants.DIE_INDEX_ZERO, max_freq[Constants.FREQ_INDEX]):
                        held_dice.append(max_num)
            elif hand_type == Hand.ToK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[Constants.NUM_INDEX]
                if turns_left == Constants.LAST_TURN:
                    if max_num == Constants.DIE_VALUE_ONE and Hand.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == Constants.DIE_VALUE_TWO and Hand.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == Constants.DIE_VALUE_THREE and Hand.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == Constants.DIE_VALUE_FOUR and Hand.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == Constants.DIE_VALUE_FIVE and Hand.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == Constants.DIE_VALUE_SIX and Hand.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setToK(check_three_kind(total_dice))
                else:
                    for die in range(Constants.DIE_INDEX_ZERO, max_freq[Constants.FREQ_INDEX]):
                        held_dice.append(max_num)
            elif hand_type == Hand.Sixes:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSixes(check_sixes(total_dice))
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_SIX)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_SIX)
            elif hand_type == Hand.Fives:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFives(check_fives(total_dice))
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_FIVE)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_FIVE)
            elif hand_type == Hand.Fours:
                if turns_left == Constants.LAST_TURN:
                    if card.getChance() == Constants.INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFours(check_fours(total_dice))
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_FOUR)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_FOUR)
            elif hand_type == Hand.Threes:
                if turns_left == Constants.LAST_TURN:
                    card.setThrees(check_threes(total_dice))      
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_THREE)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_THREE)
            elif hand_type == Hand.Twos:
                if turns_left == Constants.LAST_TURN:
                    card.setTwos(check_twos(total_dice))      
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_TWO)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_TWO)
            elif hand_type == Hand.Ones:
                if turns_left == Constants.LAST_TURN:
                    card.setOnes(check_ones(total_dice))      
                else:
                    freq = total_dice.count(Constants.DIE_VALUE_ONE)
                    for die in range(freq):
                        held_dice.append(Constants.DIE_VALUE_ONE)
            else:
                if turns_left == Constants.LAST_TURN:
                    card.setChance(check_chance(total_dice))
                else:
                    for die in total_dice:
                        if die > Constants.DIE_VALUE_FOUR:
                            held_dice.append(die)

        turns_left-=1
        print(held_dice)
    return card