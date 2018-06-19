import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


def main(size):
    return max(size) <= 20


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue

        is_fit = main(parse_variables(line))
        print('Case {}: {}'.format(idx, ['bad', 'good'][is_fit]))
