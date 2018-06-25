import sys
import time


class MergeSort:
    def __call__(self, arr):
        self._sort(arr, 0, len(arr) - 1)
        return arr

    @staticmethod
    def _merge(arr, start, middle, end):
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
    def _sort(cls, arr, start, end):
        if not end - start:
            return

        if end - start == 1:
            start_elem = arr[start]
            end_elem = arr[end]
                
            if start_elem > end_elem:
                arr[start], arr[end] = arr[start], arr[end]

            return

        middle = start + (end - start) // 2
        
        cls._sort(arr, start, middle)
        cls._sort(arr, middle + 1, end)

        cls._merge(arr, start, middle, end)
    

merge_sort = MergeSort()


if __name__ == '__main__':
    arr = []

    for line in sys.stdin:
        arr.append(int(line))

    start_time = time.time()
    merge_sort(arr)
    print('Time: {}'.format(time.time() - start_time))
