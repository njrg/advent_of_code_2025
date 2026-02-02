import csv
import pandas as pd

def read_math_problems():
    #df = pd.read_csv('input.tst', sep='\\s+', header=None, engine='python', dtype='object') # sep='\s+' > one ore more white space characters
    df = pd.read_csv('input', sep='\\s+', header=None, engine='python', dtype='object') # sep='\s+' > one ore more white space characters
    print(df.head())
    #with open('input.tst', newline='') as file:
    with open('input', newline='') as file:
        reader = csv.reader(file, skipinitialspace=True, quoting=csv.QUOTE_NONE, delimiter=' ')
        data = [[x for x in row if x != ''] for row in reader if row]  # `filter out empty fields (if x != '') and empty lines (if row)
    return(data)

def solve_math_problems(math_probs):
    solutions=[]
    # math_probs was read from the csv and is structured like so:
    # math_probs[row][col], i.e. it is a list of lists, the lists being the rows of
    # the csv-file, each entry in each row represents a column
    # We are calculating by column, so iterate over each column (number of columns is
    # read from the first row, i.e. first nested list.
    for col in range(len(math_probs[0])):
        # Check which mathematical operation should be performed (last row of each
        # column, either addition or multiplication)
        if math_probs[-1][col] == '+':
            solution=0 # for addition prime solution as 0
            # Iterate over all rows except last (with the operator + or *)
            for row in range(len(math_probs)-1):
                solution=solution + int(math_probs[row][col])
        else:
            solution=1 # for multiplication, prime solution as 1
            # Iterate over all rows except last (with the operator + or *)
            for row in range(len(math_probs)-1):
                solution=solution * int(math_probs[row][col])
        solutions.append(solution)
    return(solutions)


math_probs = read_math_problems()

solutions = solve_math_problems(math_probs)
grand_total = sum(solutions)
print(grand_total)
