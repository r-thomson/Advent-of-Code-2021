from collections import defaultdict
from os import path

starts = set()
ends = set()
connections = defaultdict(list)

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in map(str.strip, file):
        a, b = line.split('-')
        if 'start' in (a, b):
            starts.add(a if a != 'start' else b)
        elif 'end' in (a, b):
            ends.add(a if a != 'end' else b)
        else:
            connections[a].append(b)
            connections[b].append(a)

paths = []


def traverse(node: str, visited: tuple, small_revisited: bool):
    visited = visited + (node,)

    if node in ends:
        paths.append(visited)

    for adj_node in connections[node]:
        if adj_node.isupper() or adj_node not in visited:
            traverse(adj_node, visited, small_revisited)
        elif not small_revisited:
            traverse(adj_node, visited, True)


for node in starts:
    traverse(node, (), False)

print(len(paths))
