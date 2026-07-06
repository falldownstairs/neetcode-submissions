class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            big = heapq.heappop_max(stones)
            small = heapq.heappop_max(stones)
            if big != small:
                heapq.heappush_max(stones, big - small)
        return stones[0] if len(stones) == 1 else 0