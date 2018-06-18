import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


def get_relationship(x, y):
    rel = '='

    if x > y:
        rel = '>'
    elif x < y:
        rel = '<'

    return rel


def main(raw_sample):
    num_test_cases, *test_samples = raw_sample.split('\n')

    for idx in range(int(num_test_cases)):
        compared_numbers = parse_variables(test_samples[idx])
        rel = get_relationship(*compared_numbers)
        print(rel)


if __name__ == '__main__':
    main(sys.stdin.read())
