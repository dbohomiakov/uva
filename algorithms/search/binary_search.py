import random


def binary_search(arr, n):
    first_idx = 0
    last_idx = len(arr) - 1
    result = None

    while first_idx <= last_idx:
        mid_idx = first_idx + (last_idx - first_idx) // 2
        
        if n == arr[mid_idx]:
            result = mid_idx
            break
        elif n > arr[mid_idx]:
            first_idx = mid_idx + 1
        else:
            last_idx = mid_idx - 1

    return result


def rec_binary_search(first_idx, last_idx, arr, n):
    if first_idx > last_idx:
        return None
    
    mid_idx = first_idx + (last_idx - first_idx) // 2
    
    if n == arr[mid_idx]:
        return mid_idx
    elif n > arr[mid_idx]:
        return rec_binary_search(mid_idx + 1, last_idx, arr, n)
    else:
        return rec_binary_search(first_idx, mid_idx - 1, arr, n)


if __name__ == '__main__':
    # Test array
    arr = [random.randrange(1, 100, 1) for _ in range(50)]
    arr.sort()

    print('Test array:', arr, sep = '\n')
    print()

    num_1 = int(input('Pls enter the number in range 1..100 for simple binary search ->>> '))
    num_2 = int(input('Pls enter the number in range 1..100 for recursive binary search ->>> '))

    print()
    print('Simple binary search: index - {}'.format(binary_search(arr, num_1)))
    print('Recursive binary search: index - {}'.format(rec_binary_search(0, len(arr), arr, num_2)))
