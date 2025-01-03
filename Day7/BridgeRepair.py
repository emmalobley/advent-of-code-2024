def get_dict(filename):
    data_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and split the line by the colon
            key, values = line.strip().split(':')

            # Convert the part after the colon (values) into a list of integers
            value_list = list(map(int, values.split()))

            # Add the key and the list of integers to the dictionary
            data_dict[int(key)] = value_list
    return data_dict


def get_count(dictionary):
    count = 0
    for item in dictionary:

        print("We need to make " + str(item) + " from:" + str(dictionary[item]))

        my_sum = 0
        for number in dictionary[item]:
            my_sum += number
        print(my_sum)

        if my_sum == dictionary:
            count += my_sum
            print("It's a match!")

        prod = 1
        for number in dictionary[item]:
            prod *= number
        print(prod)

        if prod == dictionary:
            print("It's a match!")

    return count


dicti = get_dict('testInput.txt')

print(get_count(dicti))

