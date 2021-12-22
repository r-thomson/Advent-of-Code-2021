from os import path
from statistics import median

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = list(map(int, file.read().split(',')))

med = int(median(input))
result = sum(abs(med - val) for val in input)

print(result)
