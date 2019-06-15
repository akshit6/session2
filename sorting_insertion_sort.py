print("Enter the elements of array:")
a = list(map(int, input().split()))
len = len(a)
for i in range(1, len):
    temp = a[i]
    hole = i
    while (hole > 0 and a[hole - 1] > temp):
        a[hole] = a[hole - 1]
        hole -= 1
    a[hole] = temp
print("The sorted array is:{}".format(a))