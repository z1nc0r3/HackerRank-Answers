
# ranked = [100, 90, 90, 80, 80, 80, 75, 60, 40, 20, 20, 10, 10, 10]
# player = [50, 65, 77, 90, 102]

ranked = [100]
player = [110]

checked = []
output = []

ranked = [i for i in ranked if i >= player[0]]    

for i in range(0, len(ranked)-1):
    if ranked[i] != ranked[i+1]:
        checked.append(ranked[i])
    
checked.append(ranked[-1])
mid = checked[len(checked)//2]

length = len(checked)

for i in player:
    count = 0
    if i <= mid:
        if i < checked[-1]:
            output.append(length + 1)
            continue
        
        for j in range(length//2, length):
            if checked[j] > i:
                print('true', checked[j], i)
                count += 1
            elif checked[j] == i:
                print('equal')
                # count += 1
            else:
                break
            
        # print((length//2) * 2  - count)
        print('--->', length//2 + count)
        output.append(length - length//2 + count)
        
    else:
        print()
        for j in range(0, length//2):
            if checked[j] > i:
                count += 1
            else:
                break
            
        print(count + 1)
        output.append(count + 1)

print(checked)
print(output)