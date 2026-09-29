class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1, len(nums)):
                b=nums[j]
                if (a+b)== target:
                    return [i,j]
                    