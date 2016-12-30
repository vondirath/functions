def quicksort(thisarray):
    """
        A python Quicksort with recursion
    """
    less = []
    equal = []
    greater = []

    if len(thisarray) > 1:
        pivot = thisarray[0]
        for item in thisarray:
            if item < pivot:
                less.append(item)
            if item == pivot:
                equal.append(item)
            if item > pivot:
                greater.append(item)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return thisarray


thisarray = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(thisarray)
