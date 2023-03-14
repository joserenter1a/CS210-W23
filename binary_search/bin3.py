"""
Binary Search Practice and visualization
CS210-W23
Author: Jose Renteria
"""
import time
import random
import matplotlib.pyplot as plt


# simple linear search, you have all seen this style
def linear_search(arr: list, target: int) -> int:
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def binary_search(arr: list, target: int, low: int, high: int) -> int:
    pass  # delete when you start

    # TODO
    # base case, this cannot happen
    # exit code
    # mid formula
    # if found
    # return it
    # else if the target value is greater
    # recursively search the right sublist, shift the middle right by 1
    # if not greater, must be lower
    # recursivley search the left sublist, shift the middle left by 1


# a visualizer utility to show the time it takes to run iterations of linear vs binary search
def visualize(arr: list, target: int):
    # Measure the time it takes to run N iterations of linear search
    linear_times = []
    for i in range(500):
        start_time = time.time()
        linear_search(arr, target)
        end_time = (time.time())
        linear_times.append(end_time - start_time)

    # Measure the time it takes to run N iterations of binary search
    binary_times = []
    for i in range(500):
        start_time = time.time()
        binary_search(arr, target, 0, len(arr) - 1)
        end_time = time.time()
        binary_times.append(end_time - start_time)

    # Calculate the average time for each search algorithm
    avg_linear_time = sum(linear_times) / len(linear_times)
    avg_binary_time = sum(binary_times) / len(binary_times)
    # Create lists containing the average time for each search algorithm
    avg_linear_times = [avg_linear_time] * len(linear_times)
    avg_binary_times = [avg_binary_time] * len(binary_times)

    print(f"{round(avg_binary_time * 1000, 5)} seconds")
    print(f"{round(avg_linear_time * 1000, 5)} seconds")
    print(f"That's {round(avg_linear_time / avg_binary_time)}x slower using linear search")

    # Plot the results
    plt.plot(avg_linear_times, label=' AVG Linear Search')
    plt.plot(avg_binary_times, label='AVG Binary Search')
    plt.plot(linear_times, label='Linear Search')
    plt.plot(binary_times, label='Binary Search')
    plt.xlabel('Iteration')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # Create a sorted list of 10,000 integers
    arr = list(range(10000))
    # Generate a random target value
    target = random.randint(0, 9999)

    visualize(arr, target)
