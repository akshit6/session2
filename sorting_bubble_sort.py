
a = list(map(int,input().split()))
len = len(a)

for i in range(len-1):
    for j in range(len-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("\nThe sorted array is:")
print(a)

