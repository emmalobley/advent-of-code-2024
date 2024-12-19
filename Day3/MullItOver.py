import re


def get_text(file):
    with open(file) as f:
        txt = f.read()
    return txt


def get_mul_sum(text):

    # Use regex to replace everything between 'dont()' and the next 'do()' with a placeholder
    cleaned_text = re.sub("don't\(\)(.*?)do\(\)", '', text, flags=re.DOTALL)

    mul_pattern = r'mul\(\d+,\d+\)'
    mul_matches = re.findall(mul_pattern, cleaned_text)

    mul_sum = 0
    for item in mul_matches:
        temp = re.findall(r'\d+', item)
        numpair = list(map(int, temp))
        print(numpair)
        mul_sum = mul_sum + numpair[0]*numpair[1]
        print(mul_sum)
    return mul_sum


print(get_mul_sum(get_text("input.txt")))

