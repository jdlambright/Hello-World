def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + pivot + quick_sort(items_greater)

print(quick_sort([3,5,2,6,7,9,8,6,4,3,3,4,2,1,0]))