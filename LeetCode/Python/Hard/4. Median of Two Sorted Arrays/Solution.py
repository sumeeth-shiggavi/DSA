import sys

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
       
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        
        l = 0
        h = len(nums1)  
        
        while l <= h:
            m1 = (l + h) // 2
            m2 = (len(nums1) + len(nums2) + 1) // 2 - m1
            
           
            l1 = -sys.maxsize if m1 == 0 else nums1[m1 - 1]
            r1 = sys.maxsize if m1 == len(nums1) else nums1[m1]
            
            l2 = -sys.maxsize if m2 == 0 else nums2[m2 - 1]
            r2 = sys.maxsize if m2 == len(nums2) else nums2[m2]
            
            if l1 <= r2 and l2 <= r1:
                
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                
                else:
                    return max(l1, l2)
            elif l2 > r1:
                l = m1 + 1
            else:
                h = m1 - 1
