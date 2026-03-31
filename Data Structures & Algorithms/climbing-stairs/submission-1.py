class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0]

        def takeStep(no):
            if n==no:
                res[0] += 1
                return
            if n<no:
                return
            
            takeStep(no+1)
            takeStep(no+2)

        takeStep(0)

        return res[0]

        