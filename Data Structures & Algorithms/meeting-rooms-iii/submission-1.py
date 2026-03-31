import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        minH = [] # This will now ONLY store active meetings: (end_time, room)
        res = [0] * n
        meetings.sort()

        free_rooms = [i for i in range(n)]
        heapq.heapify(free_rooms)

        for i in range(len(meetings)):
            s, e = meetings[i]
            
            while minH and minH[0][0] <= s:
                end_time, room = heapq.heappop(minH)
                heapq.heappush(free_rooms, room)

            if free_rooms:
                room = heapq.heappop(free_rooms)
                end = s  # Room is free, so we can start exactly at 's'
            else:
                end, room = heapq.heappop(minH) # No free rooms, wait for the earliest to finish

            res[room] += 1
            if s < end:
                end += (e-s)
            else:
                end = e
            heapq.heappush(minH, (end, room))

        ans = 0
        for i in range(1, len(res)):
            if res[i] > res[ans]:
                ans = i
        return ans