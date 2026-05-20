class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        for r in range(len(numbers)-1,0,-1):
            while(numbers[l] + numbers[r] < target):
                l += 1
            if(numbers[l]+numbers[r] == target):
                return [l+1,r+1]
