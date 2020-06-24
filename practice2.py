# i feel like there was a bug in my other program but could not find it
# i made this file so I could leave the other and look at it with greg
pos = -1

def search(list, n):
    i = 0

    for i in range(len(list)):
        if list[i]==n:
            globals()['pos'] = i
            return True
    return False

list = [2, 4, 5, 7, 8, 10]
n = int(input("enter a number: "))

if search(list, n):
    print("found at ", pos + 1)

else:
    print("not found")