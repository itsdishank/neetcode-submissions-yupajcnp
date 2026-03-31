class Solution:
    def simplifyPath(self, path: str) -> str:
        # res = '/'
        pathL = path.split('/')
        # print(pathL)
        stack = []
        for i in pathL:
            if not i or i == '.':
                continue
            if i =='..':
                if stack:
                    stack.pop() 
            else:
                stack.append(i)

        # print(stack)

        return '/'+'/'.join(stack)