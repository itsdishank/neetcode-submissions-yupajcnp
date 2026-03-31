class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if len(arr) == 1:
            return 1
        if len(arr) == 2:
            if arr[1] == arr[0]:
                return 1
            return 2
        res = 0
        curLen = 1
        i = 1
        # greater = True
        while i < len(arr):
            if curLen == 1:
                if arr[i] > arr[i-1]:
                    greater = True
                    curLen = 2
                elif arr[i] < arr[i-1]:
                    greater = False
                    curLen = 2
            else:
                if arr[i] == arr[i-1]:
                    curLen = 1
                elif arr[i] > arr[i-1] and not greater:
                    greater = True
                    curLen +=1
                elif arr[i] < arr[i-1] and greater:
                    greater = False
                    curLen +=1
                else:
                    curLen = 2
            # print(i, curLen, res)
            i+=1
            res = max(curLen, res)
        return res