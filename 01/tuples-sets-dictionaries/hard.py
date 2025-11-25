import lists as l
from itertools import combinations

# TODO: Write a Python function to generate all permutations of a list in Python.
def generate_permutations(input_list):
    if len(input_list) == 0:
        return [[]]

    permutations = []

    for i in range(len(input_list)):
        current = input_list[i]
        remaining = input_list[:i] + input_list[i + 1:]
        for p in generate_permutations(remaining):
            permutations.append([current] + p)
    return permutations

print(f"Permutations of list: {generate_permutations(l.permutations_list)}")


# TODO: Write a Python function that takes a list of numbers and returns all unique pairs of the elements of the list.
def unique_pairs(input_list):
    unique_elements = set(input_list)
    return list(combinations(unique_elements, 2))

print(f"Unique pairs: {unique_pairs(l.input_list)}")