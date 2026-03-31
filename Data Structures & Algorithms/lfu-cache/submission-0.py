#“We maintain a hash map from keys to nodes, and another hash map from frequency to a doubly linked list.
#Each list stores keys of the same frequency in LRU order.
#We also track minFreq so eviction is O(1).
#On every get or put, we move the node to the next frequency list.”

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 0
        self.keyMap = {}      # key → Node
        self.freqMap = {}     # freq → DLL

    def _update(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DLL()

        self.freqMap[node.freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self._update(node)
            return

        if self.size == self.cap:
            lfu_list = self.freqMap[self.minFreq]
            removed = lfu_list.remove_last()
            del self.keyMap[removed.key]
            self.size -= 1

        newNode = Node(key, value)
        self.keyMap[key] = newNode

        if 1 not in self.freqMap:
            self.freqMap[1] = DLL()

        self.freqMap[1].add_front(newNode)
        self.minFreq = 1
        self.size += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)