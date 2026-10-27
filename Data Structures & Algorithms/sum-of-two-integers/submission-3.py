class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        print(bin(a), bin(b))

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
            print(bin(a), bin(b))

        return a if a <= max_int else ~(a ^ mask)