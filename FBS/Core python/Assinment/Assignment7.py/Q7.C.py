for i in range(9, 0,-1):
    for j in range(1, 7-i):
        print('0', end=' ')    
    for j in range(1, i+1):
        print(i, end=' ')        
    print()