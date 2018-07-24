import sys


def main(length, orig, res):
    mapping = {v: i for i, v in enumerate(orig)}
    last_idx = length - 1

    num_unsorted = 0

    for res_idx in range(length - 1, -1, -1):
        orig_idx = mapping[res[res_idx]]

        if orig_idx > last_idx:
            num_unsorted += last_idx
            break

        if orig_idx < res_idx - num_unsorted:
            num_unsorted = res_idx - orig_idx

        last_idx = min(orig_idx, last_idx)
    return '\n'.join([res[i] for i in range(num_unsorted - 1, -1, -1)])


if __name__ == '__main__':
    file = sys.stdin

    test_cases = int(file.readline().strip('\n'))

    for idx in range(test_cases):

        turtle_num = int(file.readline().strip('\n'))

        orig_stack = []
        res_stack = []

        for _ in range(turtle_num):
            orig_stack.append(file.readline().strip('\n'))

        for _ in range(turtle_num):
            res_stack.append(file.readline().strip('\n'))

        moves = main(turtle_num, orig_stack, res_stack)

        if moves:
            print(moves)
        print()
