#when I learn something new, this is where i go back to practice it on my own
pos = -1

def search(list, n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos']=i
            return True
    return False

list = [2,4,6,8,15,18]

n = int(input("enter a number: "))

if search(list, n):
    print("found at", pos + 1)
else:
    print("not found")