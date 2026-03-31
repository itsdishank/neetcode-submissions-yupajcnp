class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = j = 0
        jumps = 1
        max_jump = 0
        while i<len(nums) and max_jump < len(nums)-1:
            print(i, j, max_jump)
            # if i > max_jump:

            if i>j:
                jumps+=1
                j = max_jump
            max_jump = max(max_jump, i+nums[i])
            i+=1
            
        return jumps