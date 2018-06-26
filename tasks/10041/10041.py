import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


def main(arr):
    arr_length, *arr = arr
    arr.sort()
    mediana = arr_length // 2

    return sum([abs(arr[idx] - arr[mediana]) for idx in range(arr_length)])


if __name__ == '__main__':
    f = sys.stdin
    f.readline() # skip number of test cases

    for line in sys.stdin:        
        print(main(parse_vars(line)))

