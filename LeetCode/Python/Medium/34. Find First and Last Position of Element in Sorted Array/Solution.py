class Solution:
    def searchRange(self, nums, target):
        l=0
        h=len(nums)-1
        m=0
        res=[-1,-1]

        while l<=h:
            m= (l + h) // 2
            if target == nums[m]:                
                res[0]=m
                h = m -1
            elif nums[m]< target:
                l= m+1
            else:
                h= m-1
        l=0
        h=len(nums)-1
        m=0
        
        while l<=h:
            m= (l + h) // 2
            if target == nums[m]:
                res[1]=m
                l = m+1
            elif nums[m]< target:
                l= m+1
            else:
                h= m-1
        return res       