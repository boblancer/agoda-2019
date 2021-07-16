import sys
MAX_INT = sys.maxsize - 1
total = int(input())

for i in range(1, total + 1):
    lst = [int(x) for x in input()[1:].split()]
    s = MAX_INT
    queue = [] 
    for j in lst:
        if j >= 0 and j not in queue:
            queue.append(j)
    queue.sort()
    if len(queue) < 3:
        ans = "na"
    else: 
        ans = queue[2]
    print(i, ans)