
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
        # print(new_array)

    return new_array


def get_checksum(array):
    sum = 0
    for index, item in enumerate(array):
        if item != ".":
            sum += index * item

    return sum


sorted_array = move_file_blocks(get_blocks(get_array("input.txt")))
print(get_checksum(sorted_array))
