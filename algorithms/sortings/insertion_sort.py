import sys
import time


def insertion_sort(arr):
     arr_length = len(arr)
     for curr_idx in range(arr_length):
         curr_elem = arr[curr_idx]

         for prev_idx in range(curr_idx - 1, -1, -1):
             prev_elem = arr[prev_idx]

             if curr_elem < prev_elem:
                 arr[curr_idx] = prev_elem
                 curr_idx = prev_idx
             else:
                 break

         arr[curr_idx] = curr_elem


if __name__ == '__main__':
    arr = []

    for line in sys.stdin:
        arr.append(int(line))

    start_time = time.time()
    insertion_sort(arr)
    print('Time: {}'.format(time.time() - start_time))

