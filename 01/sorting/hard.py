import lists as l

# TODO: Implement quicksort.
def quicksort(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        pivot = input_list[len(input_list) // 2]
        left = [x for x in input_list if x < pivot]
        middle = [x for x in input_list if x == pivot]
        right = [x for x in input_list if x > pivot]
        return quicksort(left) + middle + quicksort(right)

print(f"Quicksorted list: {quicksort(l.messy_list)}")


# TODO: Implement mergesort.
def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left_half = merge_sort(input_list[:mid])
    right_half = merge_sort(input_list[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array

print(f"Merge sorted list: {merge_sort(l.messy_list)}")