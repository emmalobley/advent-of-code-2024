import re

def getSum(file):
    with open(file) as f:
        txt = f.read()
        x = re.findall("mul\(\d+,\d+\)", txt)

    sum = 0
    for item in x:
        print(item)
        temp = re.findall(r'\d+', item)
        res = list(map(int, temp))
        # nums = [int(i) for i in item.split() if i.isdigit()]
        sum = sum + res[0]*res[1]
    return sum

print(getSum("input.txt"))