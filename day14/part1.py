from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    template, _rules = file.read().split('\n\n')
    insertion_rules = [tuple(line.split(' -> ')) for line in _rules.strip().split('\n')]

for _ in range(10):
    for adjacent, insert in insertion_rules:
        insert = insert.lower()  # Insert new characters as lowercase to prevent matching
        template = template.replace(adjacent, insert.join(adjacent))
        template = template.replace(adjacent, insert.join(adjacent))  # Overlapping groups? Just do it twice
    template = template.upper()

freqs = {char: template.count(char) for char in set(template)}
print(max(freqs.values()) - min(freqs.values()))
