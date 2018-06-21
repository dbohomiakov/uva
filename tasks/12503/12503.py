import sys


START_POSITION = 0


def parse_moves(moves):
    move_shifts = []
    for move in moves:
        if move.startswith('RIGHT'):
            move_shifts.append(1)
        elif move.startswith('LEFT'):
            move_shifts.append(-1)
        else:
            shift = move_shifts[int(move.split()[-1]) - 1]
            move_shifts.append(shift)
    return move_shifts


def move_robot(moves):
    return sum(parse_moves(moves))


if __name__ == '__main__':
    file = sys.stdin
    test_cases = int(file.readline().strip())
    
    for _ in range(test_cases):
        moves = []
        num_moves = int(file.readline().strip())

        for __ in range(num_moves):
            moves.append(file.readline().strip())

        print(move_robot(moves))
        moves = []

