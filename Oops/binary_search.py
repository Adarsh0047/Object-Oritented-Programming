

def search(n,arr,low,high,):
    if high>=low:
        middle=(low+high)//2
        if n==arr[middle]:
            return middle
        elif n>arr[middle]:
            return search(n,arr,middle+1,high)
        else: 
            return search(n,arr,low,middle-1)
    else:
        return -1

arr=[9,18,1,44,32,7,21,3]
arr.sort()
print(arr)
X=search(21,arr,0,len(arr)-1)
print(X)
