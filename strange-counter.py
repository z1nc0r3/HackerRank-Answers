start = 3
t = 21
i = 0
sum = 0
rest = 0

while True:
    if sum >= t:
        rest = sum - t
        break

    sum += start
    start *= 2
    i += 1

print(rest + 1)
