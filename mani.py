list = [123,34,455,6,889,78,46,89,90]
list.sort()
n=int(input("enter a number"))
pos=-1
def bs(li,n):
    l=0
    u=len(list)+1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

if bs(list,n):
    print('found at ',pos)
else:
    print('not found')
