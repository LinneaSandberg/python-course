import lists as l

# TODO: Write a Python function to get the frequency of elements in a list.
def count_frequency(input_list):
    frequency = {}
    for item in input_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

print(f"Frequency: {count_frequency(l.input_list)}")


# TODO: Write a Python function that takes a list of tuples in the form of (Student:grade) and computes the average grade for all students.
def average_grades(input_list):
    total = 0
    count = 0

    for student, grade in input_list:
        total += grade
        count += 1
    return total / count

print(f"Average grade: {average_grades(l.grades)}")


# TODO: Write a Python function to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def square_dict(n):
    square = {x: x * x for x in range(1, n + 1)}
    return square

print(f"Square dictionary: {square_dict(21)}")


# TODO: Write a Python program to remove duplicates from a list using sets.
def remove_duplicates(input_list):
    return list(set(input_list))

print(f"List with removed duplicates: {remove_duplicates(l.duplicates)}")


# TODO: Write a Python program to find the first repeated word in a given string using sets.
def find_first_repeated(input_string):
    small_letters = input_string.lower()
    words = small_letters.split()
    duplicate = set()

    for word in words:
        if word in duplicate:
            return word
        duplicate.add(word)
    return None

print(f"First duplicate: {find_first_repeated(l.input_string)}")