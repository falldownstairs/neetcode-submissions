class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = [[] for _ in range(len(nums))]
        out = []
        hashmap = {}
        for i in nums:
            if i not in hashmap.keys():
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for i in hashmap.keys():
            storage[hashmap[i]-1].append(i)
        for i in range(len(storage)-1, -1, -1):
            for num in storage[i]:
                out.append(num)
            if len(out) == k:
                return out