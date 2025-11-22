import numbers
from easy import calculate_average

# TODO: Write a Python program that takes a list of numbers as an input and writes two separate lists containing even and odd numbers as an output.
def list_even_odd(numbers):
    even = []
    odd =  []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

even_numbers, odd_numbers = list_even_odd(numbers.numbers_list)
print(f"Even numbers: {even_numbers} and odd numbers: {odd_numbers}")


# TODO: Write a Python program to count the median of a list of numbers.
def calculate_median(numbers):
    sort_numbers = sorted(numbers)
    lenght = len(sort_numbers)

    if lenght % 2 == 0:
        return (sort_numbers[lenght // 2 - 1] + sort_numbers[lenght // 2]) / 2
    else:
        return sort_numbers[lenght // 2]

print(f"The median is {calculate_median(numbers.numbers_list)}")

# TODO: Write a Python program to count the variance of a list of numbers.
def calculate_variance(numbers):
    average = calculate_average(numbers)
    squared_diffs = [(x - average) ** 2 for x in numbers]
    return sum(squared_diffs) / (len(numbers) - 1)

print(f"The variance is {calculate_variance(numbers.numbers_list)}")

# TODO: Write a Python program to access a specific element at a given index of a list.)
def access_with_index(numbers, index):
    return numbers[index]

index = 2
print(f"The number {access_with_index(numbers.numbers_list, index)} is at index {index}")