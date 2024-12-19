
def get_grid(filename):
    file = open(filename, 'r')
    grid = []
    for row in file:
        grid.append(list(row.strip()))
    return grid


def get_xmas_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Horizontal Occurrences
    for row in range(rows):
        for col in range(cols - 3):
            if "".join(grid[row][col:col + 4]) == "XMAS":
                count += 1
            elif "".join(grid[row][col:col + 4]) == "SAMX":
                count += 1

    # Vertical Occurrences
    for col in range(cols):
        for row in range(rows - 3):
            if "".join(grid[row + i][col] for i in range(4)) == "XMAS":
                count += 1
            elif "".join(grid[row + i][col] for i in range(4)) == "SAMX":
                count += 1

    # Diagonal Top-left to Bottom-right Occurrences
    for row in range(rows - 3):
        for col in range(cols - 3):
            if "".join(grid[row + i][col + i] for i in range(4)) == "XMAS":
                count += 1
            if "".join(grid[row + i][col + i] for i in range(4)) == "SAMX":
                count += 1

    # Diagonal Top-right to Bottom-left Occurrences
    for row in range(rows - 3):
        for col in range(3, cols):
            if "".join(grid[row + i][col - i] for i in range(4)) == "XMAS":
                count += 1
            if "".join(grid[row + i][col - i] for i in range(4)) == "SAMX":
                count += 1

    return count


def get_x_mas_count(grid):
    rows = len(grid)
    cols = len(grid[0])
    ltr_count = []
    rtl_count = []

    # Diagonal Top-left to Bottom-right Occurrences
    for row in range(rows - 2):
        for col in range(cols - 2):
            if "".join(grid[row + i][col + i] for i in range(3)) == "MAS":
                ltr_count.append([row+1, col+1])
            if "".join(grid[row + i][col + i] for i in range(3)) == "SAM":
                ltr_count.append([row+1, col+1])

    # Diagonal Top-right to Bottom-left Occurrences
    for row in range(rows - 2):
        for col in range(2, cols):
            if "".join(grid[row + i][col - i] for i in range(3)) == "SAM":
                rtl_count.append([row+1, col-1])
            if "".join(grid[row + i][col - i] for i in range(3)) == "MAS":
                rtl_count.append([row+1, col-1])

    count = [item for item in ltr_count if item in rtl_count]
    return len(count)


xmas_count = get_xmas_count(get_grid("input.txt"))
x_mas_count = get_x_mas_count(get_grid("input.txt"))
print(xmas_count)
print(x_mas_count)
