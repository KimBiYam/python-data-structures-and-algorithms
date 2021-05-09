import heapq


class PriorityQueue(object):
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return self.name


def test_priority_queue():
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    pop_result = str(q.pop())
    assert(pop_result == "test2")
    print("테스트 통과!")


if __name__ == "__main__":
    test_priority_queue()
