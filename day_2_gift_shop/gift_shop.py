def read_input_data():
    with open('input', 'r', encoding='utf-8') as f:
        id_ranges = f.read()
    # Split the string into a list of ranges, strip leading and trailing whitespaces (here EOL)
    id_ranges = id_ranges.strip().split(",")
    # Split each range into a tuple with start and endpoint of the range
    id_ranges = [item.split("-") for item in id_ranges]
    return(id_ranges)

def find_invalid_ids_repeat_twice(id_ranges):
    invalid_ids = [ ]
    # Invalid ids consist of two identical patterns, thus only ids with an even
    # length can be invalid
    for start, end in id_ranges:
        for id in range(int(start), int(end)+1):
            id = str(id)
            centre = int(len(id) / 2)
            if len(id) % 2 == 0 and id[:centre] == id[centre:]:
                invalid_ids.append(id) 
    return(invalid_ids)

def find_invalid_ids_repeat_more(id_ranges):
    invalid_ids = [ ]
    # Invalid ids consist of two or more identical patterns
    for start, end in id_ranges:
        for id in range(int(start), int(end)+1):
            id = str(id)
            id_length = len(id) 
            # For every pattern of every possible length between one character and
            # half of the lengt of the entire string, check if it repeats itself
            for pattern_length in range(1, id_length // 2 + 1):
                if id_length % pattern_length == 0: # The pattern can only repeat
                    # itself if the length of the string is divisable by the length of
                    # the pattern
                    pattern = id[:pattern_length]
                    repetitions = id_length // pattern_length
                    if pattern * repetitions == id:
                        invalid_ids.append(id)
                        break # Break the loop when the first (smallest) matching
                              # pattern for a string is found. This avoids adding the
                              # string several times in case even larger patterns
                              # repeat themselves (e.g. pattern "2" and "22" for
                              # "2222") 
    return(invalid_ids)

def calculate_result(invalid_ids):
    # Add up all invalid ids
    invalid_ids = [int(item) for item in invalid_ids] # convert the ids to integers
    result = sum(invalid_ids)
    return(result)


ids = read_input_data()
#invalid_ids = find_invalid_ids_repeat_twice(ids)
invalid_ids = find_invalid_ids_repeat_more(ids)

result = calculate_result(invalid_ids)
print(result)



# Tests
def test_find_invalid_ids_repeat_twice():
    ids = find_invalid_ids_repeat_twice(read_input_data())
    assert len(ids) > 0, "No ID:s returned"
    assert type(ids) == list, "Function doesn't return a list"
    assert all(type(id) == str for id in ids), "Not a string"
    assert all(id.isnumeric() for id in ids), "ID should only contain numbers"
def test_find_invalid_ids_repeat_more():
    ids = find_invalid_ids_repeat_twice(read_input_data())
    assert len(ids) > 0, "No ID:s returned"
    assert type(ids) == list, "Function doesn't return a list"
    assert all(type(id) == str for id in ids), "Not a string"
    assert all(id.isnumeric() for id in ids), "ID should only contain numbers"
