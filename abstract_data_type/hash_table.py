from linkedlist_FIFO import LinkedListFIFO


class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

    def _createHashTable(self):
        for _ in range(self.size):
            self.slots.append(LinkedListFIFO())

    def _find(self, item):
        return item % self.size

    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item)

    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)

    def _print(self):
        for i in range(self.size):
            print(f"슬롯(slot) {i}")
            self.slots[i]._printList()


def test_hash_tables():
    hash_table = HashTableLL(3)
    for i in range(0, 20):
        hash_table._add(i)
    hash_table._print()
    print("\n항목 0,1,2를 삭제합니다.")
    hash_table._delete(0)
    hash_table._delete(1)
    hash_table._delete(2)
    hash_table._delete(3)
    hash_table._print()


if __name__ == "__main__":
    test_hash_tables()
