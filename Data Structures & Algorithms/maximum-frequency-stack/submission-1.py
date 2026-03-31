class FreqStack:

    def __init__(self):
        self.freq = {}       
        self.ind = 0  

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val][0]+=1
            self.freq[val][1].append(self.ind)
        else:
            self.freq[val] = [1, [self.ind]]
        self.ind+=1
        # print(self.freq, self.ind)
        

    def pop(self) -> int:
        # print(self.freq)
        l = []
        maxF = -1
        for item in self.freq:
            f = self.freq[item][0]
            if f > maxF:
                l = [item]
                maxF = f
            elif f == maxF:
                l.append(item)
        recent = -1
        el = -1
        # print(l)
        for i in l:
            if self.freq[i][1][-1] > recent:
                recent = self.freq[i][1][-1]
                el = i
        
        self.freq[el][0] -= 1
        self.freq[el][1].pop()
        # print(self.freq, el)
        # print()
        return el



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()