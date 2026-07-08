class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        res = 0
        t = 0
        count = Counter(tasks)
        q = deque()
        maxheap = [c for c in count.values()]
        heapq.heapify_max(maxheap)

        while maxheap or q:
            t += 1
            if maxheap:
                val = heapq.heappop_max(maxheap) - 1
                if val > 0:
                    q.append([val, t+n])
            else:
                t = q[0][1]
            if q and q[0][1] == t:
                heapq.heappush_max(maxheap, q.popleft()[0])

        return t


            