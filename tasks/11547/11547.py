import sys


def calc_expression(num):
    return (num * 63 + 7492) * 5 - 498


def get_tens_digit(num):
    return str(num)[-2]


def main(line):
    try:
        tens_digit = get_tens_digit(calc_expression(int(line)))
    except IndexError:
        tens_digit = 0
    print(tens_digit)


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue

        main(line)
