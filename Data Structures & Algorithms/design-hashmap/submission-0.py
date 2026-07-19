class MyHashMap:

    def __init__(self):
        self.key_val = []

    def put(self, key: int, value: int) -> None:
        for i, kv in enumerate(self.key_val):
            if kv[0] == key:
                self.key_val[i][1] = value
                return
        self.key_val.append([key,value])

    def get(self, key: int) -> int:
        for i, kv in enumerate(self.key_val):
            if kv[0] == key:
                return kv[1]
        return -1

    def remove(self, key: int) -> None:
        for i, kv in enumerate(self.key_val):
            if kv[0] == key:
                self.key_val.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)