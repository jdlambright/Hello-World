to_sort = [23,553,78,34,12,478,2345,11,32,47,27]
division = 1
Mod = 10
start = True
while start:
    start = False
    bucket = [[],[],[],[],[],[],[],[],[],[]]
    for num in to_sort:
        position = num % Mod // division
        bucket[position]. append(num)
        if not start and position > 0:
            start = True
    print(bucket)
    to_sort = []
    for bucknum in bucket:
        for bucknestnum in bucknum:
            to_sort.append(bucknestnum)
    Mod = Mod*10
    division = division * 10
print(to_sort)