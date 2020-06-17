pos = -1                                #this is setting a global variable

def search(list, n):                    #this is creating a function for a linear search
    i = 0                               #sets the counter to 0
    for i in range(len(list)):          #for loop that automatically runs through ever element
        if list[i] == n:                #if statement sets condition of if number is in list
            globals()['pos'] = i        #this is telling us which position it is. globals makes a local variable global
            return True                 #if the element is found it lets us know it is in the list

    return False                        #this lets us know the element was not found

list = [5,1,4,3,9,7]                    #this is the list of elements

n = float(input("enter a number: "))    #this ask the user to input a number to check if its in the list

if search(list, n):                     #this if statement says if our search finds an element tell us where it is located
    print("found at ", pos+1)
else:
    print("not found")                  #this lets the user know the element is not in the list

# another way to do this is with a while loop
# while i < len(list):
#   if list[i] == n:
#       globals()['pos'] = i
#       return True
#   i += 1