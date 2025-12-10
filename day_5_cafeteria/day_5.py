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

fresh_ranges, ingredients = read_ingredient_database()
fresh_ingredients = find_fresh_ingredients(fresh_ranges, ingredients)
print(len(fresh_ingredients))

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
