import threading
import time


class ThreadPool(object):
    def __init__(self):
        self.active = []
        self.lock = threading.Lock()

    def acquire(self, name):
        with self.lock:
            self.active.append(name)
            print(f'획득: {name} | 스레드 풀 : {self.active}')

    def release(self, name):
        with self.lock:
            self.active.remove(name)
            print(f'반환: {name} | 스레드 풀 : {self.active}')


def worker(semaphore: threading.Semaphore, pool: ThreadPool):
    with semaphore:
        name = threading.currentThread().getName()
        pool.acquire(name)
        time.sleep(1)
        pool.release(name)


if __name__ == '__main__':
    threads = []
    pool = ThreadPool()
    semaphore = threading.Semaphore(3)
    for i in range(10):
        t = threading.Thread(
            target=worker, name=f'스레드 {str(i)}', args=(semaphore, pool))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
