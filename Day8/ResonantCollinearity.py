import numpy as np


def get_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    grid_lines = [list(line) for line in lines]
    return np.array(grid_lines)


