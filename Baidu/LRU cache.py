class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # move node to tail
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash:
            self.kick(self.hash[key])
            # ???
            self.hash[key].next.value = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
# param_1 = obj.get(key)
obj.put(1, 11)
obj.put(2, 22)
obj.put(3, 33)
obj.put(4, 44)
