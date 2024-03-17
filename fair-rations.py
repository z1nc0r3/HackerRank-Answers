n = 5
b = [2, 3, 4, 5, 6]
rations = 0


def odd_counter(b):
    count = 0

    for digit in b:
        if digit % 2 == 1:
            count += 1

    return count


while True:
    if odd_counter(b) == 1:
        print("NO")
        break

    for i in range(n):
        if b[i] % 2 == 1:
            b[i] += 1
            try:
                b[i + 1] += 1
            except:
                b[i - 1] += 1

            rations += 2

    if odd_counter(b) == 0:
        print(rations)
        break
