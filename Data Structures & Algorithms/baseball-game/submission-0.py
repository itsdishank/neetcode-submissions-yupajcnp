class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op == '+':
                res = stack[-1]+ stack[-2]
                stack.append(stack[-1]+ stack[-2])
                total += res
            elif op == 'D':
                res = 2*stack[-1]
                stack.append(res)
                total += res
            elif op == 'C':
                total -= stack.pop()
            else:
                stack.append(int(op))
                total += int(op)

        return total