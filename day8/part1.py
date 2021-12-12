from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    input = file.read().splitlines()

unique_segment_lens = [2, 3, 4, 7]
digits = [part for line in input for part in line.partition('|')[2].split() if len(part) in unique_segment_lens]

print(len(digits))
