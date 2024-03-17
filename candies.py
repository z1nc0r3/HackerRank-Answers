n = 10
arr = [2, 4, 2, 6, 1, 7, 8, 9, 2, 1]

candies = [1] * n  # Initialize candies for each child with 1

# Forward pass: Ensure higher rated child gets more candies than the previous one
for i in range(1, n):
    if arr[i] > arr[i - 1]:
        candies[i] = candies[i - 1] + 1

# Backward pass: Ensure higher rated child gets more candies than the next one
for i in range(n - 2, -1, -1):
    if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
        candies[i] = candies[i + 1] + 1

total = sum(candies)

print(arr)
print(total)

# return sum(total)
