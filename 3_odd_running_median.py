import statistics

def med(lst):
    return int(statistics.median(lst))

total = int(input())

for k in range(1, total + 1):
    target = int(input())
    current = 0
    buffer = []
    res = []
    while(current != target):
        lst = [int(x) for x in input().split()]
        for i in range(1, len(lst) + 1 ):
            if (lst[i - 1] % 2):
                buffer.append(lst[i - 1])
                if i % 2 != 0 and len(buffer) % 2 != 0:    
                    res.append(med(buffer))
        current += len(lst)
    print(k, len(res))
    if res != []:
        print(" ".join([str(x) for x in res]))