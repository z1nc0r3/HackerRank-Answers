get_bin = lambda x: format(x, 'b').zfill(32)

binary = [i for i in get_bin(12)]

print(binary)

for i in range(len(binary)):
    if binary[i] == '0':
        pass
    
a = 2147483647
b = 4294967295

c = b ^ a

print(c)