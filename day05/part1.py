import re
from collections import defaultdict
from itertools import product
from os import path

points = defaultdict(int)

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    pattern = re.compile(r'\d+')
    input_nums = (map(int, numbers) for numbers in map(pattern.findall, file))
    line_coords = ([(a, b), (c, d)] for (a, b, c, d) in input_nums)

    for start, end in filter(lambda c: c[0][0] == c[1][0] or c[0][1] == c[1][1], line_coords):
        x_vals = start[0], end[0]
        y_vals = start[1], end[1]

        for x, y in product(range(min(x_vals), max(x_vals) + 1), range(min(y_vals), max(y_vals) + 1)):
            points[(x, y)] += 1

print(sum(1 for freq in points.values() if freq >= 2))
