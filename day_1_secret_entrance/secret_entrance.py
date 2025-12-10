def read_input_file():
    with open('input', 'r', encoding='utf-8') as f:
        instructions = f.readlines()
    # strip leading and trailing whitespaces (here EOL)
    instructions = [s.strip() for s in instructions]
    # Split every instruction into the L/R-part and the numerical part (as int)
    instructions = [(s[0], int(s[1:])) for s in instructions]
    return(instructions)

def calculate_password(instructions):
    zeroes = 0
    dial = 50 # starting position of dial

    for direction, number in instructions:
        # Calculate new dial position
        if direction == "R": # adding value to dial position when truning right
            dial = dial + number
            while dial > 99: # when the dial reaches 99 it starts at 0 again
                dial = dial - 100
            if dial == 0:
                zeroes += 1
        elif direction == "L": # subtracting value from dial position when truning left
            dial = dial - number
            while dial < 0: # when the dial reaches 0 it goes round to 99
                dial = dial + 100
            if dial == 0:
                zeroes += 1

    return(zeroes)

def method_zero_click(instructions):
    zero_clicks = 0
    dial = 50 # starting position of dial

    for direction, number in instructions:
        # Calculate new dial position
        if direction == "R": # adding value to dial position when truning right
            dial = dial + number
            while dial > 99: # when the dial reaches 99 it starts at 0 again
                dial = dial - 100
                zero_clicks += 1 # increment for every turn that zero is passed (and if the last turn lands on zero)
        elif direction == "L": # subtracting value from dial position when truning left
            # Check whether the dial starts at zero, then it won't pass zero on the
            # first turn even though the result will necessarily be negative (as 0
            # minus anything is a negative number). Exception to the
            # excpetion: it lands on zero on the first (and any subsequent) turn:
            # number is a multiple of 100.
            if dial == 0 and number % 100 != 0: zero_clicks -= 1 # deduct the extra click that the loop will count here in advance, unless it lands on 0 (number multiple of 100)
            dial = dial - number
            while dial < 0: # when the dial reaches 0 it goes round to 99
                dial = dial + 100
                zero_clicks += 1
            if dial == 0: zero_clicks += 1 # when it lands on 0 after all turns, add click


    return(zero_clicks)

instructions = read_input_file()
#password = calculate_password(instructions)
password = method_zero_click(instructions)
print(password)
