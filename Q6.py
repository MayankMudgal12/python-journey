def sum(n):
    if (n==0):
        return 0
    
    return sum(n-1)+ n

print(sum(3))
 