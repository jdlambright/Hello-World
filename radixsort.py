to_sort = [23,556,78,34,12,478,2345]
division = 1
Mod = 10
start = True
while start:
    start = False
    bucket = [[],[],[],[],[],[],[],[],[],[]]
    for num in to_sort:
        position = num % Mod // division
        bucket[position]. append(num)
    print(bucket)
    to_sort = []
    for bucknum in bucket:
        for bucknestnum in bucknum:
            to_sort.append(bucknestnum)
    Mod = Mod*10
    division = division * 10
print(to_sort)