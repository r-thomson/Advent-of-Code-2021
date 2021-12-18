from itertools import product
from os import path

grid = {}  # represent as a coordinate map
flashes = 0

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            grid[(x, y)] = int(char)


def flash(coord, flashed):
    flashed.add(coord)

    for offset in product((-1, 0, 1), repeat=2):
        adj_coord = tuple(map(sum, zip(coord, offset)))  # add offset to coord
        if adj_coord in grid:
            grid[adj_coord] += 1
            if grid[adj_coord] > 9 and adj_coord not in flashed:
                flash(adj_coord, flashed)


for _ in range(100):
    for coord in grid:
        grid[coord] += 1

    flashed = set()
    for coord in grid:
        if grid[coord] > 9 and coord not in flashed:
            flash(coord, flashed)

    for coord in grid:
        if grid[coord] > 9:
            grid[coord] = 0

    flashes += len(flashed)

print(flashes)
