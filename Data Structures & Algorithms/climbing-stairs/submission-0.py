class Solution:
    def climbStairs(self, n: int) -> int:
        stairmap = {}
        def recurse(n, stairmap):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n not in stairmap:
                count = recurse(n-1, stairmap) + recurse(n-2, stairmap)
                stairmap[n] = count
                return count
            else:
                return stairmap[n]
        
        return recurse(n, stairmap)

""" n = 5 -> 4, 3

4 -> 3, 2 = 2, 2, 1 = 5
3 -> 3

5"""