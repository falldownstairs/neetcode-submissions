class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        premax = height[0]
        sufmax = height[-1]
        for i in range(len(height)):
            premax = max(premax,height[i])
            prefix[i] = premax
        for i in range(len(height)-1,-1,-1):
            sufmax = max(sufmax,height[i])
            suffix[i] = sufmax
        print(prefix,suffix)
        for i in range(len(height)):
            print(prefix[i],suffix[i],height[i])
            res += (min(prefix[i],suffix[i]) - height[i])
        
        return res

        