import random
import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sizes = [5000, 6000, 7000, 8000, 9000, 10000]
times = []

for n in sizes:
    data = [random.randint(1, 10000) for _ in range(n)]
    start = time.time()
    insertion_sort(data)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print(f"n = {n}, Time taken = {elapsed:.4f} seconds")

plt.plot(sizes, times, marker='o', color='blue')
plt.title("Insertion Sort Time Complexity")
plt.xlabel("Input size (n)")
plt.ylabel("Time taken (seconds)")
plt.grid(True)
plt.show()
