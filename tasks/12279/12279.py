import sys


def main(events_serie):
    return len(events_serie) - 2 * events_serie.count('0')


if __name__ == '__main__':
    for idx, line in enumerate(sys.stdin):
        if not idx % 2:
            if line.strip() == '0':
                break
            continue

        emoogle_balance = main(parse_values(line))
        index = (idx + 1) // 2
        print(f'Case {index}: {emoogle_balance}')
