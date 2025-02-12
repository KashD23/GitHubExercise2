import random

array = [random.randint(0, 1000) for _ in range(100)]

print("Unsorted Array:")
print(array)

array.sort()

print("Sorted Array:")
print(array)