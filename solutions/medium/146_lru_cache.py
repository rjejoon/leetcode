
class DoublyLinkedListNode:
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev: DoublyLinkedListNode = prev
        self.next: DoublyLinkedListNode = next


class LRUCache:

    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.capacity = capacity
        self.head = DoublyLinkedListNode(None, None)  # dummy head
        self.tail = DoublyLinkedListNode(None, None)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._remove(node)
        self._add_to_tail(key, node.value)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._remove(self.key_to_node[key])
        self._add_to_tail(key, value)
        if len(self.key_to_node) > self.capacity:
            self._remove(self.head.next)

    def _remove(self, node: DoublyLinkedListNode) -> None:
        del self.key_to_node[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_tail(self, key, value):
        node = DoublyLinkedListNode(key, value, self.tail.prev, self.tail)
        self.key_to_node[key] = node
        node.prev.next = node
        node.next.prev = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    cache.put(4, 5)
    assert cache.get(4) == 5
    cache.put(4, 6)
    assert cache.get(4) == 6
