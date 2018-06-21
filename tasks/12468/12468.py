import sys


MIN_CHANNEL = 0
MAX_CHANNEL = 99


def parse_vars(line):
    return list(map(int, line.strip().split()))


if __name__ == '__main__':
    for line in sys.stdin:
        if line.strip() == '-1 -1':
            break
        
        min_ch, max_ch = sorted(parse_vars(line))
        print(min(max_ch - min_ch,
                  (MAX_CHANNEL - max_ch) + (min_ch - MIN_CHANNEL) + 1))
