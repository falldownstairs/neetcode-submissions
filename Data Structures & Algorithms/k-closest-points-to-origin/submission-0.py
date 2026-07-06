class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[math.sqrt(points[i][0] ** 2 + points[i][1] ** 2), points[i]] for i in range(len(points))]
        heapq.heapify(heap)
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        print(heap)
        return res