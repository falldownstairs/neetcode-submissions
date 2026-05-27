class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i, n in enumerate(temperatures):
            k = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > n:
                    k = j-i
                    break
            res.append(k)
        return res