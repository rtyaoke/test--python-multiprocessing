import multiprocessing
import time


def sleep_counter(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')


if __name__ == '__main__':
    start = time.perf_counter()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=sleep_counter, args=[1])
        p.start()
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
