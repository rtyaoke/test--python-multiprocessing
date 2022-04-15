import concurrent.futures
import time


def sleep_counter(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = range(8, 0, -1)
        results = executor.map(sleep_counter, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')
