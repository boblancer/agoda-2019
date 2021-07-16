def read_card():
    card_index = []

    for i in range(5):
        l = input().split()
        for j in range(len(l)):
            if l[j] == "X":
                card_index.append(i * 5 + j)
    return card_index

def equal(l1, l2):
    return l1.sort() == l2.sort()
    

def read_input(pattern):
    card_index = []

    for i in range(5):
        l = [int(x) for x in input().split()]
        card_index += l
    
    match = []
    for p in pattern:
        match.append(card_index[p])
    
    if pattern == []:
        return None
    return sorted(match)

total = int(input())
for i in range(1, total + 1):
    pattern = read_card()
    c = int(input())
    pattern_repo = {}
    print("Dataset", i)
    for j in range(1, c + 1):
        m = read_input(pattern)
        if m:
            # print(j," " ,m)
            exist = pattern_repo.get(tuple(m))
            if exist:
                print(j, "=>", exist)
            else:
                pattern_repo[tuple(m)] = j
    print()