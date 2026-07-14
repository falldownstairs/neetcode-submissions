class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def search(n1, n2):
            if len(n2) == 0:
                res.append(n1.copy())
            else:
                for i in range(len(n2)):
                    n1.append(n2.pop(i))
                    search(n1,n2)
                    n2.insert(i, n1.pop())
        search([], nums)
        return res