import lists as l

# TODO: Write a function in Python that takes two lists as arguments and returns the union of the lists.
def list_union(list1, list2):
    return list(set(list1).union(set(list2)))

print(f"Union of two lists: {list_union(l.names, l.names2)}")


# TODO: Write a function in Python that takes two lists as arguments and returns the intersection of the lists.
def list_intersection(list1, list2):
    return list(set(list1).intersection(set(list2)))

print(f"Intersection of two lists: {list_intersection(l.names, l.names2)}")