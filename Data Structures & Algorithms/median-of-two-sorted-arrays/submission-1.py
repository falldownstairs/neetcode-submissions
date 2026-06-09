class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1,nums2
        if len(A) > len(B):
            A, B = B, A
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = (l+r) // 2
            j = half - i - 2
            print(i,j)

            leftA = A[i] if i >= 0 else float("-infinity")
            rightA = A[i + 1] if (i + 1) < len(A) else float("infinity")
            leftB = B[j] if j >= 0 else float("-infinity")
            rightB = B[j + 1] if (j + 1) < len(B) else float("infinity")

            print(leftA,rightA,leftB,rightB)

            if leftA <= rightB and leftB <= rightA:
                if total % 2: #odd
                    return min(rightA,rightB)
                else:
                    return ((min(rightA,rightB) + max(leftA,leftB)) / 2)
            elif leftA > rightB:
                r = i - 1
            else:
                l = i + 1



        