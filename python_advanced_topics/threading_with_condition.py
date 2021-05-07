import threading


def consumer(condition: threading.Condition):
    name = threading.currentThread().getName()
    print(f'{name} 시작')
    with condition:
        print(f'{name} 대기')
        condition.wait()
        print(f'{name} 자원 소비')


def producer(condition: threading.Condition):
    name = threading.currentThread().getName()
    print(f'{name} 시작')
    with condition:
        print(f'{name} 자원 생산 후 모둔 소비자에게 알림')
        condition.notifyAll()


if __name__ == "__main__":
    condition = threading.Condition()
    consumer1 = threading.Thread(
        name='소비자1', target=consumer, args=(condition,))
    consumer2 = threading.Thread(
        name='소비자2', target=consumer, args=(condition,))
    producer = threading.Thread(name='생산자', target=producer, args=(condition,))

    consumer1.start()
    consumer2.start()
    producer.start()
