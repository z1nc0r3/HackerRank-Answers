arr = [1, 1, 4, 1, 1]

total = sum(arr)
len = len(arr)

print(total)

left = [0]
right = []

for i in range(len - 1):
    left.append(left[i] + arr[i])
    right.append(total - left[i] - arr[i])
    
right.append(0)
    
print(left)
print(right)

for i in range(len):
    if left[i] == right[i]:
        print('YES')
    
print('NO')
    