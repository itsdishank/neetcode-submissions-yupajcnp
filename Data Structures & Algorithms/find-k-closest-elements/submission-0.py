class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0             
        r = k-1
        while r < len(arr)-1:
            diff1 = abs(arr[l] - x)
            diff2 = abs(arr[r+1] - x)

            if diff2 < diff1 or arr[l] == arr[r+1]:
                l += 1
                r += 1

            else:
                break
                
        return arr[l:r+1]