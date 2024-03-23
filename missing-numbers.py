arr = [7, 2, 5, 3, 5, 3]
brr = [7, 2, 5, 4, 6, 3, 5, 3]

missing = []

for digit in brr:
    if digit not in arr and digit not in missing:
        missing.append(digit)
    else:
        arr.remove(digit)
        
print(missing)