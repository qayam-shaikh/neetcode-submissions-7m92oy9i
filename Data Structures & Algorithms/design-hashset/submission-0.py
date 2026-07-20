class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.buckets =[[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        index = key % self.size
        for val in self.buckets[index]:
            if key == val: return
        self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        for i, val in enumerate(self.buckets[index]):
            if key == val:
                self.buckets[index].pop(i)
                return

    def contains(self, key: int) -> bool:
        index = key % self.size
        for val in self.buckets[index]:
            if key == val: return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)