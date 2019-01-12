def buildSmallHeap(num):
    for i in range(int(len(num)/2),-1,-1):
        adjust(num, i)
def adjust(array,i):
    temp = array[i]
    k=i*2
    l=len(array)
    while k<l:
        if k+1 < l and array[k] > array[k + 1]:
            k+=1
        if temp<=array[k]:
            break
        else:
            array[i] = array[k]
            i = k
        k*=2
    array[i] = temp

if __name__=="__main__":
    test=[5,9,8,4,6,2,1,8,0,5]
    buildSmallHeap(test)
    print(test)
