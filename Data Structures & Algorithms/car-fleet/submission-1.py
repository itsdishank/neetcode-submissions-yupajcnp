class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = []
        for p, s in zip(position, speed):
            l.append((p,s))
        l.sort(reverse=True)

        prev = -1
        fleets = 0

        for p, s in l:
            curr = (target-p)/s
            if curr > prev:
                fleets+=1
                prev = curr

        return fleets


        