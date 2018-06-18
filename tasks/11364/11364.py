import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


def calc_min_distance(point_quantity, vector):
    """
    Calculate min distance between <point_quantity> points in vector.
    """
    min_distance = 101
    vector.sort()

    for idx in range(len(vector) - point_quantity + 1):
        min_distance = min(min_distance,
                           abs(vector[idx] - vector[idx + point_quantity - 1]))
    return min_distance * 2


def main(raw_sample):
    num_test_cases, *test_samples = raw_sample.split('\n')

    for idx in range(int(num_test_cases)):
        shop_num = int(test_samples[2 * idx])
        shop_addresses = parse_variables(test_samples[2 * idx + 1])
        min_distance = calc_min_distance(shop_num, shop_addresses)
        print(min_distance)


if __name__ == '__main__':
    main(sys.stdin.read())
