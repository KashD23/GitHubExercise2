import random

array = [random.randint(0, 1000) for _ in range(100)]

print("Unsorted Array:")
print(array)

array.sort()

print("Sorted Array:")
print(array)

# NEW FEATURE: Calculate and print the median of the sorted array
# The median is the middle value of the sorted array. If the array length is even, it averages the two middle values.
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