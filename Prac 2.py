import random
import time
import matplotlib.pyplot as plt
def merge(left, right):
    merged = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)
sizes = [5000, 10000, 15000, 20000, 25000]
times = []
for n in sizes:
    data = [random.randint(1, 100000) for _ in range(n)]
    start = time.time()
    sorted_data = merge_sort(data)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)
    print(f"n = {n}, Time taken = {elapsed:.4f} seconds")
plt.plot(sizes, times, marker='o', linestyle='-', color='purple')
plt.title("Merge Sort Time Complexity (Python)")
plt.xlabel("Input size (n)")
plt.ylabel("Time taken (seconds)")
plt.grid(True)
plt.show()
