import numpy as np


class Guard:
    def __init__(self, name, row, col, final):
        self.name = name
        self.row = row
        self.col = col
        self.final = final

    def move_guard(self, grid):
        while self.row < len(grid) and self.col < len(grid[0]) and not self.final:
            if self.name == ">":
                self.move_right(grid)
            elif self.name == "<":
                self.move_left(grid)
            elif self.name == "^":
                self.move_up(grid)
            elif self.name == "V":
                self.move_down(grid)

        return grid

    def move_left(self, grid):
        while self.col - 1 > 0 and grid[self.row][self.col - 1] != "#":
            grid[self.row][self.col] = "X"
            grid[self.row][self.col - 1] = self.name
            self.col = self.col - 1
        self.name = "^"
        if self.col == len(grid) + 1:
            self.final = (self.row, self.col)
        return grid

    def move_right(self, grid):
        while self.col + 1 < len(grid) and grid[self.row][self.col + 1] != "#":
            grid[self.row][self.col] = "X"
            grid[self.row][self.col + 1] = self.name
            self.col = self.col + 1
        self.name = "V"
        if self.col == len(grid) - 1:
            self.final = (self.row, self.col)
        return grid

    def move_up(self, grid):
        while self.row - 1 > 0 and grid[self.row - 1][self.col] != "#":
            grid[self.row][self.col] = "X"
            grid[self.row - 1][self.col] = self.name
            self.row = self.row - 1
        self.name = ">"
        if self.row == len(grid[0]) + 1:
            self.final = (self.row, self.col)
        return grid

    def move_down(self, grid):
        while self.row + 1 < len(grid[0]) and grid[self.row + 1][self.col] != "#":
            grid[self.row][self.col] = "X"
            grid[self.row + 1][self.col] = self.name
            self.row = self.row + 1
        self.name = "<"
        if self.row == len(grid[0]) - 1:
            self.final = (self.row, self.col)
        return grid


def get_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    grid_lines = [list(line) for line in lines]
    return np.array(grid_lines)


def find_guard(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "^":
                return i, j
    return None


grid = get_grid('input.txt')
guard_location = find_guard(grid)
i = guard_location[0]
j = guard_location[1]
guard = Guard("^", i, j, [])
guard.move_guard(grid)
print(guard.final)
