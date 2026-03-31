class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 2
        if n <= 2:
            return n

        for i in range(3, n+1):
            nxt = one + two
            one = two
            two = nxt
            # print(i, next)
        return nxt 
        