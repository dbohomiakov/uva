import sys

SONAR_MAX_AREA = 3


def parse_variables(line):
    return list(map(int, line.strip().split()))


def calculate_sonar_quantity(line):
    grid_rows, grid_cols = parse_variables(line)
    min_sonar_quantity = (
        sonar_per_line(grid_rows - 2, SONAR_MAX_AREA) *
        sonar_per_line(grid_cols - 2, SONAR_MAX_AREA)
    )
    return min_sonar_quantity


def sonar_per_line(line_length, sonar_area):
    x, y = divmod(line_length, SONAR_MAX_AREA)
    return x + bool(y)


def main(raw_sample):
    num_test_cases, *test_samples = raw_sample.split('\n')

    for idx in range(int(num_test_cases)):
        sonar_quantity = calculate_sonar_quantity(test_samples[idx])
        print(sonar_quantity)

if __name__ == '__main__':
    main(sys.stdin.read())
