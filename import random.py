import random

# Generate an array of 100 random integers between 0 and 1000
array = [random.randint(0, 1000) for _ in range(100)]

print("Unsorted Array:")
print(array)

# Sort the array
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

# NEW FEATURE: Calculate and print the mode of the sorted array
# The mode is the number that appears most frequently in the array.
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