import re 
from math import prod

def read_math_problems():
    with open('input.tst','r') as file:
        lines = file.readlines()
    
    # Use the last line to determine column positions
    last_line = lines[-1].rstrip('\n')
    operator_positions = [match.start() for match in re.finditer(r'\S', last_line)]
    # re.finditer: searches the string (last_line) for all occurrences of the regex
    # pattern (\S = non-whitespace character) and returns an iterator of Match objects.
    # The r prefix deonotes a ras string, which means backslashes are treated as
    # literarl characters, not escpae characters → \S is treated as the regex pattern
    # \S not as an escaped S.
    # match.start(): For each Match object returned by re.finditer, match.start()
    # gives the starting index (position) of the matched substring in the original
    # string (last_line).

    # Calculate column start/end indices
    column_indices = []
    prev_pos = 0
    for pos in operator_positions[1:]:
        # Skip the first operator (position 0), as we always append the prev_pos
        # (which for the first round is defined as 0).
        column_indices.append((prev_pos, pos -1)) # Start and end of the column
        prev_pos = pos

    # Add the last column
    column_indices.append((prev_pos, len(last_line)))

    # Extract fields for each line
    data = []
    for line in lines:
        line = line.rstrip('\n')
        row = []
        for start, end in column_indices:
            field = line[start:end]
            row.append(field)
        data.append(row)

    # Clean up the row containing the operators (strip white spaces):
    data[-1] = [s.strip() for s in data[-1]]


    # data is now structured like so:
    # data[row][col], i.e. it is a list of lists, the lists being the rows of the
    # csv-file, each entry in each row represents a column. Numbers in each column
    # are read top to bottom, columns are read right to left, numbers in each
    # column are either added or multiplied with each other as denoted in the last
    # row of each column (that last line we leave untouched and add to the math
    # problems later before returning) in further data-processing/construction of
    # numbers.
    # To construct numbers, iterate over each column (number of columns is read from
    # the first row, i.e. first nested list).  Numbers are read by iterating over
    # each string inside the column right to left (number of digits in each
    # indivudual math problem is determined by length of the first string (or any
    # other) in this column, reading the individual digits for each number from each
    # row, top to bottom.
    math_probs = []
    for col in range(len(data[0]))[::-1]:
        numbers = []
        # Iterate over all digits, right to left:
        for digit in range(len(data[0][col]))[::-1]:
            # Iterate over all rows except last to put together the numbers
            digits = []
            for row in range(len(data) - 1):
                digits.append(data[row][col][digit])
            numbers.append(''.join(digits))
            # convert numbers to integers
            numbers = [int(number) for number in numbers]
        math_probs.append(numbers)

    # Add operators to math_probs, read from right to left:
    math_probs.append(data[-1][::-1])
    return(math_probs)


def solve_math_problems(math_probs):
    solutions=[]
    # Numbers for each math problem are in the same nested list of math_probs, the
    # corresponding operator is in the last nested list of math_probs within this
    # nested list at the same position as the numbers list within math_probs.
    for problem in range(len(math_probs) - 1):
        try:
            # Check which mathematical operation should be performed (last row of each
            # column, either addition or multiplication)
            if math_probs[-1][problem] == '+':
                solution = sum(math_probs[problem])
            else: # multiplication
                solution = prod(math_probs[problem])
            solutions.append(solution)
        except (ValueError, IndexError) as e: # Handle errors in case of malformed input csv
            print(f"Error in math problem {problem}: {e}")
            solutions.append(None)
    return solutions


math_probs = read_math_problems()
print(math_probs)

solutions = solve_math_problems(math_probs)
print(solutions)
grand_total = sum(solutions)
print(grand_total)


# Tests
def test_read_math_problems():
    math_problems = read_math_problems()
    assert type(math_problems) == list, "The math problems should be retuned as a list"
    for i in range(len(math_problems) - 1):
        for num in range(len(math_problems[i])):
            assert type(math_problems[i][num]) == int, "The numbers should be integers"

    for operator in range(len(math_problems[-1])):
        assert type(math_problems[-1][operator]) == str, "The orators should be strings"

    assert len(math_problems[-1]) == len(math_problems) - 1, "The number of operators should match the number of problems"

def test_solve_math_problems():
    solutions = solve_math_problems(read_math_problems())
    assert type(solutions) == list, "Solutions should be returned as a list"
    for solution in solutions:
        assert type(solution) == int, "Solutions should be integers"
