import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


if __name__ == '__main__':
    file = sys.stdin

    test_cases = int(file.readline())

    for test_case in range(1, test_cases + 1):
        max_speed = max(parse_vars(file.readline())[1:])
        print('Case {}: {}'.format(test_case, max_speed))
