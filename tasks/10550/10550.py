import sys

def parse_variables(line):
    return list(map(int, line.strip().split()))


def calc_dial_shift(start, finish, clockwise=False):
    possible_shifts = (40 - abs(finish - start), abs(start - finish))

    if start == finish:
        shift = 0
    elif start > finish:
        shift = possible_shifts[clockwise]
    else:
        shift = possible_shifts[not clockwise]
    return shift


def main(line):
    parsed_variables = parse_variables(line)
    if not any(parsed_variables):
        return

    start_point, *combination_numbers = parsed_variables
    shift_sum = 1080 # Constant full turns shift
    clockwise = True

    for num in combination_numbers:
        shift_sum += calc_dial_shift(start_point, num, clockwise) * 9
        start_point = num
        clockwise = not clockwise

    print(shift_sum)


if __name__ == '__main__':
    for line in sys.stdin:
        main(line)
