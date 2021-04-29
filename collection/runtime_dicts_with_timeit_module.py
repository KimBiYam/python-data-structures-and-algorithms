import timeit
import random

for i in range(10000, 3000001, 20000):
    timer = timeit.Timer("random.randrange(%d) in x" % i,
                         "from __main__ import random, x")
    x = list(range(i))
    list_time = timer.timeit(number=1000)
    x = {j: None for j in range(i)}
    dict_times = timer.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, list_time, dict_times))
