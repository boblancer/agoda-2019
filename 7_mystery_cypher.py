total = int(input())

for i in range(1, total + 1):
    res = ""
    a, b = [int(x) for x in input().split()]
    string = input()
    if (not string):
        print(i, res)
        continue
    c = input()
    seq = [int(x) for x in input().split()]
    curr = 0
    for n in seq:
        curr += n
        res += string[curr]
    print(i, res)
        