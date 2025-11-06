import threading

fib_sequence = []
lock = threading.Lock()

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def compute_fib(i):
    result = fib(i)
    with lock:
        fib_sequence.append((i, result))

def multi_threaded_fibonacci(n):
    threads = []
    for i in range(n):
        t = threading.Thread(target=compute_fib, args=(i,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    fib_sequence.sort(key=lambda x: x[0])
    print("First", n, "Fibonacci numbers:")
    for index, value in fib_sequence:
        print(value, end=' ')
    print()

n = int(input("Enter the number of Fibonacci numbers to generate: "))
multi_threaded_fibonacci(n)
