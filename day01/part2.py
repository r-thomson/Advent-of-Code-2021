from itertools import islice, tee
from os import path

WINDOW_SIZE = 3

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = map(int, file)

    # Zip together offset input iterators, then sum each resulting window
    windows = zip(*(islice(iter, i, None) for i, iter in enumerate(tee(input, WINDOW_SIZE))))
    window_sums = (sum(measurements) for measurements in windows)

    input_a, input_b = tee(window_sums)  # One iterable for each side of the zip
    differences = (b - a for a, b in zip(input_a, islice(input_b, 1, None)))

    result = sum(diff > 0 for diff in differences)  # input is not consumed until here

print(result)
