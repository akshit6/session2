def partition(a,start,end):

    pindex = start
    for i in range(start,end):
        if (a[i] <= a[end]):
            a[i],a[pindex] = a[pindex],a[i]
            pindex +=1
    a[end],a[pindex] = a[pindex],a[end]
    return pindex


def quicksort(a,start,end):
    if start <  end:
        index = partition(a,start,end)
        quicksort(a,start,index-1)
        quicksort(a,index+1,end)


print("Enter the array to be sorted:")
a = list(map(int,input().split()))
len = len(a)
quicksort(a,0,len-1)
print(a)