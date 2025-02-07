
def get_array(filename):
    with open(filename) as f:
        txt = f.read()
    return list(map(int, txt))


def get_blocks(array):
    new_array = []
    number = 0
    for i in range(0, len(array), 2):
        for j in range(array[i]):
            # print(number)
            new_array.append(number)
        if i < len(array)-1:
            for k in range(array[i+1]):
                # print(".")
                new_array.append(".")
        number += 1
    # print(new_array)
    return new_array


def move_file_blocks(array):
    new_array = array
    last_index = len(array) - 1
    for index, item in enumerate(array):
        if item == "." and index < last_index:
            last_num = new_array[last_index]
            while last_num == ".":
                last_index -= 1
                last_num = new_array[last_index]
            new_array[index] = last_num
            new_array[last_index] = "."
            last_index -= 1
    return new_array


def move_as_blocks(array):
    new_array = array
    last_index = len(array) - 1

    # need to check each free space block
    # need to check each file block length

    for index, item in enumerate(array):
        if item == "." and index < last_index:
            last_num = new_array[last_index]
            while last_num == ".":
                last_index -= 1
                last_num = new_array[last_index]
            new_array[index] = last_num
            new_array[last_index] = "."
            last_index -= 1
    return new_array


def get_checksum(array):
    run_sum = 0
    array = [x for x in array if x != '.']
    for index, item in enumerate(array):
        if item != ".":
            run_sum += index * item
            # print(index, item)
            # print(run_sum)

    return run_sum


def solve_part_1():
    sorted_array = move_file_blocks(get_blocks(get_array("input.txt")))
    return get_checksum(sorted_array)


def solve_part_2():
    sorted_array = move_file_blocks(get_blocks(get_array("testInput.txt")))
    return get_checksum(sorted_array)

# print(solve_part_1())
# print(solve_part_2())
