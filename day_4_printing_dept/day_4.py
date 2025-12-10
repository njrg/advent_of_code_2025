def read_paper_grid():
    with open('input', 'r', encoding='utf-8') as f:
        paper_grid = f.readlines()
    # strip trailing EOL-characters
    paper_grid = [s.rstrip('\n') for s in paper_grid]
    # Split every line of the grid into indivdual paper rolls (list of lists)
    paper_grid = [[char for char in s] for s in paper_grid]
    return(paper_grid)

def find_accessable_rolls(paper_grid):
    accessable_rolls = 0
    for line, s in enumerate(paper_grid):
        for i, char in enumerate(s):
            empty_space = 0
            if char == "@": # Check whether there is a paper roll on the space at hand
                # Adjacent fields on the same line
                if i == 0: empty_space += 1 # If character is first in the line add an empty space
                elif s[i-1] != "@": empty_space += 1
                if i+1 == len(s): empty_space += 1 # If char is last in the line
                elif s[i+1] != "@": empty_space += 1
                # Adjacent fields on the previous line
                if line == 0:         # If we are on the first line we add 3 empty spaces
                     empty_space += 3 # and skip checking for sinle characters
                else:
                    if i == 0: empty_space += 1 # First character on the line
                    elif paper_grid[line-1][i-1] != "@": empty_space += 1
                    if paper_grid[line-1][i] != "@": empty_space += 1
                    if i+1 == len(s): empty_space += 1 # char last on the line
                    elif paper_grid[line-1][i+1] != "@": empty_space += 1
                # Adjacent fields on the following line
                if line+1 == len(paper_grid): # If we are on the last line we add 3 empty spaces
                     empty_space += 3         # and skip checking for single characters
                else:
                    if i == 0: empty_space += 1 # First character on the line
                    elif paper_grid[line+1][i-1] != "@": empty_space += 1
                    if paper_grid[line+1][i] != "@": empty_space += 1
                    if i+1 == len(s): empty_space += 1 # char last on the line
                    elif paper_grid[line+1][i+1] != "@": empty_space += 1
            if empty_space > 4:
                accessable_rolls += 1
    return(accessable_rolls)

def remove_accessable_rolls(paper_grid):
    removed_rolls = 0
    rolls_accessable = True
    while rolls_accessable:
        rolls_accessable = False
        for line, s in enumerate(paper_grid):
            for i, char in enumerate(s):
                empty_space = 0
                if char == "@": # Check whether there is a paper roll on the space at hand
                    # Adjacent fields on the same line
                    if i == 0: empty_space += 1 # If character is first in the line add an empty space
                    elif s[i-1] != "@": empty_space += 1
                    if i+1 == len(s): empty_space += 1 # If char is last in the line
                    elif s[i+1] != "@": empty_space += 1
                    # Adjacent fields on the previous line
                    if line == 0:         # If we are on the first line we add 3 empty spaces
                         empty_space += 3 # and skip checking for sinle characters
                    else:
                        if i == 0: empty_space += 1 # First character on the line
                        elif paper_grid[line-1][i-1] != "@": empty_space += 1
                        if paper_grid[line-1][i] != "@": empty_space += 1
                        if i+1 == len(s): empty_space += 1 # char last on the line
                        elif paper_grid[line-1][i+1] != "@": empty_space += 1
                    # Adjacent fields on the following line
                    if line+1 == len(paper_grid): # If we are on the last line we add 3 empty spaces
                         empty_space += 3         # and skip checking for single characters
                    else:
                        if i == 0: empty_space += 1 # First character on the line
                        elif paper_grid[line+1][i-1] != "@": empty_space += 1
                        if paper_grid[line+1][i] != "@": empty_space += 1
                        if i+1 == len(s): empty_space += 1 # char last on the line
                        elif paper_grid[line+1][i+1] != "@": empty_space += 1
                if empty_space > 4:
                    removed_rolls += 1
                    paper_grid[line][i] = "x" # "remove" the paper roll and mark the spot
                    rolls_accessable = True # as long as we can remove rolls, there might be more rolls to remove
    return(removed_rolls)

paper_grid = read_paper_grid()
accessable_rolls = find_accessable_rolls(paper_grid)
print(accessable_rolls)

removed_rolls = remove_accessable_rolls(paper_grid)
print(removed_rolls)


# Tests
def test_read_paper_grid():
    paper_grid = read_paper_grid()
    assert type(paper_grid) == list, "Should return a list"
    assert all(type(line) == list for line in paper_grid), "Not a list of lists"
    assert all([type(s) == str for s in line] for line in paper_grid), "Not a list of strings"
    assert all(len(line) > 0 for line in paper_grid), "Returns empty lines"

def test_find_accessable_rolls():
    accessable_rolls = find_accessable_rolls(read_paper_grid())
    assert type(accessable_rolls) == int, "Function doesn't return an integer"
    assert accessable_rolls >= 0, "Number must be positive"

def test_remove_accessable_rolls():
    removed_rolls = remove_accessable_rolls(read_paper_grid())
    assert type(removed_rolls) == int, "Function doesn't return an integer"
    assert removed_rolls >= 0, "Number must be positive"
