import csv
import pandas as pd

def read_math_problems():
    with open('input', newline='') as file:
        reader = csv.reader(file, skipinitialspace=True, quoting=csv.QUOTE_NONE, delimiter=' ')
        data = [[x for x in row if x != ''] for row in reader if row]  # `filter out empty fields (if x != '') and empty lines (if row)
    return data

def solve_math_problems(math_probs):
    solutions=[]
    # math_probs was read from the csv and is structured like so:
    # math_probs[row][col], i.e. it is a list of lists, the lists being the rows of
    # the csv-file, each entry in each row represents a column
    # We are calculating by column, so iterate over each column (number of columns is
    # read from the first row, i.e. first nested list.
    for col in range(len(math_probs[0])):
        try:
            # Check which mathematical operation should be performed (last row of each
            # column, either addition or multiplication)
            if math_probs[-1][col] == '+':
                solution = 0 # for addition prime solution as 0
                # Iterate over all rows except last (with the operator + or *)
                for row in range(len(math_probs) - 1):
                    solution += int(math_probs[row][col])
            else:
                solution=1 # for multiplication, prime solution as 1
                # Iterate over all rows except last (with the operator + or *)
                for row in range(len(math_probs) - 1):
                    solution *= int(math_probs[row][col])
            solutions.append(solution)
        except (ValueError, IndexError) as e: # Handle errors in case of malformed input csv
            print(f"Error in column {col}: {e}")
            solutions.append(None)
    return solutions
    # Alternative solution using list comprehension
    # from math import prod
    # return [
    #     sum(int(math_probs[row][col]) for row in range(len(math_probs) - 1))
    #     if math_probs[-1][col] == '+' else
    #     prod(int(math_probs[row][col]) for row in range(len(math_probs) - 1))
    #     for col in range(len(math_probs[0]))
    # ]

def read_math_problems_pandas():
    df = pd.read_csv('input', sep='\\s+', header=None, engine='python')
    return df

def solve_math_problems_pandas(df):
    operators = df.iloc[-1] # Last row contains operators
    values = df.iloc[:-1] # All rows except the last contain values
    solutions = []
    for col in values.columns:
        if operators[col] == '+':
            solutions.append(values[col].astype(int).sum())
        else:
            solutions.append(values[col].astype(int).prod())
    return solutions



math_probs = read_math_problems()
solutions = solve_math_problems(math_probs)
grand_total = sum(solutions)
print(grand_total)

df = read_math_problems_pandas()
solutions = solve_math_problems_pandas(df)
grand_total = sum(solutions)
print(grand_total)
