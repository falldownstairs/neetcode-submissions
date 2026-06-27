class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.usage = []

    def get(self, key: int) -> int:
        for i in range(len(self.usage)):
            if self.usage[i] == key:
                self.usage.pop(i)
                break
        self.usage.append(key)
        return self.hashmap.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if len(self.hashmap) == self.capacity and key not in self.hashmap.keys():
            for i in range(len(self.usage)):
                if self.usage[i] in self.hashmap.keys():
                    self.hashmap.pop(self.usage[i])
                    break
        self.hashmap[key] = value

        for i in range(len(self.usage)):
            if self.usage[i] == key:
                self.usage.pop(i)
                break
        self.usage.append(key)
