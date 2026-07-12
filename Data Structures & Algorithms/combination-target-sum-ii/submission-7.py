class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        hashmap = {}
        for i in candidates:
            hashmap[i] = hashmap.get(i, 0) + 1
        candidates = list(set(candidates))
        length = len(candidates)
        def search(subset, total, n):
            if total > target:
                return
            elif total == target:
                res.append(subset)
            for i in range(n, length):
                for _ in range(hashmap[candidates[i]]):
                    subset.append(candidates[i])
                    total += candidates[i]
                    search(subset.copy(), total, i+1)
                for _ in range(hashmap[candidates[i]]):
                    total -= candidates[i]
                    subset.pop()
        search([],0,0)
        return res
