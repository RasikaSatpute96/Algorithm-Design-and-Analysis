import random
import time
import matplotlib.pyplot as plt
import math

def bucket_sort(arr):
    """
    Sorts the given array using the Bucket Sort algorithm.
    """
    # Check if the array is empty or has only one element
    if len(arr) <= 1:
        return arr

    # Create empty buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Normalize input array
    max_val = max(arr)
    if max_val == 0:  # Handle the case where all elements are 0
        max_val = 1
    arr_normalized = [num / max_val for num in arr]

    # Put elements into respective buckets
    for num in arr_normalized:
        index = min(int(num * (n - 1)), n - 1)  # Ensure index is within range
        buckets[index].append(num)

    # Sort individual buckets
    for bucket in buckets:
        bucket.sort()

    # Concatenate sorted buckets
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    # Denormalize sorted array
    sorted_arr = [num * max_val for num in sorted_arr]

    return sorted_arr


def measure_time(data):
    """
    Measure the average execution time of Bucket Sort for the given data.

    Args:
        data: The data to sort.

    Returns:
        The average execution time in seconds.
    """
    start_time = time.time()
    bucket_sort(data)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    # Define the range of data sizes
    n_values = list(range(100, 1001, 100))

    # Initialize lists to store execution times for each range
    all_times = [[] for _ in range(6)]

    # Measure execution time for each range and store the times
    for n in n_values:
        data1 = random.sample(range(n), n)
        data2 = random.sample(range(min(1000, n)), n)
        data3 = random.sample(range(n ** 3), n)
        data4 = random.sample(range(1, n + 1), n)  # Use n as the upper bound
        data5 = [random.randint(0, n) * 1000 for _ in range(n)]
        data6 = list(range(n))
        num_swaps = math.ceil(math.log(n / 2, 2))
        for _ in range(num_swaps):
            idx = random.randint(0, n - 1)
            idx_swap = random.randint(0, n - 1)
            data6[idx], data6[idx_swap] = data6[idx_swap], data6[idx]

        all_data = [data1, data2, data3, data4, data5, data6]
        for i, data in enumerate(all_data):
            all_times[i].append(measure_time(data))

    # Plot the time complexity for all ranges in one graph
    plt.figure(figsize=(10, 6))
    labels = [
        '[0…n]',
        '[0…k], k < 1000',
        '[0…n^3]',
        '[0…log n]',
        'Multiples of 1000 in [0…n]',
        'In-order with Logarithmic Swaps'
    ]
    for i, times in enumerate(all_times):
        plt.plot(n_values, times, label=labels[i])

    plt.xlabel('Data size (n)')
    plt.ylabel('Average execution time (s)')
    plt.title('Bucket Sort Time Complexity for Various Ranges')
    plt.grid(True)
    plt.legend()
    plt.show()
