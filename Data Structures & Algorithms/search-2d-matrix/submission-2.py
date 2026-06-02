class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while(l<=r):
            mid = int((l+r)/2)
            print(l,r,mid)
            if matrix[mid][0] > target:
                r = mid-1
            elif matrix[mid][-1] < target:
                l = mid+1
            else:
                l = 0
                r = len(matrix[mid]) - 1
                while(l<=r):
                    m = int((l+r)/2)
                    if matrix[mid][m] > target:
                        r = m-1
                    elif matrix[mid][m] < target:
                        l = m+1
                    else:
                        return True
        return False
