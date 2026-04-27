class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = (Counter(hand))
        minH = []
        for key in c:
            minH.append(key)

        heapq.heapify(minH)
        # print(minH)

        while minH:
            val = minH[0]
            for i in range(val, val + groupSize):
                if i not in c:
                    return False
                c[i] -= 1
                if c[i] == 0:
                    heapq.heappop(minH)
        return True

                