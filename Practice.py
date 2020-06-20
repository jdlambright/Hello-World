#when I learn something new, this is where i go back to practice it on my own
pos = -1

def search(list, n):

    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid + 1
    return False

list = [2,4,6,8,15,18]

n = int(input("enter a number: "))

if search(list, n):
    print("found at ", pos +1)
else:
    print("not found")