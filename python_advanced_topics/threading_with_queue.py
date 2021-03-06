import queue
import threading

q = queue.Queue()


def worker(num):
    while True:
        item = q.get()
        if item is None:
            break
        print(f'스레드 {num+1} : 처리 완료 {item}')
        q.task_done()


if __name__ == "__main__":
    num_worker_threads = 5
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in range(20):
        q.put(item)

    q.join()

    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()
