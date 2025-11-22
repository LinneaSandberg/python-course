import numbers

# TODO: Write a Python program to count the number of even and odd numbers in a series of numbers.
def count_even_odd(numbers):
    even_count, odd_count = 0, 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

even_count, odd_count = count_even_odd(numbers.numbers_list)
print(f"It´s {even_count} even numbers and it´s {odd_count} odd numbers.")


# TODO: Write a Python program to count the average of a list of numbers.
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

print(f"{numbers.numbers_list} has the average of {calculate_average(numbers.numbers_list)}.")


# TODO: Write a Python program to get the largest number from a list.
def largest_number(numbers):
    return max(numbers)

print(f"The largest number is {largest_number(numbers.numbers_list)}.")


# TODO: Write a Python program to get the smallest number from a list.
def smallest_number(numbers):
    return min(numbers)

print(f"The smallest number is {smallest_number(numbers.numbers_list)}")