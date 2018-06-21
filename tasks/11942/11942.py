import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


def check_order(sequence):
    p_e = sequence[0] # previous element
    c_e = sequence[1] # current element
    status = 'Ordered'

    for n_e in sequence[2:]: # next element
        if not ((p_e <= c_e <= n_e) or (p_e >= c_e >= n_e)):
            status = 'Unordered'
            break

        p_e = c_e
        c_e = n_e
    return status


if __name__ == '__main__':
    file = sys.stdin
    file.readline() # skip number of test cases
    
    print('Lumberjacks:')
    
    for line in file:
        print(check_order(parse_vars(line)))
