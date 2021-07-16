cin = int(input())

for i in range(1, cin + 1):
    
    n = int(input())
    d = n
    c = 1
    while(n != 1):
        c += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3 + 1
    print(i, d, c)