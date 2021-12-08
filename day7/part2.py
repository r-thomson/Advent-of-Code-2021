from os import path
from statistics import mean

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = list(map(int, file.read().split(',')))

# Some people on reddit said the right value is ±1 from the mean ¯\_(ツ)_/¯
average = round(mean(input)) - 1
result = sum(sum(range(1, abs(average - val) + 1)) for val in input)

print(result)
