pos = -1

def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

list = [5,1,4,3,9,7]
n = float(input("enter a number: "))

if search(list, n):
    print("found at ", pos+1)
else:
    print("not found")