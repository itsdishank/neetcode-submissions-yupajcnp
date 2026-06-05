class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curCt = 0
        self.d = {}
        self.useCount = []

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        self.d[key][0] += 1

        if len(self.useCount) == self.d[key][0]:
            q = deque()
            q.append(key)
            self.useCount.append(q)
        else:
            self.useCount[self.d[key][0]].append(key)
        
        # print('get', key)
        # print(self.d)
        # print(self.useCount)
        # print()
        return self.d[key][1]

    def pop(self):
        # print('pop')
        for i in range(len(self.useCount)):
            while len(self.useCount[i])>0:
                k = self.useCount[i].popleft()
                # print(i, k, self.d)
                # print(self.useCount)
                if i == self.d[k][0]:
                    del self.d[k]
                    return


    def put(self, key: int, value: int) -> None:
        # print(self.curCt)
        # print('put', key, value)
        # print(self.d)
        # print(self.useCount)
        if key in self.d:
            self.d[key][1] = value
            self.get(key)
            return
        
        if self.curCt == self.cap:
            self.pop()
            self.curCt -= 1

        self.d[key] = [0, value]

        if len(self.useCount) == self.d[key][0]:
            q = deque()
            q.append(key)
            self.useCount.append(q)
        else:
            self.useCount[self.d[key][0]].append(key)
        self.curCt += 1
        
        
        # print('put', key, value)
        # print(self.d)
        # print(self.useCount)
        # print()
        return
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)