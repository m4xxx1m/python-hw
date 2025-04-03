import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import time


def integrate_work(f, a, step, start, end):
    acc = 0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=10000000, executor_class=ProcessPoolExecutor):
    step = (b - a) / n_iter
    batch_size = n_iter // n_jobs
    rem = n_iter % n_jobs
    start = 0
    futures = []
    with executor_class(max_workers=n_jobs) as executor:
        for _ in range(n_jobs):
            end = start + batch_size + (1 if rem > 0 else 0)
            rem -= 1
            futures.append(executor.submit(integrate_work, f, a, step, start, end))
            start = end
        result = sum(f.result() for f in futures)
    return result


if __name__ == '__main__':
    executor_classes = [ProcessPoolExecutor, ThreadPoolExecutor]
    cpu_count = os.cpu_count()

    with open('artifacts/task2.txt', 'w') as file:
        for executor_class in executor_classes:
            for n_jobs in range(1, cpu_count * 2 + 1):
                start = time.time()
                integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, executor_class=executor_class)
                end = time.time()
                print(f'{executor_class.__name__}; n_jobs={n_jobs}; time: {end - start}s',
                      file=file)
