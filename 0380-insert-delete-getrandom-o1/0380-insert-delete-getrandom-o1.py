class RandomizedSet:

    def __init__(self):
        self.internal = set()

    def insert(self, val: int) -> bool:
        if val in self.internal:
            return False
        else:
            self.internal.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.internal:
            return False
        else:
            self.internal.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.internal))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()