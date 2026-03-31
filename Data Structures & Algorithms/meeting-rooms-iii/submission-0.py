class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # if n >= len(meetings):
        #     return 0
        minH = []
        res = [0]*n
        meetings.sort()
        # print(meetings, res)

        for i in range(n):
            heapq.heappush(minH, (0, i))
        # print(minH)

        for i in range(len(meetings)):
            s, e = meetings[i]
            # print(s, e)
            # end, room = heapq.heappop(minH)
            available = [heapq.heappop(minH)]
            while minH and minH[0][0] <= s:
                available.append(heapq.heappop(minH))
            available.sort(key=lambda x: x[1], reverse = True)
            end, room = available.pop()

            res[room] += 1
            if s<end:
                end += (e-s)
            else:
                end = e
            heapq.heappush(minH, (end, room))
            while available:
                heapq.heappush(minH, available.pop())
            # print(minH)
            # print(res)
            # print()

        # print(res)
        ans = 0
        for i in range(1, len(res)):
            if res[i] >res[ans]:
                ans = i
        return ans

        # print(minH)