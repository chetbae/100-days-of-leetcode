# use nodes to store as references for keys, doubly linked list structure
class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None
            
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0

        # create head and tail markers
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        
        # map for getting Node from key
        self.map = {}

    def get(self, key: int) -> int:

        # return -1 if key does not exist
        if key not in self.map:
            return -1
        
        node = self.map[key]

        # if node not already at end of DLL, move to end
        if node.next != self.tail:

            # take node out of DLL
            node.prev.next, node.next.prev = node.next, node.prev

            # append to end of DLL
            prev = self.tail.prev
            prev.next, node.prev = node, prev
            node.next, self.tail.prev = self.tail, node
        
        # return value
        return node.value

    def put(self, key: int, value: int) -> None:

        # if key already exists, remove node from DLL and update value
        if key in self.map:
            node = self.map[key]
            node.prev.next, node.next.prev = node.next, node.prev
            node.value = value
            self.map[key] = node

        # or else instantiate new Node, increase count
        else:
            node = Node(key, value)
            self.map[key] = node
            self.count += 1

        # append to end of DLL
        prev = self.tail.prev
        prev.next, node.prev = node, prev
        node.next, self.tail.prev = self.tail, node
        
        # if count is greater than capacity, discard LRU
        if self.count > self.capacity:
            lru = self.head.next
            self.head.next, lru.next.prev = lru.next, self.head

            del self.map[lru.key]
            self.count -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)