def getLists(file):
    with open(file) as f:
        all = [(x.split()) for x in f]
        listA = []
        listB = []
        for item in all:
            print(item)
            listA.append(int(item[0]))
            listB.append(int(item[1]))
    return sorted(listA), sorted(listB)

def compareLists(listA, listB):
    count = 0
    for i in range(len(listA)):
        count = count + abs(listA[i] - listB[i])
    return count

def similarity(listA, listB):
    score = 0
    for item in listA:
        countB = listB.count(item)
        score = score + (item*countB)
    return score

x = getLists('input.txt')
print(compareLists(x[0], x[1]))
print(similarity(x[0], x[1]))
