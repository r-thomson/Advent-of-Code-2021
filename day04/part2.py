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

# I gave up on brute forcing with pure iteration spaghetti
def get_last_winning_board():
    remaining_boards = list(boards)
    for nums in accumulate(numbers, lambda s, n: s + [n], initial=[]):
        first_board = remaining_boards[0]
        remaining_boards = [board for board in remaining_boards if not is_winner(board, nums)]

        if len(remaining_boards) == 0:
            return first_board, nums


win_board, win_num = get_last_winning_board()

score = sum(sum(n for n in line if (n not in win_num)) for line in win_board) * win_num[-1]

print(score)
