class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            # print(stack)
            stack.append(asteroids[i])
            while len(stack)>=2 and stack[-1]<0 and stack[-2]>0:
                ast1 = stack.pop()
                ast2 = stack.pop()
                if abs(ast1) > ast2:
                    stack.append(ast1)
                elif abs(ast1) < ast2:
                    stack.append(ast2)
            # print(stack)
            # print()
        return stack

        