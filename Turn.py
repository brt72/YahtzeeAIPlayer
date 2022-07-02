import random
from Hand import HandTypes
from Probability import *
from Constants import *
from PlayCard import PlayCard



# Creates and returns a list of N random integers between 1 and 6 in numerical order
def roll(dice_amount):
    roll_results = []
    for die in range(dice_amount):
        roll_results.append(random.randint(MIN_DIE_VALUE, MAX_DIE_VALUE))
    roll_results.sort()
    return roll_results
    
def take_turn(card):
    turns_left = TOTAL_TURNS
    mark_card = True
    held_dice = []
    hand_type = HandTypes.Nothing
    available_hands = card.availableHands()
    while turns_left > 0 and mark_card:
        potential_hands = []

        # Roll Dice
        new_dice = roll(MAX_DICE-len(held_dice))
        total_dice = held_dice + new_dice
        total_dice.sort() 
        held_dice = []
        print(total_dice)
        
        # Determine Strategy
        prob_dict = {
            HandTypes.Ones:prob_num(total_dice, DIE_VALUE_ONE),
            HandTypes.Twos:prob_num(total_dice, DIE_VALUE_TWO),
            HandTypes.Threes:prob_num(total_dice, DIE_VALUE_THREE),
            HandTypes.Fours:prob_num(total_dice, DIE_VALUE_FOUR),
            HandTypes.Fives:prob_num(total_dice, DIE_VALUE_FIVE),
            HandTypes.Sixes:prob_num(total_dice, DIE_VALUE_SIX),
            HandTypes.ToK:prob_tok(total_dice),
            HandTypes.FoK:prob_fok(total_dice),
            HandTypes.FH:prob_fh(total_dice),
            HandTypes.SS:prob_ss(total_dice),
            HandTypes.LS:prob_ls(total_dice),
            HandTypes.Yacht:prob_yacht(total_dice)
        }

        # Check if any hand has been met
        for hand in available_hands:
            if prob_dict[hand][PROB_INDEX] == MAX_PROB_RESULT:
                potential_hands.append(hand)
        
        # If So, find the highest scoring hand
        if potential_hands != []:
            max_hand = available_hands[0]
            max_points = prob_dict[max_hand][POINT_INDEX]
            for hand in available_hands:
                if prob_dict[hand][POINT_INDEX] > max_points:
                    max_points = prob_dict[hand][POINT_INDEX]
                    max_hand = hand
            hand_type = max_hand
            if hand_type == HandTypes.Yacht:
                mark_card = False
                card.setYacht(check_yacht(total_dice))
            elif hand_type == HandTypes.LS:
                mark_card = False
                card.setLargeStraight(check_large_straight(total_dice))
            elif hand_type == HandTypes.FH:
                mark_card = False
                card.setFullHouse(check_full_house(total_dice))
            elif hand_type == HandTypes.SS:
                if turns_left == LAST_TURN or HandTypes.LS not in available_hands:
                    mark_card = False
                    card.setSmallStraight(check_small_straight(total_dice))
                else:
                    if total_dice[DIE_INDEX_ZERO] == MIN_DIE_VALUE:
                        held_dice = [DIE_VALUE_ONE, DIE_VALUE_TWO, DIE_VALUE_THREE, DIE_VALUE_FOUR]
                    elif total_dice[DIE_INDEX_FOUR] == MAX_DIE_VALUE:
                        held_dice = [DIE_VALUE_THREE, DIE_VALUE_FOUR, DIE_VALUE_FIVE, DIE_VALUE_SIX]
                    else:
                        held_dice = [DIE_VALUE_TWO, DIE_VALUE_THREE, DIE_VALUE_FOUR, DIE_VALUE_FIVE]
            elif hand_type == HandTypes.FoK:
                fok_num = total_dice[DIE_INDEX_TWO]
                if fok_num == DIE_VALUE_ONE:
                    fok_hand = HandTypes.Ones
                elif fok_num == DIE_VALUE_TWO:
                    fok_hand = HandTypes.Twos
                elif fok_num == DIE_VALUE_THREE:
                    fok_hand = HandTypes.Threes
                elif fok_num == DIE_VALUE_FOUR:
                    fok_hand = HandTypes.Fours
                elif fok_num == DIE_VALUE_FIVE:
                    fok_hand = HandTypes.Fives
                else:
                    fok_hand = HandTypes.Sixes
                if turns_left == LAST_TURN:
                    if max_points <= POINTS_HALF_MAX and fok_hand in available_hands:
                        if fok_hand == HandTypes.Ones:
                            card.setOnes(check_ones(total_dice))
                        elif fok_hand == HandTypes.Twos:
                            card.setTwos(check_twos(total_dice))
                        elif fok_hand == HandTypes.Threes:
                            card.setThrees(check_threes(total_dice))
                        elif fok_hand == HandTypes.Fours:
                            card.setFours(check_fours(total_dice))
                        elif fok_hand == HandTypes.Fives:
                            card.setFives(check_fives(total_dice))
                        else:
                            card.setSixes(check_sixes(total_dice))
                    else:
                        card.setFoK(check_four_kind(total_dice))
                else:
                    held_dice = [fok_num, fok_num, fok_num, fok_num]
            elif hand_type == HandTypes.ToK:
                tok_num = total_dice[DIE_INDEX_TWO]
                if tok_num == DIE_VALUE_ONE:
                    tok_hand = HandTypes.Ones
                elif tok_num == DIE_VALUE_TWO:
                    tok_hand = HandTypes.Twos
                elif tok_num == DIE_VALUE_THREE:
                    tok_hand = HandTypes.Threes
                elif tok_num == DIE_VALUE_FOUR:
                    tok_hand = HandTypes.Fours
                elif tok_num == DIE_VALUE_FIVE:
                    tok_hand = HandTypes.Fives
                else:
                    tok_hand = HandTypes.Sixes
                if turns_left == LAST_TURN:
                    if max_points <= POINTS_HALF_MAX and tok_hand in available_hands:
                        if tok_hand == HandTypes.Ones:
                            card.setOnes(check_ones(total_dice))
                        elif tok_hand == HandTypes.Twos:
                            card.setTwos(check_twos(total_dice))
                        elif tok_hand == HandTypes.Threes:
                            card.setThrees(check_threes(total_dice))
                        elif tok_hand == HandTypes.Fours:
                            card.setFours(check_fours(total_dice))
                        elif tok_hand == HandTypes.Fives:
                            card.setFives(check_fives(total_dice))
                        else:
                            card.setSixes(check_sixes(total_dice))
                    else:
                        card.setToK(check_three_kind(total_dice))
                else:
                    held_dice = [tok_num, tok_num, tok_num]
            elif hand_type == HandTypes.Sixes:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setSixes(check_sixes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(DIE_VALUE_SIX)
                    held_dice = total_dice[first_index:DIE_INDEX_FOUR+1]
            elif hand_type == HandTypes.Fives:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setFives(check_fives(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(DIE_VALUE_FIVE)
                    freq = total_dice.count(DIE_VALUE_FIVE)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == HandTypes.Fours:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setFours(check_fours(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(DIE_VALUE_FOUR)
                    freq = total_dice.count(DIE_VALUE_FOUR)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == HandTypes.Threes:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setThrees(check_threes(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(DIE_VALUE_THREE)
                    freq = total_dice.count(DIE_VALUE_THREE)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == HandTypes.Twos:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setTwos(check_twos(total_dice))
                    mark_card = False
                else:
                    first_index = total_dice.index(DIE_VALUE_TWO)
                    freq = total_dice.count(DIE_VALUE_TWO)
                    held_dice = total_dice[first_index:first_index+freq]
            elif hand_type == HandTypes.Ones:
                if turns_left == LAST_TURN or total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_FOUR]:
                    card.setOnes(check_ones(total_dice))
                    mark_card = False
                else:
                    freq = total_dice.count(DIE_VALUE_ONE)
                    held_dice = total_dice[DIE_INDEX_ZERO:freq]


        # If not, and a Strategy has not been decided, find the highest probability hand
        else:
            max_hand = available_hands[0]
            max_prob = prob_dict[max_hand][PROB_INDEX]
            for hand in available_hands:
                if prob_dict[hand][PROB_INDEX] > max_prob:
                    max_prob = prob_dict[hand][PROB_INDEX]
                    max_hand = hand
            hand_type = max_hand
            if hand_type == HandTypes.Yacht:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setYacht(check_yacht(total_dice))
                else:
                    max_num = check_max_freq(total_dice)
                    for die in range(max_num[FREQ_INDEX]):
                        held_dice.append(max_num[NUM_INDEX])
            elif hand_type == HandTypes.LS:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setLargeStraight(check_large_straight(total_dice))
                else:
                    (first, last) = get_ls_count(total_dice)
                    if sum(first) > sum(last):
                        if first[DIE_VALUE_ONE-1] == 1:
                            held_dice.append(DIE_VALUE_ONE)
                        if first[DIE_VALUE_TWO-1] == 1:
                            held_dice.append(DIE_VALUE_TWO)
                        if first[DIE_VALUE_THREE-1] == 1:
                            held_dice.append(DIE_VALUE_THREE)
                        if first[DIE_VALUE_FOUR-1] == 1:
                            held_dice.append(DIE_VALUE_FOUR)
                        if first[DIE_VALUE_FIVE-1] == 1:
                            held_dice.append(DIE_VALUE_FIVE)
                    else:
                        if last[DIE_VALUE_TWO-2] == 1:
                            held_dice.append(DIE_VALUE_TWO)
                        if last[DIE_VALUE_THREE-2] == 1:
                            held_dice.append(DIE_VALUE_THREE)
                        if last[DIE_VALUE_FOUR-2] == 1:
                            held_dice.append(DIE_VALUE_FOUR)
                        if last[DIE_VALUE_FIVE-2] == 1:
                            held_dice.append(DIE_VALUE_FIVE)
                        if last[DIE_VALUE_SIX-2] == 1:
                            held_dice.append(DIE_VALUE_SIX)
            elif hand_type == HandTypes.SS:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSmallStraight(check_small_straight(total_dice))
                else:
                    (first, middle, last) = get_ss_count(total_dice)
                    if sum(first) >= sum(last) and sum(first) >= sum(middle):
                        if first[DIE_VALUE_ONE-1] == 1:
                            held_dice.append(DIE_VALUE_ONE)
                        if first[DIE_VALUE_TWO-1] == 1:
                            held_dice.append(DIE_VALUE_TWO)
                        if first[DIE_VALUE_THREE-1] == 1:
                            held_dice.append(DIE_VALUE_THREE)
                        if first[DIE_VALUE_FOUR-1] == 1:
                            held_dice.append(DIE_VALUE_FOUR)
                    elif sum(middle) >= sum(last) and sum(middle) >= sum(first):
                        if middle[DIE_VALUE_TWO-2] == 1:
                            held_dice.append(DIE_VALUE_TWO)
                        if middle[DIE_VALUE_THREE-2] == 1:
                            held_dice.append(DIE_VALUE_THREE)
                        if middle[DIE_VALUE_FOUR-2] == 1:
                            held_dice.append(DIE_VALUE_FOUR)
                        if middle[DIE_VALUE_FIVE-2] == 1:
                            held_dice.append(DIE_VALUE_FIVE)
                    else:
                        if last[DIE_VALUE_THREE-3] == 1:
                            held_dice.append(DIE_VALUE_THREE)
                        if last[DIE_VALUE_FOUR-3] == 1:
                            held_dice.append(DIE_VALUE_FOUR)
                        if last[DIE_VALUE_FIVE-3] == 1:
                            held_dice.append(DIE_VALUE_FIVE)
                        if last[DIE_VALUE_SIX-3] == 1:
                            held_dice.append(DIE_VALUE_SIX)
            elif hand_type == HandTypes.FH:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFullHouse(check_full_house(total_dice))
                else:
                    state = get_fh_state(total_dice)
                    if state == FH_STATE_TWO_PAIR:
                        if total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_ONE]:
                            if total_dice[DIE_INDEX_TWO] == total_dice[DIE_INDEX_THREE]:
                                held_dice = total_dice[DIE_INDEX_ZERO:DIE_INDEX_THREE+1]
                            else:
                                held_dice = total_dice[DIE_INDEX_ZERO:DIE_INDEX_ONE+1] + total_dice[DIE_INDEX_THREE:DIE_INDEX_FOUR+1]
                        else:
                            held_dice = total_dice[DIE_INDEX_ONE:DIE_INDEX_FOUR+1]
                    elif state == FH_STATE_THREE_OF_KIND:
                        if total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_TWO]:
                            held_dice == total_dice[DIE_INDEX_ZERO:DIE_INDEX_TWO+1]
                        elif total_dice[DIE_INDEX_ONE] == total_dice[DIE_INDEX_THREE]:
                            held_dice == total_dice[DIE_INDEX_ONE:DIE_INDEX_THREE+1]
                        else:
                            held_dice == total_dice[DIE_INDEX_TWO:DIE_INDEX_FOUR+1]
                    elif state == FH_STATE_ONE_PAIR:
                        if total_dice[DIE_INDEX_ZERO] == total_dice[DIE_INDEX_ONE]:
                            held_dice = total_dice[DIE_INDEX_ZERO:DIE_INDEX_ONE+1]
                        elif total_dice[DIE_INDEX_ONE] == total_dice[DIE_INDEX_TWO]:
                            held_dice = total_dice[DIE_INDEX_ONE:DIE_INDEX_TWO+1]
                        elif total_dice[DIE_INDEX_TWO] == total_dice[DIE_INDEX_THREE]:
                            held_dice = total_dice[DIE_INDEX_TWO:DIE_INDEX_THREE+1]
                        elif total_dice[DIE_INDEX_THREE] == total_dice[DIE_INDEX_FOUR]:
                            held_dice = total_dice[DIE_INDEX_THREE:DIE_INDEX_FOUR+1]
                    # If 5 unique values, hold no dice
            elif hand_type == HandTypes.FoK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[NUM_INDEX]
                if turns_left == LAST_TURN:
                    if max_num == DIE_VALUE_ONE and HandTypes.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == DIE_VALUE_TWO and HandTypes.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == DIE_VALUE_THREE and HandTypes.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == DIE_VALUE_FOUR and HandTypes.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == DIE_VALUE_FIVE and HandTypes.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == DIE_VALUE_SIX and HandTypes.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFoK(check_four_kind(total_dice))
                else:
                    for die in range(DIE_INDEX_ZERO, max_freq[FREQ_INDEX]):
                        held_dice.append(max_num)
            elif hand_type == HandTypes.ToK:
                max_freq = check_max_freq(total_dice)
                max_num = max_freq[NUM_INDEX]
                if turns_left == LAST_TURN:
                    if max_num == DIE_VALUE_ONE and HandTypes.Ones in available_hands:
                        card.setOnes(check_ones(total_dice))
                    elif max_num == DIE_VALUE_TWO and HandTypes.Twos in available_hands:
                        card.setTwos(check_twos(total_dice))
                    elif max_num == DIE_VALUE_THREE and HandTypes.Threes in available_hands:
                        card.setThrees(check_threes(total_dice))
                    elif max_num == DIE_VALUE_FOUR and HandTypes.Fours in available_hands:
                        card.setFours(check_fours(total_dice))
                    elif max_num == DIE_VALUE_FIVE and HandTypes.Fives in available_hands:
                        card.setFives(check_fives(total_dice))
                    elif max_num == DIE_VALUE_SIX and HandTypes.Sixes in available_hands:
                        card.setSixes(check_sixes(total_dice))
                    elif card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setToK(check_three_kind(total_dice))
                else:
                    for die in range(DIE_INDEX_ZERO, max_freq[FREQ_INDEX]):
                        held_dice.append(max_num)
            elif hand_type == HandTypes.Sixes:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setSixes(check_sixes(total_dice))
                else:
                    freq = total_dice.count(DIE_VALUE_SIX)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_SIX)
            elif hand_type == HandTypes.Fives:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFives(check_fives(total_dice))
                else:
                    freq = total_dice.count(DIE_VALUE_FIVE)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_FIVE)
            elif hand_type == HandTypes.Fours:
                if turns_left == LAST_TURN:
                    if card.getChance() == INCOMPLETE_ENTRY:
                        card.setChance(check_chance(total_dice))
                    else:
                        card.setFours(check_fours(total_dice))
                else:
                    freq = total_dice.count(DIE_VALUE_FOUR)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_FOUR)
            elif hand_type == HandTypes.Threes:
                if turns_left == LAST_TURN:
                    card.setThrees(check_threes(total_dice))      
                else:
                    freq = total_dice.count(DIE_VALUE_THREE)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_THREE)
            elif hand_type == HandTypes.Twos:
                if turns_left == LAST_TURN:
                    card.setTwos(check_twos(total_dice))      
                else:
                    freq = total_dice.count(DIE_VALUE_TWO)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_TWO)
            elif hand_type == HandTypes.Ones:
                if turns_left == LAST_TURN:
                    card.setOnes(check_ones(total_dice))      
                else:
                    freq = total_dice.count(DIE_VALUE_ONE)
                    for die in range(freq):
                        held_dice.append(DIE_VALUE_ONE)
            else:
                if turns_left == LAST_TURN:
                    card.setChance(check_chance(total_dice))
                else:
                    for die in total_dice:
                        if die > DIE_VALUE_FOUR:
                            held_dice.append(die)

        turns_left-=1
    return card