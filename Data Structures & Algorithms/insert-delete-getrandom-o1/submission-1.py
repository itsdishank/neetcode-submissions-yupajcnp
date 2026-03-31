class RandomizedSet:

    def __init__(self):
        self.l = []
        self.i = {}
        

    def insert(self, val: int) -> bool:
        if val in self.i:
            return False

        self.l.append(val)
        self.i[val] = len(self.l)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.i:
            return False
        
        idx = self.i[val]
        
        self.l[self.i[val]], self.l[-1] = self.l[-1], self.l[self.i[val]]
        self.i[self.l[idx]] = idx
        self.l.pop()
        del self.i[val]
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.l)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()