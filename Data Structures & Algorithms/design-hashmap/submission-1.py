class MyHashMap:

    def __init__(self):
        self.SIZE = 1009
        self.buckets = [[] for _ in range(self.SIZE)]

    def put(self, key: int, value: int) -> None:
        index = key % self.SIZE
        if not self.buckets[index]:
            self.buckets[index].append([key,value])
            return
        for i, kv in enumerate(self.buckets[index]):
            if kv[0] == key:
                self.buckets[index][i][1] = value
                return
        self.buckets[index].append([key,value])

    def get(self, key: int) -> int:
        index = key % self.SIZE
        if not self.buckets[index]:
            return -1
        for i, kv in enumerate(self.buckets[index]):
            if kv[0] == key:
                return self.buckets[index][i][1]
        

    def remove(self, key: int) -> None:
        index = key % self.SIZE
        if not self.buckets[index]:
            return 
        for i, kv in enumerate(self.buckets[index]):
            if kv[0] == key:
                self.buckets[index].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)