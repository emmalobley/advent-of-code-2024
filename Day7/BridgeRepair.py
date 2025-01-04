import itertools


def get_dict(filename):
    data_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            key, values = line.strip().split(':')

            value_list = list(map(int, values.split()))

            data_dict[int(key)] = value_list
    return data_dict


def apply_operations(numbers, ops):
    result = numbers[0]
    for num, op in zip(numbers[1:], ops):
        if op == '+':
            result += num
        elif op == '*':
            result *= num
        elif op == '||':
            result = int(str(result)+str(num))
    return result


def find_matching_expression(numbers, target):
    operators = ['+', '*', '||']
    num_operations = len(numbers) - 1
    possible_ops = itertools.product(operators, repeat=num_operations)

    for ops in possible_ops:
        result = apply_operations(numbers, ops)
        if result == target:
            return ops
    return None


def get_count(dictionary):
    count = 0
    for item in dictionary:
        operators = find_matching_expression(dictionary[item], item)

        if operators:
            count += item
    return count


dicti = get_dict('input.txt')

print(get_count(dicti))
