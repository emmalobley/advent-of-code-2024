from collections import defaultdict, deque


def topological_sort(update, rules):
    # Step 1: Build the graph
    graph = defaultdict(list)
    in_degree = {node: 0 for node in update}

    valid_rules = [rule for rule in rules if rule[0] in update and rule[1] in update]

    for a, b in valid_rules:
        graph[a].append(b)
        in_degree[b] += 1

    # Step 2: Find nodes with no incoming edges (in_degree == 0)
    queue = deque([node for node in update if in_degree[node] == 0])

    result = []
    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 3: If the result contains all nodes, return it; otherwise, it's a cycle (impossible to sort)
    if len(result) == len(update):
        return result
    else:
        raise ValueError("The constraints lead to a cycle, so sorting is not possible.")


def get_text(filename):
    with open(filename) as f:
        lines = f.read()
    return lines.split("\n\n")[0], lines.split("\n\n")[1]


def check_update_order(update, rules):
    fail = 0
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                fail += 1

    if fail > 0:
        return False
    return True


def change_update_order(update, rules):
    sorted_list = []
    for rule in rules:
        if rule in update:
            sorted_list.append(rule)
    return sorted_list


def get_count(filename):
    order_rules = [list(map(int, num.split('|'))) for num in get_text(filename)[0].split('\n')]
    # update_numbers = [list(map(int, num.split(','))) for num in get_text(filename)[1].split('\n')]
    update_numbers = [
        [int(x) for x in num.split(',') if x]  # Only convert non-empty strings to int
        for num in get_text(filename)[1].split('\n')
    ]
    # print(update_numbers)
    middle_count = 0
    incorrect_middles = 0

    for update in update_numbers:
        if check_update_order(update, order_rules) and len(update) > 0:
            middle_count += update[int(len(update) / 2)]
        elif len(update) > 0:
            update = topological_sort(update, order_rules)
            incorrect_middles += update[int(len(update) / 2)]
    return middle_count, incorrect_middles


print(get_count("input.txt"))
