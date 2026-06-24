class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.next=None
        self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.cap=capacity
        self.H=Node(0,0)
        self.T=Node(0,0)
        self.H.next=self.T
        self.T.prev=self.H

    def insert(self,node):
        prev=self.T.prev

        prev.next=node
        node.prev=prev
        node.next=self.T
        self.T.prev=node

    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key,value)
            if self.cap>len(self.cache):
                self.insert(node)
            else:
                lru=self.H.next
                self.remove(lru)
                self.insert(node)
                del self.cache[lru.key]
            self.cache[key]=node

