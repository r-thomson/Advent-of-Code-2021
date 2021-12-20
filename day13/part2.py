from os import path

points = set()
folds = []

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    points_input, folds_input = file.read().split('\n\n')

    for point in points_input.strip().split('\n'):
        points.add(tuple(map(int, point.split(','))))

    for fold in folds_input.strip().split('\n'):
        axis, num = fold.removeprefix('fold along ').split('=')
        folds.append((axis, int(num)))

for axis, value in folds:
    new_points = set()

    for x, y in points:
        if axis == 'x':
            new_point = (x if x < value else 2*value - x, y)
        elif axis == 'y':
            new_point = (x, y if y < value else 2*value - y)
        new_points.add(new_point)

    points = new_points


max_x = max(x for x, _ in points)
max_y = max(y for _, y in points)

for y in range(max_y + 1):
    print(''.join('#' if (x, y) in points else ' ' for x in range(max_x + 1)))
