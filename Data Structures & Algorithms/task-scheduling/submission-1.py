class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ct = Counter(tasks)

        max_ct = max(ct.values())
        max_f = 0
        for count in ct.values():
            if count == max_ct:
                max_f+=1

        baseline = (max_ct-1)*(n+1)+max_f

        return max(len(tasks), baseline)