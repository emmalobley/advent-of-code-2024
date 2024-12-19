def get_text(filename):
    with open(filename) as f:
        lines = f.read()
    return lines.split("\n\n")[0], lines.split("\n\n")[1]


def check_update_order(update, rules):
    fail = 0
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) >= update.index(rule[1]):
                fail += 1

    if fail > 0:
        return False
    return True


order_rules = [list(map(int, num.split('|'))) for num in get_text("testInput.txt")[0].split('\n')]
update_numbers = [list(map(int, num.split(','))) for num in get_text("testInput.txt")[1].split('\n')]
middle_count = 0

for update in update_numbers:
    if check_update_order(update, order_rules) == True:
        middle_count += update[int(len(update)/2)]
print(middle_count)

