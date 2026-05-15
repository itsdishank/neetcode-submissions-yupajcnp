class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rCt= 0
        dCt= 0
        cur = 0
        s = set()
        i = 0
        while True:
            for i in range(len(senate)):
                if i in s:
                    continue
                if senate[i] == 'R':
                    if cur < 0:
                        s.add(i)
                        # dCt -= 1
                    else:
                        rCt += 1
                    cur += 1
                else:
                    if cur > 0:
                        s.add(i)
                        # rCt -= 1
                    else:
                        dCt += 1
                    cur-= 1
                # print(i, senate[i], cur, rCt, dCt, s)



            # if i == len(senate):
            if not dCt or not rCt:
                return 'Dire' if dCt else 'Radiant'
            rCt = dCt = 0