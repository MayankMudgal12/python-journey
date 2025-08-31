def facto(n):
    a = n
    prod = 1

    while (n > 0):
        prod*= n
        n-=1
    print(prod)


facto(30)
        