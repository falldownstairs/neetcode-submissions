import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r
        while(l<=r):
            mid = (l+r)//2
            c = 0
            for b in piles:
                c += math.ceil(float(b)/mid)
            if(c <= h):
                r = mid-1
                k = mid
            else:
                l = mid+1
        return k