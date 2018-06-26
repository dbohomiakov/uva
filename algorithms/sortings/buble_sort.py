import sys
import time


def buble_sort(arr):
    length = len(arr)

    for i in range(length):
        for j in range(0, length - i):
            if arr[i] >= arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    arr = []

    for line in sys.stdin:
        arr.append(int(line))

    start_time = time.time()
    buble_sort(arr)
    print('Time: {}'.format(time.time() - start_time))
