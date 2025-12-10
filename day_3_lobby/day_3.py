# AoC 2025, day 3: Lobby

# Steps:
# - find the highest digit in each line that is not the last character
# - record the digit and it's first position
# - find the highest number after the postion of the first one up to the last
#   character
# - concatenate the new number and record it

def read_battery_banks():
    with open('input', 'r', encoding='utf-8') as f:
        battery_banks = f.readlines()
    # strip leading and trailing whitespaces (here EOL)
    battery_banks = [s.strip() for s in battery_banks]
    # Split every battery bank into indivdual batteries (list of lists) and convert
    # to integer
    battery_banks = [[int(char) for char in s] for s in battery_banks]
    return(battery_banks)

def find_highest_joltage_2(battery_banks):
    highest_joltages = []
    for bat in battery_banks:
        max_val_1 = bat[0]
        for index, val in list(enumerate(bat))[1:-1]: # find the max value for the first digit
            if val > max_val_1:
                max_val_1 = val
                max_pos_1 = index
        max_val_2 = bat[max_pos_1 + 1]
        for val in bat[max_pos_1 + 1:]: # find max value for the second digit
            if val > max_val_2:
                max_val_2 = val
        joltage = int(str(max_val_1) + str(max_val_2))
        highest_joltages.append(joltage)
    return(highest_joltages)

def find_highest_joltage_12(battery_banks):
    highest_joltages = []
    # Idea: in the firs run search highest number in the range 0-(-11), set current
    # postion to found number, second run highest number in current_position+1 -
    # (-10) and so on, run twelve times.
    # Variables needed: current_postition, run_count, max_val, max_values (list for
    # found max values)
    for bat in battery_banks:
        pos = 0
        max_vals = []
        for count in range(12):
            max_val = bat[pos]
            # Find the max value for the counth digit
            # Set start end end position for the search in the list:
            start = pos + 1 # this I could do directly in the call of the for loop
            if count < 11:
                end = count - 11
            elif count == 11:      # for the last run I have to set end to nothing as
                end = None         # 11-11 would be 0 and thus selecting the first position
            for index, val in list(enumerate(bat))[start:end]:
                if val > max_val:
                    max_val = val
                    pos = index
            pos += 1
            max_vals.append(str(max_val))
        joltage = int("".join(max_vals))
        highest_joltages.append(joltage)
    return(highest_joltages)


battery_banks = read_battery_banks()
#highest_joltages = find_highest_joltage_2(battery_banks)
highest_joltages = find_highest_joltage_12(battery_banks)

result = sum(highest_joltages)
print(result)
