import sys


def parse_vars(line):
    return list(map(int, line.strip().split()))


def flip(arr, idx):
    for i in range((idx + 1) // 2):
        arr[i], arr[idx - i] = arr[idx - i], arr[i]


def main(arr):
    flips = []
    arr_length = len(arr)
    
    for i in range(arr_length - 1):
        max_elem_idx = 0
        max_elem = arr[max_elem_idx]
        
        for j in range(1, arr_length - i):
            if arr[j] > max_elem:
                max_elem_idx = j
                max_elem = arr[j]

        if max_elem_idx == arr_length - i - 1:
            continue

        if max_elem_idx:
            flip(arr, max_elem_idx)
            flips.append(arr_length - max_elem_idx)

        flip(arr, arr_length - i - 1)
        flips.append(i + 1)

    flips.append(0)
    return ' '.join(map(str, flips))


if __name__ == '__main__':
    for line in sys.stdin:
        arr = parse_vars(line)
        print(' '.join(map(str, arr)))
        print(main(arr))
