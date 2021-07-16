total = int(input())

def alpha(c):
    return ord(c) >= ord("A") and ord(c) <= ord("Z")

for m in range(1, total + 1):
    
    s = input()
    c = int(input())

    decode = {}
    res = ""
    p = False
    for j in range(1, c + 1):
        original, decoded = input().split(" ", 1)
        for i in range(len(original)):
            decode[original[i]] = decoded[i]
    for cha in s:
        if not alpha(cha):
            res += cha
            continue
        if decode.get(cha):
            res += decode.get(cha)
        else: 
            print(m,"CANNOT DECODE")
            p = True
            break
    if not p:
        print(m, res)
            