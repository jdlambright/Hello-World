#merge sort code
def create_array(size=10, max=50):
    from random import randint
    return [randin(0,max)for _ in range(size)]

a=[2,4,6,8]
b=[1,3,5,7]

def merge(a,b):
    c=[] #final output of array
    a_idx,b_idx = 0,0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx+=1
        else:
            c.append(b[b_idx])
            b_idx+=1
    if a_idx==len(a): c.extend(b[b_idx:])
    else:             c.extend(a[a_idx:])

def merge_sort(a):
    if len(a)<=1: return a
    left,right = merge_sort(a[:len(a)/2]), merge_sort(a[len(a)/2:])
    return merge(left,right)