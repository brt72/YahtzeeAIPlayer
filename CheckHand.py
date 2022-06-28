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