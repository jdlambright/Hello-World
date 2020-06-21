# i feel like there was a bug in my other program but could not find it
# i made this file so I could leave the other and look at it with greg
pos = -1

def search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u)// 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid + 1
    return False

list = [2,3,5,6,8,9,15]
n = int(input("Enter a number: "))

if search(list, n):
    print("found at ", pos+1)
else:
    print("not found")
