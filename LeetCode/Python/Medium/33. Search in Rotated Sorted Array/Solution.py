class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,h,m= 0 , len(nums)-1 , 0
        while(l<=h):
            m=(l+h)// 2
            if target == nums[m]:
                return m
            elif nums[l]<= nums[m]:
                if target>= nums[l] and target< nums[m]:
                    h=m-1
                else:
                    l=m+1
            else:
                if target>nums[m] and target<=nums[h]:
                    l=m+1
                else:
                    h=m-1
        return -1

        