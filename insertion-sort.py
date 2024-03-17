n = 6
arr = [1, 4, 3, 5, 6, 2]

for i in range(n):
    for j in range(i+1, -1, -1):
        print(arr[i], arr[j])
        
        if arr[j] < arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            print('inside', arr)
        else:
            pass
            