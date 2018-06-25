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


class MergeSort:
    def __call__(self, arr):
        self.sort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def merge(arr, start, middle, end):
        arr1 = arr[start: middle + 1]
        arr2 = arr[middle: end]
        arr1_remain = middle - start + 1
        arr2_remain = end - middle
        
        for i in range(arr1_remain + arr2_remain):
            if arr1_remain and arr2_remain:
                if arr1[0] <= arr2[0]:
                    arr[start + i] = arr1.pop(0)
                    arr1_remain -= 1
                else:
                    arr[start + i] = arr2.pop(0)
                    arr2_remain -= 1
            elif arr1_remain:
                arr[start + i] = arr1.pop(0)
                arr1_remain -= 1
            elif arr2_remain:
                arr[start + i] = arr2.pop(0)
                arr2_remain -= 1

    @classmethod
    def sort(cls, arr, start, end):
        if not end - start:
            return

        if end - start == 1:
            start_elem = arr[start]
            end_elem = arr[end]
                
            if start_elem > end_elem:
                arr[start], arr[end] = arr[start], arr[end]

            return

        middle = start + (end - start) // 2
        
        cls.sort(arr, start, middle)
        cls.sort(arr, middle + 1, end)

        cls.merge(arr, start, middle, end)
    

merge_sort = MergeSort()


if __name__ == '__main__':
    # Test array
    arr = [random.randrange(1, 100000, 1) for _ in range(100000)]
    

    start = time()
    selection_sort(arr[:])
    print('Sorted array selection:', 'Time: {}'.format(time() - start), sep = '\n')

    start = time()
    insertion_sort(arr[:])
    print('Sorted array insertion:', 'Time: {}'.format(time() - start), sep = '\n')

    start = time()
    merge_sort(arr[:])
    print('Sorted array merge_sort:', 'Time: {}'.format(time() - start), sep = '\n')
