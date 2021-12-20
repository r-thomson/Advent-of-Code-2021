from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    template, _rules = file.read().split('\n\n')
    insertion_rules = dict(line.split(' -> ') for line in _rules.strip().split('\n'))

adj_freqs = defaultdict(int)
for adj in zip(template, template[1:]):
    adj_freqs[''.join(adj)] += 1

for i in range(40):  # Just wait I guess
    new_freqs = defaultdict(int)

    for adjacent, insert in insertion_rules.items():
        freq = adj_freqs[adjacent]
        new_freqs[adjacent[0] + insert] += freq
        new_freqs[insert + adjacent[1]] += freq

    adj_freqs = new_freqs

char_freqs = defaultdict(int)
for adj, freq in adj_freqs.items():
    char_freqs[adj[0]] += freq
char_freqs[template[-1]] += 1  # don't forget the last character!

print(max(char_freqs.values()) - min(char_freqs.values()))
