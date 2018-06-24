import random
from time import time


def selection_sort(arr):
    arr_length = len(arr)

    for i in range(arr_length):
        min_idx = i

        for j in range(i + 1, arr_length):
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


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

     return arr

 
if __name__ == '__main__':
    # Test array
    arr = [random.randrange(1, 100000, 1) for _ in range(10000)]

    # print('Test array:', arr, sep = '\n')

    start = time()
    selection_sort(arr[:])
    print('Sorted array selection:', 'Time: {}'.format(time() - start), sep = '\n')

    start = time()
    insertion_sort(arr[:])
    print('Sorted array insertion:', 'Time: {}'.format(time() - start), sep = '\n')
