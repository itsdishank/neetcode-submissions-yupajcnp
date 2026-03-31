class UnionFind:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 1:
            return True
        if any(num == 1 for num in nums):
            return False

        MAX = max(nums)
        sieve = [0] * (MAX + 1)
        p = 2
        while p * p <= MAX:
            if sieve[p] == 0:
                for composite in range(p * p, MAX + 1, p):
                    sieve[composite] = p
            p += 1

        uf = UnionFind(N + MAX + 1)
        for i in range(N):
            num = nums[i]
            if sieve[num] == 0:  # num is prime
                uf.union(i, N + num)
                continue

            while num > 1:
                prime = sieve[num] if sieve[num] != 0 else num
                uf.union(i, N + prime)
                while num % prime == 0:
                    num //= prime

        root = uf.find(0)
        for i in range(1, N):
            if uf.find(i) != root:
                return False
        return True