n = 6
c = [2]
c = sorted(c)
        
global_max = c[0]

if n - 1 - c[-1] > global_max:
    global_max = n - 1 - c[-1]
    
    
for i in range(0, len(c)-1):
    local_max = abs(c[i] - c[i+1])//2
    if local_max > global_max:
        global_max = local_max
        
print(global_max)