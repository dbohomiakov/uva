import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


if __name__ == '__main__':
    file = sys.stdin

    test_cases = int(file.readline().strip())
    
    for idx in range(1, test_cases + 1):
        high_jump = 0
        low_jump = 0

        file.readline() # skip number of walls

        walls = parse_vars(file.readline())
        current_position = walls[0]

        for wall in walls[1:]:
            if current_position == wall:
                continue
            elif current_position < wall:
                high_jump += 1
            else:
                low_jump += 1

            current_position = wall

        print('Case {}: {} {}'.format(idx, high_jump, low_jump))
