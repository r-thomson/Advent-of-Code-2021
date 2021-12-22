from itertools import accumulate
from os import path


with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as file:
    numbers, boards = file.read().strip().split('\n\n', maxsplit=1)

numbers = [int(n) for n in numbers.split(',')]
boards = [board.split('\n') for board in boards.split('\n\n')]
boards = [[[int(n) for n in line.split()] for line in board] for board in boards]


def transpose(matrix):
    return list(map(list, zip(*matrix)))


def is_winner(board, nums):
    for config in (board, transpose(board)):
        if any(all(num in nums for num in line) for line in config):
            return True
    return False


# 🍝
num_acc = accumulate(numbers, lambda s, n: s + [n], initial=[])
win_board, win_num = next((board, nums) for nums in num_acc for board in boards if is_winner(board, nums))

score = sum(sum(n for n in line if (n not in win_num)) for line in win_board) * win_num[-1]

print(score)
