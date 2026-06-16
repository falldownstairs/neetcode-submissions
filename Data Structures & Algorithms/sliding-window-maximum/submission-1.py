class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        for i in range(len(nums)):
            l = 0
            r = len(window)
            target = nums[i]
            mid = (l + r) // 2
            while l < r:
                mid = (l + r) // 2
                if window[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            window.insert(l, target)
            if i >= k:
                window.remove(nums[i-k])
            if i >= k-1:
                res.append(window[-1])


        return res