import random

array = [random.randint(0, 1000) for _ in range(100)]

print("Unsorted Array:")
print(array)

array.sort()

print("Sorted Array:")
print(array)

# NEW FEATURE: Calculate and print the median of the sorted array
def calculate_median(arr):
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

median = calculate_median(array)
print("Median of the Sorted Array:")
print(median)

# NEW FEATURE: Calculate and print the mode of the sorted array
def calculate_mode(arr):
    frequency = {}
    max_count = 0
    mode = []

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_count:
            max_count = frequency[num]

    for num, count in frequency.items():
        if count == max_count:
            mode.append(num)

    return mode

mode = calculate_mode(array)
print("Mode of the Sorted Array:")
print(mode)

# NEW FEATURE: Calculate and print the range of the sorted array
def calculate_range(arr):
    return arr[-1] - arr[0]

range_value = calculate_range(array)
print("Range of the Sorted Array:")
print(range_value)