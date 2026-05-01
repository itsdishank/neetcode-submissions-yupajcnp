class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = []
        for p, s in zip(position, speed):
            t.append((p, s))

        t.sort(reverse = True)
        # print(t)
        prevTime = 0
        fleet = 0
        for p, s in t:
            curTime = ((target - p)/s)
            # print(prevTime)
            # print(curTime)
            if curTime > prevTime:
                fleet += 1
                prevTime = curTime
            # print(fleet)
            # print()

        return fleet