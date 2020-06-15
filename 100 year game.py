pos = -1                                #this is setting a global variable

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
                l = mid+1
            else:
                u = mid+1
    return False

list = [2,6,8,22,37,44,107]                    #this is the list of elements

n = float(input("enter a number: "))    #this ask the user to input a number to check if its in the list

if search(list, n):                     #this if statement says if our search finds an element tell us where it is located
    print("found at ", pos+1)
else:
    print("not found")
