class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits.reverse()
        # print(digits)
        one = True
        i = len(digits)-1
        while i>=0 and one:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i-=1
        # if one:
        return [1] + digits
        