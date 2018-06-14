import sys
from functools import lru_cache


def parse_input(raw_sample):
    splited_input = raw_sample.strip().split()
    return list(map(int, splited_input))


@lru_cache(maxsize=None, typed=True)
def calculate_cycle_length(number):
    """
    Recursive implementation of calculating sum of iterations until next number
    will be equal 1.
    """
    if number == 1:
        return 1

    if not number % 2:
        next_number = number / 2
    else:
        next_number = 3 * number + 1

    return 1 + calculate_cycle_length(next_number)


def calculate_max_сycle_length(start_range, finish_range):
    max_сycle_length = 0

    for i in range(start_range, finish_range + 1):
        max_сycle_length = max(calculate_cycle_length(i), max_сycle_length)

    return max_сycle_length


def main(raw_sample):
    parsed_input = parse_input(raw_sample)
    max_cycle_length = calculate_max_сycle_length(min(parsed_input), max(parsed_input))
    print(f'{parsed_input[0]} {parsed_input[1]} {max_cycle_length}')


if __name__ == '__main__':
    for line in sys.stdin:
        main(line)
