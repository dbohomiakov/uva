import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


def main(line, case_number):
    line.sort()
    print(f'Case {case_number}: {line[1]}')


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue
        main(parse_variables(line), idx)
