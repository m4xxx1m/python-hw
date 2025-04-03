import time
from threading import Thread
from multiprocessing import Process


def fib(n: int) -> int:
    prod = 1
    for i in range(2, n+1):
        prod *= i
    return prod


def run_sequential(n: int, times: int):
    for _ in range(times):
        fib(n)


def run_processes(n: int, times: int):
    processes = []
    for _ in range(times):
        p = Process(target=fib, args=(n,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()


def run_threads(n: int, times: int):
    threads = []
    for _ in range(times):
        t = Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def run(func, file, n: int, times: int):
    start = time.time()
    func(n, times)
    end = time.time()
    print(f'{func.__name__}: {end - start}s', file=file)


if __name__ == '__main__':
    n = 50000
    times = 10
    with open('artifacts/task1.txt', 'w') as file:
        print(f'n = {n}; times = {times}', file=file)
        run(run_sequential, file, n, times)
        run(run_threads, file, n, times)
        run(run_processes, file, n, times)
