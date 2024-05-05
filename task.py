
import timeit
import random

# Алгоритми сортування 

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])
    return result

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def timsort(arr):
    return sorted(arr)

def test_time(algorithm, data):
    setup_code = f"from __main__ import {algorithm}"
    test_code = f"{algorithm}({data})"
    execution_time = timeit.timeit(test_code, setup=setup_code, number=3)
    return execution_time

# Тестові дані
data_size = 1000
test_data = [random.randint(0, 10000) for _ in range(data_size)]

merge_sort_time = test_time("merge_sort", test_data)
insertion_sort_time = test_time("insertion_sort", test_data)
timsort_time = test_time("timsort", test_data)

print("Час сортування злиттям:", merge_sort_time)
print("Час сортування вставками:", insertion_sort_time)
print("Час вбудованого Timsort:", timsort_time)
