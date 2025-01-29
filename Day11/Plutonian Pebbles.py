def get_stoned(filename):
    with open(filename) as f:
        line = f.read().split()
    return line


def blink(stones):
    new_stones = []
    for index, stone in enumerate(stones):
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone)//2])
            new_stones.append(str(int(stone[len(stone)//2:])))
        else:
            new_stones.append(str(int(stone) * 2024))

    return new_stones


def n_blinks(n, stones):
    for i in range(n):
        stones = blink(stones)
    return len(stones)


original_stones = get_stoned("testInput.txt")
print(n_blinks(25, original_stones))
