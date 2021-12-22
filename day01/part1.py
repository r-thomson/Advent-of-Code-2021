from itertools import islice, tee
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = map(int, file)

    input_a, input_b = tee(input)  # One iterable for each side of the zip
    differences = (b - a for a, b in zip(input_a, islice(input_b, 1, None)))

    result = sum(diff > 0 for diff in differences)  # input is not consumed until here

print(result)
