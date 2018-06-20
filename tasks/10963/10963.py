import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


def calculate_gap_width(boundary):
    return abs(boundary[0] - boundary[1]) + 1


if __name__ == '__main__':
    read_line = sys.stdin.readline

    num_cases = int(read_line())
    read_line() # skip blank line in the beginning of test case data

    for n in range(num_cases):
        is_closed = 'yes'
        num_column = int(read_line())
        gap_width = calculate_gap_width(parse_vars(read_line()))

        for _ in range(num_column - 1):
            if gap_width != calculate_gap_width(parse_vars(read_line())):
                is_closed = 'no'

        read_line() # skip blank line between test cases

        print(is_closed)
        
        if n != num_cases -1:
            print()
