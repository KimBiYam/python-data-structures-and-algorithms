import random
import time


def benchmark(func):
    def wrapper(*args, **kwargs):
        perf_counter = time.perf_counter()
        res = func(*args, **kwargs)
        print(f'{func.__name__} {time.perf_counter() - perf_counter}')
        return res
    return wrapper


@benchmark
def random_tree(number):
    temp = [n for n in range(number)]
    for _ in range(number+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp


if __name__ == "__main__":
    random_tree(10000)
