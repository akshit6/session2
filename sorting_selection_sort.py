print("Enter the unsorted array:")
a = list(map(int, input().split()))
len = len(a)
print(a)
min = a[0]

for i in range(len - 1):
    min = a[i]
    index = i
    for j in range(i + 1, len):
        if a[j] < min:
            index = j
            min = a[j]

    a[i], a[index] = a[index], a[i]
print("The sorted array is:")
print(a)