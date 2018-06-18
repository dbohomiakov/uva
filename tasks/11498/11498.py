import sys


def parse_variables(line):
    return list(map(int, line.strip().split()))


def check_quadrant(origin, coordinates):
    x_o, y_o = origin
    x, y = coordinates

    if not all([x_o - x, y_o - y]):
        return 'divisa'
    
    quadrant_x =  'E' if x > x_o else 'O'
    quadrant_y = 'N' if y > y_o else 'S'

    return quadrant_y + quadrant_x


def main(raw_sample):
    test_cases = raw_sample.split('\n')
    division_point = case_num = current_case_num = None

    for test_case in test_cases:
        test_case = parse_variables(test_case)

        if len(test_case) == 1 and test_case[0] == 0:
            return

        if not case_num:
            case_num = test_case[0]
            current_case_num = 0
            continue

        if not division_point:
            division_point = test_case
            continue
            
        print(check_quadrant(division_point, test_case))

        current_case_num += 1
        if current_case_num == case_num:
            division_point = case_num = current_case_num = None
        

if __name__ == '__main__':
    main(sys.stdin.read())
