import sys
import time


def selection_sort(arr):
    arr_length = len(arr)

    for i in range(arr_length):
        min_idx = i

        for j in range(i + 1, arr_length):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr = []

    for line in sys.stdin:
        arr.append(int(line))

    start_time = time.time()
    selection_sort(arr)
    print('Time: {}'.format(time.time() - start_time))
