friends = 1
price = [1, 3, 5, 7, 9]

flowers = len(price)
price = sorted(price)

cost = 0

if friends >= flowers:
    print(sum(price))

multiplier = 0
round = 1

for i in range(flowers - 1, -1, -1):
    cost += price[i] * (multiplier + 1)

    if round == friends:
        multiplier += 1
        round = 1
    else:
        round += 1


print(cost)
