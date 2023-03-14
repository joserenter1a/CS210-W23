"""
Binary Search Practice
CS210-W23
Author: Jose Renteria
"""
import time
import random
import matplotlib.pyplot as plt


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Create a sorted list of 10,000 integers
arr = list(range(10000))

# Generate a random target value
target = random.randint(0, 9999)

# Measure the time it takes to run 100 iterations of linear search
linear_times = []
for i in range(500):
    start_time = time.time()
    linear_search(arr, target)
    end_time = time.time()
    linear_times.append(end_time - start_time)

# Measure the time it takes to run 100 iterations of binary search
binary_times = []
for i in range(500):
    start_time = time.time()
    binary_search(arr, target)
    end_time = time.time()
    binary_times.append(end_time - start_time)

# Plot the results
plt.plot(linear_times, label='Linear Search')
plt.plot(binary_times, label='Binary Search')
plt.xlabel('Iteration')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
