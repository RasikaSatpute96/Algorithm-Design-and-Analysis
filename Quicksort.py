import random
import time
import matplotlib.pyplot as plt
import math

def quick_sort(data):
    """
    Sorts the given data using the Quick Sort algorithm.

    Args:
        data: A list of comparable elements.

    Returns:
        A new list containing the sorted data.
    """
    if len(data) <= 1:
        return data  # Already sorted or empty

    pivot = data[len(data) // 2]
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

def measure_time(data):
    """
    Measures the average execution time of Quick Sort for the given data.

    Args:
        data: The data to sort.

    Returns:
        The average execution time in seconds.
    """
    start_time = time.time()
    quick_sort(data)
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
        data4 = [random.randint(0, int(math.log(n))) for _ in range(n)]

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
    plt.title('Quick Sort Time Complexity for Various Ranges')
    plt.grid(True)
    plt.legend()
    plt.show()
