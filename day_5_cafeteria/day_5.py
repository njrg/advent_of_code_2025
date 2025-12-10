def read_ingredient_database():
    with open('input', 'r', encoding='utf-8') as f:
        # read the input file, split the two datasets (list of ingredients and ranges
        # of fresh ingredients)
        ingredient_db = f.read().split('\n\n')
    # Strip leading/trailing whitespaces
    ingredient_db = [s.strip() for s in ingredient_db]
    # Split the datasets into datapoints, new line as delimiter
    ingredient_db = [dataset.split('\n') for dataset in ingredient_db]
    # unpack the two datasets
    fresh_ranges, ingredients = ingredient_db
    # Split the fresh ranges into list containing start and end-point of the range
    fresh_ranges = [r.split('-') for r in fresh_ranges]
    # Convert everything to integers
    fresh_ranges = [[int(rp) for rp in r] for r in fresh_ranges]
    ingredients = [int(ingr) for ingr in ingredients]
    return fresh_ranges, ingredients

def find_fresh_ingredients(fresh_ranges, ingredients):
    fresh_ingredients = []
    for ingr in ingredients:
        for start, end in fresh_ranges:
            if ingr >= start and ingr <= end:
                fresh_ingredients.append(ingr)
                break # if the ingredient at hand is in at least one range, no need to look further
    return(fresh_ingredients)

def merge_ranges(fresh_ranges):
    if not fresh_ranges:
        return []
    # Sort ranges by start value
    fresh_ranges.sort()
    merged_ranges = [fresh_ranges[0]]
    for current_start, current_end in fresh_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        if current_start <= last_end + 1:
            # If overlapping or adjacent: merge ranges
            new_start = last_start
            new_end = max(last_end, current_end)
            merged_ranges[-1] = [new_start, new_end]
        else:
            merged_ranges.append((current_start, current_end))
    return(merged_ranges)

def find_fresh_ingredient_ids(fresh_ranges):
    fresh_ingredient_ids = set()
    for start, end in fresh_ranges:
        for i in range(start, end + 1):
            fresh_ingredient_ids.add(i)
    return fresh_ingredient_ids


fresh_ranges, ingredients = read_ingredient_database()
fresh_ingredients = find_fresh_ingredients(fresh_ranges, ingredients)
print(len(fresh_ingredients))

merged_ranges = merge_ranges(fresh_ranges)
print(merged_ranges)
#fresh_ingr_ids = find_fresh_ingredient_ids(merged_ranges)
#print(len(fresh_ingr_ids))

# Tests
def test_read_ingredient_database():
    fresh_ranges, ingredients = read_ingredient_database()
    assert type(fresh_ranges) == list, "fresh_ranges should be a list"
    assert all(type(range) == list for range in fresh_ranges), "fresh_ranges should be a list of lists"

def test_find_fresh_ingredients():
    fresh_ingredients = find_fresh_ingredients(fresh_ranges, ingredients)
    assert type(fresh_ingredients) == list, "fresh_ingredients should be a list"
    assert len(fresh_ingredients) > 0, "function returns empty list"
    assert all(type(ingr) == int for ingr in fresh_ingredients), "fresh_ingredients should be a list of integers"
    assert all(ingr > 0 for ingr in fresh_ingredients), "ingredient id should be > 0"

def test_merge_ranges():
    fresh_ranges, ingr = read_ingredient_database()
    merged_ranges = merge_ranges(fresh_ranges)
    assert type(merged_ranges) == list, "merged_ranges should be a list"
    assert all(type(range) == list for range in merged_ranges), "merged_ranges should be a list of lists"

def test_find_fresh_ingredient_ids():
    fresh_ids = find_fresh_ingredient_ids(fresh_ranges)
    assert type(fresh_ids) == set, "fresh_ingredient_ids should be a list"
    assert len(fresh_ids) > 0, "find_fresh_ingredient_ids returns an empty set"
    assert all(type(ingr) == int for ingr in fresh_ids), "fresh_ingredient_ids should be a set of integers"
    assert all(ingr > 0 for ingr in fresh_ids), "ingredient id should be > 0"
