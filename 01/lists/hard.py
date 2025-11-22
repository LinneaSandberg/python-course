import numbers
from moderate import calculate_median

# TODO: Write a Python program that computes the median absolute deviation (MAD) of an input list of numbers.
def media_absolute_deviation(numbers):
    median = calculate_median(numbers)
    absolute_deviations = [abs(x - median) for x in numbers]
    return calculate_median(absolute_deviations)

print(f"The MAD is {media_absolute_deviation(numbers.numbers_list)}")

# TODO: Write a Python program to remove duplicates from a list.
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

print(f"The unique numbers is {remove_duplicates(numbers.duplicated_number_list)}")

# TODO: Write a Python program to generate all sublists of a list.
def generate_sublists(numbers):
    if not numbers:
        return [[]]

    first_element = numbers[0]
    sublist_without_first = generate_sublists(numbers[1:])
    sublist_with_first = [[first_element] + sublist for sublist in sublist_without_first]
    return sublist_without_first + sublist_with_first

sublists = generate_sublists(numbers.sublist_list)
for sublist in sublists:
    print(sublist)