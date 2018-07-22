import sys


def main(length, orig, res):
    idx_orig = length

    num_unsorted = 0

    for i in range(length - 1, -1, -1):
        if not idx_orig:
            break

        for j in range(idx_orig - 1, -1, -1):
            if res[i] == orig[j]:
                idx_orig = j
                break
            else:
                num_unsorted += 1
                if not j:
                    idx_orig = j
                continue
    return '\n'.join(reversed(res[:num_unsorted]))


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
