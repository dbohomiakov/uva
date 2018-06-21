import sys


def sum_number_digits(number):
    
    if len(number) == 1:
        return number

    return sum_number_digits(str(sum(map(int, number))))


if __name__ == '__main__':
    for line in sys.stdin:

        if not int(line):
            break

        print(sum_number_digits(line.strip()))
