from collections import defaultdict
from os import path

risks = {}

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            risks[(x, y)] = int(char)

start = (0, 0)
dest = (max(x for x, _ in risks.keys()), max(y for _, y in risks.keys()))


def get_risks(path):
    return sum(risks[coord] for coord in path[1:])  # dont count start position


def taxicab_dist(a, b):
    return sum(abs(a - b) for a, b in zip(a, b))


# Originally, I rolled my own mediocre A* implementation. It worked for
# every sample I threw at it, but failed for the true input. So fuck it,
# here's the pseudo-code from Wikipedia.                I am very tired.
def find_best_path():
    open_set = set([start])
    came_from = {}

    # Risk just to get to this point
    known_risk = defaultdict(lambda: float('inf'))
    known_risk[start] = 0

    # Known risk + optimistic estimation
    est_risk = defaultdict(lambda: float('inf'))
    est_risk[start] = taxicab_dist(start, dest)

    while len(open_set) != 0:
        current = min(open_set, key=est_risk.__getitem__)
        if current == dest:
            total_path = [current]
            while current in came_from:
                total_path.insert(0, current := came_from[current])
            return total_path

        open_set.remove(current)

        for neighbor in (tuple(map(sum, zip(current, off))) for off in [(1, 0), (-1, 0), (0, 1), (0, -1)]):
            if neighbor not in risks:
                continue

            tenative_risk = known_risk[current] + risks[neighbor]
            if tenative_risk < known_risk[neighbor]:
                came_from[neighbor] = current
                known_risk[neighbor] = tenative_risk
                est_risk[neighbor] = tenative_risk + taxicab_dist(neighbor, dest)
                if neighbor not in open_set:
                    open_set.add(neighbor)

    raise Exception


print(get_risks(find_best_path()))
