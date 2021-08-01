
def func(arr):
    for a in arr:
        if a%2==0:
            return False
    return serch(arr)
def serch(arr):
    if arr:
        return True
    m=max(arr)
    if m!=len(arr):
        return False
    index=arr.index(m)
    tmp=arr[0:index]+arr[index+1:]
    for i in range(len(tmp)):
        if serch(tmp[0:i]) and serch(tmp[i:]):
            return True
    return False

def Test(arr):
    if func(arr):
        print("YES")
    else:
        print("NO")

Test([1,1,3])

Test([1,2])