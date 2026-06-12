class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_nodes = dict()
        
        # define doubly linked list (dll)
        self.head = Node() # dummy head node 
        self.tail = Node() # dummy tail node

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_dll(self, node) -> None:

        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev =  prev_node

    def _insert_dll(self, node) -> None:
        # insert at MRU position
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node        

    def get(self, key: int) -> int:

        if key not in self.cache_nodes:
            return -1

        self._remove_dll(self.cache_nodes[key])
        self._insert_dll(self.cache_nodes[key])

        return self.cache_nodes[key].value
                
    def put(self, key: int, value: int) -> None:

        if key in self.cache_nodes:
            self._remove_dll(self.cache_nodes[key])

        mru_node = Node(key,value)
        self.cache_nodes[key] = mru_node

        self._insert_dll(mru_node)

        if len(self.cache_nodes) > self.capacity:
            lru_node = self.tail.prev
            self._remove_dll(lru_node)
            del self.cache_nodes[lru_node.key]
        
