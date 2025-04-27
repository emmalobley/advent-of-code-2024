import math
import re

# need to solve C = A*x + B*y
# x and y unknown
# Linear Diophantine Equations
# k * gcd(A, B) = C
# integer k


def get_all_prizes(filename):
    results = []

    with open(filename, "r") as file:
        lines = file.readlines()

        for i in range(0, len(lines), 4):
            a_match = re.findall(r'X\+?(\d+), Y\+?(\d+)', lines[i])
            b_match = re.findall(r'X\+?(\d+), Y\+?(\d+)', lines[i+1])
            prize_match = re.findall(r'X=(\d+), Y=(\d+)', lines[i+2])

            if a_match and b_match and prize_match:
                a_coords = tuple(map(int, a_match[0]))
                b_coords = tuple(map(int, b_match[0]))
                prize_coords = tuple(map(int, prize_match[0]))
                # prize_coords = prize_coords[0] + 10000000000000, prize_coords[1] + 10000000000000

                results.append({
                    'a': a_coords,
                    'b': b_coords,
                    'prize': prize_coords
                })

    # print(results)
    return results


def find_combinations(v1, v2, target):
    (x1, y1) = v1
    (x2, y2) = v2
    (x3, y3) = target
    solutions = []
    # We'll search for a reasonable range of 'a'
    max_a = 10000  # Can adjust based on expected problem size
    for a in range(max_a + 1):
        x_part = x3 - a * x1
        y_part = y3 - a * y1

        if x2 == 0:
            if x_part != 0:
                continue
            b_x = 0
        elif x_part % x2 == 0:
            b_x = x_part // x2
        else:
            continue

        if y2 == 0:
            if y_part != 0:
                continue
            b_y = 0
        elif y_part % y2 == 0:
            b_y = y_part // y2
        else:
            continue

        if b_x == b_y and b_x >= 0:
            solutions.append((a, b_x))

    return solutions


def check_prizes(all_prizes):
    token_count = 0
    for item in all_prizes:
        (x1, y1) = item["a"]
        (x2, y2) = item["b"]
        (x3, y3) = item["prize"]

        if int(x3 % math.gcd(x1, x2)) == 0 and int(y3 % math.gcd(y1, y2)) == 0:
            # print(item)
            # print("This is a potential prize win!")
            # print(find_combinations(item["a"], item["b"], item["prize"]))
            prize_pairs = find_combinations(item["a"], item["b"], item["prize"])
            if len(prize_pairs) > 0:
                (a, b) = prize_pairs[0]
                token_count += 3*a+b

    return token_count


print(check_prizes(get_all_prizes("testInput.txt")))



# print(math.gcd(3, 6))
