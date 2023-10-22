
def first_search(arr,n,k):
    start =0
    end = n-1
    ans = -1
    while(start<=end):
        mid = int((start+end)/2)
        if arr[mid] == k:
            ans = mid
            end = mid -1
        elif arr[mid] < k:
            start = mid +1
        else:
            end = mid-1
    return ans

def last_search(arr,n,k):
    start =0
    end = n-1
    ans = -1
    while(start<=end):
        mid = int((start+end)/2)
        if arr[mid] == k:
            ans = mid
            start = mid + 1
        elif arr[mid] < k:
            start = mid +1
        else:
            end = mid-1
    return ans
         
def firstAndLastPosition(arr, n, k):
    temp =[]
    first = first_search(arr,n,k)
    last = last_search(arr,n,k)
    temp.append(first)
    temp.append(last)
    return temp

    

    
arr = [1,2,2,2,2]
k =2
n=len(arr)
ans = last_search(arr,n,k)
print(ans)
            