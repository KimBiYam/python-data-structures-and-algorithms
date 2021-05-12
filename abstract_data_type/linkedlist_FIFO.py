from node import Node


class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.pointer
        print()

    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node

    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")

    def _add(self, value):
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node
        self.tail = node

    def addNode(self, value):
        if not self.head:
            self._addFirst(value)
        else:
            self._add(value)

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i

    def _find_by_value(self, value):
        prev = None
        node = self.head
        found = False
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found

    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print(f"인덱스 {index}에 해당하는 노드가 없습니다.")

    def deleteNodeByValue(self, value):
        node, prev, i = self._find_by_value(value)
        if node and node.value == value:
            if not prev:
                self.head = node.pointer
            else:
                prev.pointer = node.pointer
        else:
            print(f"값 {value}에 해당하는 노드가 없습니다.")


if __name__ == "__main__":
    linkedList = LinkedListFIFO()
    for i in range(1, 5):
        linkedList.addNode(i)
    print("연결 리스트 출력:")
    linkedList._printList()
    print("인덱스가 2인 노드 삭제 후 , 연결 리스트 출력:")
    linkedList.deleteNode(2)
    linkedList._printList()
    print("값이 15인 노드 추가 후, 연결 리스트 출력:")
    linkedList.addNode(15)
    linkedList._printList()
    print("모든 노드 삭제 후, 연결 리스트 출력:")
    for i in range(linkedList.length-1, -1, -1):
        linkedList.deleteNode(i)
    linkedList._printList()
