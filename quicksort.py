def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop

    greater = []
    lower = []

    for item in seq:
        if item < pivot:
            greater.append(item)
        else:
            lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([4,2,3,1,5]))