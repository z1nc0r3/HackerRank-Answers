s = 'aaabccddd'
while True:
    char = []
    count = []
    output = []
    i = 1

    char.append(s[0])
    count.append(1)

    og_s = s
    
    while i < len(s):
        if s[i] == char[-1]:
            count[-1] += 1
        else:
            char.append(s[i])
            count.append(1)
        
        i += 1
            
    print(char, count)
        
    for j in range(len(count)):
        count[j] = count[j] % 2
        output.append(char[j] * count[j])
        
    print(i, s, output)
    s = ''.join(output)
    
    if s == og_s:
        break
    elif len(s) == 0:
        s = 'Empty String'
        break
    
print(s)