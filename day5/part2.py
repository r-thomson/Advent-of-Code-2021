import re
from collections import defaultdict
from itertools import product
from os import path


def incl_range(start, stop):
    step = 1 if stop > start else -1
    return range(start, stop + step, step)


points = defaultdict(int)

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    pattern = re.compile(r'\d+')
    input_nums = (map(int, numbers) for numbers in map(pattern.findall, file))
    line_coords = ([(a, b), (c, d)] for (a, b, c, d) in input_nums)

    for start, end in line_coords:
        x_range = incl_range(start[0], end[0])
        y_range = incl_range(start[1], end[1])

        if len(x_range) == 1 or len(y_range) == 1:  # Straight lines
            line_points = product(x_range, y_range)
        else:  # Diagonals
            line_points = zip(x_range, y_range)

        for x, y in line_points:
            points[(x, y)] += 1

print(sum(1 for freq in points.values() if freq >= 2))
