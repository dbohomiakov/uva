import sys


def calc_expression(num):
    return num * 315 + 36962


def get_tens_digit(num):
    return str(num)[-2]


def main(line):
    tens_digit = get_tens_digit(calc_expression(int(line)))
    print(tens_digit)


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx:
            continue

        main(line)
