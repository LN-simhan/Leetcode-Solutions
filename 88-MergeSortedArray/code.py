class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p = m-1
        q = n-1
        r = m+n-1

        while(q>=0):
            if p<0:
                nums1[r]=nums2[q]
                q-=1
            elif q<0:
                pass
            elif nums2[q]>=nums1[p]:
                nums1[r]=nums2[q]
                q-=1
            elif nums1[p]>nums2[q]:
                nums1[r]=nums1[p]
                p-=1
            r-=1     