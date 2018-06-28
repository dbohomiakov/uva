import sys


def parse_vars(line):
    return int(line.strip())


def main(peoples, speeds):
    if peoples == 1:
        return speeds[0], str(speeds[0])

    distance = 0
    moves = []
    speeds = sorted(speeds)
    transp = [speeds.pop(0), speeds.pop(0)]
    transp_diff = 2 * transp[1] - transp[0]

    left_t_1 = True
    left_t_2 = True

    to_right = True

    while peoples:
        if to_right:
            if (peoples == 3 and left_t_2) or (peoples > 3 and (speeds[-1] < transp_diff or speeds[-2] < transp_diff)):
                second_traveller = speeds.pop(0)
                left_t_1 = not left_t_1
                distance += second_traveller
                moves.append('{} {}'.format(transp[0], second_traveller))
            elif left_t_1 and left_t_2:
                left_t_1 = left_t_2 = False
                distance += transp[1]
                moves.append('{} {}'.format(transp[0], transp[1]))
            else:
                second_traveller = speeds.pop(-1)
                distance += second_traveller
                moves.append('{} {}'.format(speeds.pop(-1), second_traveller))
            peoples -= 2
        else:
            if not left_t_1:
                left_t_1 = not left_t_1
                distance += transp[0]
                moves.append(str(transp[0]))
            else:
                left_t_2 = not left_t_2
                distance += transp[1]
                moves.append(str(transp[1]))
            peoples += 1

        to_right = not to_right

    return distance, '\n'.join(moves)


if __name__ == '__main__':
    file = sys.stdin

    test_cases = parse_vars(file.readline())
    file.readline()  # skip empty line-separator

    for _ in range(test_cases):
        if _:
            print()

        speeds = []
        num_peoples = parse_vars(file.readline())

        for __ in range(num_peoples):
            speeds.append(parse_vars(file.readline()))
        
        print(*main(num_peoples, speeds), sep='\n')

        file.readline()  # skip empty line-separator
