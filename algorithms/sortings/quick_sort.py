import time
import sys
import random


class QuickSort:
    def __call__(self, arr):
        self._sort(arr, 0, len(arr) - 1)

    @classmethod
    def _sort(cls, arr, start, end):
        if not end - start:
            return

        pivot_idx = random.randrange(start, end, 1)
        pivot_idx = cls._partitioning(arr, start, pivot_idx, end)

        if pivot_idx != start:
            cls._sort(arr, start, pivot_idx - 1)
        if pivot_idx != end:
            cls._sort(arr, pivot_idx + 1, end)

    @staticmethod
    def _partitioning(arr, start, pivot_idx, end):
        """
        First swap pivot element with start element from range. And imagine
        that we delete pivot element from the range temporarily to have a hole
        on that place for swap purposes.
        Start from the end to find element which less then pivot element
        to put it on the 'empty' place in range.
        After that find element from the begin which more then pivot element
        and put it on the 'empty' place from previous step.
        Repeat algo untill you check all elements and put pivot element on
        'empty' place.

        Example: Assume that pivot element is 12.
        [4, 13, 29, <12>, 24, 16, 1]
        [<12>, 13, 29, 4, 24, 16, 1]
        [ _ , 13, 29, 4, 24, 16, 1]
        [1, 13, 29, 4, 24, 16, _ ]
        [1, _ , 29, 4, 24, 16, 13]
        ...
        [1, 4, _ , 29, 24, 16, 13]
        [1, 4, <12> , 29, 24, 16, 13]
        """
        pivot_element = arr[pivot_idx]
        hole_idx = start
        arr[start], arr[pivot_idx] = arr[pivot_idx], arr[start]
        is_reverse = True
        lft_shift = 1
        rght_shift = 0

        for i in range(end - start):
            if is_reverse:
                if arr[end - rght_shift] <= pivot_element:
                    arr[hole_idx] = arr[end - rght_shift]
                    hole_idx = end - rght_shift
                    is_reverse = not is_reverse
                rght_shift += 1
            else:
                if arr[start + lft_shift] > pivot_element:
                    arr[hole_idx] = arr[start + lft_shift]
                    hole_idx = start + lft_shift
                    is_reverse = not is_reverse
                lft_shift += 1

        arr[hole_idx] = pivot_element
        return hole_idx


quick_sort = QuickSort()


if __name__ == '__main__':
    arr = []

    for line in sys.stdin:
        arr.append(int(line))

    start_time = time.time()
    quick_sort(arr)
    print('Time: {}'.format(time.time() - start_time))
