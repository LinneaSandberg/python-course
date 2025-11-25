import lists as l

# TODO: Implement insertion sort.
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = key
    return input_list

print(f"Insertion sorted list: {insertion_sort(l.messy_list)}")


# TODO: Implement bubble sort.
def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list

print(f"Bubble sorted list: {insertion_sort(l.messy_list)}")