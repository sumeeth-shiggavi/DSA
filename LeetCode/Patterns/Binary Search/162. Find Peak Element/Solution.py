class Solution:
    def findPeakElement(self,nums):
        
        l=0
        r=len(nums)-1
        m=0
        while l<=r:
            m= (l + r) // 2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
            elif nums[m] > nums[m-1] and nums[m] < nums[m+1]:
                l=m + 1
            else:
                r=m -1
        